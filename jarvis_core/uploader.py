import os
from jarvis_core.ingest import read_pdf, read_odf
from jarvis_core.chunker import chunk_and_hash
from jarvis_core.encoder import encode_chunks
from jarvis_core.vector_store import collection


def process_uploaded_file(filepath):

    if filepath.endswith(".pdf"):
        text = read_pdf(filepath)

    elif filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()

    elif filepath.endswith(".odt") or filepath.endswith(".ods"):
        text = read_odf(filepath)

    else:
        return

    chunk_data = chunk_and_hash(text)

    chunks = []
    ids = []
    metadatas = []

    filename = os.path.basename(filepath)

    for chunk, h in chunk_data:
        enriched_chunk = f"[FILE: {filename}] {chunk}"

        chunks.append(enriched_chunk)
        ids.append(h)
        metadatas.append({"source": filename})

    embeddings = encode_chunks(chunks)

    try:
        collection.delete(
            where={"source": os.path.basename(filepath)}
        )
    except Exception:
        pass

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids
    )