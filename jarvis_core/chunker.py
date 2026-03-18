
import hashlib

def hash_chunk(chunk):
    return hashlib.sha256(chunk.encode()).hexdigest()

def chunk_text(text, chunk_size=200,overlapping = 50):  #overlapping 50 words to keep context intact while breaking chunks
    words = text.split()  #words list
    chunks = []           #storeslist of words , a chunk

    for i in range(0, len(words), chunk_size-overlapping): 
        chunk = " ".join(words[i:i+chunk_size]) #add 150 words into a sentence
        chunks.append(chunk)

    return chunks

def chunk_and_hash(text):
    chunks = chunk_text(text)
    chunk_data = []

    for chunk in chunks:
        h = hash_chunk(chunk)
        chunk_data.append((chunk, h))

    return chunk_data

