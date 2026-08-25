const NAV = [
  ["0", "⌂", "平台简介", "index.html", "home"],
  ["1", "↥", "导入数据", "data-import.html", "import"],
  ["2", "◉", "行业画像", "data-library.html", "library"],
  ["3", "▱", "供应链位置", "supply-map.html", "map"],
  ["4", "◌", "优先节点", "risk-exposure.html", "risk"],
  ["5", "☁", "压力测试", "stress-test.html", "stress"],
  ["6", "☷", "AI 诊断与报告", "agent-analysis.html", "agent"]
];

const PAGE_META = {
  map: ["▱", "供应链位置"],
  report: ["☷", "AI 诊断与报告"]
};

function aquaVistaSymbol(className = "logo-symbol") {
  return `<svg class="${className}" viewBox="0 0 64 64" role="img" aria-label="AquaVista">
    <defs>
      <linearGradient id="avSidebarWater" x1="11" y1="8" x2="55" y2="58" gradientUnits="userSpaceOnUse">
        <stop offset="0" stop-color="#3D9DB3"/>
        <stop offset="0.52" stop-color="#2FA7A0"/>
        <stop offset="1" stop-color="#153A3E"/>
      </linearGradient>
      <clipPath id="avSidebarClip">
        <path d="M32 4C43.6 17.4 53.8 29.2 53.8 42.2C53.8 53.2 44.9 60 32 60C19.1 60 10.2 53.2 10.2 42.2C10.2 29.2 20.4 17.4 32 4Z"/>
      </clipPath>
    </defs>
    <path class="av-water" d="M32 4C43.6 17.4 53.8 29.2 53.8 42.2C53.8 53.2 44.9 60 32 60C19.1 60 10.2 53.2 10.2 42.2C10.2 29.2 20.4 17.4 32 4Z"/>
    <g clip-path="url(#avSidebarClip)">
      <path class="av-stream" fill="none" stroke-opacity=".42" stroke-width="3.2" stroke-linecap="round" d="M18.5 42.2C25.6 37 29.1 27.8 31.2 16.9"/>
      <path class="av-leaf" fill="none" stroke-width="4.4" stroke-linecap="round" d="M19.8 43.8C29.4 37.5 36.9 28.8 47.9 24.3"/>
      <path class="av-data-line" fill="none" stroke-opacity=".88" stroke-width="2.7" stroke-linecap="round" stroke-linejoin="round" d="M23.2 38.8L30.5 34L36.8 36.9L44 29.7"/>
      <rect x="24" y="40.5" width="4.2" height="8.5" rx="1.7" fill="#F5F7F4" fill-opacity=".86"/>
      <rect x="31" y="37.5" width="4.2" height="11.5" rx="1.7" fill="#F5F7F4" fill-opacity=".86"/>
      <rect x="38" y="33.2" width="4.2" height="15.8" rx="1.7" fill="#F5F7F4" fill-opacity=".86"/>
    </g>
  </svg>`;
}

const INDUSTRY_CATALOG = {
  sugar_sugarcane: {
    industryId: "sugar",
    materialId: "sugarcane",
    status: "active",
    title: "制糖业 - 甘蔗",
    enterprise: "中粮糖业",
    subtitle: "上游甘蔗与进口原糖供应链水风险筛查",
    assessmentDate: "2026-08-18",
    sourceVersion: "数据版本 v2.0",
    method: "E_k = Σ(w_i × r_i)",
    requiredFields: ["节点编号", "产区/供应商", "精确位置", "采购比例(E)", "BWS系数R", "置信度"],
    mechanisms: [
      {
        indicator: "长期干旱与旱季供水下降",
        why: "甘蔗生长期较长，对稳定供水和土壤墒情敏感。",
        consequence: "供水不足会影响单产、含糖量和压榨期原料稳定性。",
        measures: ["核实灌溉水源与旱季取水许可", "建立低风险备选产区", "对高贡献节点设置采购上限或替代采购预案"]
      },
      {
        indicator: "基准水压力",
        why: "BWS 系数用于反映区域用水竞争和可用水资源压力。",
        consequence: "水压力较高的产区在扩产、采购放量或旱季冲击下更容易形成供应约束。",
        measures: ["优先复核高 R 值节点", "与供应商共同开展节水灌溉和用水效率改造", "对数据置信度较低节点补充坐标级 Aqueduct 查询"]
      },
      {
        indicator: "季节波动与洪涝",
        why: "甘蔗产区同时可能面临旱季缺水和汛期洪涝，对田间管理和物流造成扰动。",
        consequence: "极端波动会影响收割窗口、运输连续性和工厂开榨节奏。",
        measures: ["建立收割期天气与水文监测", "准备跨区域调拨机制", "把洪涝与干旱风险分别列入供应商审查清单"]
      },
      {
        indicator: "采购集中与单点失效",
        why: "高采购占比节点即使区域 R 值不高，也会因企业暴露量大而成为管理优先级节点。",
        consequence: "核心节点失效时，总 SWE 可能下降，但供应缺口和替代依赖会显著上升。",
        measures: ["识别前 3 个贡献节点并设定管理责任人", "为第一贡献节点建立替代来源池", "跟踪剩余供应链风险是否向第二节点集中"]
      }
    ],
    nodes: [
      {
        id: "N01",
        material: "甘蔗",
        supplier: "中粮糖业-广西蔗区",
        area: "广西崇左/江州/北海",
        preciseLocation: "广西崇左市/江州区/北海市",
        purchaseShare: 0.0844432546052039,
        production: 7223.2,
        productionYear: "2023",
        waterFootprint: 540000000,
        riskR: 0.15,
        regionRisk: "低",
        confidence: "中",
        dataNature: "企业产区数据",
        sources: "中国国家统计局/人民网；WRI Aqueduct 4.0；Mekonnen & Hoekstra (2011)",
        drivers: ["长期干旱与旱季供水下降", "季节波动与洪涝", "灌溉水源稳定性"],
        map: [38, 55]
      },
      {
        id: "N02",
        material: "甘蔗",
        supplier: "中粮糖业-云南蔗区",
        area: "云南梁河",
        preciseLocation: "云南德宏州梁河县",
        purchaseShare: 0.0185517500184126,
        production: 1586.9,
        productionYear: "2023",
        waterFootprint: 540000000,
        riskR: 0.3,
        regionRisk: "低",
        confidence: "中",
        dataNature: "企业产区数据",
        sources: "中国国家统计局/人民网；WRI Aqueduct 4.0；Mekonnen & Hoekstra (2011)",
        drivers: ["长期干旱与旱季供水下降", "季节波动与洪涝"],
        map: [34, 60]
      },
      {
        id: "N03",
        material: "甘蔗(原糖)",
        supplier: "中粮糖业-巴西进口",
        area: "巴西圣保罗/中南部",
        preciseLocation: "巴西圣保罗州/中南部蔗区",
        purchaseShare: 0.762224526561537,
        production: 65200,
        productionYear: "2023/2024",
        waterFootprint: 3500000000,
        riskR: 0.05,
        regionRisk: "高",
        confidence: "低",
        dataNature: "进口采购拆分估算",
        sources: "FAOSTAT；WRI Aqueduct 4.0；企业产区数据；Mekonnen & Hoekstra (2011)",
        drivers: ["采购集中与单点失效", "季节波动与洪涝", "进口补充采购占比高"],
        map: [22, 72]
      },
      {
        id: "N04",
        material: "甘蔗(原糖)",
        supplier: "中粮糖业-泰国进口",
        area: "泰国中部平原",
        preciseLocation: "泰国中部平原/东北部蔗区",
        purchaseShare: 0.0964821935231958,
        production: 8253,
        productionYear: "2023/2024",
        waterFootprint: 360000000,
        riskR: 0.8,
        regionRisk: "中",
        confidence: "低",
        dataNature: "进口采购拆分估算",
        sources: "FAOSTAT；中国糖业协会；泰国甘蔗糖业局；WRI Aqueduct 4.0",
        drivers: ["基准水压力", "长期干旱与旱季供水下降", "地下水消耗"],
        map: [58, 62]
      },
      {
        id: "N05",
        material: "甘蔗(原糖)",
        supplier: "中粮糖业-古巴进口",
        area: "古巴中部/西部",
        preciseLocation: "古巴中部/西部蔗区",
        purchaseShare: 0.00350716806700094,
        production: 300,
        productionYear: "2023/2024",
        waterFootprint: 65000000,
        riskR: 0.15,
        regionRisk: "低",
        confidence: "低",
        dataNature: "进口采购拆分估算",
        sources: "USDA FAS；文献估算；WRI Aqueduct 4.0",
        drivers: ["季节波动与洪涝", "部分灌溉依赖"],
        map: [28, 46]
      },
      {
        id: "N06",
        material: "甘蔗(原糖)",
        supplier: "中粮糖业-澳大利亚进口",
        area: "澳大利亚昆士兰",
        preciseLocation: "澳大利亚昆士兰州",
        purchaseShare: 0.0347911072246493,
        production: 2976,
        productionYear: "2023",
        waterFootprint: 550000000,
        riskR: 0.05,
        regionRisk: "低",
        confidence: "低",
        dataNature: "进口采购拆分估算",
        sources: "FAOSTAT；Canegrowers Australia；WRI Aqueduct 4.0",
        drivers: ["灌溉水源稳定性", "季节波动与洪涝"],
        map: [72, 78]
      }
    ],
    scenarios: [
      {
        id: "dry20",
        name: "旱季供水下降",
        shortName: "Ri +20%",
        description: "保持采购结构和水足迹不变，将各节点水风险参数 Ri 提高 20%。",
        mode: "riskFactor",
        factor: 1.2
      },
      {
        id: "extreme40",
        name: "极端干旱",
        shortName: "Ri +40%",
        description: "保持采购结构不变，将 Ri 提高 40%，并按 1.0 做上限截断。",
        mode: "riskFactor",
        factor: 1.4,
        cap: 1
      },
      {
        id: "brazilFail",
        name: "供应商单点失效",
        shortName: "巴西节点失效",
        description: "巴西节点供应能力暂时失效，当前口径下该节点 SWE 置 0，同时记录供应缺口。",
        mode: "nodeFailure",
        failedNodeId: "N03"
      }
    ]
  },
  dairy_milk: {
    status: "placeholder",
    title: "乳制品 - 原奶",
    enterprise: "待接入",
    subtitle: "后续行业模板已预留"
  },
  oilseed_soy: {
    status: "placeholder",
    title: "食品加工 - 大豆",
    enterprise: "待接入",
    subtitle: "后续行业模板已预留"
  }
};

