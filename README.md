# soyoung-skills-hub

新氧（soyoung）连锁医美业务 AI 技能市场，面向数据智能部的技能集合。将业务知识、数据查询、分析复盘能力封装为可复用的 AI Agent 技能模块。

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/wxyang27/soyoung-skills-hub.git

# 方式一：批量安装所有技能
cp -r skills/* ~/.codex/skills/

# 方式二：安装单个技能
npx skills add ./skills/chain-nl-query
```

> 使用 `maxcompute-pyodps` 技能前需要配置 ODPS 凭据（环境变量或 `.env.odps` 文件），详见该技能的 SKILL.md。

---

## 技能清单

### 知识层（业务背景 + 指标口径）

| 技能 | 说明 | 文件数 |
|------|------|--------|
| `chain-business-context` | 连锁业务全景知识库 — 数仓四层架构（DIM/DWD/DWS/DM）、49 张核心表（十大主题）、19 原子 + 132 衍生指标体系、核心公式与参考值、七步标准分析流程、五套核心分析逻辑、异常诊断路径、SQL 编写规范 | 4 |
| `chain-metric-dictionary` | 连锁指标口径字典 — 19 个原子指标（A001-A019）、132 个衍生指标（D001-D132）的定义/计算逻辑/SQL 示例、10 个维度切片体系、112 个用户画像字段、派生指标计算规则、核心数据源与口径说明 | 5 |

### 查询层（自然语言取数 + 数仓连接）

| 技能 | 说明 | 文件数 |
|------|------|--------|
| `chain-nl-query` ⭐ | **自然语言 → 标准口径 SQL** — 五步取数流程（解析需求 → 匹配口径 → 定表 → 组装 SQL → 自检输出），内置澄清协议（不确定口径先追问），产出可执行 SQL 并可按需执行返回数据 | 13 |
| `nl2sql` | 自然语言 → MaxCompute SQL 模板库 — 内置四维业务知识 RAG（指标语义 + 维度值域 + 计算逻辑 + Schema 映射），覆盖收入/渠道/品项/LTV/新老客/同比环比 6 类模板 | 13 |
| `maxcompute-pyodps` | PyODPS 连接器 — 连接阿里云 MaxCompute 数仓，查看表结构、执行只读 SQL 查询、获取分区信息、导出 CSV。内置安全校验，拒绝写/删/改/DDL | 6 |

### 分析层（专题复盘）

| 技能 | 说明 | 文件数 |
|------|------|--------|
| `gross-margin-review` ⭐ | **品项毛利率三维复盘** — 收入侧毛利结构（三类品：大师团/绿标品/常规品，互斥分类）、成本侧耗材 + 手工费、补贴侧额度定价策略（促销补贴/门店改价/历史价差/成本型补贴）、会员等级灌券漏斗（发券→用券→核销→纯薅→0 元成本）、六步复盘法 + 诊断矩阵 | 12 |

### 规划中

| 技能 | 说明 |
|------|------|
| `data-monitor` | 核心指标自动监控与飞书预警 |
| `auto-report` | 周报/月报自动生成与推送 |
| `data-lineage` | 数据血缘自动分析与变更影响评估 |

---

## 技能协作关系

```
                    ┌──────────────────────┐
                    │ chain-business-context│ ← 知识层：表结构 + 分析框架
                    │ chain-metric-dictionary│ ← 知识层：指标定义 + 口径
                    └──────┬───────────────┘
                           │ 提供业务背景和指标口径
                           ▼
            ┌──────────────────────────────┐
            │       chain-nl-query          │ ← 查询层：NL → 标准口径 SQL
            │          nl2sql               │ ← 查询层：模板 + RAG 生成 SQL
            └──────────────┬───────────────┘
                           │ 产出可执行 SQL
                           ▼
            ┌──────────────────────────────┐
            │      maxcompute-pyodps        │ ← 连接层：执行 SQL 取数
            └──────────────┬───────────────┘
                           │ 返回数据
                           ▼
            ┌──────────────────────────────┐
            │    gross-margin-review        │ ← 分析层：专题复盘 + 诊断
            └──────────────────────────────┘
```

- **知识层** 为查询层提供表结构、字段名、指标定义和过滤条件
- **查询层** 把自然语言翻译成正确口径的 SQL，调用连接层执行
- **连接层** 连接 MaxCompute 安全执行只读查询
- **分析层** 整合以上三层能力，做专题深度复盘

---

## 目录结构

```
soyoung-skills-hub/
├── README.md
├── .gitignore
├── skills/                              # 自研技能（6 个）
│   ├── chain-business-context/          # 知识层：连锁业务全景
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   │       └── 连锁业务问答背景.md
│   │
│   ├── chain-metric-dictionary/         # 知识层：指标口径字典
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   └── references/
│   │       ├── 连锁经营指标口径回答.md
│   │       ├── 【经管中心】一文掌握连锁数据库表！.docx
│   │       └── 【经管中心】一文掌握连锁指标字典！.xlsx
│   │
│   ├── chain-nl-query/                  # 查询层：NL → 标准口径 SQL
│   │   ├── SKILL.md
│   │   ├── README.md
│   │   ├── references/                  # 9 个参考文件
│   │   │   ├── 01-atomic-metrics.md     # 19 原子指标
│   │   │   ├── 02-derived-metrics.md    # 132 衍生指标
│   │   │   ├── 03-user-profile-fields.md# 112 用户画像字段
│   │   │   ├── 04-dimensions.md         # 维度字典 + 字段名差异表
│   │   │   ├── 05-tables.md             # 49 张核心表地图
│   │   │   ├── 06-data-sources.md       # 数据源目录
│   │   │   ├── 07-dashboard-metrics.md  # 288 看板指标映射
│   │   │   ├── 08-sql-conventions.md    # SQL 编写规范
│   │   │   └── examples.md              # 完整示例
│   │   └── scripts/
│   │       ├── query_runner.py          # 只读取数执行器
│   │       └── README.md
│   │
│   ├── nl2sql/                          # 查询层：模板 + RAG
│   │   ├── SKILL.md
│   │   ├── references/                  # 四维知识库
│   │   │   ├── metric-semantics.md
│   │   │   ├── dimension-dictionary.md
│   │   │   ├── calculation-logic.md
│   │   │   └── schema-mapping.json
│   │   ├── scripts/
│   │   │   ├── rag_query.py             # RAG 检索器
│   │   │   └── build_knowledge_base.py  # 知识库构建
│   │   └── templates/                   # 6 个 SQL 模板
│   │       ├── revenue.yaml
│   │       ├── channel.yaml
│   │       ├── product.yaml
│   │       ├── customer.yaml
│   │       ├── compare.yaml
│   │       └── ltv.yaml
│   │
│   ├── maxcompute-pyodps/               # 连接层：PyODPS
│   │   ├── SKILL.md
│   │   ├── references/
│   │   │   └── connection-guide.md
│   │   └── scripts/
│   │       └── mc_query.py              # CLI：schema/sql/partitions
│   │
│   └── gross-margin-review/             # 分析层：品项毛利率复盘
│       ├── SKILL.md                     # 三维分析框架 + 六步复盘法
│       └── references/                  # 12 个参考文件
│           ├── 01_品项毛利率_近12月_三类品.sql
│           ├── 02_让利补贴_分用券时等级漏斗.sql
│           ├── 03_0元单成本_分会员等级.sql
│           ├── 04_让利补贴_分发券时等级漏斗_纯薅.sql
│           ├── H1补贴毛利复盘_总览.html
│           ├── 毛利率专题全量汇总.md
│           ├── 毛利率专题文档汇总（2026 H1）.md
│           ├── 毛利率数据模型详解.md
│           ├── 毛利率聊天记录原文.txt
│           ├── 补贴看板_品项sku额度分析_20260604_1426.xlsx
│           └── 题2_门店补贴数据.xlsx
│
├── external/                            # 外部精选技能
├── templates/                           # 新技能脚手架模板
└── .github/                             # CI 校验
```

---

## 安装方式

**方式一：批量安装（推荐）**

```bash
cp -r skills/* ~/.codex/skills/
```

**方式二：单个安装**

```bash
npx skills add ./skills/chain-nl-query
npx skills add ./skills/gross-margin-review
```

**方式三：链接安装（开发时使用，修改实时生效）**

```bash
ln -s $(pwd)/skills/chain-nl-query ~/.codex/skills/chain-nl-query
```

---

## 贡献

1. 基于 `templates/` 目录中的模板创建新技能
2. 每个技能必须包含 `SKILL.md`（含 frontmatter 元数据）
3. 参考文档放 `references/`，可执行脚本放 `scripts/`
4. 向 `master` 分支发起 PR

### 技能开发规范

```
skill-name/
├── SKILL.md                         # 必填：技能主文件（含 YAML frontmatter）
├── README.md                        # 可选：技能说明
├── agents/                          # 可选：Agent 框架元数据
│   └── openai.yaml
├── references/                      # 可选：参考文档（按需加载的知识库）
├── scripts/                         # 可选：可执行脚本
└── templates/                       # 可选：模板文件（SQL/YAML 等）
```

### SKILL.md Frontmatter 格式

```yaml
---
name: skill-name
description: 一句话描述 + 触发场景 + 关键词
---
```

---

## 技术栈

- **数据仓库**：阿里云 MaxCompute（ODPS），Project `soyoung_dw`，北京 Region
- **查询引擎**：PyODPS SDK（Python ≥ 3.8）
- **AI Agent 框架**：Claude Code Skills / Codex Skills
- **RAG 检索引擎**：ChromaDB + Sentence Transformers（`nl2sql` 技能用）
- **协作平台**：飞书（消息推送 / 看板 / 知识库 / 多维表格）
