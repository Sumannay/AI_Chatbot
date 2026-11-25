from groq import Groq

from .config import (
    GROQ_API_KEY,
    MODEL_NAME
)


client = Groq(
    api_key=GROQ_API_KEY
)


def chat_model(messages):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content