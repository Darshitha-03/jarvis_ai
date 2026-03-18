# vector_store.py
import chromadb
from jarvis_core.encoder import encode_chunks
from jarvis_core.hasher import hash_chunk

# Persistent DB
client = chromadb.PersistentClient(path="./jarvis_db")
collection = client.get_or_create_collection(name="jarvis_memory")


# MAIN FUNCTION TO STORE CHUNKS
def store_chunks(chunks, filenames):
    for i, chunk in enumerate(chunks):

        # Create hash for each chunk
        chunk_hash = hash_chunk(chunk)

        # 🔍 VERIFY HASHING HERE
        print("=================================")
        print("CHUNK:", chunk)
        print("HASH :", chunk_hash)

        # Check if already exists
        existing = collection.get(ids=[chunk_hash])
        if existing["ids"]:
            print("⚠️ Skipping existing chunk\n")
            continue

        # Create embedding
        embedding = encode_chunks([chunk])[0]   # FIXED BUG: encode_chunks needs list

        # Store in ChromaDB
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[chunk_hash],
            metadatas=[{"hash": chunk_hash, "file": filenames[i]}]
        )

        print("✅ Stored new chunk\n")
