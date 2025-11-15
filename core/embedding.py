import numpy as np
import json

def embed(text):
    vector = np.zeros(128)
    for c in text[:128]:
        vector[ord(c) % 128] += 1
    return vector.tolist()

def load_vector(embedding_bytes):
    # Convert bytes from DB back to np.array
    embedding_list = json.loads(embedding_bytes.decode())
    return np.array(embedding_list)
