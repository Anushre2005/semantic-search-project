# semantic_search.py (Streamlit Version)

from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
import streamlit as st # NEW: Import Streamlit

# --- Configuration ---
DOCUMENT_FILE = "documents.txt"
EMBEDDING_FILE = "document_embeddings.npy"
MODEL_NAME = "all-MiniLM-L6-v2"

# --- Functions (remain mostly the same, no need for global vars now) ---
@st.cache_resource # NEW: Cache the model loading for performance
def load_model(model_name):
    """Loads the Sentence Transformer model."""
    print(f"Loading Sentence Transformer model: {model_name}...")
    model = SentenceTransformer(model_name)
    print("Model loaded successfully.")
    return model

@st.cache_data # NEW: Cache data loading and embedding generation
def load_and_process_documents(filepath, _model):
    """Loads documents and generates/loads embeddings."""
    documents = []
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            documents = [line.strip() for line in f if line.strip()]
    else:
        st.error(f"Error: {filepath} not found. Please create it with your documents.")
        return [], None

    if not documents:
        st.warning(f"No documents found in {filepath}. Please add some text.")
        return [], None

    document_embeddings = None
    if os.path.exists(EMBEDDING_FILE) and os.path.getsize(EMBEDDING_FILE) > 0:
        try:
            document_embeddings = np.load(EMBEDDING_FILE)
            if len(documents) != document_embeddings.shape[0]:
                st.warning("Document count mismatch with existing embeddings. Re-generating embeddings.")
                document_embeddings = None # Force regeneration
        except Exception as e:
            st.error(f"Error loading embeddings: {e}. Re-generating embeddings.")
            document_embeddings = None # Force regeneration

    if document_embeddings is None:
        with st.spinner('Generating document embeddings... This may take a moment.'):
            document_embeddings = model.encode(documents, show_progress_bar=False) # No console progress bar in Streamlit
        np.save(EMBEDDING_FILE, document_embeddings)
        st.success("Embeddings generated and saved.")

    return documents, document_embeddings

def semantic_search(query, documents, document_embeddings, model, top_k=5):
    """Performs a semantic search for a given query."""
    if not query.strip():
        return [] # Return empty if query is empty

    query_embedding = model.encode([query])[0]
    similarities = cosine_similarity(query_embedding.reshape(1, -1), document_embeddings)[0]
    top_k_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for i in top_k_indices:
        score = similarities[i]
        document = documents[i]
        results.append((score, document))
    return results

# --- Streamlit App Layout ---
st.set_page_config(page_title="Semantic Search Engine Prototype", layout="centered")

st.title("🔍 Semantic Search Engine Prototype")
st.write("Enter a query to find semantically similar documents from our corpus.")

# Load model and documents
# st.cache_resource ensures the model is loaded only once across app runs
model = load_model(MODEL_NAME)

# st.cache_data ensures documents and embeddings are loaded/generated only once
documents, document_embeddings = load_and_process_documents(DOCUMENT_FILE, model)

if documents and document_embeddings is not None:
    user_query = st.text_input("Your Search Query:", "") # Text input widget
    search_button = st.button("Search")

    if search_button or user_query: # Search when button clicked or text input changes (for convenience)
        if not user_query.strip():
            st.warning("Please enter a search query.")
        else:
            with st.spinner("Searching..."):
                results = semantic_search(user_query, documents, document_embeddings, model, top_k=5)

            if results:
                st.subheader("Search Results:")
                for i, (score, doc) in enumerate(results):
                    st.write(f"**{i+1}. Document:** {doc}")
                    st.write(f"**Similarity Score:** {score:.4f}")
                    st.markdown("---")
            else:
                st.info("No results found for your query.")
else:
    st.warning("Please ensure 'documents.txt' exists and contains text.")

st.sidebar.header("About This Project")
st.sidebar.info(
    "This prototype demonstrates a semantic search engine using pre-trained "
    "HuggingFace Sentence-Transformers to generate text embeddings. "
    "It leverages vector similarity for meaning-based search, "
    "a key component in advanced AI applications like recommendation systems and intelligent assistants."
)
st.sidebar.text(f"Model used: {MODEL_NAME}")
st.sidebar.text(f"Documents loaded: {len(documents) if documents else 0}")