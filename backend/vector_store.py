from pathlib import Path
import pickle
import faiss


BASE_DIR = Path(__file__).resolve().parent.parent

PROCESSED_DIR = BASE_DIR / "data" / "processed"

INDEX_PATH = PROCESSED_DIR / "documents.index"
CHUNKS_PATH = PROCESSED_DIR / "document_chunks.pkl"


def load_vector_store():

    index = faiss.read_index(
        str(INDEX_PATH)
    )

    with open(CHUNKS_PATH, "rb") as file:
        chunks = pickle.load(file)

    return index, chunks