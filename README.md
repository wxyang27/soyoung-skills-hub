# soyoung-skills-hub

新氧连锁业务 Claude Code 技能市场，包含自研数据分析技能和精选外部技能。

## 快速开始

```bash
git clone https://github.com/<your-account>/soyoung-skills-hub.git
cd soyoung-skills-hub
npx skills add ./skills/nl2sql
```

## 技能清单

### 自研技能

| 技能 | 说明 | 状态 |
|------|------|------|
| `nl2sql` | 自然语言 → MaxCompute SQL 标准模板库 | 🔜 规划中 |
| `data-monitor` | 核心指标自动监控与飞书预警 | 🔜 规划中 |
| `auto-report` | 周报/月报自动生成与推送 | 🔜 规划中 |
| `data-lineage` | 数据血縁自动分析与变更影响评估 | 🔜 规划中 |

### 外部精选

| 技能 | 来源 | 说明 |
|------|------|------|
| `notebooklm` | [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py) | NotebookLM CLI/API 集成 |

## 目录结构

```
soyoung-skills-hub/
├── skills/          # 自研技能（每个一个文件夹，xx-xx-xx 命名）
├── external/        # 外部技能（git submodule）
├── templates/       # 新技能脚手架
└── .github/         # CI 校验
```

## 技能命名规范

采用 `xx-xx-xx` 格式，全小写，单词间用连字符分隔：

- `nl2sql` — NL2SQL 模板库
- `data-monitor` — 数据监控
- `auto-report` — 自动化报告
- `data-lineage` — 血縁分析

## 贡献

1. 基于 `templates/SKILL_TEMPLATE.md` 创建新技能
2. 提交前运行 `python scripts/validate.py`
3. 向 master 发 PR
