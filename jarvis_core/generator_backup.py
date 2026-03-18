from huggingface_hub import InferenceClient

MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
client = InferenceClient(model=MODEL_NAME)

def generate_answer(context, question):
    system_prompt = """You are Jarvis, an AI assistant.
Use ONLY the context to answer.
If not in context, say: I don't know."""

    user_prompt = f"""
Context:
{context}

Question: {question}
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=150,
        temperature=0.1
    )
    print(response.choices[0].message.content)

    return response.choices[0].message.content


# WEB WRAPPER FUNCTION
def jarvis_answer(question):
    from jarvis_core.retriever import retrieve

    docs, metas = retrieve(question, top_k=3)
    context = "\n".join(docs)

    answer = generate_answer(context, question)
    print(answer)

    return {
        "answer": answer,
        "chunks": docs,
        "metadata": metas
    }
