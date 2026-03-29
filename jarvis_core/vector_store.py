import chromadb
from jarvis_core.encoder import encode_chunks
from jarvis_core.hasher import hash_chunk

client = chromadb.PersistentClient(path="./jarvis_db")
collection = client.get_or_create_collection(name="jarvis_memory")


def store_chunks(chunks, filenames):
    for i, chunk in enumerate(chunks):

        chunk_hash = hash_chunk(chunk)

        existing = collection.get(ids=[chunk_hash])
        if existing["ids"]:
            continue

        embedding = encode_chunks([chunk])[0]

        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[chunk_hash],
            metadatas=[{
                "source": filenames[i],
                "hash": chunk_hash
            }]
        )