const DEFAULT_INDUSTRY = "sugar_sugarcane";
const state = {
  industryKey: localStorage.getItem("aquavista.industry") || DEFAULT_INDUSTRY,
  scenarioId: localStorage.getItem("aquavista.scenario") || "dry20",
  uploadedNodes: loadUploadedNodes()
};

function loadUploadedNodes() {
  try {
    const raw = localStorage.getItem("aquavista.uploadedNodes");
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    const nodes = Array.isArray(parsed) ? parsed : Array.isArray(parsed?.nodes) ? parsed.nodes : null;
    if (!nodes || !nodes.length) return null;

    const purchaseSum = nodes.reduce((sum, node) => sum + Number(node?.purchaseShare || 0), 0);
    if (!(purchaseSum > 0)) return null;

    const hasRisk = nodes.some((node) => Number(node?.riskR || 0) > 0);
    if (!hasRisk) {
      const rawCsv = localStorage.getItem("aquavista.uploadedCsv");
      if (rawCsv) {
        const reparsed = parseCsv(rawCsv);
        if (reparsed.length && reparsed.some((node) => Number(node?.riskR || 0) > 0)) {
          const normalized = normalizeNodes(reparsed);
          localStorage.setItem("aquavista.uploadedNodes", JSON.stringify(normalized));
          return normalized;
        }
      }
      localStorage.removeItem("aquavista.uploadedNodes");
      return null;
    }

    return nodes;
  } catch {
    return null;
  }
}

function activeIndustry() {
  const selected = INDUSTRY_CATALOG[state.industryKey] || INDUSTRY_CATALOG[DEFAULT_INDUSTRY];
  if (selected.status !== "active") return INDUSTRY_CATALOG[DEFAULT_INDUSTRY];
  return selected;
}

function activeNodes() {
  if (state.uploadedNodes && state.uploadedNodes.length) {
    const validRisk = state.uploadedNodes.some((node) => Number(node.riskR || 0) > 0);
    const validWater = state.uploadedNodes.some((node) => Number(node.waterFootprint || 0) > 0);
    const validShare = state.uploadedNodes.some((node) => Number(node.purchaseShare || 0) > 0);
    if (validRisk && validWater && validShare) return state.uploadedNodes;
    localStorage.removeItem("aquavista.uploadedNodes");
    localStorage.removeItem("aquavista.uploadedCsv");
    state.uploadedNodes = null;
  }
  return activeIndustry().nodes;
}

function normalizeNodes(nodes) {
  const total = nodes.reduce((sum, node) => sum + Number(node.purchaseShare || 0), 0);
  if (!(total > 0)) return [];
  return nodes.map((node) => ({
    ...node,
    purchaseShare: Number(node.purchaseShare || 0) / total
  }));
}

function clamp(value, min = 0, max = 1) {
  return Math.min(max, Math.max(min, value));
}

function calcRows(nodes, scenario = null) {
  let working = nodes.map((node) => ({ ...node, scenarioNote: "" }));

  if (scenario?.mode === "riskFactor") {
    working = working.map((node) => ({
      ...node,
      scenarioRiskR: clamp(node.riskR * scenario.factor, 0, scenario.cap || 1),
      scenarioNote: `Ri ${scenario.shortName}`
    }));
  } else if (scenario?.mode === "nodeFailure") {
    working = working.map((node) => ({
      ...node,
      scenarioRiskR: node.riskR,
      scenarioFailed: node.id === scenario.failedNodeId,
      purchaseShare: node.id === scenario.failedNodeId ? 0 : node.purchaseShare,
      scenarioNote: node.id === scenario.failedNodeId ? "节点失效" : "剩余供应"
    }));
  }

  if (scenario?.mode === "nodeFailure") {
    working = working.map((node) => ({
      ...node,
      purchaseShare: node.scenarioFailed ? 0 : node.purchaseShare
    }));
  }

  working = working.map((node) => {
    const effectiveRisk = node.scenarioFailed ? 0 : (node.scenarioRiskR ?? node.riskR);
    const waterFootprint = Number(node.waterFootprint || 0);
    const swe = node.purchaseShare * waterFootprint * effectiveRisk;
    return { ...node, effectiveRisk, swe };
  });

  const total = working.reduce((sum, node) => sum + node.swe, 0);
  const ranked = [...working].sort((a, b) => b.swe - a.swe);
  const rankMap = new Map(ranked.map((node, index) => [node.id, index + 1]));

  return working
    .map((node) => ({
      ...node,
      contribution: total > 0 ? node.swe / total : 0,
      rank: rankMap.get(node.id),
      priority: priorityLabel(rankMap.get(node.id))
    }))
    .sort((a, b) => a.rank - b.rank);
}

function priorityLabel(rank) {
  if (rank <= 3) return "优先管理";
  if (rank <= 5) return "跟踪观察";
  return "低优先级";
}

