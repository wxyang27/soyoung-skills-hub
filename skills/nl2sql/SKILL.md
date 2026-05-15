---
name: nl2sql
description: 新氧连锁 NL2SQL 标准模板库 —— 将自然语言需求转为 MaxCompute SQL，覆盖收入/渠道/品项/LTV/新老客等高频分析场景。内部集成四维业务知识 RAG（指标语义+维度值域+计算逻辑+Schema映射）。
metadata:
  version: 0.1.0
  author: Xinyang
  tags: [soyoung, maxcompute, sql, analytics]
---

# nl2sql — 自然语言 → MaxCompute SQL

## 触发方式

- 关键词：收入、渠道、品项、LTV、新客、老客、客单价、留存率、同比、环比、分析、查询
- 用户说法示例："昨天老客收入""近3个月渠道分布""奇迹胶原5月销量"
- 显式调用：`/nl2sql`

## 四维知识库

本技能内置 RAG 检索器，在生成 SQL 之前自动检索：

| 维度 | 来源 | 用途 |
|------|------|------|
| 指标语义 | references/metric-semantics.md | "老客收入" → exe_income, is_new=0 |
| 维度值域 | references/dimension-dictionary.md | "私域" → cx_second_channel='私域活动' |
| 计算逻辑 | references/calculation-logic.md | _all_d dp用法、客单价分母 |
| Schema映射 | references/schema-mapping.json | 字段名、表名、分区策略 |

检索方式：`python scripts/rag_query.py "用户问题"` ，返回 Top-5 相关知识片段。

## 模板选择流程

```
用户问题
  → RAG 检索四维知识库（补充业务上下文）
    → 匹配模板 keywords
      → 提取参数（日期/渠道/品项/新老客）
        → 填充 SQL 模板
          → pyodps 执行
            → 飞书卡片输出
```

## 模板清单

| 模板 | 文件 | 覆盖场景 |
|------|------|---------|
| revenue | templates/revenue.yaml | 收入查询（按日/月/渠道/新老客） |
| channel | templates/channel.yaml | 渠道分析（一级/二级/三级） |
| product | templates/product.yaml | 品项排名/筛选 |
| customer | templates/customer.yaml | 新老客拆分 |
| compare | templates/compare.yaml | 同比/环比对比 |
| ltv | templates/ltv.yaml | LTV 趋势/切片 |

## 使用示例

```
用户：昨天老客收入
  → 匹配 revenue 模板
  → RAG 检索："老客收入" → is_new=0, exe_income, dp+executed_date
  → 参数：date=yesterday, customer_type=old
  → SQL：SELECT SUM(exe_income) FROM ... WHERE dp='2026-05-15' AND executed_date='2026-05-14' AND is_new=0
  → 飞书卡片：老客收入 · 2026-05-14 | ¥XXX
```

## 依赖

- Python 环境（pyodps, chromadb, sentence-transformers）
- MaxCompute 连接（~/.odps/config.ini）
- lark-cli 飞书消息发送
- 首次使用前运行：`python scripts/build_knowledge_base.py`
