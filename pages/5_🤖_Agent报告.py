# -*- coding: utf-8 -*-
"""
页面五: Agent 报告
"""
import streamlit as st
import pandas as pd
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import calculations

st.set_page_config(page_title="Agent 报告", page_icon="🤖", layout="wide")

st.title("🤖 Agent 报告")
st.markdown("### 对话式 AI Agent 生成可追溯的风险简报")

st.markdown("---")

# 检查数据
if st.session_state.get('matched_data') is None:
    st.warning("⚠️ 请先在 **📥 项目/数据导入** 页面加载数据")
    st.stop()

df = st.session_state['matched_data']
result = st.session_state.get('result')

if result is None:
    result = calculations.calc_exposure(df)

# 初始化对话历史
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# ===== 左右分栏 =====
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("💬 对话界面")

    # 对话历史显示
    chat_container = st.container(height=400, border=True)

    with chat_container:
        if len(st.session_state['chat_history']) == 0:
            st.info("""
            👋 **欢迎使用水风险管理 AI Agent!**

            我可以帮助你:
            - 📊 解释当前的风险敞口
            - 🎯 提供情境化目标建议
            - 📄 生成 TNFD LEAP 简报
            - 📥 导出 CDP Water 预填表

            **示例问题**:
            - "我的采购组合水风险如何?"
            - "哪些节点应该优先调整?"
            - "生成完整风险简报"
            """)
        else:
            for msg in st.session_state['chat_history']:
                if msg['role'] == 'user':
                    st.markdown(f"**👤 你**: {msg['content']}")
                else:
                    st.markdown(f"**🤖 Agent**: {msg['content']}")

    # 输入框
    st.markdown("---")

    col_a, col_b = st.columns([4, 1])

    with col_a:
        user_input = st.text_input(
            "输入你的问题",
            placeholder="例如: 我的采购结构有什么问题?",
            label_visibility="collapsed"
        )

    with col_b:
        send_btn = st.button("发送", type="primary", use_container_width=True)

    # 快捷按钮
    st.markdown("**快捷操作**")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📊 风险总览", use_container_width=True):
            user_input = "请告诉我当前采购组合的水风险总览"
            send_btn = True

    with col2:
        if st.button("🎯 目标建议", use_container_width=True):
            user_input = "请给出情境化的采购调整目标建议"
            send_btn = True

    with col3:
        if st.button("📄 生成简报", use_container_width=True):
            user_input = "生成完整的 TNFD LEAP 风险简报"
            send_btn = True

    with col4:
        if st.button("🔄 清空对话", use_container_width=True):
            st.session_state['chat_history'] = []
            st.rerun()

    # 处理输入
    if send_btn and user_input:
        # 添加用户消息
        st.session_state['chat_history'].append({
            'role': 'user',
            'content': user_input
        })

        # 生成 Agent 回复(简化版,不调用真实 API)
        response = generate_agent_response(user_input, df, result)

        # 添加 Agent 回复
        st.session_state['chat_history'].append({
            'role': 'agent',
            'content': response
        })

        st.rerun()

with col2:
    st.subheader("📋 TNFD LEAP 简报")

    # 实时简报侧栏
    with st.container(border=True, height=500):
        st.markdown("### L - Locate (定位)")
        st.markdown(f"""
        - **节点数**: {result['n_nodes']} 个
        - **涉及国家**: {df['国家'].nunique()} 个
        - **原材料**: {df['原材料'].nunique()} 类
        - **高风险节点**: {result['n_high_risk']} 个
        """)

        st.markdown("---")
        st.markdown("### E - Evaluate (评估)")
        st.markdown(f"""
        - **加权敞口**: {result['E_k']:.3f}
        - **高风险占比**: {result['P_h']*100:.1f}%
        - **HHI 集中度**: {result['HHI']:.3f}
        - **前3大贡献**: {result['top3_contrib']*100:.1f}%
        """)

        st.markdown("---")
        st.markdown("### A - Assess (评价)")

        # 情境化目标建议
        suggestions = calculations.suggest_context_based_targets(df)

        if len(suggestions) > 0:
            st.markdown(f"**发现 {len(suggestions)} 个高风险节点需要调整**")
            st.markdown("(详见对话区)")
        else:
            st.markdown("✅ 当前采购结构风险可控")

        st.markdown("---")
        st.markdown("### P - Prepare (准备)")
        st.markdown("""
        **下一步行动**:
        1. 与高风险供应商沟通水管理计划
        2. 评估替代供应商可行性
        3. 建立应急采购预案
        4. 披露 CDP Water / TNFD
        """)

