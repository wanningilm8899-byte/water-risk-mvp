# -*- coding: utf-8 -*-
"""
页面二: 供应链地图
"""
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import calculations, site_ui

st.set_page_config(page_title="供应链地图", page_icon="🗺️", layout="wide")

site_ui.apply_global_styles()
site_ui.render_sidebar("供应链地图")
site_ui.render_topbar("供应链地图", "匹配层级：坐标 / 省级 / 国家级")
site_ui.render_page_header(
    "供应链地图与位置匹配",
    "将供应节点表格转为空间视图：节点连线至匹配流域，点的大小表示采购权重，颜色表示节点所在地区水风险等级。当前以示例坐标和国家级风险兜底演示。",
    "工作流 · 第 3 步 / 共 7 步"
)
site_ui.render_editable_notice("位置、行政区、流域匹配链路确定后，可替换地图节点字段和风险图层。")

# ===== 风险通知栏 =====
site_ui.render_risk_alerts(st.session_state.get('result'))

st.markdown("---")

# 检查数据
if st.session_state.get('matched_data') is None:
    st.warning("⚠️ 请先在 **📥 项目/数据导入** 页面加载数据")
    st.stop()

df = st.session_state['matched_data']

# ===== 筛选面板 =====
st.subheader("🔍 筛选与图层控制")

col1, col2, col3, col4 = st.columns(4)

with col1:
    materials = ['全部'] + sorted(df['原材料'].unique().tolist())
    selected_material = st.selectbox("原材料", materials)

with col2:
    countries = ['全部'] + sorted(df['国家'].unique().tolist())
    selected_country = st.selectbox("国家", countries)

with col3:
    risk_threshold = st.slider("风险阈值", 0.0, 1.0, 0.4, 0.1)

with col4:
    show_labels = st.checkbox("显示节点标签", value=True)

# 筛选数据
df_filtered = df.copy()
if selected_material != '全部':
    df_filtered = df_filtered[df_filtered['原材料'] == selected_material]
if selected_country != '全部':
    df_filtered = df_filtered[df_filtered['国家'] == selected_country]

if df_filtered.empty:
    st.warning("当前筛选条件下没有节点，请调整原材料或国家筛选。")
    st.stop()

st.markdown("---")

# ===== 交互式地图 =====
st.subheader("🌍 交互式地图")

col1, col2 = st.columns([3, 1])

