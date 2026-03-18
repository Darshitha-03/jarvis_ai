from sentence_transformers import SentenceTransformer

# Load model once (will download first time)
model = SentenceTransformer('all-MiniLM-L6-v2')

def encode_chunks(chunks):
    # Ensure input is a list
    if isinstance(chunks, str):
        chunks = [chunks]

    # Generate embeddings
    embeddings = model.encode(chunks)

    # Convert to list (ChromaDB compatible)
    return embeddings.tolist()