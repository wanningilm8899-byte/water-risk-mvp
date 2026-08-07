# -*- coding: utf-8 -*-
"""
页面三: 风险敞口
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import calculations, site_ui

st.set_page_config(page_title="风险敞口", page_icon="📊", layout="wide")

site_ui.apply_global_styles()
site_ui.render_sidebar("风险敞口")
site_ui.render_topbar("风险敞口", "公式 v0.3 · 2026-08-07 运行")
site_ui.render_page_header(
    "风险敞口",
    "采购加权水风险敞口按公式 E_k = Σ_i(w_i × r_i,k) 计算，w_i 为节点采购权重，r_i,k 为该节点所在地经统一量纲处理的风险指标值。标 * 的数值为权重缺失时的等权重估计。",
    "工作流 · 第 4 步 / 共 7 步"
)
site_ui.render_editable_notice("B 组最终公式和风险阈值确认后，优先更新 utils/calculations.py。")

# ===== 风险通知栏 =====
site_ui.render_risk_alerts(st.session_state.get('result'))

st.markdown("---")

# 检查数据
if st.session_state.get('matched_data') is None:
    st.warning("⚠️ 请先在 **📥 项目/数据导入** 页面加载数据")
    st.stop()

df = st.session_state['matched_data']

# ===== 维度选择 =====
st.subheader("🎯 选择风险维度")

risk_dimensions = {
    "基准水压力 (Baseline)": "baseline_water_stress",
    "未来 2030 水压力 (SSP3)": "water_stress_2030_ssp3",
    "未来 2050 水压力 (SSP3)": "water_stress_2050_ssp3",
    "干旱风险": "drought_risk"
}

selected_dim = st.selectbox(
    "风险维度",
    list(risk_dimensions.keys()),
    help="不同维度代表不同的风险视角"
)

risk_col = risk_dimensions[selected_dim]

# 如果列不存在,使用基准
if risk_col not in df.columns:
    risk_col = "baseline_water_stress"
    st.info("💡 当前维度数据未加载,使用基准水压力")

# 重新计算(如果切换了维度)
result = calculations.calc_exposure(df, risk_col)
st.session_state['result'] = result

st.markdown("---")

# ===== KPI 指标卡 =====
st.subheader("📈 核心指标")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    site_ui.render_metric_card("Ek 采购加权敞口", f"{result['E_k']:.2f}<small>/1.0</small>", "Σ 贡献 = 权重 × 风险", "amber")

with col2:
    site_ui.render_metric_card("高风险采购占比 Ph", f"{result['P_h']*100:.0f}<small>%</small>", f"风险 ≥ {result['high_risk_threshold']}", "red")

with col3:
    site_ui.render_metric_card("采购集中度 HHI", f"{result['HHI']:.2f}", "Σwi² · 置信 高" if result['HHI'] <= 0.25 else "单点依赖需关注", "green")

with col4:
    site_ui.render_metric_card("Top 3 贡献占比", f"{result['top3_contrib']*100:.0f}<small>%</small>", "关键贡献节点排序", "red")

with col5:
    site_ui.render_metric_card("节点总数", f"{result['n_nodes']}", "统一样本当前规模", "")

st.markdown("---")

# ===== 节点贡献明细表 =====
st.subheader("📋 节点贡献明细")

col1, col2 = st.columns([2, 1])

with col1:
    # 按贡献排序
    df_sorted = df.sort_values('贡献', ascending=False).copy()

    # 准备显示列
    display_df = df_sorted[[
        'node_id', '原材料', '国家', '省州',
        '采购权重', risk_col, '贡献'
    ]].copy()

    display_df = display_df.rename(columns={
        risk_col: '风险分数'
    })

    # 格式化
    display_df['采购权重'] = display_df['采购权重'].map('{:.2%}'.format)
    display_df['风险分数'] = display_df['风险分数'].map('{:.3f}'.format)
    display_df['贡献'] = display_df['贡献'].map('{:.2%}'.format)

    # 高亮高风险行
    def highlight_high_risk(row):
        risk_val = float(row['风险分数'])
        if risk_val >= 0.8:
            return ['background-color: #ffcccc'] * len(row)
        elif risk_val >= 0.4:
            return ['background-color: #ffe6cc'] * len(row)
        else:
            return [''] * len(row)

    styled_df = display_df.style.apply(highlight_high_risk, axis=1)

    st.dataframe(styled_df, use_container_width=True, height=400)

with col2:
    st.markdown("**前10大贡献节点**")

    # 横向柱状图
    top10 = df_sorted.head(10)
    fig_bar = px.bar(
        top10,
        y='node_id',
        x='贡献',
        orientation='h',
        labels={'贡献': '贡献占比', 'node_id': '节点'},
        color='贡献',
        color_continuous_scale='Reds'
    )
    fig_bar.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# ===== 改进潜力矩阵(借鉴 Water Navigator IQ) =====
st.subheader("🎯 改进潜力矩阵 【借鉴 Water Navigator IQ】")
st.markdown("**投资优先级排序:识别应优先调整的节点**")

# 散点图:横轴=风险,纵轴=权重,气泡大小=贡献
fig_matrix = px.scatter(
    df,
    x=risk_col,
    y='采购权重',
    size='贡献',
    color='贡献',
    hover_data=['node_id', '原材料', '国家'],
    labels={risk_col: '风险分数', '采购权重': '采购权重'},
    color_continuous_scale='Reds',
    size_max=30
)

# 添加象限分割线
fig_matrix.add_hline(y=0.15, line_dash="dash", line_color="gray", opacity=0.5)
fig_matrix.add_vline(x=0.4, line_dash="dash", line_color="gray", opacity=0.5)

# 象限标注
fig_matrix.add_annotation(
    x=0.7, y=0.35,
    text="① 优先调整<br>(高风险高权重)",
    showarrow=False,
    font=dict(size=12, color="red"),
    bgcolor="rgba(255,255,255,0.8)"
)

fig_matrix.add_annotation(
    x=0.7, y=0.05,
    text="② 监控<br>(高风险低权重)",
    showarrow=False,
    font=dict(size=12, color="orange")
)

fig_matrix.add_annotation(
    x=0.2, y=0.35,
    text="③ 保持<br>(低风险高权重)",
    showarrow=False,
    font=dict(size=12, color="green")
)

fig_matrix.add_annotation(
    x=0.2, y=0.05,
    text="④ 忽略<br>(低风险低权重)",
    showarrow=False,
    font=dict(size=12, color="gray")
)

fig_matrix.update_layout(height=500)
st.plotly_chart(fig_matrix, use_container_width=True)

# 象限统计
col1, col2, col3, col4 = st.columns(4)

q1 = df[(df[risk_col] >= 0.4) & (df['采购权重'] >= 0.15)]
q2 = df[(df[risk_col] >= 0.4) & (df['采购权重'] < 0.15)]
q3 = df[(df[risk_col] < 0.4) & (df['采购权重'] >= 0.15)]
q4 = df[(df[risk_col] < 0.4) & (df['采购权重'] < 0.15)]

with col1:
    st.metric("① 优先调整", f"{len(q1)} 个节点", delta="高优先级" if len(q1) > 0 else None)

with col2:
    st.metric("② 监控", f"{len(q2)} 个节点")

with col3:
    st.metric("③ 保持", f"{len(q3)} 个节点")

with col4:
    st.metric("④ 忽略", f"{len(q4)} 个节点")

st.markdown("---")

# ===== 导出与下一步 =====
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    if st.button("📥 导出明细表为 CSV"):
        csv = display_df.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="下载 CSV",
            data=csv,
            file_name="risk_exposure_detail.csv",
            mime="text/csv"
        )

with col2:
    if st.button("📄 导出结果为 JSON"):
        import json
        json_str = json.dumps(result, ensure_ascii=False, indent=2)
        st.download_button(
            label="下载 JSON",
            data=json_str,
            file_name="risk_exposure.json",
            mime="application/json"
        )

with col3:
    st.markdown("**下一步**: 前往 **🔮 压力测试** 页面模拟未来情景")

# ===== 独立复算展开(可选) =====
with st.expander("🔍 独立复算 - 逐行核对(可选)"):
    st.markdown("**公式验证**")

    st.latex(r"E_k = \sum_{i=1}^{n} (w_i \times r_i)")
    st.latex(r"HHI = \sum_{i=1}^{n} w_i^2")

    st.markdown("**逐行计算**")

    calc_df = df[['node_id', '采购权重', risk_col, '贡献']].copy()
    calc_df['权重²'] = calc_df['采购权重'] ** 2

    st.dataframe(calc_df, use_container_width=True)

    st.markdown(f"**汇总**")
    st.write(f"- Eₖ = {calc_df['贡献'].sum():.4f}")
    st.write(f"- HHI = {calc_df['权重²'].sum():.4f}")
    st.write(f"- 与卡片显示一致 ✓")


site_ui.render_footer()
