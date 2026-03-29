def retrieve(query, top_k=5):
    from jarvis_core.encoder import encode_chunks
    from jarvis_core.vector_store import collection

    query_lower = query.lower()

    mentioned_file = None
    possible_files = ["josaa.txt", "gatereply.txt"]

    for fname in possible_files:
        base = fname.replace(".txt", "")
        if fname in query_lower or base in query_lower:
            mentioned_file = fname
            break

    if mentioned_file:
        query_embedding = encode_chunks([query])

        results = collection.query(
            query_embeddings=query_embedding,
            n_results=top_k,
            where={"source": mentioned_file}
        )

        if not results.get("documents") or not results["documents"][0]:
            return [], []

        docs = results["documents"][0]
        metas = results["metadatas"][0]

        return docs, metas

    enhanced_query = f"""
    Find information about: {query}.
    This refers to document content, summaries, and details inside files.
    """

    query_embedding = encode_chunks([enhanced_query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    if not results.get("documents") or not results["documents"][0]:
        return [], []

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    return docs, metas