function calcSummary(nodes, scenario = null) {
  const rows = calcRows(nodes, scenario);
  const total = rows.reduce((sum, node) => sum + node.swe, 0);
  const hhi = rows.reduce((sum, node) => sum + node.purchaseShare ** 2, 0);
  const top3 = rows.filter((node) => node.rank <= 3);
  const top3Contribution = top3.reduce((sum, node) => sum + node.contribution, 0);
  const highPriorityShare = top3.reduce((sum, node) => sum + node.purchaseShare, 0);
  const failedNode = scenario?.mode === "nodeFailure" ? nodes.find((node) => node.id === scenario.failedNodeId) : null;

  return {
    rows,
    total,
    hhi,
    top3,
    top3Contribution,
    highPriorityShare,
    supplyGap: failedNode ? failedNode.purchaseShare : 0
  };
}

function formatNumber(value, digits = 0) {
  return Number(value).toLocaleString("zh-CN", { maximumFractionDigits: digits, minimumFractionDigits: digits });
}

function formatPercent(value, digits = 1) {
  return `${(value * 100).toLocaleString("zh-CN", { maximumFractionDigits: digits, minimumFractionDigits: digits })}%`;
}

function badge(text, tone = "gray") {
  return `<span class="badge ${tone}">${text}</span>`;
}

function metric(label, value, foot, tone = "teal") {
  return `<div class="panel metric ${tone}"><div class="metric-label">${label}</div><div class="metric-value">${value}</div><div class="muted">${foot}</div></div>`;
}

function toneForRisk(label) {
  if (label === "高") return "red";
  if (label === "中") return "amber";
  if (label === "低") return "green";
  return "gray";
}

function toneForPriority(rank) {
  if (rank <= 1) return "red";
  if (rank <= 3) return "amber";
  return "green";
}

function userVerdict(base, scenario, stressed) {
  const first = base.top3[0];
  const delta = stressed.total - base.total;
  return {
    headline: "当前最需要管理的不是“最高区域风险”，而是“采购暴露最大的关键节点”。",
    body: `${first.area} 是第一优先节点，贡献 ${formatPercent(first.contribution, 2)}。${scenario.name}下风险敞口${delta >= 0 ? "上升" : "下降"} ${formatNumber(Math.abs(delta))}，需要优先复核该节点采购占比、替代来源和供应连续性。`,
    nextAction: "先处理巴西、泰国、广西三个节点；其余节点保持季度复核。"
  };
}

function actionCards(base) {
  const actions = [
    {
      title: "立即复核巴西节点",
      body: "确认进口原糖采购占比、具体蔗区和替代来源。该节点是第一贡献节点，也是单点失效情景的主要供应缺口来源。",
      tone: "red"
    },
    {
      title: "核实泰国水压力",
      body: "泰国节点 Ri 最高，旱季供水和地下水消耗需要进入供应商审查清单。",
      tone: "amber"
    },
    {
      title: "建立国内产区监测",
      body: "广西进入前三，应关注旱季供水、汛期波动和压榨期原料稳定。",
      tone: "teal"
    }
  ];
  return `<div class="decision-grid">${actions.map((item, index) => `<article class="decision-card ${item.tone}">
    <span>${index + 1}</span>
    <strong>${item.title}</strong>
    <p>${item.body}</p>
  </article>`).join("")}</div>`;
}

function priorityCards(rows) {
  return `<div class="priority-list">${rows.slice(0, 3).map((node) => `<article class="priority-card ${toneForPriority(node.rank)}">
    <div class="priority-rank">${node.rank}</div>
    <div>
      <strong>${node.area}</strong>
      <p>${node.rank === 1 ? "第一管理优先节点" : node.rank === 2 ? "高水压力重点节点" : "国内产区重点节点"}</p>
      <div class="priority-meta">
        <span>贡献 ${formatPercent(node.contribution, 2)}</span>
        <span>采购 ${formatPercent(node.purchaseShare, 2)}</span>
      </div>
    </div>
  </article>`).join("")}</div>`;
}

function evidenceDetails(label, innerHtml) {
  return `<details class="evidence"><summary>${label}</summary>${innerHtml}</details>`;
}

function mapLabelClass(node) {
  const placements = {
    N01: "label-right",
    N02: "label-left",
    N03: "label-right",
    N04: "label-right",
    N05: "label-right",
    N06: "label-left"
  };
  return placements[node.id] || "label-right";
}

function mapPosition(node) {
  const positions = {
    N01: [37, 43],
    N02: [34, 55],
    N03: [23, 72],
    N04: [58, 56],
    N05: [26, 34],
    N06: [73, 78]
  };
  return positions[node.id] || node.map || [50, 50];
}

function quadrantPlacement(node) {
  const positions = {
    N01: { left: 18, bottom: 24, label: "label-above" },
    N02: { left: 12, bottom: 36, label: "label-right" },
    N03: { left: 82, bottom: 16, label: "label-left" },
    N04: { left: 20, bottom: 76, label: "label-right" },
    N05: { left: 10, bottom: 22, label: "label-left" },
    N06: { left: 14, bottom: 12, label: "label-right" }
  };
  return positions[node.id] || {
    left: clamp(8 + node.purchaseShare * 86, 6, 88),
    bottom: clamp(8 + node.riskR * 84, 8, 86),
    label: "label-right"
  };
}

function industrySelector() {
  return `<div class="industry-switcher">${Object.entries(INDUSTRY_CATALOG).map(([key, item]) => {
    const active = key === state.industryKey && item.status === "active";
    const disabled = item.status !== "active";
    return `<button class="industry-option ${active ? "active" : ""}" ${disabled ? "disabled" : ""} data-industry="${key}">
      <strong>${item.title}</strong>
      <span>${item.enterprise} · ${disabled ? "待接入" : "已接入"}</span>
    </button>`;
  }).join("")}</div>`;
}

function rowsTable(rows, compact = false) {
  return `<table>
    <thead>
      <tr>
        <th>排名</th><th>节点</th><th>产区/供应商</th><th>采购比例</th><th>Ri</th><th>SWE</th><th>贡献度</th><th>区域风险</th><th>置信度</th>
      </tr>
    </thead>
    <tbody>
      ${rows.map((node) => `<tr>
        <td class="rank">${node.rank}</td>
        <td><strong>${node.id}</strong><div class="muted">${node.material}</div></td>
        <td>${node.area}<div class="muted">${compact ? node.scenarioNote || node.dataNature : node.supplier}</div></td>
        <td class="num">${formatPercent(node.purchaseShare, 2)}</td>
        <td class="num">${node.effectiveRisk.toFixed(2)}</td>
        <td class="num">${formatNumber(node.swe)}</td>
        <td class="num">${formatPercent(node.contribution, 2)}</td>
        <td>${badge(node.regionRisk, toneForRisk(node.regionRisk))}</td>
        <td>${badge(node.confidence, node.confidence === "中" ? "amber" : "gray")}</td>
      </tr>`).join("")}
    </tbody>
  </table>`;
}

function progress(active) {
  return `<div class="progress">${NAV.slice(1, 7).map((item, i) => {
    const step = i + 1;
    const stateName = i < active ? "done" : i === active ? "active" : "";
    const label = i < active ? "已完成" : i === active ? "当前" : "待处理";
    return `<div class="step ${stateName}"><div class="bubble">${i < active ? "✓" : step}</div><strong>${item[2]}</strong><span>${label}</span></div>`;
  }).join("")}</div>`;
}

function landingLogo() {
  return aquaVistaSymbol("av-logo-symbol");
}

function landingHeader() {
  return `<header class="landing-header">
    <a class="landing-brand" href="index.html" aria-label="AquaVista 首页">
      ${landingLogo()}
      <span><strong>AquaVista</strong><em>AI-POWERED WATER RISK INTELLIGENCE</em></span>
    </a>
    <nav class="landing-nav" aria-label="首页导航">
      <a href="#product">产品</a>
      <a href="risk-exposure.html">风险分析</a>
      <a href="#workflow">解决方案</a>
      <a href="#ai">关于我们</a>
    </nav>
    <div class="landing-actions">
      <a class="landing-login" href="data-import.html">登录</a>
      <a class="landing-button primary" href="data-import.html">开始分析</a>
    </div>
  </header>`;
}

