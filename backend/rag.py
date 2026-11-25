from sentence_transformers import SentenceTransformer

from .vector_store import load_vector_store


embedding_model = None
index, chunks = load_vector_store()


def get_embedding_model():

    global embedding_model

    if embedding_model is None:

        print("Loading embedding model...")

        embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Embedding model loaded!")

    return embedding_model


def retrieve_documents(question, k=3):

    model = get_embedding_model()

    question_embedding = model.encode(
        [question],
        convert_to_numpy=True
    ).astype("float32")

    distances, indices = index.search(
        question_embedding,
        k
    )

    results = []

    for distance, idx in zip(
        distances[0],
        indices[0]
    ):

        if idx == -1:
            continue

        results.append({
            "text": chunks[idx]["text"],
            "source": chunks[idx]["source"],
            "distance": float(distance)
        })

    return results


def build_rag_prompt(question, results):

    context = "\n\n".join(
        f"Source: {result['source']}\n"
        f"{result['text']}"
        for result in results
    )

    return f"""
You are an intelligent AI assistant.

Use the document context when it is relevant.

Rules:
- Do not invent information.
- Use the documents for document-related questions.
- If the answer is not present, say so.
- Answer clearly and naturally.

DOCUMENT CONTEXT:

{context}

USER QUESTION:

{question}
"""