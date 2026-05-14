import streamlit as st
import pandas as pd
import numpy as np
import faiss
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Network Log AI Assistant",
    layout="wide"
)

st.title("🔥 Network Log AI Assistant (RAG)")
st.write("Ask questions about your network logs.")

# =========================
# LOAD EMBEDDING MODEL
# =========================
@st.cache_resource
def load_embedding_model():
    model = SentenceTransformer(
        'sentence-transformers/all-MiniLM-L6-v2'
    )
    return model

embed_model = load_embedding_model()

# =========================
# LOAD LLM
# =========================
@st.cache_resource
def load_llm():
    model_name = "Qwen/Qwen2.5-1.5B-Instruct"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16
    )

    return tokenizer, model

tokenizer, model = load_llm()

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader(
    "Upload Network Log CSV",
    type=["csv"]
)

if uploaded_file is not None:

    # =========================
    # READ CSV
    # =========================
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # =========================
    # CREATE DOCUMENTS
    # =========================
    df = df.fillna("")

    def row_to_document(row):
        return " | ".join(
            [f"{col}: {row[col]}" for col in df.columns]
        )

    df["document"] = df.apply(row_to_document, axis=1)

    documents = df["document"].tolist()

    st.success(f"✅ Total Documents: {len(documents)}")

    # =========================
    # CREATE EMBEDDINGS
    # =========================
    with st.spinner("Creating embeddings..."):

        embeddings = embed_model.encode(
            documents,
            normalize_embeddings=True
        )

        embeddings = np.array(embeddings)

    st.success("✅ Embeddings created")

    # =========================
    # CREATE FAISS INDEX
    # =========================
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)

    # Save index
    faiss.write_index(index, "faiss_index.idx")
    st.success("✅ FAISS index saved")

    # =========================
    # QUERY INPUT
    # =========================
    st.subheader("Ask Question")

    query = st.text_input(
        "Example: give me warning logs"
    )

    top_k = st.slider(
        "Top K Results",
        min_value=1,
        max_value=20,
        value=5
    )

    # =========================
    # ASK BUTTON
    # =========================
    if st.button("Search"):
        if query:
            with st.spinner("Searching logs..."):

                # Query embedding
                query_embedding = embed_model.encode(
                    [query],
                    normalize_embeddings=True
                )

                query_embedding = np.array(query_embedding)

                # Search FAISS
                D, I = index.search(query_embedding, k=top_k)

                # Context
                retrieved_docs = [
                    documents[i]
                    for i in I[0]
                ]

                context = "\n".join(retrieved_docs)

            # =========================
            # SHOW RETRIEVED LOGS
            # =========================
            st.subheader("Retrieved Logs")

            for idx, doc in enumerate(retrieved_docs, 1):
                st.code(doc)

            # =========================
            # PROMPT
            # =========================
            messages = [
                {
                    "role": "system",
                    "content": """
You are a network log analyzer.

Rules:
- Use ONLY the context
- If answer not found, say: not found in logs
- If packet loss or warning exists, it can indicate issue/down
"""
                },
                {
                    "role": "user",
                    "content": f"""
Context:
{context}

Question:
{query}
"""
                }
            ]

            prompt = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )

            # =========================
            # GENERATE ANSWER
            # =========================
            with st.spinner("Generating answer..."):

                inputs = tokenizer(
                    prompt,
                    return_tensors="pt"
                ).to(model.device)

                outputs = model.generate(
                    **inputs,
                    max_new_tokens=200,
                    temperature=0.3,
                    top_p=0.9
                )

                answer = tokenizer.decode(
                    outputs[0],
                    skip_special_tokens=True
                )

            # =========================
            # SHOW ANSWER
            # =========================
            st.subheader("AI Answer")

            st.write(answer)