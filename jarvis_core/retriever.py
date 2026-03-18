from jarvis_core.encoder import encode_chunks
from jarvis_core.vector_store import collection

def retrieve(query, top_k=3):
    query_embedding = encode_chunks([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    return docs, metas
