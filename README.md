# MkDocs RAG Assistant 🤖

This project is a **Retrieval-Augmented Generation (RAG)** system designed to answer questions about [MkDocs](https://www.mkdocs.org/) based on its official documentation. It uses **Google Gemini 2.0 Flash** for reasoning and **ChromaDB** for semantic search, wrapped in a user-friendly **Streamlit** chat interface.

## Screenshots
<img width="517" height="604" alt="image" src="https://github.com/user-attachments/assets/8f7a21d0-6008-4879-886d-2f02e4c6889f" />


## 🚀 Features

*   **RAG Pipeline**: Retrieves relevant documentation chunks to answer user queries accurately.
*   **Vector Search**: Uses **ChromaDB** with Google's `text-embedding-004` model for high-quality semantic retrieval.
*   **LLM Power**: Powered by **Gemini 2.0 Flash** for fast and accurate responses.
*   **Smart Chunking**: Implements a hybrid splitting strategy (Markdown Headers + Recursive Character) to preserve context.
*   **Interactive UI**: Clean chat interface built with **Streamlit**.

## 🛠️ Tech Stack

*   **Python 3.10+**
*   **LangChain**: For document loading and text splitting.
*   **ChromaDB**: Vector database for storing embeddings.
*   **Google Gen AI SDK**: For accessing Gemini models.
*   **Streamlit**: For the web application.

## 📋 Prerequisites

1.  **Python**: Ensure you have Python installed.
2.  **Google API Key**: You need an API key from [Google AI Studio](https://aistudio.google.com/).

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mha66/mkdocs-RAG
    cd RAG
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Mac/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

## ⚙️ Data Ingestion (Building the Knowledge Base)

Before running the app, you need to process the documentation and build the vector database.

1.  Open the `embedding.ipynb` notebook.
2.  Run all cells in order.
    *   This will load the Markdown files from `mkdocs/docs/`.
    *   Clean and split the text into chunks.
    *   Generate embeddings using `models/text-embedding-004`.
    *   Store them in the `db/` folder (ChromaDB).

## ▶️ Running the Application

Once the database is ready, launch the chat interface:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

## 📂 Project Structure

```
RAG/
├── app.py              # Streamlit chat application
├── rag.py              # Core RAG logic (retrieval & generation)
├── embedding.ipynb     # Notebook for data processing & embedding
├── requirements.txt    # Python dependencies
├── .env                # API keys (not committed)
├── db/                 # ChromaDB storage (generated)
└── mkdocs/             # Source documentation files
```

## 📝 License

This project is for educational purposes.
