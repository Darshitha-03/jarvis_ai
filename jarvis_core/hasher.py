# hasher.py
import hashlib

def hash_chunk(chunk):
    return hashlib.sha256(chunk.encode()).hexdigest()