with col1:
    # 创建地图
    # 计算中心点
    center_lat = df_filtered['纬度'].mean()
    center_lon = df_filtered['经度'].mean()

    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=3,
        tiles="CartoDB positron"
    )

    # 风险颜色映射
    def get_risk_color(risk_score):
        if risk_score >= 0.8:
            return 'darkred'
        elif risk_score >= 0.4:
            return 'red'
        elif risk_score >= 0.2:
            return 'orange'
        else:
            return 'green'

    # 添加节点标记
    for idx, row in df_filtered.iterrows():
        risk = row.get('baseline_water_stress', 0.3)
        weight = row['采购权重']

        # 弹窗内容
        popup_html = f"""
        <div style="font-family: Arial; min-width: 200px;">
            <h4 style="margin: 0 0 10px 0; color: #333;">{row['node_id']}</h4>
            <table style="width: 100%; font-size: 12px;">
                <tr><td><b>原材料</b></td><td>{row['原材料']}</td></tr>
                <tr><td><b>产地</b></td><td>{row['国家']}/{row['省州']}</td></tr>
                <tr><td><b>采购权重</b></td><td>{weight*100:.1f}%</td></tr>
                <tr><td><b>风险分数</b></td><td>{risk:.3f}</td></tr>
                <tr><td><b>风险等级</b></td><td>
                    <span style="color: {get_risk_color(risk)};">
                        {'极高' if risk >= 0.8 else '高' if risk >= 0.4 else '中' if risk >= 0.2 else '低'}
                    </span>
                </td></tr>
                <tr><td><b>贡献</b></td><td>{row.get('贡献', 0)*100:.2f}%</td></tr>
            </table>
        </div>
        """

        # 添加圆形标记(大小代表权重)
        folium.CircleMarker(
            location=[row['纬度'], row['经度']],
            radius=weight * 200 + 5,  # 基础半径 5,按权重放大
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=f"{row['node_id']}: {row['原材料']}",
            color=get_risk_color(risk),
            fill=True,
            fillColor=get_risk_color(risk),
            fillOpacity=0.6,
            weight=2
        ).add_to(m)

        # 标签
        if show_labels:
            folium.Marker(
                location=[row['纬度'], row['经度']],
                icon=folium.DivIcon(html=f"""
                    <div style="font-size: 10px; font-weight: bold;
                                color: {get_risk_color(risk)};
                                text-shadow: 1px 1px 2px white;">
                        {row['node_id']}
                    </div>
                """)
            ).add_to(m)

    # 添加图例
    legend_html = """
    <div style="position: fixed; bottom: 50px; right: 50px; z-index: 1000;
                background: white; padding: 15px; border-radius: 10px;
                border: 2px solid #ccc; font-family: Arial; font-size: 12px;">
        <h4 style="margin: 0 0 10px 0;">风险等级</h4>
        <div><span style="color: darkred;">●</span> 极高 (≥0.8)</div>
        <div><span style="color: red;">●</span> 高 (0.4-0.8)</div>
        <div><span style="color: orange;">●</span> 中 (0.2-0.4)</div>
        <div><span style="color: green;">●</span> 低 (<0.2)</div>
        <hr style="margin: 10px 0;">
        <p style="margin: 0; font-size: 10px; color: gray;">
            圆圈大小 = 采购权重
        </p>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    # 显示地图
    st_folium(m, width=None, height=500)

with col2:
    st.markdown("**地图说明**")
    st.markdown(f"""
    - **节点总数**: {len(df_filtered)}
    - **筛选后**: {len(df_filtered)}
    - **高风险节点**: {len(df_filtered[df_filtered['baseline_water_stress'] >= risk_threshold])}

    **操作提示**:
    - 点击圆圈查看详情
    - 拖拽移动地图
    - 滚轮缩放
    """)

    st.markdown("---")

    st.markdown("**风险分布统计**")

    # 风险分布直方图
    risk_bins = [0, 0.2, 0.4, 0.8, 1.0]
    risk_labels = ['低', '中', '高', '极高']
    df_filtered['风险等级'] = pd.cut(
        df_filtered['baseline_water_stress'],
        bins=risk_bins,
        labels=risk_labels
    )

    risk_dist = df_filtered['风险等级'].value_counts().sort_index()

    for level in risk_labels:
        count = risk_dist.get(level, 0)
        pct = count / len(df_filtered) * 100 if len(df_filtered) > 0 else 0
        st.metric(level, f"{count} 个", f"{pct:.1f}%")

st.markdown("---")

# ===== 节点匹配结果表 =====
st.subheader("📋 节点匹配结果表")

# 准备显示列
display_df = df_filtered[[
    'node_id', '原材料', '国家', '省州',
    '纬度', '经度', '采购权重', 'baseline_water_stress', '贡献'
]].copy()

display_df = display_df.rename(columns={
    'baseline_water_stress': '风险分数'
})

# 格式化
display_df['采购权重'] = display_df['采购权重'].map('{:.2%}'.format)
display_df['风险分数'] = display_df['风险分数'].map('{:.3f}'.format)
display_df['贡献'] = display_df['贡献'].map('{:.2%}'.format)

# 按贡献排序
display_df = display_df.sort_values('贡献', ascending=False)

st.dataframe(
    display_df,
    use_container_width=True,
    height=300
)

# ===== 导出功能 =====
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    if st.button("📥 导出表格为 CSV"):
        csv = display_df.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="下载 CSV",
            data=csv,
            file_name="supply_chain_nodes.csv",
            mime="text/csv"
        )

with col2:
    st.info("💡 后续可添加: 导出地图为 PNG")

with col3:
    st.markdown("**下一步**: 前往 **📊 风险敞口** 页面查看量化指标")


site_ui.render_footer()
