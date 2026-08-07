# -*- coding: utf-8 -*-
"""Reusable UI helpers and visual theme for the MVP site."""
from __future__ import annotations

from html import escape
from typing import Dict, Iterable, List, Optional

import streamlit as st

from utils import site_content


RISK_COLORS = {
    "red": "#dc2626",
    "orange": "#ea580c",
    "yellow": "#ca8a04",
    "green": "#16a34a"
}


def apply_global_styles() -> None:
    """Apply the shared visual system."""
    st.markdown(
        """
        <style>
        :root {
            --ink: #102a2b;
            --muted: #6e7d82;
            --line: #dfe8e5;
            --panel: #ffffff;
            --wash: #f7faf8;
            --nav: #0b3032;
            --nav-2: #123f41;
            --nav-text: #c7dbd7;
            --aqua: #6dd6cc;
            --teal: #0b8f84;
            --teal-dark: #073536;
            --teal-soft: #e3f4f1;
            --green-soft: #e5f6eb;
            --amber: #d58b21;
            --amber-soft: #fff1d8;
            --red: #c44937;
            --red-soft: #fee8e3;
            --shadow: 0 12px 30px rgba(16, 42, 43, 0.08);
        }

        .stApp {
            background: var(--wash);
            color: var(--ink);
        }

        .block-container {
            padding-top: 1.55rem;
            padding-bottom: 3rem;
            max-width: 1550px;
        }

        h1, h2, h3, h4, h5, h6 {
            color: var(--ink);
            letter-spacing: 0;
        }

        header[data-testid="stHeader"] {
            background: rgba(247,250,248,0.86);
            border-bottom: 1px solid rgba(223,232,229,0.8);
            backdrop-filter: blur(12px);
        }

        section[data-testid="stSidebar"],
        section[data-testid="stSidebar"] > div,
        div[data-testid="stSidebar"],
        div[data-testid="stSidebar"] > div {
            background: var(--nav);
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        section[data-testid="stSidebar"] .st-emotion-cache-1cypcdb,
        section[data-testid="stSidebar"] .st-emotion-cache-6qob1r {
            background: var(--nav);
        }

        div[data-testid="stSidebar"] * {
            color: var(--nav-text);
        }

        div[data-testid="stSidebarNav"] {
            display: none;
        }

        div[data-testid="stSidebar"] a,
        section[data-testid="stSidebar"] a {
            color: var(--nav-text) !important;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 700;
        }

        div[data-testid="stSidebar"] a:hover,
        section[data-testid="stSidebar"] a:hover {
            background: rgba(255,255,255,0.06);
        }

        div[data-testid="stMetric"] {
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 14px 16px;
            box-shadow: 0 8px 22px rgba(18, 36, 30, 0.05);
        }

        div[data-testid="stMetricValue"] {
            color: var(--teal);
        }

        div.stButton > button,
        div[data-testid="stDownloadButton"] > button {
            border-radius: 8px;
            border: 1px solid #b7cac3;
            color: var(--ink);
            background: #ffffff;
            min-height: 40px;
        }

        div.stButton > button[kind="primary"],
        div.stButton > button:hover,
        div[data-testid="stDownloadButton"] > button:hover {
            border-color: var(--teal);
            color: var(--teal);
        }

        .wp-shell-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
            border-bottom: 1px solid var(--line);
            padding-bottom: 18px;
            margin-bottom: 24px;
        }

        .wp-breadcrumb {
            color: #8a9a9d;
            font-size: 14px;
            font-weight: 650;
        }

        .wp-breadcrumb strong {
            color: var(--ink);
        }

        .wp-top-actions {
            display: flex;
            align-items: center;
            justify-content: flex-end;
            gap: 10px;
            flex-wrap: wrap;
        }

        .wp-status-chip {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: 1px solid var(--line);
            border-radius: 8px;
            background: #fff;
            color: #496164;
            padding: 7px 12px;
            font-size: 13px;
            font-weight: 700;
        }

        .wp-dot {
            width: 8px;
            height: 8px;
            border-radius: 999px;
            background: #37a36e;
            display: inline-block;
        }

        .wr-hero {
            border: 1px solid var(--line);
            border-radius: 8px;
            background:
                linear-gradient(135deg, rgba(227,244,241,0.95), rgba(255,255,255,0.98) 50%, rgba(255,247,232,0.92)),
                #ffffff;
            padding: 28px 32px;
            margin: 4px 0 22px;
            box-shadow: var(--shadow);
        }

        .wr-kicker {
            color: var(--teal);
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 0;
            margin-bottom: 8px;
        }

        .wr-title {
            color: var(--ink);
            font-size: clamp(30px, 3.4vw, 48px);
            line-height: 1.08;
            font-weight: 800;
            letter-spacing: 0;
            margin: 0 0 12px;
        }

        .wr-subtitle {
            color: var(--muted);
            font-size: 17px;
            line-height: 1.65;
            max-width: 850px;
            margin: 0;
        }

        .wr-pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 20px;
        }

        .wr-pill {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            border: 1px solid #b8d8d1;
            background: rgba(255,255,255,0.78);
            color: #31534c;
            font-size: 13px;
            padding: 7px 11px;
            white-space: nowrap;
        }

        .wr-section-title {
            color: var(--ink);
            font-size: 22px;
            line-height: 1.25;
            font-weight: 760;
            margin: 10px 0 8px;
        }

        .wr-muted {
            color: var(--muted);
            font-size: 14px;
            line-height: 1.55;
        }

        .wr-card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 14px;
            margin: 12px 0 22px;
        }

        .wr-card {
            background: var(--panel);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 17px 18px;
            box-shadow: var(--shadow);
            min-height: 142px;
        }

        .wr-card h3 {
            font-size: 17px;
            line-height: 1.32;
            margin: 0 0 8px;
        }

        .wr-card p {
            color: var(--muted);
            font-size: 14px;
            line-height: 1.58;
            margin: 0;
        }

        .wr-tag {
            display: inline-block;
            border-radius: 999px;
            background: var(--teal-soft);
            color: var(--teal);
            font-size: 12px;
            font-weight: 700;
            padding: 4px 8px;
            margin-bottom: 10px;
        }

        .wr-tag-amber {
            background: #fff0c2;
            color: #8a4b00;
        }

        .wr-tag-plum {
            background: #ebe7ff;
            color: var(--plum);
        }

        .wr-status-strip {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 10px;
            margin: 12px 0 18px;
        }

        .wr-status-item {
            background: rgba(255,255,255,0.82);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 12px 14px;
        }

        .wr-status-label {
            color: var(--muted);
            font-size: 12px;
            margin-bottom: 4px;
        }

        .wr-status-value {
            color: var(--ink);
            font-weight: 760;
            font-size: 15px;
        }

        .wr-page-head {
            margin: 0 0 20px;
            padding: 0 0 4px;
        }

        .wr-page-head h1 {
            font-size: 34px;
            line-height: 1.16;
            margin: 0 0 8px;
        }

        .wr-page-head p {
            color: var(--muted);
            font-size: 15px;
            line-height: 1.58;
            margin: 0;
        }

        .wr-alert {
            border-radius: 8px;
            border: 1px solid #f0d3a1;
            background: #fff8e8;
            padding: 12px 14px;
            color: #68420d;
            margin: 8px 0;
        }

        .wr-alert strong {
            color: #3f2a0a;
        }

        .wp-logo {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 24px 10px 20px;
        }

        .wp-logo-mark {
            width: 34px;
            height: 34px;
            border: 2px solid var(--aqua);
            border-radius: 50% 50% 50% 8px;
            transform: rotate(-45deg);
            flex: 0 0 auto;
        }

        .wp-logo-title {
            color: #ffffff;
            font-size: 20px;
            font-weight: 820;
            line-height: 1.05;
        }

        .wp-logo-sub {
            color: #75aaa7;
            font-size: 11px;
            letter-spacing: 1.7px;
            line-height: 1.25;
            font-weight: 760;
        }

        .wp-project-card {
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 8px;
            padding: 16px 17px;
            margin: 0 8px 28px;
        }

        .wp-project-label {
            color: #76a5a1;
            font-size: 12px;
            font-weight: 700;
            margin-bottom: 7px;
        }

        .wp-project-title {
            color: #fff;
            font-size: 17px;
            line-height: 1.35;
            font-weight: 820;
            margin-bottom: 6px;
        }

        .wp-project-meta {
            color: #91b8b4;
            font-size: 12px;
            line-height: 1.45;
        }

        .wp-side-heading {
            color: #669693;
            font-size: 12px;
            font-weight: 760;
            letter-spacing: 0.5px;
            margin: 18px 10px 8px;
        }

        .wp-side-item {
            display: grid;
            grid-template-columns: 24px 22px 1fr;
            align-items: center;
            gap: 8px;
            padding: 10px 12px;
            border-radius: 8px;
            margin: 4px 2px;
            color: var(--nav-text);
            font-size: 15px;
            font-weight: 650;
        }

        div[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"],
        section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {
            min-height: 38px;
            padding-left: 10px;
            margin: 2px 0 2px 6px;
        }

        div[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] *,
        section[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] * {
            color: var(--nav-text) !important;
            font-weight: 760 !important;
        }

        .wp-side-item.active {
            background: rgba(255,255,255,0.10);
            color: #ffffff;
            box-shadow: inset 4px 0 0 var(--aqua);
        }

        .wp-side-icon,
        .wp-side-num {
            color: #84b7b3;
            font-weight: 760;
            text-align: center;
        }

        .wp-side-footer {
            border-top: 1px solid rgba(255,255,255,0.09);
            margin: 28px 4px 0;
            padding: 16px 8px 4px;
            color: #91b8b4;
            font-size: 12px;
            line-height: 1.55;
        }

        .wp-panel {
            background: #fff;
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 20px 22px;
        }

        .wp-panel-tight {
            background: #fff;
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 16px 18px;
        }

        .wp-metric-card {
            position: relative;
            background: #fff;
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 20px 22px 18px 28px;
            min-height: 128px;
            overflow: hidden;
        }

        .wp-metric-card::before {
            content: "";
            position: absolute;
            top: 23px;
            bottom: 23px;
            left: 14px;
            width: 8px;
            border-radius: 99px;
            background: var(--teal);
        }

        .wp-metric-card.amber::before { background: var(--amber); }
        .wp-metric-card.red::before { background: var(--red); }
        .wp-metric-card.green::before { background: #369869; }

        .wp-metric-label {
            color: #637579;
            font-size: 13px;
            font-weight: 780;
            margin-bottom: 6px;
        }

        .wp-metric-value {
            color: var(--ink);
            font-size: 36px;
            line-height: 1.05;
            font-weight: 840;
            letter-spacing: 0;
        }

        .wp-metric-value small {
            color: #9aa9ad;
            font-size: 16px;
            font-weight: 720;
        }

        .wp-metric-foot {
            color: #88989b;
            font-size: 12px;
            margin-top: 9px;
            font-weight: 650;
        }

        .wp-badge {
            display: inline-flex;
            align-items: center;
            border-radius: 999px;
            padding: 4px 9px;
            font-size: 12px;
            font-weight: 760;
            margin: 2px 4px 2px 0;
            background: var(--teal-soft);
            color: var(--teal);
            white-space: nowrap;
        }

        .wp-badge.green { background: var(--green-soft); color: #287a4d; }
        .wp-badge.amber { background: var(--amber-soft); color: #9a5c10; }
        .wp-badge.red { background: var(--red-soft); color: var(--red); }
        .wp-badge.gray { background: #eef2f1; color: #667477; }

        .wp-progress {
            display: grid;
            grid-template-columns: repeat(7, minmax(72px, 1fr));
            gap: 6px;
            align-items: start;
            margin: 18px 0 8px;
        }

        .wp-progress-step {
            position: relative;
            text-align: center;
            color: #8a989c;
            font-size: 12px;
            font-weight: 700;
        }

        .wp-progress-dot {
            width: 34px;
            height: 34px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            background: #f0f5f3;
            border: 2px solid #d8e3df;
            color: #789097;
            margin-bottom: 8px;
        }

        .wp-progress-step.done .wp-progress-dot {
            background: var(--teal);
            color: #fff;
            border-color: var(--teal);
        }

        .wp-progress-step.active .wp-progress-dot {
            background: #fff;
            color: var(--teal);
            border-color: var(--teal);
        }

        .wp-list {
            display: grid;
            gap: 12px;
        }

        .wp-list-item {
            display: grid;
            grid-template-columns: 10px 1fr;
            gap: 12px;
            padding-bottom: 12px;
            border-bottom: 1px solid #edf2f0;
        }

        .wp-list-item:last-child { border-bottom: none; padding-bottom: 0; }
        .wp-bullet { width: 8px; height: 8px; border-radius: 999px; margin-top: 7px; background: var(--teal); }
        .wp-bullet.amber { background: var(--amber); }
        .wp-bullet.red { background: var(--red); }

        .wp-table-wrap {
            background: #fff;
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: var(--shadow);
            padding: 10px 10px 4px;
        }

        .wr-footer {
            color: var(--muted);
            border-top: 1px solid var(--line);
            margin-top: 24px;
            padding: 18px 0 4px;
            text-align: center;
            font-size: 13px;
        }

        @media (max-width: 760px) {
            .wr-hero {
                padding: 22px 18px;
            }
            .wr-title {
                font-size: 34px;
            }
            .wr-status-strip {
                grid-template-columns: 1fr;
            }
            .wp-progress {
                grid-template-columns: repeat(2, 1fr);
            }
            .wp-shell-top {
                align-items: flex-start;
                flex-direction: column;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def render_sidebar(active: str = "首页总览") -> None:
    """Render the custom WaterPulse-style sidebar."""
    items = [
        ("首页总览", "0", "⌂", "首页.py"),
        ("数据导入", "1", "↥", "pages/1_📥_项目数据导入.py"),
        ("数据资源库", "2", "◉", None),
        ("供应链地图", "3", "▱", "pages/2_🗺️_供应链地图.py"),
        ("风险敞口", "4", "◌", "pages/3_📊_风险敞口.py"),
        ("压力测试", "5", "☁", "pages/4_🔮_压力测试.py"),
        ("Agent 分析", "6", "☷", "pages/5_🤖_Agent报告.py"),
        ("报告导出", "7", "▤", None),
    ]

    with st.sidebar:
        st.markdown(
            """
            <div class="wp-logo">
                <div class="wp-logo-mark"></div>
                <div>
                    <div class="wp-logo-title">水脉 WaterPulse</div>
                    <div class="wp-logo-sub">UPSTREAM WATER RISK<br>AGENT</div>
                </div>
            </div>
            <div class="wp-project-card">
                <div class="wp-project-label">当前项目</div>
                <div class="wp-project-title">甲公司 · 植物基蛋白原料</div>
                <div class="wp-project-meta">C14 食品制造业 · 2026 评估年度</div>
            </div>
            <div class="wp-side-heading">分析流程</div>
            """,
            unsafe_allow_html=True
        )

        for label, num, icon, target in items:
            if target and label != active:
                st.page_link(target, label=f"{icon}  {num}  {label}")
            else:
                class_name = "wp-side-item active" if label == active else "wp-side-item"
                st.markdown(
                    f'<div class="{class_name}"><span class="wp-side-icon">{escape(icon)}</span>'
                    f'<span class="wp-side-num">{escape(num)}</span><span>{escape(label)}</span></div>',
                    unsafe_allow_html=True
                )

        st.markdown(
            """
            <div class="wp-side-heading">系统</div>
            <div class="wp-side-item"><span class="wp-side-icon">⚙</span><span class="wp-side-num">·</span><span>设置 / 审计日志</span></div>
            <div class="wp-side-footer">
                <div>● 本地资料库已连接 · L2 服务层</div>
                <div style="margin-top:12px;"><strong style="color:#fff;">D 组 · MVP 负责</strong><br>研究原型 · 可远程部署</div>
            </div>
            """,
            unsafe_allow_html=True
        )


def render_topbar(page_title: str, right: str = "大模型 API 已连接") -> None:
    st.markdown(
        f"""
        <div class="wp-shell-top">
            <div class="wp-breadcrumb">水脉 WaterPulse&nbsp;&nbsp;/&nbsp;&nbsp;<strong>{escape(page_title)}</strong></div>
            <div class="wp-top-actions">
                <span class="wp-status-chip"><span class="wp-dot"></span>{escape(right)}</span>
                <span class="wp-status-chip">规则降级模式可切换</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_page_header(title: str, subtitle: str, kicker: str = "MVP 工作台") -> None:
    st.markdown(
        f"""
        <div class="wr-page-head">
            <div class="wr-kicker">{escape(kicker)}</div>
            <h1>{escape(title)}</h1>
            <p>{escape(subtitle)}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_metric_card(label: str, value: str, foot: str, tone: str = "") -> None:
    st.markdown(
        f"""
        <div class="wp-metric-card {escape(tone)}">
            <div class="wp-metric-label">{escape(label)}</div>
            <div class="wp-metric-value">{value}</div>
            <div class="wp-metric-foot">{escape(foot)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_progress(active_step: int = 4) -> None:
    labels = ["数据导入", "数据校验", "位置匹配", "敞口计算", "压力测试", "Agent 解释", "报告导出"]
    html = []
    for index, label in enumerate(labels, start=1):
        state = "done" if index < active_step else "active" if index == active_step else ""
        symbol = "✓" if index < active_step else str(index)
        sub = "已完成" if index < active_step else "进行中" if index == active_step else "未开始"
        html.append(
            f'<div class="wp-progress-step {state}">'
            f'<div class="wp-progress-dot">{escape(symbol)}</div>'
            f'<div>{escape(label)}</div>'
            f'<div class="wr-muted">{escape(sub)}</div>'
            f'</div>'
        )
    st.markdown(f'<div class="wp-progress">{"".join(html)}</div>', unsafe_allow_html=True)


def render_badges(labels: Iterable[str], tone: str = "green") -> None:
    html = "".join([f'<span class="wp-badge {escape(tone)}">{escape(label)}</span>' for label in labels])
    st.markdown(html, unsafe_allow_html=True)


def render_list(items: List[Dict[str, str]]) -> None:
    html = []
    for item in items:
        tone = item.get("tone", "")
        html.append(
            f'<div class="wp-list-item">'
            f'<span class="wp-bullet {escape(tone)}"></span>'
            f'<div><strong>{escape(item.get("title", ""))}</strong>'
            f'<div class="wr-muted">{escape(item.get("body", ""))}</div></div>'
            f'</div>'
        )
    st.markdown(f'<div class="wp-list">{"".join(html)}</div>', unsafe_allow_html=True)


def render_hero() -> None:
    project = site_content.get_project()
    st.markdown(
        f"""
        <section class="wr-hero">
            <div class="wr-kicker">一天内完成的网页初步设计 · 可替换信息已预留</div>
            <h1 class="wr-title">{escape(project["name"])}</h1>
            <p class="wr-subtitle">{escape(project["subtitle"])}。{escape(project["design_goal"])}</p>
            <div class="wr-pill-row">
                <span class="wr-pill">{escape(project["version"])}</span>
                <span class="wr-pill">负责人：{escape(project["owner"])}</span>
                <span class="wr-pill">更新：{escape(project["last_updated"])}</span>
                <span class="wr-pill">ABC 组信息可替换</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True
    )


def render_status_strip() -> None:
    milestones = site_content.get_milestones()
    if not milestones:
        return

    items = []
    for item in milestones:
        items.append(
            f'<div class="wr-status-item">'
            f'<div class="wr-status-label">{escape(item.get("date", ""))} · {escape(item.get("status", ""))}</div>'
            f'<div class="wr-status-value">{escape(item.get("title", ""))}</div>'
            f'<div class="wr-muted">{escape(item.get("description", ""))}</div>'
            f'</div>'
        )

    st.markdown(
        f"""<div class="wr-status-strip">{''.join(items)}</div>""",
        unsafe_allow_html=True
    )


def render_group_cards() -> None:
    cards = []
    tag_class = {"A": "", "B": "wr-tag-amber", "C": "wr-tag-plum"}

    for group in site_content.get_groups():
        slots = group.get("editable_slots", [])
        hooks = group.get("page_hooks", [])
        cards.append(
            f'<article class="wr-card">'
            f'<span class="wr-tag {tag_class.get(group.get("key"), "")}">{escape(group.get("name", ""))} · 可修改</span>'
            f'<h3>{escape(group.get("theme", ""))}</h3>'
            f'<p><strong>当前状态：</strong>{escape(group.get("current_status", ""))}</p>'
            f'<p><strong>预留内容：</strong>{escape(" / ".join(slots[:3]))}</p>'
            f'<p><strong>影响页面：</strong>{escape("、".join(hooks[:3]))}</p>'
            f'</article>'
        )

    st.markdown(
        f"""<div class="wr-card-grid">{''.join(cards)}</div>""",
        unsafe_allow_html=True
    )


def render_feature_cards(cards: Iterable[Dict[str, str]]) -> None:
    html_cards = []
    for item in cards:
        html_cards.append(
            f'<article class="wr-card">'
            f'<span class="wr-tag">{escape(item.get("tag", ""))}</span>'
            f'<h3>{escape(item.get("title", ""))}</h3>'
            f'<p>{escape(item.get("body", ""))}</p>'
            f'</article>'
        )

    st.markdown(
        f"""<div class="wr-card-grid">{''.join(html_cards)}</div>""",
        unsafe_allow_html=True
    )


def render_editable_notice(context: Optional[str] = None) -> None:
    notes = site_content.get_editable_notes()
    note_text = " ".join(notes[:2]) if notes else "ABC 组未定信息已集中预留。"
    if context:
        note_text = f"{context} {note_text}"

    st.markdown(
        f"""
        <div class="wr-alert">
            <strong>可修改信息提示：</strong>{escape(note_text)}
        </div>
        """,
        unsafe_allow_html=True
    )


def render_risk_alerts(result: Optional[Dict]) -> None:
    if not result:
        return

    from utils import calculations

    for alert in calculations.get_risk_alerts(result):
        color = RISK_COLORS.get(alert.get("color"), "#ca8a04")
        st.markdown(
            f"""
            <div class="wr-alert" style="border-color:{color}33;background:{color}10;">
                <strong style="color:{color};">{escape(alert.get("text", ""))}</strong>
                <span> | {escape(alert.get("action", ""))}</span>
            </div>
            """,
            unsafe_allow_html=True
        )


def render_footer() -> None:
    project = site_content.get_project()
    st.markdown(
        f"""
        <div class="wr-footer">
            {escape(project["name"])} · {escape(project["version"])} · {escape(project["owner"])} · 本项目为研究原型，不构成专业咨询建议
        </div>
        """,
        unsafe_allow_html=True
    )
