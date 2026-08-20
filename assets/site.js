const NAV = [
  ["0", "⌂", "管理总览", "index.html", "home"],
  ["1", "↥", "导入数据", "data-import.html", "import"],
  ["2", "◉", "行业画像", "data-library.html", "library"],
  ["3", "▱", "供应链位置", "supply-map.html", "map"],
  ["4", "◌", "优先节点", "risk-exposure.html", "risk"],
  ["5", "☁", "情景影响", "stress-test.html", "stress"],
  ["6", "☷", "AI 建议", "agent-analysis.html", "agent"],
  ["7", "▤", "报告下载", "report-export.html", "report"]
];

const PAGE_META = {
  map: ["▱", "供应链位置"]
};

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
    method: "SWEi = Ei × Wi × Ri",
    requiredFields: ["节点编号", "产区/供应商", "精确位置", "采购比例(E)", "水足迹W", "BWS系数R", "置信度"],
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
      },
      {
        id: "shift10",
        name: "采购调整模板",
        shortName: "N03 → N06 10%",
        description: "扩展模板：将第一贡献节点 10% 采购占比转移到低风险备选节点，用于后续 C 组采购调整情景。",
        mode: "purchaseShift",
        fromNodeId: "N03",
        toNodeId: "N06",
        shiftShare: 0.1,
        experimental: true
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
  industryKey: localStorage.getItem("waterpulse.industry") || DEFAULT_INDUSTRY,
  scenarioId: localStorage.getItem("waterpulse.scenario") || "dry20",
  uploadedNodes: loadUploadedNodes()
};

