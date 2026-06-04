# chain-nl-query · 连锁自然语言取数 Skill

把一句自然语言的取数需求 → 翻译成**符合公司标准口径**的、可执行的 SQL（需要时再执行返回数据）。
**只做取数，不做经营分析/诊断/归因。** 不确定且影响结果时，会先向提问者确认口径。

基于两份资料构建：
- 《【经管中心】一文掌握连锁数据库表！》→ 49 张核心表地图
- 《【经管中心】一文掌握连锁指标字典！》→ 19 原子 + 132 衍生 + 112 用户画像字段 + 288 看板指标 + 维度/数据源

## 目录结构
```
chain-nl-query/
├── SKILL.md                      # 主入口：取数流程 + 澄清协议 + 口径速查
├── README.md                     # 本文件：说明与部署
├── references/
│   ├── 01-atomic-metrics.md      # 19 原子指标（定义/聚合/SQL）
│   ├── 02-derived-metrics.md     # 132 衍生指标（索引 + 过滤模板 + 复合 SQL）
│   ├── 03-user-profile-fields.md # 112 用户画像字段（用户级）
│   ├── 04-dimensions.md          # 维度字典 + 字段名差异裁决（关键）
│   ├── 05-tables.md              # 49 张核心表地图 + 关联键 + 避坑
│   ├── 06-data-sources.md        # 指标字典口径的底表目录
│   ├── 07-dashboard-metrics.md   # 288 看板指标 → 标准口径映射
│   ├── 08-sql-conventions.md     # 分区/过滤/时间翻译/方言/骨架
│   └── examples.md               # NL → 澄清 → SQL 完整示例
└── scripts/
    ├── query_runner.py           # 可选：只读取数执行器（ODPS）
    └── README.md                 # 执行与部署说明
```

## 部署到别的地方

这是一个标准的「文件型 Skill」，自包含、可整目录拷贝。

- **Claude Code / Agent 项目级 Skill**：把整个 `chain-nl-query/` 目录放到目标项目的 skills 目录（如 `.claude/skills/` 或你团队约定的 skills 路径）。模型会按 `SKILL.md` 的 `description` 自动触发，按需打开 `references/`。
- **其它 LLM/Agent 框架**：把 `SKILL.md` 作为系统提示/工具说明载入，`references/*.md` 作为可检索知识库（RAG 或按需读取）。
- **执行能力**可选，见 `scripts/README.md`：可只产 SQL，也可配 `query_runner.py` 或接环境已有的查询接口。

打包：
```bash
zip -r chain-nl-query.zip chain-nl-query
```

## 重新生成 references（当字典/表文档更新时）
`references/01,02,03,05,06,07` 由源文档自动生成；`04,08,examples` 为人工编写。
源文档更新后，用生成脚本重跑前者（脚本：`/tmp/gen_refs.py` 的逻辑，读 docx/xlsx 产出 md），
再人工复核 `04-dimensions.md` 的字段名差异表是否仍准确。

## 维护要点
- **字段名以实际 SQL 为准**（字典登记名常与实表不一致），见 `references/04-dimensions.md`。
- 字典里个别 SQL 有待确认项（如核销客单价的人次口径、渗透率的品项字段），已在对应文件标注。
- 看板指标约 259/288 未进标准字典，命中这类需按澄清协议确认口径。