st.markdown("---")

# ===== 导出功能 =====
st.subheader("📥 导出报告")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📄 导出 TNFD LEAP 简报 (DOCX)", use_container_width=True):
        # 生成 DOCX(简化版)
        docx_content = generate_tnfd_report(df, result)
        st.download_button(
            label="下载 DOCX",
            data=docx_content,
            file_name=f"TNFD_LEAP_Report_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
        st.success("✅ 报告已生成(MVP 版本为文本格式,后期将生成完整 DOCX)")

with col2:
    if st.button("📋 导出 CDP Water 预填表 (JSON)", use_container_width=True):
        # 生成 CDP 预填表
        cdp_json = generate_cdp_prefill(df, result)
        st.download_button(
            label="下载 JSON",
            data=cdp_json,
            file_name=f"CDP_Water_Prefill_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )
        st.success("✅ CDP 预填表已生成")

with col3:
    if st.button("💾 保存对话历史", use_container_width=True):
        history_text = "\n\n".join([
            f"[{msg['role'].upper()}] {msg['content']}"
            for msg in st.session_state['chat_history']
        ])
        st.download_button(
            label="下载 TXT",
            data=history_text,
            file_name=f"Chat_History_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )


# ===== Agent 响应生成函数(简化版) =====
def generate_agent_response(user_input: str, df: pd.DataFrame, result: dict) -> str:
    """
    生成 Agent 回复(MVP 版本使用规则,不调用真实 LLM API)
    后期接入 Claude/GPT API
    """
    user_input_lower = user_input.lower()

    # 规则匹配
    if any(k in user_input_lower for k in ['风险', '总览', '如何', '怎么样']):
        return f"""
根据计算结果,你的采购组合水风险状况如下:

**核心指标** [引用:计算引擎]
- 加权水风险敞口: **{result['E_k']:.3f}**
- 高风险采购占比: **{result['P_h']*100:.1f}%** ({result['n_high_risk']} 个节点)
- HHI 集中度: **{result['HHI']:.3f}** {"(⚠️ 偏高,存在单点依赖)" if result['HHI'] > 0.25 else "(正常)"}

**主要风险**:
{', '.join(result['high_risk_nodes'][:3]) if result['high_risk_nodes'] else '无高风险节点'}

**数据来源**: Aqueduct 4.0 基准水压力 [引用:AQD-40]
"""

    elif any(k in user_input_lower for k in ['建议', '目标', '调整', '优先']):
        suggestions = calculations.suggest_context_based_targets(df)

        if len(suggestions) == 0:
            return "✅ 当前采购结构风险可控,无需立即调整。建议定期复核(每季度)。"

        response = f"**情境化目标建议** [基于 SBTN Freshwater 框架]\n\n发现 **{len(suggestions)}** 个高风险节点需要调整:\n\n"

        for i, row in suggestions.head(5).iterrows():
            response += f"""
**{row['node_id']}** - {row['原材料']} ({row['产地']})
- 当前风险: {row['当前风险分数']}
- 当前权重: {row['当前采购权重']}
- 建议: {row['建议目标']}
- 优先级: {row['优先级']}
- 依据: {row['依据']}

"""
        return response

    elif any(k in user_input_lower for k in ['简报', 'tnfd', 'leap']):
        return f"""
**TNFD LEAP 完整简报**

### L - Locate (定位)
你的采购组合涉及 **{result['n_nodes']}** 个节点,分布在 **{df['国家'].nunique()}** 个国家,涵盖 **{df['原材料'].nunique()}** 类原材料。

高风险节点识别: {', '.join(result['high_risk_nodes'][:5]) if result['high_risk_nodes'] else '无'}

### E - Evaluate (评估)
- 加权水风险敞口 Eₖ = **{result['E_k']:.3f}** [引用:计算引擎]
- 高风险采购占比 P_h = **{result['P_h']*100:.1f}%**
- HHI 集中度 = **{result['HHI']:.3f}**

### A - Assess (评价)
基于压力测试,未来 SSP3-RCP7.0 2030 情景下,风险敞口可能上升 10-20%。
建议优先调整 {', '.join(result['high_risk_nodes'][:3])}。

### P - Prepare (准备)
1. 与高风险供应商建立水管理合作(AWS 认证)
2. 增加低风险地区采购占比
3. 建立应急采购预案
4. 披露 CDP Water / TNFD

**完整报告可导出为 DOCX** ↓
"""

    else:
        return f"""
我理解你的问题了。基于当前数据:

- 你有 **{result['n_nodes']}** 个采购节点
- 加权风险敞口为 **{result['E_k']:.3f}**
- {'⚠️ 需要关注高风险节点' if result['n_high_risk'] > 0 else '✅ 整体风险可控'}

你可以问我:
- "哪些节点风险最高?"
- "应该如何调整采购结构?"
- "生成完整 TNFD 简报"
"""


def generate_tnfd_report(df: pd.DataFrame, result: dict) -> str:
    """生成 TNFD LEAP 简报文本(MVP 版本)"""
    report = f"""
水风险管理 AI Agent - TNFD LEAP 简报
生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

========================================
L - Locate (定位)
========================================

节点总数: {result['n_nodes']}
涉及国家: {df['国家'].nunique()}
原材料类别: {df['原材料'].nunique()}
高风险节点: {result['n_high_risk']} 个

========================================
E - Evaluate (评估)
========================================

核心指标:
- 加权水风险敞口 Eₖ: {result['E_k']:.3f}
- 高风险采购占比 P_h: {result['P_h']*100:.1f}%
- HHI 集中度: {result['HHI']:.3f}
- 前3大贡献占比: {result['top3_contrib']*100:.1f}%

数据来源: Aqueduct 4.0 基准水压力 (2023-2024)

========================================
A - Assess (评价)
========================================

{f"识别到 {result['n_high_risk']} 个高风险节点需要关注" if result['n_high_risk'] > 0 else "整体风险可控"}

========================================
P - Prepare (准备)
========================================

建议行动:
1. 与高风险供应商建立水管理合作
2. 评估替代供应商可行性
3. 增加低风险地区采购占比
4. 建立应急采购预案

========================================
附录: 引用列表
========================================

[1] Aqueduct 4.0, WRI, CC BY 4.0
[2] TNFD LEAP 框架
[3] SBTN Freshwater 方法学

本报告由水风险管理 AI Agent 自动生成
MVP 版本 v0.1 | D 组: 赵清莹
"""
    return report


def generate_cdp_prefill(df: pd.DataFrame, result: dict) -> str:
    """生成 CDP Water 预填表(MVP 版本)"""
    import json

    high_risk = df[df['baseline_water_stress'] >= 0.4]

    cdp_data = {
        "W1.2_basin_water_stress": {
            "description": "企业设施所在流域的水压力",
            "data": df.groupby('国家')['baseline_water_stress'].mean().to_dict()
        },
        "W3.3_value_chain_risks": [
            {
                "supplier": row['node_id'],
                "material": row['原材料'],
                "location": f"{row['国家']}/{row['省州']}",
                "risk_type": "Physical - Water stress",
                "risk_level": "High" if row['baseline_water_stress'] > 0.4 else "Medium",
                "exposure_pct": f"{row['采购权重']*100:.1f}%"
            }
            for idx, row in high_risk.iterrows()
        ],
        "W4.1_actions": [
            "建立水管理合作(AWS认证)",
            "评估替代供应商",
            "增加低风险地区采购"
        ],
        "W8.1_targets": {
            "target_description": "降低高风险地区采购占比至 < 30%",
            "baseline_year": 2024,
            "target_year": 2030,
            "context_based": True,
            "framework": "SBTN Freshwater"
        },
        "metadata": {
            "generated_by": "水风险管理 AI Agent MVP v0.1",
            "date": datetime.now().isoformat(),
            "data_source": "Aqueduct 4.0"
        }
    }

    return json.dumps(cdp_data, ensure_ascii=False, indent=2)
