# 水风险管理 AI Agent - MVP v0.1

## 📋 项目说明

面向科技农食企业供应链的轻量级水风险评估平台

**开发时间**: 2026-08-05  
**版本**: MVP v0.1 演示版

---

## 🎯 核心功能

### 5 个核心页面

1. **📥 项目/数据导入**
   - 加载示例数据或上传 CSV
   - 数据质量仪表盘(雷达图)
   - 字段校验与归一化

2. **🗺️ 供应链地图**
   - Folium 交互式地图
   - 节点风险可视化
   - 按原材料/国家筛选

3. **📊 风险敞口**
   - 计算加权水风险敞口 Eₖ
   - 改进潜力矩阵(四象限)
   - 节点贡献明细表

4. **🔮 压力测试**
   - 3 类情景:旱季供水下降/极端干旱/供应商中断
   - 基准 vs 情景对比
   - 预测性标注

5. **🤖 Agent 报告**
   - 对话式问答(规则版,后期接 LLM API)
   - 生成 TNFD LEAP 简报
   - 导出 CDP Water 预填表

---

## 🚀 快速开始

### 🌐 在线演示(推荐)

**远程访问**: 部署到 Streamlit Cloud 后可 24/7 在线访问

👉 **3 步部署到云端**: 查看 `快速部署.md`

### 💻 本地运行

#### 环境要求

- Python 3.9+
- Windows / macOS / Linux

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动应用

```bash
streamlit run 首页.py
```

应用将在浏览器中自动打开: `http://localhost:8501`

---

## 📁 项目结构

```
water_risk_mvp/
├── 首页.py                    # 主页入口
├── pages/                     # 多页应用
│   ├── 1_📥_项目数据导入.py
│   ├── 2_🗺️_供应链地图.py
│   ├── 3_📊_风险敞口.py
│   ├── 4_🔮_压力测试.py
│   └── 5_🤖_Agent报告.py
├── utils/                     # 工具模块
│   ├── data_api.py           # 数据访问层(统一接口,后期可切换数据库)
│   └── calculations.py       # 核心计算引擎(确定性函数)
├── data/                      # 数据目录
│   ├── sample_nodes_v1.csv   # 示例数据(10个节点)
│   └── industry_material_map.json
├── requirements.txt           # Python 依赖
└── README.md                  # 本文件
```

---

## 🔧 关键设计决策

### 1. 数据访问层设计(为后期数据库预留接口)

**现在**: 所有数据从 CSV/JSON 读取  
**后期**: 只需修改 `utils/data_api.py`,业务代码无需改动

示例:
```python
# data_api.py 中的接口
def load_sample_nodes(version: str = "v1") -> pd.DataFrame:
    """
    现在:从 CSV 读取
    后期:从数据库 SELECT * FROM procurement_nodes WHERE version = ?
    """
    # 现在
    return pd.read_csv(DATA_DIR / f"sample_nodes_{version}.csv")
    
    # 后期只需改成:
    # return pd.read_sql(f"SELECT * FROM nodes WHERE version='{version}'", conn)
```

### 2. MVP 阶段的简化

| 功能 | MVP 实现 | 后期增强 |
|---|---|---|
| 风险数据 | 国家级模拟值 | Aqueduct 4.0 流域级真实数据 |
| 坐标匹配 | 直接使用输入坐标 | 空间数据库查询流域 |
| Agent 对话 | 规则生成回复 | 调用 Claude/GPT API |
| 数据存储 | session_state + CSV | PostgreSQL + PostGIS |
| 情景参数 | 简化固定值 | C 组验证的完整参数卡 |

### 3. 可扩展性保证

- ✅ 所有计算函数独立可测试
- ✅ 数据访问层统一接口
- ✅ 配置与代码分离
- ✅ 日志记录预留(access.log)
- ✅ 版本控制预留(data version 参数)

---

## 📊 示例数据说明

MVP 自带 10 个示例节点,涵盖:

- **原材料**: 甘蔗、甜菜、大豆、玉米、番茄、原奶、棕榈、茶叶
- **国家**: 中国、巴西、美国、阿根廷、马来西亚、新西兰
- **风险范围**: 0.08 - 0.65 (基于真实国家级 Aqueduct 数据)

---

## 🎓 设计参考

本项目借鉴了 **Ecolab Water Navigator IQ** (2026年4月发布) 的以下功能:

1. 数据质量仪表盘(雷达图)
2. 改进潜力矩阵(四象限散点图)
3. 情境化目标建议(SBTN 框架)
4. 预测性 vs 当前的标注区分
5. CDP Water 自动预填表

**核心差异**:
- IQ 面向大型企业多厂区 + 内部 IoT 数据
- 本项目面向中小企业供应链 + 公开数据

参考链接:
- [Water Navigator IQ 产品页](https://www.ecolab.com/corporate-responsibility/environment/water-stewardship/water-navigator-iq)

---

## 📝 后续开发计划

### Phase 1: 数据集成(8/15 - 8/22)

- [ ] 下载真实 Aqueduct 4.0 数据
- [ ] 实现坐标→流域空间匹配
- [ ] 接入 FAOSTAT/AQUASTAT
- [ ] 验证与 B 组数据对齐

### Phase 2: Agent 增强(8/22 - 8/28)

- [ ] 集成 Claude/GPT API
- [ ] 5 个工具函数定义
- [ ] System Prompt 优化
- [ ] 引用追溯机制

### Phase 3: 部署与测试(8/29 - 9/10)

- [ ] Streamlit Cloud 部署
- [ ] 2-3 个真实案例测试
- [ ] 录屏演示
- [ ] 文档完善

---

## ⚠️ MVP 限制

1. **模拟数据**: 当前使用简化的国家级风险值,非真实流域级数据
2. **简化 Agent**: 使用规则生成回复,未接入真实 LLM API
3. **无持久化**: 数据仅存在 session_state,刷新即丢失
4. **单用户**: 不支持多用户并发与权限管理
5. **未验证准确性**: 计算结果需与 B 组最终方法学对齐

---

## 📄 许可声明

本项目为研究原型,不构成专业咨询建议。

数据来源:
- Aqueduct 4.0 (WRI) - CC BY 4.0
- FAOSTAT/AQUASTAT (FAO) - CC BY-NC-SA 3.0

---

**最后更新**: 2026-08-05  
**版本**: MVP v0.1