function landingHeroVisual(base, scenario, stressed) {
  const nodes = base.rows.slice(0, 6);
  const nodeDots = nodes.map((node) => {
    const [left, top] = mapPosition(node);
    const tone = toneForPriority(node.rank);
    const size = Math.max(9, Math.min(22, 9 + node.purchaseShare * 18));
    return `<span class="hero-node ${tone}" style="left:${left}%;top:${top}%;width:${size}px;height:${size}px">
      <i>${node.id}</i>
    </span>`;
  }).join("");
  const first = base.top3[0];
  const second = base.top3[1];
  const delta = stressed.total - base.total;
  return `<div class="hero-visual" aria-label="供应链水风险分析演示图">
    <div class="visual-topline">
      <span>DEMO ANALYSIS VIEW</span>
      <strong>SCENARIO 2030</strong>
    </div>
    <div class="visual-stage">
      <svg class="visual-map" viewBox="0 0 640 420" aria-hidden="true">
        <path d="M122 90c72-34 148-27 205 14 37 27 86 31 138 18 45-11 86-1 109 36 25 40 7 89-35 111-50 26-98-1-147 16-64 23-91 79-165 65-67-13-73-72-120-89-42-16-72-45-61-88 9-34 38-62 76-83Z" fill="none" stroke="currentColor" stroke-width="1.2" />
        <path d="M72 302c88-52 154-53 229-18 58 27 108 28 193 0" fill="none" stroke="currentColor" stroke-width="1.1" stroke-dasharray="6 10" />
        <path d="M112 262C188 194 270 184 360 232c64 34 115 23 181-38" fill="none" stroke="currentColor" stroke-width="1.1" stroke-dasharray="3 9" />
      </svg>
      <svg class="visual-links" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
        <path d="M24 72 C 34 42, 48 34, 58 56 S 74 70, 73 78" />
        <path d="M38 43 C 46 40, 50 46, 58 56" />
        <path d="M26 34 C 39 47, 47 58, 58 56" />
      </svg>
      ${nodeDots}
      <div class="visual-panel risk-panel">
        <span>WATER RISK</span>
        <strong>Location Matched</strong>
      </div>
      <div class="visual-panel exposure-panel">
        <span>SUPPLY EXPOSURE</span>
        <strong>${first.id} · ${first.area}</strong>
      </div>
      <div class="visual-panel priority-panel">
        <span>HIGH PRIORITY</span>
        <strong>${second.id} · ${second.area}</strong>
      </div>
    </div>
    <div class="visual-footer">
      <div><span>Risk Exposure</span><strong>${formatNumber(base.total)}</strong></div>
      <div><span>Scenario Change</span><strong>${delta >= 0 ? "+" : ""}${formatNumber(delta)}</strong></div>
      <div><span>Top 3 Nodes</span><strong>${base.top3.map((node) => node.id).join(" / ")}</strong></div>
    </div>
    <p class="demo-note">Demo: 使用当前样例数据生成，仅用于展示分析结果形态。</p>
  </div>`;
}

function analyticsPreview(base, scenario, stressed) {
  const delta = stressed.total - base.total;
  const rows = base.top3.map((node) => `<div class="preview-row">
    <span>${node.id}</span>
    <strong>${node.area}</strong>
    <em>${formatPercent(node.contribution, 1)}</em>
  </div>`).join("");
  return `<div class="analytics-preview">
    <div class="preview-toolbar">
      <div><span>DEMO RESULT</span><strong>AquaVista Risk Analysis</strong></div>
      <a href="risk-exposure.html">查看完整分析</a>
    </div>
    <div class="preview-grid">
      <div class="preview-map">
        <svg viewBox="0 0 440 320" aria-hidden="true">
          <path d="M72 96c60-44 128-48 189-14 42 24 84 16 117 43 48 40 22 112-35 124-49 11-82-21-126-5-62 23-112 17-143-28-28-41-41-88-2-120Z" />
          <path d="M82 232c82-49 149-45 219-7" />
          <path d="M112 145c54 24 100 57 149 87" />
        </svg>
        ${base.rows.slice(0, 6).map((node) => {
          const [left, top] = mapPosition(node);
          return `<span class="preview-dot ${toneForPriority(node.rank)}" style="left:${left}%;top:${top}%">${node.id}</span>`;
        }).join("")}
      </div>
      <div class="preview-side">
        <div class="preview-metric"><span>Risk Exposure</span><strong>${formatNumber(base.total)}</strong><em>当前样例数据口径</em></div>
        <div class="preview-metric"><span>High-Risk Procurement</span><strong>${formatPercent(base.highPriorityShare, 1)}</strong><em>前三管理优先节点采购占比</em></div>
        <div class="preview-metric"><span>${scenario.name}</span><strong>${delta >= 0 ? "+" : ""}${formatNumber(delta)}</strong><em>假设情景下的敞口变化</em></div>
      </div>
    </div>
    <div class="preview-bottom">
      <div>
        <span>Top Risk Nodes</span>
        ${rows}
      </div>
      <div class="preview-insight">
        <span>Key Insights</span>
        <p>结果不是单一水风险地图，而是把采购结构、供应链位置和地点水风险连接后，识别企业真正需要管理的风险敞口。</p>
      </div>
    </div>
    <p class="demo-note">Demo: 预览使用项目内当前样例节点，不代表真实企业风险承诺。</p>
  </div>`;
}

