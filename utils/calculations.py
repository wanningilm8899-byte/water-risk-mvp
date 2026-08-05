# -*- coding: utf-8 -*-
"""
水风险管理 AI Agent - 核心计算引擎
所有计算均为确定性函数,可独立复核
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Optional

# ============ 敞口计算 ============

def calc_exposure(df: pd.DataFrame,
                  risk_col: str = "baseline_water_stress") -> Dict:
    """
    计算采购加权水风险敞口
    基于 B 组验证的公式: Eₖ = Σᵢ(wᵢ × rᵢₖ)

    Args:
        df: 节点数据,必须包含 '采购权重' 和风险列
        risk_col: 风险维度列名

    Returns:
        包含 E_k, P_h, HHI, top3_contrib 等指标的字典
    """
    # 权重归一化校验
    total_weight = df['采购权重'].sum()
    if abs(total_weight - 1.0) > 0.01:
        df = df.copy()
        df['采购权重'] = df['采购权重'] / total_weight

    # 如果风险列不存在,用模拟值
    if risk_col not in df.columns:
        df = df.copy()
        df[risk_col] = simulate_risk_scores(df)

    # 采购加权敞口
    E_k = (df['采购权重'] * df[risk_col]).sum()

    # 高风险采购占比(阈值 0.4 源自 Aqueduct 高风险切分)
    HIGH_RISK = 0.4
    P_h = df.loc[df[risk_col] >= HIGH_RISK, '采购权重'].sum()

    # HHI 集中度
    HHI = (df['采购权重'] ** 2).sum()

    # 前3大贡献节点
    df['贡献'] = df['采购权重'] * df[risk_col]
    df_sorted = df.sort_values('贡献', ascending=False)
    top3_contrib = df_sorted.head(3)['贡献'].sum() / E_k if E_k > 0 else 0

    # 高风险节点列表
    high_risk_nodes = df[df[risk_col] >= HIGH_RISK]['node_id'].tolist()

    return {
        "E_k": round(float(E_k), 4),
        "P_h": round(float(P_h), 4),
        "HHI": round(float(HHI), 4),
        "top3_contrib": round(float(top3_contrib), 4),
        "n_nodes": len(df),
        "high_risk_threshold": HIGH_RISK,
        "high_risk_nodes": high_risk_nodes,
        "n_high_risk": len(high_risk_nodes)
    }

# ============ 压力测试 ============

def apply_scenario(df: pd.DataFrame,
                   scenario: str,
                   risk_col: str = "baseline_water_stress",
                   year: int = 2030,
                   disrupt_nodes: Optional[List[str]] = None,
                   disrupt_ratio: float = 0.5) -> pd.DataFrame:
    """
    应用压力测试情景,返回调整后的数据框
    基于 C 组推荐的 3 类情景

    Args:
        df: 原始节点数据
        scenario: '基准' / '旱季供水下降' / '极端干旱' / '供应商单点失效'
        year: 未来情景年份
        disrupt_nodes: 中断的节点 ID 列表
        disrupt_ratio: 中断比例(0-1)

    Returns:
        调整后的数据框
    """
    df_new = df.copy()

    # 确保有风险列
    if risk_col not in df_new.columns:
        df_new[risk_col] = simulate_risk_scores(df_new)

    if scenario == "基准":
        pass  # 不做任何改动

    elif scenario == "旱季供水下降":
        # 将风险值 +10% (模拟未来 SSP3-RCP7.0)
        df_new[risk_col] = np.clip(df_new[risk_col] * 1.1, 0, 1)

    elif scenario == "极端干旱":
        # 将风险值 +20%
        df_new[risk_col] = np.clip(df_new[risk_col] * 1.2, 0, 1)

    elif scenario == "供应商单点失效":
        if disrupt_nodes:
            for node in disrupt_nodes:
                mask = df_new['node_id'] == node
                df_new.loc[mask, '采购权重'] *= (1 - disrupt_ratio)

        # 归一化权重
        total = df_new['采购权重'].sum()
        if total > 0:
            df_new['采购权重'] = df_new['采购权重'] / total

    # 重新计算贡献
    df_new['贡献'] = df_new['采购权重'] * df_new[risk_col]

    return df_new

# ============ 情境化目标建议 ============

def suggest_context_based_targets(df: pd.DataFrame,
                                   risk_col: str = "baseline_water_stress",
                                   threshold: float = 0.4) -> pd.DataFrame:
    """
    根据流域水压力等级建议采购占比调整目标
    基于 SBTN Freshwater 框架(借鉴 Water Navigator IQ)

    Returns:
        包含建议目标的数据框
    """
    high_risk = df[df[risk_col] >= threshold].copy()

    suggestions = []
    for idx, row in high_risk.iterrows():
        current_weight = row['采购权重']
        risk_score = row[risk_col]

        if risk_score >= 0.8:
            target = "建议退出或建立水管理合作(AWS认证)"
            priority = "高"
        elif risk_score >= 0.4:
            target = f"建议降至 < 20% (当前 {current_weight*100:.0f}%)"
            priority = "中"
        elif risk_score >= 0.2:
            target = f"建议降至 < 30% (当前 {current_weight*100:.0f}%)"
            priority = "低"
        else:
            continue

        suggestions.append({
            "node_id": row["node_id"],
            "原材料": row["原材料"],
            "产地": f"{row['国家']}/{row['省州']}",
            "当前风险分数": f"{risk_score:.2f}",
            "当前采购权重": f"{current_weight*100:.1f}%",
            "建议目标": target,
            "优先级": priority,
            "依据": "基于 Aqueduct 4.0 + SBTN Freshwater"
        })

    return pd.DataFrame(suggestions)

# ============ 数据质量评估 ============

def assess_data_quality(df: pd.DataFrame) -> Dict:
    """
    评估数据质量(借鉴 Water Navigator IQ 的质量仪表盘)

    Returns:
        质量指标字典
    """
    total = len(df)

    # 5 个维度
    metrics = {
        "字段完整度": df.notna().mean().mean(),
        "坐标有效率": ((df['纬度'].between(-90, 90)) &
                     (df['经度'].between(-180, 180))).mean(),
        "权重归一化": 1.0 if abs(df['采购权重'].sum() - 1.0) < 0.01 else 0.5,
        "来源可追溯率": df['来源'].notna().mean(),
    }

    # 数据性质分布
    nature_dist = df['数据性质'].value_counts(normalize=True).to_dict()

    # 整体评级
    avg_score = np.mean(list(metrics.values()))
    if avg_score >= 0.9:
        grade = "A"
        color = "green"
    elif avg_score >= 0.7:
        grade = "B"
        color = "yellow"
    elif avg_score >= 0.5:
        grade = "C"
        color = "orange"
    else:
        grade = "D"
        color = "red"

    return {
        "metrics": metrics,
        "nature_dist": nature_dist,
        "grade": grade,
        "color": color,
        "avg_score": round(avg_score, 3)
    }

# ============ 辅助函数 ============

def simulate_risk_scores(df: pd.DataFrame) -> pd.Series:
    """
    模拟风险分数(MVP 演示用,后期用真实 Aqueduct 数据)
    根据国家给出合理的风险值
    """
    country_risk_map = {
        'CHN': 0.42,
        'BRA': 0.18,
        'USA': 0.28,
        'ARG': 0.15,
        'MYS': 0.32,
        'NZL': 0.08,
        'IDN': 0.35,
        'IND': 0.65,
    }

    # 添加一些随机扰动
    np.random.seed(42)
    risks = df['国家'].map(country_risk_map).fillna(0.3)
    risks += np.random.normal(0, 0.05, len(df))
    risks = np.clip(risks, 0, 1)

    return pd.Series(risks, index=df.index)

def get_risk_alerts(result: Dict) -> List[Dict]:
    """
    生成风险通知(借鉴 Water Navigator IQ)

    Returns:
        通知列表,每个通知包含 text, color, action
    """
    alerts = []

    if result["P_h"] > 0.4:
        alerts.append({
            "text": f"⚠️ 警告: 超过 {result['P_h']*100:.0f}% 采购来自高风险地区",
            "color": "red",
            "action": "查看页面三风险敞口明细"
        })

    if result["HHI"] > 0.25:
        alerts.append({
            "text": f"⚠️ 警告: 采购集中度 HHI={result['HHI']:.2f} 过高,存在单点依赖风险",
            "color": "orange",
            "action": "查看页面四供应商中断情景"
        })

    if result["n_high_risk"] > 0:
        alerts.append({
            "text": f"🔍 发现 {result['n_high_risk']} 个高风险节点",
            "color": "yellow",
            "action": "查看节点详情"
        })

    return alerts
