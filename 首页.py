# -*- coding: utf-8 -*-
"""
水风险管理 AI Agent - 主页
"""
import streamlit as st
import sys
from pathlib import Path

# 添加 utils 到路径
sys.path.insert(0, str(Path(__file__).parent))

from utils import data_api

# 页面配置
st.set_page_config(
    page_title="水风险管理 AI Agent",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 初始化示例数据
data_api.init_sample_data()

# 初始化 session state
if 'project_data' not in st.session_state:
    st.session_state['project_data'] = None
if 'matched_data' not in st.session_state:
    st.session_state['matched_data'] = None
if 'result' not in st.session_state:
    st.session_state['result'] = None

# ===== 主页内容 =====
st.title("💧 水风险管理 AI Agent")
st.markdown("### 面向科技农食企业供应链的轻量级水风险评估平台")

st.markdown("---")

# 产品定位
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## 📋 产品定位

    **目标用户**: 科技农食企业供应链与 ESG 团队

    **核心功能**:
    - 🌍 **定位风险**: 自动识别上游原材料产地的水风险
    - 📊 **量化敞口**: 计算采购加权水风险敞口与集中度
    - 🔮 **情景测试**: 模拟未来气候变化与供应商中断的影响
    - 🤖 **AI 解释**: 对话式 Agent 生成可追溯的风险简报
    - 📄 **披露支持**: 对齐 TNFD LEAP 与 CDP Water 框架

    **差异化定位**:
    - 区别于 Ecolab Water Navigator IQ 的"企业多厂区实时监控"
    - 本项目聚焦"供应链上游长期情景规划"
    - 基于公开数据,低门槛,快速部署
    """)

with col2:
    st.info("""
    ### 🎯 MVP 版本说明

    **当前状态**: v0.1 演示版

    **已实现**:
    - ✅ 5 个核心页面
    - ✅ 敞口计算引擎
    - ✅ 3 类压力测试
    - ✅ 数据质量仪表盘

    **待完善** (ABC组数据确定后):
    - ⏳ 真实 Aqueduct 数据
    - ⏳ 完整坐标→流域匹配
    - ⏳ 真实 LLM API 集成
    """)

st.markdown("---")

# 快速开始
st.markdown("## 🚀 快速开始")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 1️⃣ 数据导入

    前往 **📥 项目/数据导入** 页面:
    - 上传采购清单 CSV
    - 或加载示例数据
    - 完成字段校验
    """)

with col2:
    st.markdown("""
    ### 2️⃣ 风险评估

    查看:
    - **🗺️ 供应链地图**: 空间分布
    - **📊 风险敞口**: 加权风险与集中度
    - **🔮 压力测试**: 未来情景模拟
    """)

with col3:
    st.markdown("""
    ### 3️⃣ 生成报告

    前往 **🤖 Agent 报告** 页面:
    - 对话式问答
    - 生成 TNFD LEAP 简报
    - 导出 CDP Water 预填表
    """)

st.markdown("---")

# 数据说明
with st.expander("📚 数据来源与质量声明"):
    st.markdown("""
    ### 数据来源

    1. **Aqueduct 4.0** (WRI): 基准水压力、未来情景 [CC BY 4.0]
    2. **FAOSTAT** (FAO): 农产品产量与面积 [CC BY-NC-SA 3.0]
    3. **AQUASTAT** (FAO): 国家级水资源数据 [CC BY-NC-SA 3.0]
    4. **HydroBASINS**: 流域边界 [免费使用]

    ### MVP 阶段数据状态

    ⚠️ **当前使用模拟数据**: 本 MVP 版本使用简化的国家级风险值与模拟坐标匹配。
    真实数据集成将在 ABC 组数据确定后完成(预计 2026-08-15)。

    ### 质量保证

    - ✅ 所有计算公式已由 B 组验证
    - ✅ 确定性函数可独立复核
    - ✅ 数据来源完全可追溯
    - ✅ 预留数据库接口,后期可平滑切换
    """)

with st.expander("🎓 设计参考: Ecolab Water Navigator IQ"):
    st.markdown("""
    本项目借鉴了 Ecolab Water Navigator IQ (2026年4月22日发布) 的以下设计理念:

    1. **数据质量仪表盘**: 强调质量对决策的影响
    2. **情境化目标建议**: 基于 SBTN 框架的 context-based targets
    3. **投资优先级排序**: 改进潜力矩阵帮助决策
    4. **预测性标注**: 明确区分"当前"与"预测性"风险
    5. **自动披露支持**: 一键导出 CDP Water 预填表

    **核心差异**:
    - IQ 面向大型企业多厂区,需要内部 IoT 数据
    - 本项目面向中小企业上游供应链,只用公开数据
    - IQ 是商业 SaaS,本项目是开源研究 MVP

    参考链接:
    - [Water Navigator IQ 产品页](https://www.ecolab.com/corporate-responsibility/environment/water-stewardship/water-navigator-iq)
    - [发布公告(2026-04-22)](https://en-kr.ecolab.com/news/2026/04/ecolab-unleashes-water-intelligence-to-drive-growth-in-the-ai-era)
    """)

st.markdown("---")

# 页面底部信息
st.markdown("""
<div style="text-align: center; color: gray; padding: 20px;">
    <p>水风险管理 AI Agent MVP v0.1 | D 组: 赵清莹 | 2026-08-05</p>
    <p>本项目为研究原型,不构成专业咨询建议</p>
</div>
""", unsafe_allow_html=True)
