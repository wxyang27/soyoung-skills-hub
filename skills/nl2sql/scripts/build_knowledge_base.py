"""
构建四维业务知识向量库
读取 references/ 下的结构化文档 → 分块 → 向量化 → 存入 Chroma
"""

import os
import json
import chromadb
from chromadb.utils import embedding_functions

# ============================================================
# 配置
# ============================================================
REF_DIR = os.path.join(os.path.dirname(__file__), "..", "references")
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "..", "chroma_db")
COLLECTION_NAME = "soyoung_business_knowledge"

# ============================================================
# 文档分块
# ============================================================

def chunk_markdown_table(filepath: str, category: str):
    """将 Markdown 中的每个表格行作为一个 chunk"""
    chunks = []
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 按 ## 标题分段
    sections = content.split("\n## ")
    for section in sections:
        lines = section.strip().split("\n")
        if not lines:
            continue
        title = lines[0].replace("#", "").strip()
        body = "\n".join(lines[1:])

        # 完整段落作为一个 chunk
        if len(body.strip()) > 20:
            chunks.append({
                "id": f"{category}::{title[:30]}",
                "text": f"[{category}] {section.strip()[:2000]}",
                "metadata": {"category": category, "section": title, "source": os.path.basename(filepath)}
            })
    return chunks

def chunk_json_schema(filepath: str, category: str):
    """将 JSON Schema 中的每个表/字段作为一个 chunk"""
    chunks = []
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 每个表
    for table_name, table_info in data.get("tables", {}).items():
        # 表级别 chunk
        chunks.append({
            "id": f"schema::table::{table_name}",
            "text": f"[Schema/Table] {table_name}: {table_info.get('description','')}. "
                    f"Type: {table_info.get('type','')}, "
                    f"Partition: {json.dumps(table_info.get('partition',{}))}, "
                    f"Business date col: {table_info.get('business_date_col','')}",
            "metadata": {"category": category, "type": "table", "name": table_name}
        })

        # 每个关键字段
        for field_name, field_info in table_info.get("key_fields", {}).items():
            chunks.append({
                "id": f"schema::field::{table_name}::{field_name}",
                "text": f"[Schema/Field] {table_name}.{field_name}: "
                        f"{field_info.get('description','')}. "
                        f"Type: {field_info.get('type','')}",
                "metadata": {"category": category, "type": "field", "table": table_name, "field": field_name}
            })

    # 约定
    for key, val in data.get("conventions", {}).items():
        chunks.append({
            "id": f"schema::convention::{key}",
            "text": f"[Schema/Convention] {key}: {json.dumps(val, ensure_ascii=False)}",
            "metadata": {"category": category, "type": "convention", "key": key}
        })

    return chunks

# ============================================================
# 构建向量库
# ============================================================

def build():
    print("Building knowledge base...")

    client = chromadb.PersistentClient(path=CHROMA_DIR)

    # 删除旧 collection（如果存在）
    try:
        client.delete_collection(COLLECTION_NAME)
        print(f"  Deleted old collection: {COLLECTION_NAME}")
    except Exception:
        pass

    # 使用 sentence-transformers 做 embedding
    ef = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="paraphrase-multilingual-MiniLM-L12-v2"
    )

    collection = client.create_collection(
        name=COLLECTION_NAME,
        embedding_function=ef
    )

    # 加载所有参考文档
    file_map = {
        "metric-semantics.md": ("指标语义", chunk_markdown_table),
        "dimension-dictionary.md": ("维度值域", chunk_markdown_table),
        "calculation-logic.md": ("计算逻辑", chunk_markdown_table),
        "schema-mapping.json": ("Schema映射", chunk_json_schema),
    }

    all_chunks = []
    for filename, (category, chunk_func) in file_map.items():
        filepath = os.path.join(REF_DIR, filename)
        if os.path.exists(filepath):
            chunks = chunk_func(filepath, category)
            all_chunks.extend(chunks)
            print(f"  {filename}: {len(chunks)} chunks")
        else:
            print(f"  {filename}: NOT FOUND")

    # 批量写入
    if all_chunks:
        ids = [c["id"] for c in all_chunks]
        texts = [c["text"] for c in all_chunks]
        metadatas = [c["metadata"] for c in all_chunks]

        collection.add(ids=ids, documents=texts, metadatas=metadatas)
        print(f"\nTotal: {len(all_chunks)} chunks indexed in '{COLLECTION_NAME}'")

    # 测试检索
    print("\n--- Test Query ---")
    results = collection.query(query_texts=["老客收入怎么查"], n_results=3)
    for i, (doc_id, doc_text, distance) in enumerate(zip(
        results["ids"][0], results["documents"][0], results["distances"][0]
    )):
        print(f"  #{i+1} [{doc_id}] dist={distance:.3f}: {doc_text[:100]}...")

    print("\nDone.")


if __name__ == "__main__":
    build()