function homePage() {
  const industry = activeIndustry();
  const scenario = industry.scenarios.find((item) => item.id === state.scenarioId) || industry.scenarios[0];
  const base = calcSummary(activeNodes());
  const stressed = calcSummary(activeNodes(), scenario);

  return `
    ${landingHeader()}
    <main class="landing-main">
      <section class="landing-hero" id="product">
        <div class="hero-copy">
          <div class="eyebrow">AI-POWERED WATER RISK INTELLIGENCE</div>
          <h1>洞见水风险，<br>守护供应链韧性</h1>
          <p>AquaVista 将企业关键原材料、供应链位置、采购结构与水风险数据连接起来，帮助企业识别风险敞口、比较情景变化，并形成可追溯的管理建议。</p>
          <div class="hero-cta">
            <a class="landing-button primary large" href="data-import.html">开始风险分析</a>
            <a class="landing-button secondary large" href="#workflow">了解产品</a>
          </div>
        </div>
        ${landingHeroVisual(base, scenario, stressed)}
      </section>

      <section class="landing-section value-section">
        <div class="section-intro">
          <span>Product Value</span>
          <h2>从分散的数据，<br>到可执行的风险洞察</h2>
          <p>连接行业、原材料、供应链位置、采购结构与地点水风险，让企业从“看见风险”进一步走向“理解风险、管理风险”。</p>
        </div>
        <div class="value-grid">
          ${[
            ["01", "多源数据融合", "连接行业、原材料、供应链位置与水风险数据。"],
            ["02", "供应链风险敞口", "识别高风险采购、关键贡献节点与集中度。"],
            ["03", "情景模拟", "比较未来风险、节点中断和采购结构变化。"],
            ["04", "AI 风险洞察", "组织数据、调用工具、解释结果并生成可追溯报告。"]
          ].map((item) => `<article class="value-item">
            <div class="value-index">${item[0]}</div>
            <div class="value-symbol"><span></span></div>
            <h3>${item[1]}</h3>
            <p>${item[2]}</p>
          </article>`).join("")}
        </div>
      </section>

      <section class="landing-section workflow-section" id="workflow">
        <div class="section-intro compact">
          <span>Workflow</span>
          <h2>从数据，到决策</h2>
        </div>
        <div class="workflow-line">
          ${[
            ["01", "数据输入", "导入企业供应链节点、采购结构和原材料信息。"],
            ["02", "风险匹配", "把产地与地点水风险指标连接并保留数据来源。"],
            ["03", "敞口计算", "基于确定性函数计算贡献度、集中度和优先级。"],
            ["04", "情景测试", "在假设压力情景下比较结构变化。"],
            ["05", "AI 洞察", "解释结果、提示数据缺口并组织管理建议。"],
            ["06", "管理报告", "输出可追溯、可下载的风险诊断报告。"]
          ].map((item) => `<article class="workflow-step">
            <span>${item[0]}</span>
            <strong>${item[1]}</strong>
            <p>${item[2]}</p>
          </article>`).join("")}
        </div>
      </section>

      <section class="landing-section preview-section">
        <div class="section-intro">
          <span>Analytics Preview</span>
          <h2>最终得到的不是地图，<br>而是一套可追溯的风险管理结果</h2>
          <p>供应链节点、地点风险、采购权重、风险敞口和情景变化被放在同一张分析界面中，便于管理层判断下一步。</p>
        </div>
        ${analyticsPreview(base, scenario, stressed)}
      </section>

      <section class="landing-section ai-section" id="ai">
        <div class="ai-copy">
          <span>AI Intelligence</span>
          <h2>AI 不只是回答问题，<br>而是参与整个风险分析流程。</h2>
          <p>AI 负责组织流程、调用工具、解释结果和辅助生成报告；风险结果来自数据、规则和确定性函数，AI 不直接编造风险分数。</p>
        </div>
        <div class="ai-flow">
          ${["数据检查", "工具调用", "确定性计算", "结果解释", "报告生成"].map((item, index) => `<div class="ai-step">
            <span>${String(index + 1).padStart(2, "0")}</span>
            <strong>${item}</strong>
          </div>`).join("")}
        </div>
      </section>

      <section class="final-cta">
        <h2>从识别风险，<br>到管理风险。</h2>
        <p>让数据成为风险管理的起点，让 AI 帮助企业看见下一步。</p>
        <a class="landing-button light large" href="data-import.html">开始风险分析 →</a>
      </section>
    </main>`;
}

function importPage() {
  const industry = activeIndustry();
  const rows = calcSummary(activeNodes()).rows;
  const presets = industry.nodes;

  return `
    <section class="grid import-layout">
      <div class="panel">
        <h3>填写或选择节点数据</h3>
        <p class="lead-small">能从行业样本中确定的信息可以直接选择；企业自己的采购比例、具体位置或补充说明可以手动填写。</p>
        <div class="manual-form">
          <label>产区模板</label>
          <select id="presetNode">
            <option value="">自定义节点</option>
            ${presets.map((node) => `<option value="${node.id}">${node.area}</option>`).join("")}
          </select>

          <label>原材料</label>
          <select id="manualMaterial">
            <option value="甘蔗">甘蔗</option>
            <option value="甘蔗(原糖)">甘蔗(原糖)</option>
          </select>

          <label>产区/供应商</label>
          <input id="manualArea" type="text" placeholder="例如：广西崇左/江州/北海" />

          <label>精确位置</label>
          <input id="manualLocation" type="text" placeholder="可填写市县、蔗区或供应商地址" />

          <label>采购比例</label>
          <input id="manualShare" type="number" min="0" max="100" step="0.01" placeholder="例如：25，表示 25%" />

          <label>水足迹 W</label>
          <select id="manualWater">
            <option value="540000000">540,000,000 m3/yr</option>
            <option value="3500000000">3,500,000,000 m3/yr</option>
            <option value="360000000">360,000,000 m3/yr</option>
            <option value="550000000">550,000,000 m3/yr</option>
            <option value="65000000">65,000,000 m3/yr</option>
            <option value="custom">手动输入</option>
          </select>

          <label>自定义 W</label>
          <input id="manualWaterCustom" type="number" min="0" step="1" placeholder="无法选择时填写" />

          <label>区域水风险 Ri</label>
          <select id="manualRisk">
            <option value="0.05">0.05</option>
            <option value="0.15">0.15</option>
            <option value="0.3">0.30</option>
            <option value="0.8">0.80</option>
            <option value="custom">手动输入</option>
          </select>

          <label>自定义 Ri</label>
          <input id="manualRiskCustom" type="number" min="0" max="1" step="0.01" placeholder="0-1 之间" />

          <label>置信度</label>
          <select id="manualConfidence">
            <option value="中">中</option>
            <option value="低">低</option>
            <option value="高">高</option>
          </select>
        </div>
        <div class="button-row">
          <button class="button primary" id="addManualNodeBtn">添加节点</button>
          <button class="button" id="clearManualNodesBtn">清空录入</button>
          <button class="button" id="useSampleBtn">使用示例数据</button>
        </div>
        <div id="manualStatus" class="notice"></div>
      </div>
      <div class="panel">
        <h3>从文件导入</h3>
        <p class="lead-small">如果已经整理好节点表，可以直接上传 CSV；上传后会替换当前手动录入的数据。</p>
        <div class="upload-box compact-upload">
          <input id="csvInput" type="file" accept=".csv,text/csv" />
          <div>
            <strong>上传 CSV 企业节点表</strong>
            <p class="muted">支持列名：节点编号、产区/供应商、精确位置、采购比例(E)、水足迹W、BWS系数R、置信度。</p>
          </div>
        </div>
        <div class="button-row">
          <button class="button" id="downloadTemplateBtn">下载 CSV 模板</button>
        </div>
        <div id="uploadStatus" class="notice"></div>
        <hr class="soft-divider" />
        <h3>当前数据状态</h3>
        ${validationPanel(activeNodes())}
        ${evidenceDetails("查看需要的字段", `<div class="field-cloud">${industry.requiredFields.map((field) => badge(field, "gray")).join("")}</div>`)}
      </div>
    </section>
    <section class="panel">
      <h3>导入后会得到什么</h3>
      <div class="outcome-strip">
        <span>优先节点</span><span>压力测试</span><span>AI 诊断</span><span>诊断报告</span>
      </div>
      ${evidenceDetails("查看节点预览", rowsTable(rows))}
    </section>`;
}

function validationPanel(nodes) {
  const share = nodes.reduce((sum, node) => sum + node.purchaseShare, 0);
  const missing = nodes.flatMap((node) => ["id", "area", "purchaseShare", "riskR"].filter((key) => node[key] === undefined || node[key] === null || node[key] === ""));
  return `<div class="validation-list">
    <div><strong>${nodes.length}</strong><span>节点数量</span></div>
    <div><strong>${formatPercent(share, 2)}</strong><span>采购比例合计</span></div>
    <div><strong>${missing.length}</strong><span>缺失字段</span></div>
    <div><strong>${nodes.filter((node) => node.confidence === "低").length}</strong><span>低置信度节点</span></div>
  </div>
  <p class="muted">本结果为筛查和优先级排序，不解释为实际财务损失概率。</p>`;
}

function libraryPage() {
  const industry = activeIndustry();
  return `
    ${industrySelector()}
    <section class="grid two">
      <div class="panel">
        <h3>为什么甘蔗供应链会有水风险</h3>
        <div class="mechanism-list">
          ${industry.mechanisms.map((item) => `<article class="mechanism">
            <strong>${item.indicator}</strong>
            <p>${item.why}</p>
            <p class="muted">${item.consequence}</p>
          </article>`).join("")}
        </div>
      </div>
      <div class="panel">
        <h3>系统会怎么转成建议</h3>
        <div class="action-list">
          ${industry.mechanisms.map((item) => `<div class="action-item">
            <span>${item.indicator}</span>
            <ul>${item.measures.map((measure) => `<li>${measure}</li>`).join("")}</ul>
          </div>`).join("")}
        </div>
      </div>
    </section>`;
}

