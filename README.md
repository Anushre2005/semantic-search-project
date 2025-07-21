🔍 Semantic Search Engine Prototype

This project implements a powerful semantic search engine capable of understanding the meaning and intent behind search queries, rather than just relying on keyword matching. It leverages state-of-the-art natural language processing models and a scalable vector database to provide highly relevant search results.

The application is built with Streamlit for an interactive user interface, making it easy to demonstrate the capabilities of semantic search.

✨ Features

Semantic Search: Understands the meaning of queries to return semantically similar documents.

HuggingFace Sentence-Transformers: Utilizes pre-trained transformer models for generating high-quality text embeddings.

Pinecone Integration: Employs Pinecone, a cloud-native vector database, for efficient and scalable storage and retrieval of millions of high-dimensional embeddings.

Interactive Streamlit UI: Provides a user-friendly web interface for entering queries and viewing ranked results.

Scalable Architecture: Demonstrates a fundamental architecture for building real-world AI search and recommendation systems.


🚀 Live Demo

Experience the Semantic Search Engine live on Streamlit Community Cloud:

👉 https://semantic-search-project-x6tb6zaanzfylxz42jtkpt.streamlit.app/

(Important: Please replace YOUR_STREAMLIT_APP_URL_HERE with the actual URL of your deployed Streamlit app once it's live. You will get this URL from the Streamlit Community Cloud dashboard after successful deployment.)


🛠️ Technologies Used
Python

Streamlit: For building the interactive web application.

Sentence-Transformers: For generating text embeddings.

HuggingFace Transformers: Underlying library for transformer models.

Pinecone: Vector database for storing and querying embeddings.

NumPy: For numerical operations.

scikit-learn: For cosine similarity calculations.


⚙️ Setup and Local Installation

Follow these steps to set up and run the project locally on your machine.

1. Clone the Repository

git clone https://github.com/Anushre2005/semantic-search-project.git

cd semantic-search-project

2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

python -m venv venv

# On Windows:

.\venv\Scripts\activate

# On macOS/Linux:

source venv/bin/activate

3. Install Dependencies

Install all required Python packages using the requirements.txt file.

pip install -r requirements.txt

4. Set Up Pinecone Credentials

This project requires a Pinecone account for its vector database.

Sign up for a free account at Pinecone.io.

Obtain your API Key and Environment from your Pinecone dashboard.

Set them as environment variables in your terminal session before running the app.

For PowerShell (Windows):

$env:PINECONE_API_KEY='YOUR_ACTUAL_API_KEY'

$env:PINECONE_ENVIRONMENT='YOUR_ACTUAL_ENVIRONMENT' # e.g., 'gcp-starter' or 'us-west-2'

For Command Prompt (Windows):

set PINECONE_API_KEY=YOUR_ACTUAL_API_KEY

set PINECONE_ENVIRONMENT=YOUR_ACTUAL_ENVIRONMENT

For macOS/Linux:

export PINECONE_API_KEY='YOUR_ACTUAL_API_KEY'

export PINECONE_ENVIRONMENT='YOUR_ACTUAL_ENVIRONMENT'

(Note: Replace YOUR_ACTUAL_API_KEY and YOUR_ACTUAL_ENVIRONMENT with your actual credentials.)

5. Prepare Your Document Corpus

The documents.txt file serves as your search corpus. You can modify its content to include any text you wish to search through.

Example documents.txt content:

The quick brown fox jumps over the lazy dog.

Machine learning is a field of study that gives computers the ability to learn without being explicitly programmed.

Artificial intelligence is a broader concept where machines can perform tasks that typically require human intelligence.

Pinecone is a vector database designed for building AI applications that need to perform real-time similarity searches.

HuggingFace provides open-source tools to build, train, and deploy state-of-the-art models.

🚀 How to Run the App

Once setup is complete and your virtual environment is active, run the Streamlit app:

streamlit run semantic_search.py

This will open the application in your web browser, usually at http://localhost:8501.

📂 Project Structure

semantic-search-project/

├── .gitignore          # Specifies files/folders to ignore in Git

├── documents.txt       # Your text corpus for the search engine

├── requirements.txt    # Python dependencies

├── semantic_search.py  # The main Streamlit application code

└── venv/               # Python virtual environment (ignored by Git)


💡 Future Enhancements

Advanced Data Ingestion: Support for ingesting data from various sources (CSV, JSON, databases) with rich metadata.

User Authentication: Implement user login for personalized search experiences.

Hybrid Search: Combine semantic search with traditional keyword search for improved relevance.

Feedback Mechanism: Allow users to rate search results to fine-tune the model or ranking.

More Sophisticated UI: Enhance the Streamlit interface with more advanced components and visualizations.

🤝 Contributing

Feel free to fork this repository, open issues, or submit pull requests to contribute to this project.

📧 Contact

Anushree Revankar

Email: anushree.revankar102@gmail.com
