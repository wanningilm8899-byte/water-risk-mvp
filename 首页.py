# -*- coding: utf-8 -*-
"""
水风险管理 AI Agent - 首页总览
"""
import sys
from pathlib import Path

import plotly.express as px
import streamlit as st

sys.path.insert(0, str(Path(__file__).parent))

from utils import calculations, data_api, site_content, site_ui


st.set_page_config(
    page_title="水脉 WaterPulse",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

site_ui.apply_global_styles()
site_ui.render_sidebar("首页总览")
site_ui.render_topbar("首页总览", "本地资料库已连接")

data_api.init_sample_data()

for key in ("project_data", "matched_data", "result"):
    if key not in st.session_state:
        st.session_state[key] = None

df = st.session_state.get("matched_data")
if df is None:
    df = data_api.load_sample_nodes("v1")
    df["baseline_water_stress"] = calculations.simulate_risk_scores(df)
    df["贡献"] = df["采购权重"] * df["baseline_water_stress"]

result = calculations.calc_exposure(df)
project = site_content.get_project()
quality = calculations.assess_data_quality(df)


site_ui.render_page_header(
    "甲公司上游原材料水风险总览",
    "植物基蛋白核心原料的采购组合水风险入口。数据来自公开披露与本地样本库匹配结果，工作假设字段将在报告中如实说明，不作为企业真实结论。",
    "项目总览 · PHASE 1 MVP"
)

tabs = st.tabs(["总览", "按原材料", "按产地"])

with tabs[0]:
    summary_left, summary_right = st.columns([2.5, 1])

    with summary_left:
        st.markdown(
            f"""
            <div class="wp-panel">
                <div style="display:grid;grid-template-columns:repeat(4,minmax(120px,1fr));gap:18px;">
                    <div><div class="wr-muted">行业分类</div><strong>C14 食品制造业</strong></div>
                    <div><div class="wr-muted">关键原材料</div><strong>大豆 / 甘蔗 / 甜菜等</strong></div>
                    <div><div class="wr-muted">评估年度</div><strong>2026</strong></div>
                    <div><div class="wr-muted">供应节点数</div><strong>{len(df)} 个</strong></div>
                </div>
                <div style="margin-top:16px;">
                    <span class="wp-badge green">数据性质：公开披露 {int((df["数据性质"] == "真实披露").sum())}</span>
                    <span class="wp-badge amber">工作假设 {int((df["数据性质"] == "工作假设").sum())}</span>
                    <span class="wp-badge gray">模拟 {int((df["数据性质"] == "模拟").sum())}</span>
                    <span class="wp-badge green">位置匹配 {quality["metrics"]["坐标有效率"]:.0%}</span>
                    <span class="wp-badge amber">数据质量 {quality["grade"]}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with summary_right:
        st.markdown(
            """
            <div class="wp-panel">
                <div class="wr-muted">状态标识图例</div>
                <span class="wp-badge green">已确定</span>
                <span class="wp-badge amber">工作假设</span>
                <span class="wp-badge red">待验证</span>
                <span class="wp-badge gray">暂不纳入</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        site_ui.render_metric_card("采购加权水风险敞口 Ek", f"{result['E_k']:.2f}<small> / 1.0</small>", "Σ wi × ri,k · 置信 中", "amber")
    with m2:
        site_ui.render_metric_card("高风险采购占比 Ph", f"{result['P_h']*100:.0f}<small>%</small>", f"阈值 r ≥ {result['high_risk_threshold']:.1f}", "red")
    with m3:
        site_ui.render_metric_card("采购集中度 HHI", f"{result['HHI']:.2f}", "按供应节点权重估计", "green")
    with m4:
        site_ui.render_metric_card("Top 3 节点贡献占比", f"{result['top3_contrib']*100:.0f}<small>%</small>", "用于定位优先调查对象", "red")

    lower_left, lower_right = st.columns([2, 1])

    with lower_left:
        st.markdown('<div class="wp-panel"><strong>分析流程 · 端到端进度</strong><div class="wr-muted">每一步均可回看输入、公式版本与运行时间。</div>', unsafe_allow_html=True)
        site_ui.render_progress(active_step=5 if st.session_state.get("matched_data") is not None else 1)

        material = df.groupby("原材料", as_index=False)["贡献"].sum().sort_values("贡献", ascending=False)
        fig = px.bar(
            material,
            x="原材料",
            y="贡献",
            color="贡献",
            color_continuous_scale=["#3d9a67", "#d58b21", "#c44937"],
            text=material["贡献"].map(lambda v: f"{v:.2%}")
        )
        fig.update_layout(
            title="按原材料产区分解敞口",
            height=370,
            margin=dict(l=10, r=10, t=55, b=10),
            showlegend=False,
            paper_bgcolor="white",
            plot_bgcolor="white",
            yaxis_title="贡献占比",
            xaxis_title=""
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with lower_right:
        st.markdown('<div class="wp-panel-tight"><strong>数据质量提示</strong>', unsafe_allow_html=True)
        site_ui.render_list([
            {
                "title": "采购权重合计已归一化",
                "body": f"当前权重和 {df['采购权重'].sum():.0%}，系统按统一口径计算敞口。",
                "tone": "amber"
            },
            {
                "title": "公开披露与工作假设分层标记",
                "body": "样例数据中已区分真实披露、工作假设和模拟数据，报告会保留来源说明。",
                "tone": ""
            },
            {
                "title": "ABC 组信息保留替换空间",
                "body": "行业范围、数据链路、压力情景参数确认后集中替换。",
                "tone": ""
            }
        ])
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown('<div class="wp-panel-tight" style="margin-top:18px;"><strong>快速入口</strong>', unsafe_allow_html=True)
        st.page_link("pages/1_📥_项目数据导入.py", label="加载统一 10 节点演示样本")
        st.page_link("pages/3_📊_风险敞口.py", label="查看敞口复核表")
        st.page_link("pages/5_🤖_Agent报告.py", label="向 Agent 提问本项目结果")
        st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:
    st.dataframe(
        df.groupby("原材料", as_index=False)
        .agg(采购权重=("采购权重", "sum"), 平均风险=("baseline_water_stress", "mean"), 敞口贡献=("贡献", "sum"))
        .sort_values("敞口贡献", ascending=False),
        use_container_width=True,
        hide_index=True
    )

with tabs[2]:
    st.dataframe(
        df[["node_id", "原材料", "供应商", "国家", "省州", "采购权重", "baseline_water_stress", "数据性质", "来源"]]
        .rename(columns={"baseline_water_stress": "基准水风险"}),
        use_container_width=True,
        hide_index=True
    )


st.markdown("---")
st.markdown('<div class="wr-section-title">ABC 组待定信息占位</div>', unsafe_allow_html=True)
site_ui.render_group_cards()
site_ui.render_editable_notice("实质内容依据项目文件当前版本：AI 负责理解、追问与解释；风险数值由确定性函数和可追溯数据产生。")
site_ui.render_footer()
