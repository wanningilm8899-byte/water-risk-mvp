# -*- coding: utf-8 -*-
"""Shared content configuration for the Streamlit site."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List


DATA_DIR = Path(__file__).parent.parent / "data"
CONTENT_PATH = DATA_DIR / "site_content.json"


DEFAULT_CONTENT: Dict[str, Any] = {
    "project": {
        "name": "水风险管理 AI Agent",
        "subtitle": "面向科技农食企业供应链的轻量级水风险评估平台",
        "version": "MVP v0.2 初步设计版",
        "owner": "D 组",
        "last_updated": "2026-08-07",
        "design_goal": "先完成可演示网站外壳、视觉风格与核心流程；ABC 组未定信息以可替换模块保留。"
    },
    "groups": [],
    "milestones": [],
    "editable_notes": []
}


@lru_cache(maxsize=1)
def load_site_content() -> Dict[str, Any]:
    """Load editable content. Falls back to defaults if the JSON is unavailable."""
    if not CONTENT_PATH.exists():
        return DEFAULT_CONTENT

    with open(CONTENT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    merged = DEFAULT_CONTENT.copy()
    merged.update(data)
    return merged


def get_project() -> Dict[str, str]:
    return load_site_content().get("project", DEFAULT_CONTENT["project"])


def get_groups() -> List[Dict[str, Any]]:
    return load_site_content().get("groups", [])


def get_milestones() -> List[Dict[str, str]]:
    return load_site_content().get("milestones", [])


def get_editable_notes() -> List[str]:
    return load_site_content().get("editable_notes", [])