function mapPage() {
  const rows = calcSummary(activeNodes()).rows;
  const maxShare = Math.max(...rows.map((node) => node.purchaseShare));
  return `
    <section class="grid map-layout">
      <div class="panel">
        <h3>图层</h3>
        <p>${badge("节点大小=采购比例", "teal")}${badge("颜色=管理优先级", "amber")}${badge("标签=产区", "gray")}</p>
        <div class="legend">
          <span><i class="dot red-dot"></i>优先管理</span>
          <span><i class="dot amber-dot"></i>跟踪观察</span>
          <span><i class="dot green-dot"></i>低优先级</span>
        </div>
      </div>
      <div class="panel map-panel">
        <h3>供应链节点分布</h3>
        <div class="map-canvas">
          <div class="map-gridline"></div>
          ${rows.map((node) => {
            const size = 32 + (node.purchaseShare / maxShare) * 34;
            const tone = toneForPriority(node.rank);
            const position = mapPosition(node);
            return `<button class="map-node ${tone} ${mapLabelClass(node)}" style="left:${position[0]}%;top:${position[1]}%;width:${size}px;height:${size}px" title="${node.area}">
              <span>${node.id}</span><em>${node.area}</em>
            </button>`;
          }).join("")}
        </div>
      </div>
      <div class="panel">
        <h3>位置匹配说明</h3>
        <div class="list">
          ${rows.slice(0, 4).map((node) => `<div class="list-item">
            <strong>${node.area}</strong>
            <span>${node.preciseLocation}</span>
            <small>${node.dataNature}</small>
          </div>`).join("")}
        </div>
      </div>
    </section>`;
}

function riskPage() {
  const base = calcSummary(activeNodes());
  return `
    <section class="grid two">
      <div class="panel">
        <h3>优先处理顺序</h3>
        ${priorityCards(base.rows)}
        ${evidenceDetails("查看完整排序表", rowsTable(base.rows))}
      </div>
      <div class="panel">
        <h3>为什么是这三个</h3>
        <div class="plain-answer">
          <p><strong>巴西</strong>：采购暴露最大，是当前最重要的管理节点。</p>
          <p><strong>泰国</strong>：区域水压力最高，外部水风险恶化时最敏感。</p>
          <p><strong>广西</strong>：国内主产区进入前三，需要做旱季和汛期监测。</p>
        </div>
        ${evidenceDetails("查看双维度图", `<div class="quadrant">
          ${base.rows.map((node) => {
            const placement = quadrantPlacement(node);
            return `<span class="point ${toneForPriority(node.rank)} ${placement.label}" style="left:${placement.left}%;bottom:${placement.bottom}%">${node.id}<em>${node.area}</em></span>`;
          }).join("")}
          <label class="x-label">企业采购占比</label><label class="y-label">区域风险 Ri</label>
        </div>`)}
      </div>
    </section>`;
}

function stressPage() {
  const industry = activeIndustry();
  const base = calcSummary(activeNodes());
  const scenario = industry.scenarios.find((item) => item.id === state.scenarioId) || industry.scenarios[0];
  const stressed = calcSummary(activeNodes(), scenario);
  const delta = stressed.total - base.total;

  return `
    <section class="panel">
      <div class="section-head">
        <h3>选择一个压力测试情景</h3>
        <div class="segmented">
          ${industry.scenarios.map((item) => `<button class="${item.id === scenario.id ? "active" : ""}" data-scenario="${item.id}">
            ${item.name}
          </button>`).join("")}
        </div>
      </div>
      <p class="lead-small">${scenario.description}</p>
    </section>
    <section class="grid two">
      <div class="panel">
        <h3>结果怎么变</h3>
        <div class="impact-panel ${delta >= 0 ? "red" : "green"}">
          <span>${scenario.name}</span>
          <strong>${delta >= 0 ? "+" : ""}${formatNumber(delta)}</strong>
          <p>${scenario.mode === "nodeFailure" ? `供应缺口 ${formatPercent(stressed.supplyGap, 2)}，剩余风险转向 ${stressed.top3[0].area}。` : `总敞口变化 ${formatPercent(Math.abs(delta) / base.total, 2)}，前三优先节点基本不变。`}</p>
        </div>
        ${evidenceDetails("查看情景后排名", rowsTable(stressed.rows, true))}
      </div>
      <div class="panel">
        <h3>管理含义</h3>
        ${scenarioNarrative(base, stressed, scenario)}
      </div>
    </section>`;
}

function scenarioNarrative(base, stressed, scenario) {
  if (scenario.mode === "nodeFailure") {
    const newTop = stressed.top3[0];
    return `<div class="callout amber">
      <strong>不要把 SWE 下降解释为风险下降</strong>
      <p>巴西节点失效后，剩余供应链总 SWE 为 ${formatNumber(stressed.total)}，但同时形成 ${formatPercent(stressed.supplyGap, 2)} 的供应缺口。剩余风险重新集中到 ${newTop.area}，其贡献度升至 ${formatPercent(newTop.contribution, 2)}。</p>
    </div>`;
  }
  return `<div class="callout red">
    <strong>${scenario.name}放大了既有风险结构</strong>
    <p>总 SWE 从 ${formatNumber(base.total)} 变为 ${formatNumber(stressed.total)}。前三节点仍为 ${stressed.top3.map((node) => node.area).join("、")}，说明当前风险结构主要由采购规模和既有区域风险共同决定。</p>
  </div>`;
}

function agentPage() {
  const industry = activeIndustry();
  const scenario = industry.scenarios.find((item) => item.id === state.scenarioId) || industry.scenarios[0];
  const base = calcSummary(activeNodes());
  const stressed = calcSummary(activeNodes(), scenario);
  const first = base.top3[0];
  const second = base.top3[1];
  const third = base.top3[2];
  const delta = stressed.total - base.total;

  return `
    <section class="ai-workbench">
      <div class="ai-hero-panel">
        <div>
          <div class="kicker">AI DIAGNOSIS COPILOT</div>
          <h2>面向供应链水风险的 AI 诊断工作台</h2>
          <p>用户可以围绕关键原材料、供应链节点、风险敞口、压力情景和管理建议提出问题。AI 接入后将在这里读取当前分析上下文，并返回面向管理决策的诊断回答。</p>
        </div>
        <div class="ai-status-stack">
          <span>数据上下文已加载</span>
          <span>当前分析结果已同步</span>
          <span>报告出口已就绪</span>
        </div>
      </div>

      <div class="ai-console-layout">
        <div class="ai-chat-panel">
          <div class="chat-head">
            <div>
              <span>Conversation</span>
              <strong>AquaVista AI 诊断窗口</strong>
            </div>
            <em>待接入企业 AI 服务</em>
          </div>
          <div class="chat-body">
            <div class="chat-message assistant">
              <span>AI</span>
              <p>我已准备读取当前项目的供应链节点、采购结构、地点水风险、敞口计算和压力测试结果。你可以询问“为什么某个节点优先级更高”、“情景变化意味着什么”或“报告中应如何解释数据缺口”。</p>
            </div>
            <div class="chat-prompt-grid">
              ${[
                "哪些供应链节点对风险敞口贡献最高？",
                `${scenario.name}下风险结构发生了什么变化？`,
                "报告里应该如何说明数据置信度？",
                "下一步管理动作应该优先从哪里开始？"
              ].map((item) => `<button type="button">${item}</button>`).join("")}
            </div>
          </div>
          <div class="chat-composer">
            <textarea rows="3" placeholder="输入你想了解的问题，例如：为什么巴西节点是第一优先管理节点？"></textarea>
            <button type="button" class="button primary">发送</button>
          </div>
          <p class="chat-note">当前为前端对话窗口位置预留；接入 AI 后，用户问题将在此提交并由网站 AI 返回回答。</p>
        </div>

        <aside class="ai-side-panel">
          <div class="context-card dark">
            <span>Current Context</span>
            <strong>${industry.enterprise} · ${industry.title}</strong>
            <p>当前界面使用项目内节点数据作为 AI 诊断上下文，Demo 或用户上传数据会进入同一分析流程。</p>
          </div>
          <div class="report-download-card">
            <span>Report Delivery</span>
            <h3>报告交付</h3>
            <p>报告作为 AI 诊断界面的交付出口保留，不再单独占用一个页面入口。</p>
            <div class="report-actions">
              <a class="button primary" href="aquavista-sugarcane-diagnosis-report.pdf">下载 PDF</a>
              <a class="button" href="diagnosis-report.html" download>下载 HTML</a>
              <a class="button" href="diagnosis-report.html">打开报告</a>
            </div>
          </div>
          <div class="context-card">
            <span>Risk Exposure</span>
            <strong>${formatNumber(base.total)}</strong>
            <p>前三优先节点：${[first, second, third].filter(Boolean).map((node) => node.id).join(" / ")}</p>
          </div>
          <div class="context-card">
            <span>Scenario Change</span>
            <strong>${delta >= 0 ? "+" : ""}${formatNumber(delta)}</strong>
            <p>${scenario.name}下的风险敞口变化已同步到当前诊断上下文。</p>
          </div>
        </aside>
      </div>
    </section>`;
}