function loadUploadedNodes() {
  try {
    const raw = localStorage.getItem("waterpulse.uploadedNodes");
    return raw ? JSON.parse(raw) : null;
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
  return state.uploadedNodes && state.uploadedNodes.length ? state.uploadedNodes : activeIndustry().nodes;
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
      scenarioNote: node.id === scenario.failedNodeId ? "节点失效" : "剩余供应"
    }));
  } else if (scenario?.mode === "purchaseShift") {
    working = working.map((node) => ({ ...node, scenarioRiskR: node.riskR }));
    const from = working.find((node) => node.id === scenario.fromNodeId);
    const to = working.find((node) => node.id === scenario.toNodeId);
    if (from && to) {
      const shifted = Math.min(from.purchaseShare, scenario.shiftShare);
      from.purchaseShare -= shifted;
      to.purchaseShare += shifted;
      from.scenarioNote = `转出 ${formatPercent(shifted, 1)}`;
      to.scenarioNote = `转入 ${formatPercent(shifted, 1)}`;
    }
  }

  working = working.map((node) => {
    const effectiveRisk = node.scenarioRiskR ?? node.riskR;
    const swe = node.scenarioFailed ? 0 : node.purchaseShare * node.waterFootprint * effectiveRisk;
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
      priority: priorityLabel(rankMap.get(node.id), node.contribution)
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
    N01: "label-above",
    N02: "label-left",
    N03: "label-right",
    N04: "label-right",
    N05: "label-left",
    N06: "label-above"
  };
  return placements[node.id] || "label-right";
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

function homePage() {
  const industry = activeIndustry();
  const base = calcSummary(activeNodes());
  const scenario = industry.scenarios.find((item) => item.id === state.scenarioId) || industry.scenarios[0];
  const stressed = calcSummary(activeNodes(), scenario);
  const verdict = userVerdict(base, scenario, stressed);

  return `
    ${industrySelector()}
    <section class="panel hero-panel executive">
      <div class="kicker">${industry.enterprise} · ${industry.title}</div>
      <h2>${verdict.headline}</h2>
      <p>${verdict.body}</p>
      <div class="button-row">
        <a class="button primary" href="agent-analysis.html">查看 AI 建议</a>
        <a class="button" href="diagnosis-report.html">打开诊断报告</a>
      </div>
    </section>
    <section class="grid two">
      <div class="panel">
        <h3>今天先看这三个节点</h3>
        ${priorityCards(base.rows)}
        ${evidenceDetails("查看排序依据", rowsTable(base.rows, true))}
      </div>
      <div class="panel">
        <h3>建议动作</h3>
        ${actionCards(base)}
      </div>
    </section>`;
}

function importPage() {
  const industry = activeIndustry();
  const rows = calcSummary(activeNodes()).rows;
  const usingUpload = Boolean(state.uploadedNodes);

  return `
    <section class="grid two">
      <div class="panel">
        <h3>选择数据来源</h3>
        <p class="lead-small">演示时可直接使用示例数据；企业试用时上传一张节点表即可。</p>
        <div class="upload-box">
          <input id="csvInput" type="file" accept=".csv,text/csv" />
          <div>
            <strong>上传 CSV 企业节点表</strong>
            <p class="muted">支持列名：节点编号、产区/供应商、精确位置、采购比例(E)、水足迹W、BWS系数R、置信度。</p>
          </div>
        </div>
        <div class="button-row">
          <button class="button primary" id="useSampleBtn">使用示例数据</button>
          <button class="button" id="downloadTemplateBtn">下载 CSV 模板</button>
        </div>
        <div id="uploadStatus" class="notice"></div>
      </div>
      <div class="panel">
        <h3>当前数据状态</h3>
        ${validationPanel(activeNodes())}
        ${evidenceDetails("查看需要的字段", `<div class="field-cloud">${industry.requiredFields.map((field) => badge(field, "gray")).join("")}</div>`)}
      </div>
    </section>
    <section class="panel">
      <h3>导入后会得到什么</h3>
      <div class="outcome-strip">
        <span>优先节点</span><span>情景影响</span><span>AI 建议</span><span>诊断报告</span>
      </div>
      ${evidenceDetails("查看节点预览", rowsTable(rows))}
    </section>`;
}

function validationPanel(nodes) {
  const share = nodes.reduce((sum, node) => sum + node.purchaseShare, 0);
  const missing = nodes.flatMap((node) => ["id", "area", "purchaseShare", "waterFootprint", "riskR"].filter((key) => node[key] === undefined || node[key] === null || node[key] === ""));
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
    </section>
    <section class="panel">
      <h3>后续新增行业</h3>
      <p class="lead-small">后续接入其他行业时，只需要补充行业机制、节点数据和情景规则，用户界面仍保持同一套决策流程。</p>
      ${evidenceDetails("查看扩展字段", `<div class="schema-grid">
        ${["industryId", "materialId", "mechanisms", "nodes", "scenarios", "requiredFields"].map((field) => `<div><strong>${field}</strong><span>系统配置项</span></div>`).join("")}
      </div>`)}
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
            return `<button class="map-node ${tone} ${mapLabelClass(node)}" style="left:${node.map[0]}%;top:${node.map[1]}%;width:${size}px;height:${size}px" title="${node.area}">
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
        <h3>选择一个管理问题</h3>
        <div class="segmented">
          ${industry.scenarios.map((item) => `<button class="${item.id === scenario.id ? "active" : ""}" data-scenario="${item.id}">
            ${item.name}${item.experimental ? "<small>扩展</small>" : ""}
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
    <p>总 SWE 从 ${formatNumber(base.total)} 变为 ${formatNumber(stressed.total)}。前三节点仍为 ${stressed.top3.map((node) => node.area).join("、")}，说明当前风险结构主要由采购规模、水足迹和既有区域风险共同决定。</p>
  </div>`;
}

function agentPage() {
  const industry = activeIndustry();
  const scenario = industry.scenarios.find((item) => item.id === state.scenarioId) || industry.scenarios[0];
  const base = calcSummary(activeNodes());
  const stressed = calcSummary(activeNodes(), scenario);
  const diagnosis = buildDiagnosis(base, stressed, scenario);

  return `
    <section class="grid two">
      <div class="panel">
        <div class="section-head">
          <h3>AI 给管理层的建议</h3>
          <div>
            <a class="button primary" href="diagnosis-report.html">打开正式报告</a>
            <a class="button" href="waterpulse-sugarcane-diagnosis-report.pdf">下载 PDF</a>
          </div>
        </div>
        ${diagnosisList(diagnosis.filter((item) => ["总体诊断", "短期管理措施", "中长期管理措施", "数据缺口与置信度"].includes(item.title)))}
      </div>
      <div class="panel">
        <h3>建议先做的 3 件事</h3>
        ${actionCards(base)}
        ${evidenceDetails("查看诊断原则", `<div class="guardrail-grid">
          ${["只基于已导入数据", "不编造风险指标", "不自行改写计算结果", "不改变节点优先级", "不假设采购比例", "不解释为损失概率"].map((item, index) => `<div class="${index === 0 ? "ok" : ""}">${item}</div>`).join("")}
        </div>`)}
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
  const industry = activeIndustry();
  const scenario = industry.scenarios.find((item) => item.id === state.scenarioId) || industry.scenarios[0];
  const base = calcSummary(activeNodes());
  const stressed = calcSummary(activeNodes(), scenario);
  return `
    <section class="grid two">
      <div class="panel">
        <h3>最终交付</h3>
        <div class="report-card">
          <h2>${industry.enterprise} ${industry.title}水风险诊断</h2>
          <p>基准总 SWE：<strong>${formatNumber(base.total)}</strong> m3/yr</p>
          <p>前三节点：${base.top3.map((node) => `${node.id} ${node.area} ${formatPercent(node.contribution, 2)}`).join("；")}</p>
          <p>当前情景：${scenario.name}，情景总 SWE ${formatNumber(stressed.total)} m3/yr。</p>
          <p>数据缺口：进口拆分比例、蔗区坐标、供应商灌溉水源。</p>
        </div>
        <div class="button-row">
          <a class="button primary" href="diagnosis-report.html">打开正式报告文件</a>
          <a class="button primary" href="waterpulse-sugarcane-diagnosis-report.pdf">下载正式报告 PDF</a>
          <a class="button" href="diagnosis-report.html" download>下载正式报告 HTML</a>
          <button class="button" onclick="window.print()">打印</button>
        </div>
      </div>
      <div class="panel">
        <h3>报告里包含什么</h3>
        <div class="plain-answer">
          <p>一页管理结论。</p>
          <p>A/B/C 组依据和数据缺口。</p>
          <p>短期与中长期管理建议。</p>
        </div>
      </div>
    </section>`;
}

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/).filter(Boolean);
  const headers = lines.shift().split(",").map((item) => item.trim());
  return lines.map((line, index) => {
    const cells = line.split(",").map((item) => item.trim());
    const row = Object.fromEntries(headers.map((header, i) => [header, cells[i] || ""]));
    return {
      id: row["节点编号"] || `U${String(index + 1).padStart(2, "0")}`,
      material: row["原材料"] || "甘蔗",
      supplier: row["产区/供应商"] || row["供应商"] || "用户上传节点",
      area: row["产区/供应商"] || row["精确位置"] || "用户上传节点",
      preciseLocation: row["精确位置"] || row["产区/供应商"] || "待补充",
      purchaseShare: Number(row["采购比例(E)"] || row["采购比例"] || 0),
      waterFootprint: Number(row["水足迹W"] || row["水足迹"] || 0),
      riskR: Number(row["BWS系数R"] || row["区域风险R"] || 0),
      regionRisk: row["区域风险等级"] || "待定",
      confidence: row["置信度"] || "低",
      dataNature: "用户上传",
      sources: row["数据来源"] || "用户上传",
      drivers: ["长期干旱与旱季供水下降", "基准水压力"],
      map: [25 + index * 10, 45 + (index % 3) * 10],
      production: 0,
      productionYear: ""
    };
  }).filter((node) => node.purchaseShare > 0 && node.waterFootprint > 0);
}

