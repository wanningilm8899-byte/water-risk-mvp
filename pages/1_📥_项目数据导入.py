# -*- coding: utf-8 -*-
"""
页面一: 项目/数据导入
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import data_api, calculations, site_ui

st.set_page_config(page_title="数据导入", page_icon="📥", layout="wide")

site_ui.apply_global_styles()
site_ui.render_sidebar("数据导入")
site_ui.render_topbar("数据导入", "CSV 模板可下载")
site_ui.render_page_header(
    "项目/数据导入",
    "选择行业与关键原材料，导入供应节点数据。系统会检查必填字段、坐标范围与采购权重合计，并将无法精确匹配的字段标记为工作假设。",
    "工作流 · 第 1 步 / 共 7 步"
)
site_ui.render_editable_notice("B 组最终字段、来源说明和校验规则确定后，可替换这里的数据模板。")

# ===== 风险通知栏 =====
site_ui.render_risk_alerts(st.session_state.get('result'))

st.markdown("---")

# ===== 数据源选择 =====
st.subheader("1 · 行业与原材料")

industry_cols = st.columns([1, 1, 1, 1])
with industry_cols[0]:
    st.markdown('<span class="wp-badge gray">C13 农副食品加工业</span>', unsafe_allow_html=True)
with industry_cols[1]:
    st.markdown('<span class="wp-badge green">C14 食品制造业</span>', unsafe_allow_html=True)
with industry_cols[2]:
    st.markdown('<span class="wp-badge gray">C15 酒 / 饮料 / 精制茶制造业</span>', unsafe_allow_html=True)
with industry_cols[3]:
    st.markdown('<span class="wp-badge amber">待 A 组细化</span>', unsafe_allow_html=True)

st.markdown("**关键原材料（与行业联动）**")
site_ui.render_badges(["甘蔗", "大豆", "玉米", "番茄", "原奶", "棕榈", "茶叶"], "green")

st.markdown("---")
st.subheader("2 · 导入方式")

col1, col2, col3 = st.columns(3)

with col1:
    mode = st.radio(
        "数据加载方式",
        ["📦 加载示例数据", "📁 上传 CSV", "✍️ 手动输入"],
        horizontal=False
    )

with col2:
    if mode == "📦 加载示例数据":
        st.info("""
        **示例数据说明**
        - 10 个节点
        - 涵盖 5 类原材料
        - 5 个国家
        - 权重已归一化
        """)
    elif mode == "📁 上传 CSV":
        st.info("""
        **CSV 格式要求**
        - node_id, 原材料, 供应商
        - 国家, 省州, 纬度, 经度
        - 采购权重, 数据性质, 来源
        """)
    else:
        st.info("""
        **手动输入**
        - 适合快速测试
        - 少量节点(1-5个)
        """)

# ===== 加载数据 =====
df = None

if mode == "📦 加载示例数据":
    if st.button("🚀 加载示例数据", type="primary"):
        df = data_api.load_sample_nodes("v1")
        st.success(f"✅ 成功加载 {len(df)} 个节点")

elif mode == "📁 上传 CSV":
    uploaded_file = st.file_uploader("选择 CSV 文件", type=['csv'])
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ 成功读取 {len(df)} 行数据")
        except Exception as e:
            st.error(f"❌ 读取失败: {e}")

elif mode == "✍️ 手动输入":
    st.markdown("**快速输入(简化版)**")
    num_nodes = st.number_input("节点数量", min_value=1, max_value=5, value=2)

    nodes = []
    for i in range(num_nodes):
        with st.expander(f"节点 {i+1}", expanded=(i==0)):
            col1, col2 = st.columns(2)
            with col1:
                material = st.selectbox(f"原材料 {i+1}",
                    ['甘蔗', '甜菜', '大豆', '玉米', '番茄', '原奶'], key=f"mat_{i}")
                country = st.selectbox(f"国家 {i+1}",
                    ['CHN', 'BRA', 'USA', 'ARG', 'MYS'], key=f"cty_{i}")
            with col2:
                weight = st.slider(f"权重 {i+1}", 0.0, 1.0, 0.5, key=f"wgt_{i}")
                province = st.text_input(f"省州 {i+1}", "示例省份", key=f"prv_{i}")

            nodes.append({
                'node_id': f"S{i+1:03d}",
                '原材料': material,
                '供应商': f"{province}{material}供应商",
                '国家': country,
                '省州': province,
                '纬度': 30.0 + i,
                '经度': 120.0 + i,
                '采购权重': weight,
                '数据性质': '手动输入',
                '来源': 'MVP 手动输入'
            })

    if st.button("✅ 确认输入"):
        df = pd.DataFrame(nodes)
        # 归一化权重
        df['采购权重'] = df['采购权重'] / df['采购权重'].sum()
        st.success(f"✅ 创建 {len(df)} 个节点")

# ===== 数据预览与校验 =====
if df is not None:
    st.markdown("---")
    st.subheader("2️⃣ 数据预览与校验")

    # 数据表格
    st.dataframe(df, use_container_width=True, height=300)

    # 字段校验
    st.markdown("**字段校验结果**")
    col1, col2, col3, col4 = st.columns(4)

    required_cols = ['node_id', '原材料', '国家', '采购权重']
    missing = [c for c in required_cols if c not in df.columns]

    with col1:
        if not missing:
            st.success(f"✅ 必填字段完整 ({len(required_cols)})")
        else:
            st.error(f"❌ 缺失字段: {', '.join(missing)}")

    with col2:
        if '纬度' in df.columns and '经度' in df.columns:
            valid_coords = ((df['纬度'].between(-90, 90)) &
                          (df['经度'].between(-180, 180))).sum()
            st.success(f"✅ 有效坐标: {valid_coords}/{len(df)}")
        else:
            st.warning("⚠️ 缺少坐标字段")

    with col3:
        if '采购权重' in df.columns:
            weight_sum = df['采购权重'].sum()
            if abs(weight_sum - 1.0) < 0.01:
                st.success(f"✅ 权重归一化: {weight_sum:.3f}")
            else:
                st.warning(f"⚠️ 权重和: {weight_sum:.3f} (将自动归一化)")
                df['采购权重'] = df['采购权重'] / weight_sum

    with col4:
        if '来源' in df.columns:
            traceable = df['来源'].notna().sum()
            st.success(f"✅ 可追溯: {traceable}/{len(df)}")
        else:
            st.warning("⚠️ 缺少来源字段")

    # ===== 数据质量仪表盘(借鉴 Water Navigator IQ) =====
    st.markdown("---")
    st.subheader("3️⃣ 数据质量总览 【借鉴 Water Navigator IQ】")

    quality = calculations.assess_data_quality(df)

    col1, col2 = st.columns([2, 1])

    with col1:
        # 雷达图
        st.markdown("**5 维质量雷达图**")
        metrics = quality['metrics']

        fig = go.Figure(data=go.Scatterpolar(
            r=list(metrics.values()),
            theta=list(metrics.keys()),
            fill='toself',
            marker_color='rgb(100, 180, 100)',
            line_color='rgb(50, 150, 50)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1],
                    tickformat=".0%"
                )
            ),
            showlegend=False,
            height=350
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # 整体评级
        st.markdown("**整体质量等级**")
        grade = quality['grade']
        color = quality['color']
        score = quality['avg_score']

        color_map = {
            "green": "#28a745",
            "yellow": "#ffc107",
            "orange": "#fd7e14",
            "red": "#dc3545"
        }

        st.markdown(f"""
        <div style="text-align: center; padding: 30px;
                    background: {color_map[color]}; border-radius: 10px;">
            <h1 style="color: white; margin: 0; font-size: 80px;">{grade}</h1>
            <p style="color: white; margin: 10px 0 0 0; font-size: 20px;">
                综合得分: {score:.1%}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # 数据性质分布
        st.markdown("**数据性质分布**")
        nature_dist = quality['nature_dist']
        fig_pie = go.Figure(data=[go.Pie(
            labels=list(nature_dist.keys()),
            values=list(nature_dist.values()),
            hole=.3
        )])
        fig_pie.update_layout(height=250, showlegend=True)
        st.plotly_chart(fig_pie, use_container_width=True)

    # ===== 确认入库 =====
    st.markdown("---")
    st.subheader("4️⃣ 确认并进入下一步")

    col1, col2, col3 = st.columns([1, 1, 2])

    with col1:
        if st.button("✅ 确认数据,进入下一步", type="primary", use_container_width=True):
            # 保存到 session state
            st.session_state['project_data'] = df
            st.session_state['matched_data'] = df.copy()  # MVP 阶段直接复制

            # 添加模拟风险分数
            st.session_state['matched_data']['baseline_water_stress'] = \
                calculations.simulate_risk_scores(df)
            st.session_state['matched_data']['贡献'] = \
                st.session_state['matched_data']['采购权重'] * \
                st.session_state['matched_data']['baseline_water_stress']

            # 计算敞口
            result = calculations.calc_exposure(st.session_state['matched_data'])
            st.session_state['result'] = result

            st.success("✅ 数据已保存! 请前往 **🗺️ 供应链地图** 或 **📊 风险敞口** 页面")
            st.balloons()

    with col2:
        if st.button("🔄 重新加载", use_container_width=True):
            st.session_state['project_data'] = None
            st.session_state['matched_data'] = None
            st.session_state['result'] = None
            st.rerun()

    with col3:
        st.info("💡 提示: 数据确认后,可在其他页面查看风险分析结果")

else:
    st.info("👆 请先选择数据源并加载数据")


site_ui.render_footer()