function buildDiagnosis(base, stressed, scenario) {
  const top3 = base.top3;
  const scenarioDelta = stressed.total - base.total;
  const nodeAdvice = top3.flatMap((node) => {
    const mechanisms = activeIndustry().mechanisms.filter((item) => node.drivers.includes(item.indicator));
    return mechanisms.slice(0, 1).map((item) => `${node.id} ${node.area}：${item.measures[0]}，对应风险原因“${item.indicator}”。`);
  });
  return [
    { title: "总体诊断", body: `基准总 SWE 为 ${formatNumber(base.total)} m3/yr，风险管理优先级集中在 ${top3.map((node) => node.area).join("、")}。` },
    { title: "前三大风险节点", body: top3.map((node) => `${node.rank}. ${node.id} ${node.area}，贡献度 ${formatPercent(node.contribution, 2)}`).join("；") },
    { title: "风险原因", body: top3.map((node) => `${node.id}：${node.drivers.join("、")}`).join("；") },
    { title: "风险传导路径", body: "水风险变化会通过供水稳定性、单产、含糖量、采购成本和压榨连续性传导到企业经营管理。" },
    { title: "情景对比", body: `${scenario.name}下总 SWE 为 ${formatNumber(stressed.total)}，相对基准${scenarioDelta >= 0 ? "增加" : "减少"} ${formatNumber(Math.abs(scenarioDelta))}。` },
    { title: "短期管理措施", body: nodeAdvice.slice(0, 2).join(" ") },
    { title: "中长期管理措施", body: "建立替代产区池、供应商水管理合作机制和坐标级水风险数据更新流程。" },
    { title: "数据缺口与置信度", body: "进口原糖四国产区采购占比为当前估算口径，需用企业真实采购台账和具体蔗区坐标复核。" }
  ];
}

function diagnosisList(items) {
  return `<div class="diagnosis-list">${items.map((item) => `<article>
    <strong>${item.title}</strong>
    <p>${item.body}</p>
  </article>`).join("")}</div>`;
}

function agentPayload(base, stressed, scenario) {
  return {
    industry: activeIndustry().title,
    enterprise: activeIndustry().enterprise,
    calculationConclusion: {
      baselineTotalSWE: Math.round(base.total),
      top3: base.top3.map((node) => ({ id: node.id, area: node.area, contribution: Number((node.contribution * 100).toFixed(2)) }))
    },
    scenarioConclusion: {
      scenario: scenario.name,
      totalSWE: Math.round(stressed.total),
      supplyGap: Number((stressed.supplyGap * 100).toFixed(2))
    },
    dataGaps: ["进口原糖拆分比例", "具体蔗区坐标", "供应商级灌溉水源"]
  };
}

function reportPage() {
  return agentPage();
}

function firstNonEmpty(row, aliases, fallback = "") {
  for (const key of aliases) {
    const value = row[key];
    if (value !== undefined && value !== null && String(value).trim() !== "") {
      return value;
    }
  }
  return fallback;
}

function numberFromAliases(row, aliases, fallback = 0) {
  const raw = firstNonEmpty(row, aliases, fallback);
  const parsed = Number(String(raw).replace(/,/g, ""));
  return Number.isFinite(parsed) ? parsed : fallback;
}

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/).filter(Boolean);
  const headers = lines.shift().split(",").map((item) => item.trim());
  return lines.map((line, index) => {
    const cells = line.split(",").map((item) => item.trim());
    const row = Object.fromEntries(headers.map((header, i) => [header, cells[i] || ""]));
    return {
      id: firstNonEmpty(row, ["node_id", "节点编号", "节点ID", "编号", "节点"], `U${String(index + 1).padStart(2, "0")}`),
      material: firstNonEmpty(row, ["原材料", "material", "材料", "品类"], "甘蔗"),
      supplier: firstNonEmpty(row, ["产区/供应商", "供应商", "供应商名称", "supplier"], "用户上传节点"),
      area: firstNonEmpty(row, ["区域", "地区", "产区", "country", "region"], firstNonEmpty(row, ["产区/供应商", "供应商", "供应商名称", "supplier"], "用户上传节点")),
      preciseLocation: firstNonEmpty(row, ["精确位置", "详细位置", "坐标", "经纬度", "precise_location", "location"], firstNonEmpty(row, ["产区/供应商", "供应商", "供应商名称", "supplier"], "待补充")),
      purchaseShare: numberFromAliases(row, ["采购比例(E)", "采购比例", "采购权重", "购买占比", "purchase_share", "procurement_share", "share"]),
      waterFootprint: numberFromAliases(row, ["水足迹W", "水足迹", "water_footprint", "W"]),
      riskR: numberFromAliases(row, ["BWS系数R", "区域风险R", "水风险R", "风险系数", "risk_r", "risk_score", "baseline_water_stress", "Ri", "区域水风险", "水风险"]),
      regionRisk: firstNonEmpty(row, ["区域风险等级", "区域风险", "风险等级", "region_risk"], "待定"),
      confidence: firstNonEmpty(row, ["置信度", "confidence"], "中"),
      dataNature: "用户上传",
      sources: firstNonEmpty(row, ["数据来源", "source", "sources"], "用户上传"),
      drivers: ["长期干旱与旱季供水下降", "基准水压力变化"],
      map: [25 + index * 10, 45 + (index % 3) * 10],
      production: 0,
      productionYear: ""
    };
  }).filter((node) => node.purchaseShare > 0);
}

function setFieldValue(id, value) {
  const element = document.getElementById(id);
  if (element) element.value = value ?? "";
}

function selectedPresetNode() {
  const presetId = document.getElementById("presetNode")?.value;
  return activeIndustry().nodes.find((node) => node.id === presetId);
}

function fillManualFormFromPreset() {
  const node = selectedPresetNode();
  if (!node) return;
  setFieldValue("manualMaterial", node.material);
  setFieldValue("manualArea", node.area);
  setFieldValue("manualLocation", node.preciseLocation);
  setFieldValue("manualShare", Number((node.purchaseShare * 100).toFixed(2)));
  setFieldValue("manualWater", String(node.waterFootprint));
  setFieldValue("manualWaterCustom", "");
  setFieldValue("manualRisk", String(node.riskR));
  setFieldValue("manualRiskCustom", "");
  setFieldValue("manualConfidence", node.confidence);
}

