# -*- coding: utf-8 -*-
"""
水风险管理 AI Agent - 数据访问层
关键设计:统一接口,现在用 CSV,后期换数据库只改这个文件
"""
import pandas as pd
import json
from pathlib import Path
from typing import Optional, List, Dict

# 数据目录
DATA_DIR = Path(__file__).parent.parent / "data"

# ============ 统一数据接口(后期可切换到数据库) ============

def load_sample_nodes(version: str = "v1") -> pd.DataFrame:
    """
    加载采购节点样本数据
    现在:从 CSV 读取
    后期:从数据库 SELECT * FROM procurement_nodes WHERE version = ?
    """
    csv_path = DATA_DIR / f"sample_nodes_{version}.csv"
    if csv_path.exists():
        return pd.read_csv(csv_path)
    else:
        # 返回空模板
        return pd.DataFrame(columns=[
            'node_id', '原材料', '供应商', '国家', '省州',
            '纬度', '经度', '采购权重', '数据性质', '来源'
        ])

def get_risk_score(lat: float, lon: float,
                   indicator: str = "baseline_water_stress") -> Optional[float]:
    """
    根据坐标查询风险分数
    现在:从预处理 CSV 读取(简化为国家级兜底)
    后期:空间数据库查询 SELECT risk FROM aqueduct_basin WHERE ST_Contains(geom, ST_Point(lon, lat))
    """
    # 简化版:国家级兜底映射
    country_risk = {
        'CHN': {'baseline_water_stress': 0.42, 'drought_risk': 0.35},
        'BRA': {'baseline_water_stress': 0.18, 'drought_risk': 0.25},
        'USA': {'baseline_water_stress': 0.28, 'drought_risk': 0.30},
        'ARG': {'baseline_water_stress': 0.15, 'drought_risk': 0.22},
        'MYS': {'baseline_water_stress': 0.32, 'drought_risk': 0.28},
    }
    # 后期会通过坐标→流域→风险的完整链路
    return None  # MVP 阶段先返回 None,在计算层模拟

def get_industry_materials(industry_code: str) -> List[str]:
    """
    ENCORE 行业→原材料映射
    现在:从 JSON 文件
    后期:从数据库 SELECT material FROM encore_mapping WHERE industry = ?
    """
    json_path = DATA_DIR / "industry_material_map.json"
    if json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            mapping = json.load(f)
        return mapping.get(industry_code, [])
    else:
        # 默认候选(基于 A 组推荐)
        return ['甘蔗', '甜菜', '大豆', '玉米', '番茄', '原奶', '棕榈', '茶叶']

def save_user_upload(df: pd.DataFrame, session_id: str) -> bool:
    """
    保存用户上传数据
    现在:存到 session state + 可选写 CSV
    后期:写入数据库 INSERT INTO user_uploads (session_id, data, timestamp)
    """
    # MVP 阶段只返回成功,实际存在 st.session_state
    return True

def get_aqueduct_metadata() -> Dict:
    """
    获取 Aqueduct 数据源元数据
    现在:硬编码
    后期:从数据库 SELECT * FROM data_sources WHERE id = 'aqueduct_4.0'
    """
    return {
        "id": "AQD-40",
        "name": "Aqueduct 4.0",
        "version": "4.0",
        "download_date": "2026-08-01",
        "license": "CC BY 4.0",
        "source_url": "https://www.wri.org/applications/aqueduct/water-risk-atlas",
        "indicators": [
            "baseline_water_stress",
            "water_stress_2030_ssp3",
            "drought_risk",
            "seasonal_variability"
        ]
    }

def log_access(user_id: str, action: str, data_id: str):
    """
    记录数据访问日志
    现在:写本地 log 文件
    后期:INSERT INTO access_logs (user_id, action, data_id, timestamp)
    """
    log_path = DATA_DIR.parent / "logs" / "access.log"
    log_path.parent.mkdir(exist_ok=True)

    from datetime import datetime
    ts = datetime.now().isoformat()
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{ts} | {user_id} | {action} | {data_id}\n")

# ============ 示例数据生成(MVP 演示用) ============

def generate_sample_data() -> pd.DataFrame:
    """
    生成 10 个示例节点(基于 B 组验证的行业与原材料)
    """
    import numpy as np
    np.random.seed(42)

    materials_data = [
        ('甘蔗', 'BRA', '圣保罗', -23.55, -46.63),
        ('甜菜', 'CHN', '新疆', 43.82, 87.62),
        ('大豆', 'USA', '爱荷华', 41.88, -93.10),
        ('玉米', 'ARG', '布宜诺斯艾利斯', -34.60, -58.38),
        ('番茄', 'CHN', '山东', 36.67, 117.00),
        ('原奶', 'NZL', '奥克兰', -36.85, 174.76),
        ('棕榈', 'MYS', '沙巴', 5.98, 116.07),
        ('茶叶', 'CHN', '云南', 25.04, 102.71),
        ('大豆', 'BRA', '马托格罗索', -15.60, -56.10),
        ('甘蔗', 'CHN', '广西', 23.10, 108.37),
    ]

    nodes = []
    for i, (material, country, province, lat, lon) in enumerate(materials_data):
        node_id = f"S{i+1:03d}"
        weight = np.random.dirichlet(np.ones(10))[i]  # 归一化权重

        nodes.append({
            'node_id': node_id,
            '原材料': material,
            '供应商': f'{province}{material}供应商',
            '国家': country,
            '省州': province,
            '纬度': lat,
            '经度': lon,
            '采购权重': weight,
            '数据性质': np.random.choice(['真实披露', '工作假设', '模拟'], p=[0.3, 0.5, 0.2]),
            '来源': 'MVP 演示样本数据'
        })

    df = pd.DataFrame(nodes)
    # 归一化权重
    total_weight = df['采购权重'].sum()
    df['采购权重'] = df['采购权重'] / total_weight
    return df

# ============ 初始化:生成示例数据 ============

def init_sample_data():
    """初始化示例数据文件"""
    sample_path = DATA_DIR / "sample_nodes_v1.csv"
    if not sample_path.exists():
        df = generate_sample_data()
        DATA_DIR.mkdir(exist_ok=True)
        df.to_csv(sample_path, index=False, encoding='utf-8-sig')
        print(f"[OK] Generated sample data: {sample_path}")

    # 生成行业映射
    map_path = DATA_DIR / "industry_material_map.json"
    if not map_path.exists():
        mapping = {
            "C13": ["大豆", "玉米", "油菜籽", "甘蔗", "甜菜"],
            "C14": ["番茄", "水稻", "茶叶", "原奶"],
            "C15": ["甘蔗", "水稻", "茶叶", "棕榈"]
        }
        with open(map_path, 'w', encoding='utf-8') as f:
            json.dump(mapping, f, ensure_ascii=False, indent=2)
        print(f"[OK] Generated industry mapping: {map_path}")

if __name__ == "__main__":
    init_sample_data()
