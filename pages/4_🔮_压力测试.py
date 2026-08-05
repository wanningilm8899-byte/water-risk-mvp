# -*- coding: utf-8 -*-
"""
页面四: 压力测试
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import calculations

st.set_page_config(page_title="压力测试", page_icon="🔮", layout="wide")

st.title("🔮 压力测试")
st.markdown("### 模拟未来气候变化与供应商中断的影响")

st.markdown("---")

# 检查数据
if st.session_state.get('matched_data') is None:
    st.warning("⚠️ 请先在 **📥 项目/数据导入** 页面加载数据")
    st.stop()

df_base = st.session_state['matched_data'].copy()
result_base = st.session_state.get('result')

if result_base is None:
    result_base = calculations.calc_exposure(df_base)

# ===== 情景选择 =====
st.subheader("🎯 选择压力测试情景 (基于 C 组推荐)")

scenarios = {
    "📊 基准": {
        "name": "基准",
        "icon": "📊",
        "desc": "当前风险(基于 2023-2024 基线数据)",
        "color": "#0066cc",
        "is_predictive": False
    },
    "🔮 旱季供水下降": {
        "name": "旱季供水下降",
        "icon": "🔮",
        "desc": "预测性风险: SSP3-RCP7.0 2030 情景,地表水可用量下降",
        "color": "#ff9933",
        "is_predictive": True
    },
    "⚠️ 极端干旱": {
        "name": "极端干旱",
        "icon": "⚠️",
        "desc": "预测性风险: 极端情景,多年一遇严重干旱",
        "color": "#cc3333",
        "is_predictive": True
    },
    "🧪 供应商单点失效": {
        "name": "供应商单点失效",
        "icon": "🧪",
        "desc": "压力测试: 假设性情景,核心供应商因水相关问题停工",
        "color": "#9933cc",
        "is_predictive": False
    }
}

selected_scenario_key = st.radio(
    "选择情景",
    list(scenarios.keys()),
    horizontal=True,
    format_func=lambda x: scenarios[x]["icon"] + " " + scenarios[x]["name"]
)

selected_scenario = scenarios[selected_scenario_key]

# 情景说明卡片
st.info(f"**{selected_scenario['icon']} {selected_scenario['name']}**: {selected_scenario['desc']}")

st.markdown("---")

# ===== 参数面板 =====
st.subheader("⚙️ 情景参数")

disrupt_nodes = []
disrupt_ratio = 0.5

if selected_scenario["name"] == "供应商单点失效":
    col1, col2 = st.columns(2)

    with col1:
        disrupt_nodes = st.multiselect(
            "选择中断的节点",
            df_base['node_id'].tolist(),
            help="模拟这些节点的采购受到影响"
        )

    with col2:
        disrupt_ratio = st.slider(
            "中断比例",
            0.0, 1.0, 0.5, 0.1,
            help="0.5 = 采购减少 50%, 1.0 = 完全中断"
        )

    if not disrupt_nodes:
        st.warning("⚠️ 请至少选择 1 个节点进行中断测试")

else:
    st.markdown(f"**{selected_scenario['name']}** 情景使用默认参数")

st.markdown("---")

# ===== 应用情景 =====
df_scenario = calculations.apply_scenario(
    df_base,
    selected_scenario["name"],
    disrupt_nodes=disrupt_nodes,
    disrupt_ratio=disrupt_ratio
)

result_scenario = calculations.calc_exposure(df_scenario)

# ===== 对比视图(借鉴 Water Navigator IQ 预测性标注) =====
st.subheader("📊 基准 vs 情景对比")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### 📊 基准情景")
    st.markdown("**当前风险 (2023-2024 基线数据)**")

    subcol1, subcol2, subcol3 = st.columns(3)

    with subcol1:
        st.metric("加权敞口", f"{result_base['E_k']:.3f}")

    with subcol2:
        st.metric("高风险占比", f"{result_base['P_h']*100:.1f}%")

    with subcol3:
        st.metric("HHI 集中度", f"{result_base['HHI']:.3f}")

with col2:
    st.markdown(f"### {selected_scenario['icon']} {selected_scenario['name']}")

    if selected_scenario['is_predictive']:
        st.markdown("**🔮 预测性风险 - 非确定性结果**")
    else:
        st.markdown("**🧪 压力测试 - 假设性情景**")

    subcol1, subcol2, subcol3 = st.columns(3)

    delta_ek = result_scenario['E_k'] - result_base['E_k']
    delta_ph = result_scenario['P_h'] - result_base['P_h']
    delta_hhi = result_scenario['HHI'] - result_base['HHI']

    with subcol1:
        st.metric(
            "加权敞口",
            f"{result_scenario['E_k']:.3f}",
            delta=f"{delta_ek:+.3f}"
        )

    with subcol2:
        st.metric(
            "高风险占比",
            f"{result_scenario['P_h']*100:.1f}%",
            delta=f"{delta_ph*100:+.1f}%"
        )

    with subcol3:
        st.metric(
            "HHI 集中度",
            f"{result_scenario['HHI']:.3f}",
            delta=f"{delta_hhi:+.3f}"
        )

st.markdown("---")

# ===== 节点级差异分析 =====
st.subheader("🔍 节点级差异分析")

# 合并基准与情景数据
df_compare = df_base[['node_id', '原材料', '国家', '采购权重', '贡献']].copy()
df_compare = df_compare.rename(columns={
    '采购权重': '基准权重',
    '贡献': '基准贡献'
})

df_compare['情景权重'] = df_scenario['采购权重'].values
df_compare['情景贡献'] = df_scenario['贡献'].values

df_compare['权重变化'] = df_compare['情景权重'] - df_compare['基准权重']
df_compare['贡献变化'] = df_compare['情景贡献'] - df_compare['基准贡献']

# 筛选有显著变化的节点(变化 > 5%)
df_changed = df_compare[abs(df_compare['贡献变化']) > 0.05].copy()

if len(df_changed) > 0:
    st.markdown(f"**发现 {len(df_changed)} 个节点有显著变化(Δ > 5%)**")

    # 格式化显示
    display_cols = ['node_id', '原材料', '国家', '基准贡献', '情景贡献', '贡献变化']
    df_display = df_changed[display_cols].copy()

    df_display['基准贡献'] = df_display['基准贡献'].map('{:.2%}'.format)
    df_display['情景贡献'] = df_display['情景贡献'].map('{:.2%}'.format)
    df_display['贡献变化'] = df_display['贡献变化'].map('{:+.2%}'.format)

    # 按变化幅度排序
    df_display = df_display.sort_values('贡献变化', ascending=False, key=lambda x: x.str.replace('%', '').astype(float))

    st.dataframe(df_display, use_container_width=True, height=300)

else:
    st.info("💡 当前情景下,节点贡献无显著变化")

st.markdown("---")

# ===== 可视化对比 =====
st.subheader("📈 可视化对比")

col1, col2 = st.columns(2)

with col1:
    # KPI 对比雷达图
    st.markdown("**关键指标对比**")

    categories = ['加权敞口', '高风险占比', 'HHI 集中度']

    # 归一化到 0-1
    base_vals = [
        result_base['E_k'] / 1.0,
        result_base['P_h'],
        result_base['HHI'] / 0.5
    ]

    scenario_vals = [
        result_scenario['E_k'] / 1.0,
        result_scenario['P_h'],
        result_scenario['HHI'] / 0.5
    ]

    fig_radar = go.Figure()

    fig_radar.add_trace(go.Scatterpolar(
        r=base_vals,
        theta=categories,
        fill='toself',
        name='基准',
        line_color='blue'
    ))

    fig_radar.add_trace(go.Scatterpolar(
        r=scenario_vals,
        theta=categories,
        fill='toself',
        name=selected_scenario['name'],
        line_color=selected_scenario['color']
    ))

    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        showlegend=True,
        height=350
    )

    st.plotly_chart(fig_radar, use_container_width=True)

with col2:
    # 前 5 大节点贡献对比
    st.markdown("**前 5 大节点贡献对比**")

    top5_base = df_base.nlargest(5, '贡献')
    top5_scenario = df_scenario.nlargest(5, '贡献')

    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        name='基准',
        x=top5_base['node_id'],
        y=top5_base['贡献'],
        marker_color='blue'
    ))

    fig_bar.add_trace(go.Bar(
        name=selected_scenario['name'],
        x=top5_scenario['node_id'],
        y=top5_scenario['贡献'],
        marker_color=selected_scenario['color']
    ))

    fig_bar.update_layout(
        barmode='group',
        yaxis_title='贡献',
        xaxis_title='节点',
        height=350
    )

    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# ===== 管理建议(简化版 Agent 输出) =====
st.subheader("💡 管理建议")

if delta_ek > 0.1:
    st.warning(f"""
    **⚠️ 风险显著上升**

    在 **{selected_scenario['name']}** 情景下,加权风险敞口上升 {delta_ek*100:.1f}%。

    **建议行动**:
    1. 识别高风险节点,评估替代供应商
    2. 与关键供应商建立水管理合作(如 AWS 认证)
    3. 增加低风险地区的采购占比
    4. 建立应急采购预案
    """)
elif delta_ek < -0.05:
    st.success(f"""
    **✅ 风险有所下降**

    在 **{selected_scenario['name']}** 情景下,风险敞口下降 {abs(delta_ek)*100:.1f}%。

    **建议**: 继续保持当前采购结构,定期复核。
    """)
else:
    st.info(f"""
    **📊 风险基本稳定**

    在 **{selected_scenario['name']}** 情景下,风险敞口变化较小。

    **建议**: 关注高风险节点,持续监控外部环境变化。
    """)

st.markdown("---")

# ===== 导出与下一步 =====
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    if st.button("📥 导出对比结果"):
        import json
        comparison = {
            "scenario": selected_scenario['name'],
            "baseline": result_base,
            "scenario_result": result_scenario,
            "delta": {
                "E_k": delta_ek,
                "P_h": delta_ph,
                "HHI": delta_hhi
            }
        }
        json_str = json.dumps(comparison, ensure_ascii=False, indent=2)
        st.download_button(
            label="下载 JSON",
            data=json_str,
            file_name=f"scenario_{selected_scenario['name']}.json",
            mime="application/json"
        )

with col2:
    if st.button("🔄 切换其他情景"):
        st.rerun()

with col3:
    st.markdown("**下一步**: 前往 **🤖 Agent 报告** 页面生成完整简报")