function attachEvents() {
  document.querySelectorAll("[data-industry]").forEach((button) => {
    button.addEventListener("click", () => {
      state.industryKey = button.dataset.industry;
      localStorage.setItem("waterpulse.industry", state.industryKey);
      render();
    });
  });
  document.querySelectorAll("[data-scenario]").forEach((button) => {
    button.addEventListener("click", () => {
      state.scenarioId = button.dataset.scenario;
      localStorage.setItem("waterpulse.scenario", state.scenarioId);
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
        document.getElementById("uploadStatus").textContent = "未识别到有效节点，请检查采购比例、水足迹和 BWS 系数字段。";
        return;
      }
      const total = nodes.reduce((sum, node) => sum + node.purchaseShare, 0);
      const normalized = nodes.map((node) => ({ ...node, purchaseShare: node.purchaseShare / total }));
      state.uploadedNodes = normalized;
      localStorage.setItem("waterpulse.uploadedNodes", JSON.stringify(normalized));
      render();
    });
  }
  const useSampleBtn = document.getElementById("useSampleBtn");
  if (useSampleBtn) {
    useSampleBtn.addEventListener("click", () => {
      state.uploadedNodes = null;
      localStorage.removeItem("waterpulse.uploadedNodes");
      render();
    });
  }
  const downloadTemplateBtn = document.getElementById("downloadTemplateBtn");
  if (downloadTemplateBtn) {
    downloadTemplateBtn.addEventListener("click", () => {
      downloadFile("waterpulse_upload_template.csv", "节点编号,原材料,产区/供应商,精确位置,采购比例(E),水足迹W,BWS系数R,区域风险等级,置信度,数据来源\nN01,甘蔗,示例产区,示例位置,0.25,540000000,0.15,低,中,企业上传\n");
    });
  }
  const downloadReportBtn = document.getElementById("downloadReportBtn");
  if (downloadReportBtn) {
    downloadReportBtn.addEventListener("click", () => {
      const report = document.querySelector(".report-card").outerHTML;
      downloadFile("waterpulse_diagnosis.html", `<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>WaterPulse 诊断结果</title><body>${report}</body></html>`);
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
  const currentNav = NAV.find((item) => item[4] === page) || ["", ...(PAGE_META[page] || ["⌂", "管理总览"]), "index.html", page];
  const navHtml = NAV.map((item) => `<a class="nav-item ${item[4] === page ? "active" : ""}" href="${item[3]}"><span>${item[1]}</span><strong>${item[2]}</strong></a>`).join("");
  document.getElementById("app").innerHTML = `
    <div class="app-shell">
      <aside class="sidebar">
        <a class="logo" href="index.html"><span class="logo-mark"></span><span><strong>WaterPulse</strong><em>AI Water Risk Agent</em></span></a>
        <div class="project-card">
          <span>当前项目</span>
          <strong>${industry.enterprise}</strong>
          <em>${industry.title}</em>
        </div>
        <nav>${navHtml}</nav>
        <div class="side-note">结果用于筛查和优先级排序，不代表实际财务损失概率。</div>
      </aside>
      <main>
        <header class="topbar">
          <div>
            <div class="crumb">WaterPulse / ${currentNav[2]}</div>
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
