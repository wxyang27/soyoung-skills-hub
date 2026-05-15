"""
RAG 检索器：根据自然语言问题，从向量库检索最相关的业务知识
返回值可直接注入 SQL 生成的 Prompt
"""

import os
import sys
import chromadb
from chromadb.utils import embedding_functions

CHROMA_DIR = os.path.join(os.path.dirname(__file__), "..", "chroma_db")
COLLECTION_NAME = "soyoung_business_knowledge"


class BusinessKnowledgeRAG:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=CHROMA_DIR)
        self.ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="paraphrase-multilingual-MiniLM-L12-v2"
        )
        self.collection = self.client.get_collection(
            name=COLLECTION_NAME,
            embedding_function=self.ef
        )

    def search(self, query: str, n_results: int = 5):
        """搜索相关知识"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return [
            {
                "id": rid,
                "text": doc,
                "distance": dist,
                "metadata": meta
            }
            for rid, doc, dist, meta in zip(
                results["ids"][0],
                results["documents"][0],
                results["distances"][0],
                results["metadatas"][0]
            )
        ]

    def build_context(self, query: str) -> str:
        """构建 Prompt 上下文"""
        results = self.search(query, n_results=5)
        lines = ["## 检索到的业务知识\n"]
        for i, r in enumerate(results):
            lines.append(f"### 知识片段 {i+1} (相关度: {1-r['distance']:.2f})")
            lines.append(f"来源: {r['metadata'].get('category','')} → {r['metadata'].get('section', r['metadata'].get('name',''))}")
            lines.append(f"```\n{r['text']}\n```")
            lines.append("")
        return "\n".join(lines)

    def print_search(self, query: str):
        """打印检索结果"""
        results = self.search(query)
        for i, r in enumerate(results):
            meta = r["metadata"]
            source = f"{meta.get('category','')}/{meta.get('section', meta.get('name',''))}"
            print(f"  #{i+1} [{source}] dist={r['distance']:.3f}")
            print(f"      {r['text'][:120]}...")
            print()


if __name__ == "__main__":
    rag = BusinessKnowledgeRAG()

    queries = [
        "老客收入怎么查",
        "渠道分析用什么字段",
        "LTV下降原因",
        "客单价怎么算",
        "_all_d表怎么用dp分区"
    ]

    for q in queries:
        print(f"Q: {q}")
        rag.print_search(q)
