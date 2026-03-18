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

# 🛡️ Safety check (DOES NOT break existing flow)
    if not docs or docs == [None]:
        return {
            "answer": "I couldn't find relevant information.",
            "chunks": [],
            "metadata": []
        }

# 🛡️ Filter out None values (safe)
    clean_docs = [doc for doc in docs if doc]

    context = "\n".join(clean_docs)

    answer = generate_answer(context, question)
    print(answer)
    print("📄 Retrieved docs:", docs)

    return {
        "answer": answer,
        "chunks": docs,
        "metadata": metas
    }
      