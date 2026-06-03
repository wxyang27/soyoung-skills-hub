# soyoung-skills-hub

新氧连锁业务数据技能市场，包含自研数据分析技能和精选外部技能。

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/wxyang27/soyoung-skills-hub.git ~/.codex/skills

# 或者只安装单个技能
npx skills add ./skills/nl2sql
```

## 技能清单

### 自研技能

| 技能 | 说明 | 状态 |
|------|------|------|
| `chain-business-context` | 连锁业务问答背景 — 数仓表结构、指标体系、分析方法 | ✅ 已完成 |
| `chain-metric-dictionary` | 连锁指标口径查询 — 原子/衍生指标定义、计算逻辑、SQL | ✅ 已完成 |
| `nl2sql` | 自然语言 → MaxCompute SQL（收入/渠道/品项/LTV等） | ✅ 已完成 |
| `data-monitor` | 核心指标自动监控与飞书预警 | 🔜 规划中 |
| `auto-report` | 周报/月报自动生成与推送 | 🔜 规划中 |
| `data-lineage` | 数据血缘自动分析与变更影响评估 | 🔜 规划中 |

### 外部精选

| 技能 | 来源 | 说明 |
|------|------|------|
| `notebooklm` | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | NotebookLM CLI/API 集成 |

## 目录结构

```
soyoung-skills-hub/
├── skills/                      # 自研技能（直接复制到 ~/.codex/skills/ 即可使用）
│   ├── chain-business-context/  # 连锁业务问答背景
│   ├── chain-metric-dictionary/ # 连锁指标口径查询
│   └── nl2sql/                  # NL2SQL 模板库
├── external/                    # 外部技能
├── templates/                   # 新技能脚手架
└── .github/                     # CI 校验
```

## 安装方式

方式一：将整个 skills/ 目录复制到 Codex 技能目录
```bash
cp -r skills/* ~/.codex/skills/
```

方式二：使用 npx 安装单个技能
```bash
npx skills add ./skills/nl2sql
```

## 贡献

1. 基于 `templates/SKILL_TEMPLATE.md` 创建新技能
2. 向 master 发 PR

## 技能开发指南

每个技能文件夹遵循标准结构：

```
skill-name/
├── SKILL.md                     # 技能主文件（必填）
├── agents/openai.yaml           # UI元数据
├── references/                  # 参考文档（按需加载）
├── scripts/                     # 可执行脚本
└── templates/                   # 模板文件
```