function readNumberField(id) {
  const value = Number(document.getElementById(id)?.value || 0);
  return Number.isFinite(value) ? value : 0;
}

function addManualNode() {
  const preset = selectedPresetNode();
  const area = document.getElementById("manualArea")?.value.trim();
  const purchaseInput = readNumberField("manualShare");
  const waterMode = document.getElementById("manualWater")?.value;
  const riskMode = document.getElementById("manualRisk")?.value;
  const waterFootprint = waterMode === "custom" ? readNumberField("manualWaterCustom") : Number(waterMode || 0);
  const riskR = riskMode === "custom" ? readNumberField("manualRiskCustom") : Number(riskMode || 0);
  const status = document.getElementById("manualStatus");

  if (!area || purchaseInput <= 0 || riskR < 0) {
    if (status) status.textContent = "请至少补充产区、采购比例和区域水风险。";
    return;
  }

  const existing = state.uploadedNodes && state.uploadedNodes.length ? [...state.uploadedNodes] : [];
  const id = preset?.id || `U${String(existing.length + 1).padStart(2, "0")}`;
  const nextNode = {
    ...(preset || {}),
    id,
    material: document.getElementById("manualMaterial")?.value || preset?.material || "甘蔗",
    supplier: area,
    area,
    preciseLocation: document.getElementById("manualLocation")?.value.trim() || area,
    purchaseShare: purchaseInput > 1 ? purchaseInput / 100 : purchaseInput,
    waterFootprint: waterFootprint > 0 ? waterFootprint : 0,
    riskR: clamp(riskR, 0, 1),
    regionRisk: preset?.regionRisk || "待定",
    confidence: document.getElementById("manualConfidence")?.value || "中",
    dataNature: preset ? "模板选择后补充" : "手动录入",
    sources: "企业填写",
    drivers: preset?.drivers || ["长期干旱与旱季供水下降", "基准水压力"],
    map: preset?.map || [42, 50],
    production: preset?.production || 0,
    productionYear: preset?.productionYear || ""
  };

  const index = existing.findIndex((node) => node.id === id);
  if (index >= 0) existing[index] = nextNode;
  else existing.push(nextNode);

  state.uploadedNodes = existing;
  localStorage.setItem("aquavista.uploadedNodes", JSON.stringify(existing));
  render();
}

function attachEvents() {
  document.querySelectorAll("[data-industry]").forEach((button) => {
    button.addEventListener("click", () => {
      state.industryKey = button.dataset.industry;
      localStorage.setItem("aquavista.industry", state.industryKey);
      render();
    });
  });
  document.querySelectorAll("[data-scenario]").forEach((button) => {
    button.addEventListener("click", () => {
      state.scenarioId = button.dataset.scenario;
      localStorage.setItem("aquavista.scenario", state.scenarioId);
      render();
    });
  });
  const csvInput = document.getElementById("csvInput");
  if (csvInput) {
    csvInput.addEventListener("change", async (event) => {
      const file = event.target.files[0];
      if (!file) return;
      const text = await file.text();
      const nodes = parseCsv(text);
      if (nodes.length < 1) {
        document.getElementById("uploadStatus").textContent = "未识别到有效节点，请检查采购比例和 BWS 系数字段。";
        return;
      }
      const total = nodes.reduce((sum, node) => sum + node.purchaseShare, 0);
      if (!(total > 0)) {
        document.getElementById("uploadStatus").textContent = "未识别到有效的采购比例，请检查 CSV 列名或数值格式。";
        return;
      }
      const normalized = normalizeNodes(nodes);
      state.uploadedNodes = normalized;
      localStorage.setItem("aquavista.uploadedNodes", JSON.stringify(normalized));
      localStorage.setItem("aquavista.uploadedCsv", text);
      render();
    });
  }
  const presetNode = document.getElementById("presetNode");
  if (presetNode) {
    presetNode.addEventListener("change", fillManualFormFromPreset);
  }
  const addManualNodeBtn = document.getElementById("addManualNodeBtn");
  if (addManualNodeBtn) {
    addManualNodeBtn.addEventListener("click", addManualNode);
  }
  const clearManualNodesBtn = document.getElementById("clearManualNodesBtn");
  if (clearManualNodesBtn) {
    clearManualNodesBtn.addEventListener("click", () => {
      state.uploadedNodes = null;
      localStorage.removeItem("aquavista.uploadedNodes");
      localStorage.removeItem("aquavista.uploadedCsv");
      render();
    });
  }
  const useSampleBtn = document.getElementById("useSampleBtn");
  if (useSampleBtn) {
    useSampleBtn.addEventListener("click", () => {
      state.uploadedNodes = null;
      localStorage.removeItem("aquavista.uploadedNodes");
      localStorage.removeItem("aquavista.uploadedCsv");
      render();
    });
  }
  const downloadTemplateBtn = document.getElementById("downloadTemplateBtn");
  if (downloadTemplateBtn) {
    downloadTemplateBtn.addEventListener("click", () => {
      downloadFile("aquavista_upload_template.csv", "节点编号,原材料,产区/供应商,精确位置,采购比例(E),水足迹W,BWS系数R,区域风险等级,置信度,数据来源\nN01,甘蔗,示例产区,示例位置,0.25,540000000,0.15,低,中,企业上传\n");
    });
  }
  const downloadReportBtn = document.getElementById("downloadReportBtn");
  if (downloadReportBtn) {
    downloadReportBtn.addEventListener("click", () => {
      const report = document.querySelector(".report-card").outerHTML;
      downloadFile("aquavista_diagnosis.html", `<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>AquaVista 诊断结果</title><body>${report}</body></html>`);
    });
  }
}

function downloadFile(name, content) {
  const blob = new Blob([content], { type: "text/plain;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = name;
  a.click();
  URL.revokeObjectURL(url);
}

function escapeHtml(value) {
  return value.replace(/[&<>"']/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#039;" }[char]));
}

const PAGES = {
  home: homePage,
  import: importPage,
  library: libraryPage,
  map: mapPage,
  risk: riskPage,
  stress: stressPage,
  agent: agentPage,
  report: reportPage
};

function render() {
  const page = document.body.dataset.page || "home";
  const industry = activeIndustry();
  if (page === "home") {
    document.getElementById("app").innerHTML = `<div class="landing-shell">${homePage()}</div>`;
    attachEvents();
    return;
  }
  const currentNav = NAV.find((item) => item[4] === page) || ["", ...(PAGE_META[page] || ["⌂", "平台简介"]), "index.html", page];
  const activePage = page === "report" ? "agent" : page;
  const navHtml = NAV.map((item) => `<a class="nav-item ${item[4] === activePage ? "active" : ""}" href="${item[3]}"><span>${item[1]}</span><strong>${item[2]}</strong></a>`).join("");
  document.getElementById("app").innerHTML = `
    <div class="app-shell">
      <aside class="sidebar">
        <a class="logo" href="index.html">${aquaVistaSymbol()}<span><strong>AquaVista</strong><em>AI-POWERED WATER RISK INTELLIGENCE</em></span></a>
        <nav>${navHtml}</nav>
        <div class="side-note">结果用于筛查和优先级排序，不代表实际财务损失概率。</div>
      </aside>
      <main>
        <header class="topbar">
          <div>
            <div class="crumb">AquaVista / ${currentNav[2]}</div>
            <h1>${currentNav[2]}</h1>
          </div>
          <div class="header-actions">
            ${badge(industry.sourceVersion, "teal")}
            ${badge(state.uploadedNodes ? "用户数据" : "示例数据", state.uploadedNodes ? "amber" : "green")}
          </div>
        </header>
        ${PAGES[page] ? PAGES[page]() : homePage()}
      </main>
    </div>`;
  attachEvents();
}

render();



