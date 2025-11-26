from chromadb import PersistentClient
from google import genai
import chromadb.utils.embedding_functions as embedding_functions
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

chroma_client = PersistentClient(path="db/")

google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(
    api_key=api_key,
    model_name="models/text-embedding-004",
    task_type="RETRIEVAL_QUERY" # Optimized for search queries
)

collection = chroma_client.get_collection(name="mkdocsGPT", embedding_function=google_ef)
client = genai.Client(api_key=api_key)

system_instruction = f"""You are an expert technical support assistant for MkDocs.
Your goal is to help users understand and use MkDocs based strictly on the provided documentation.

Instructions:
1. Use ONLY the provided context to answer the question. Do not use outside knowledge.
2. If the answer is not found in the context, politely state that you don't have that information.
3. Format your answer in clear Markdown.
4. Be concise and direct."""

def get_answer(prompt: str) -> str:
    results = collection.query(
        query_texts=[prompt],
        n_results=5
    )
    documents = results["documents"][0]

    # Build prompt for Gemini
    context = "\n\n".join(documents)
    
    user_message = f"""Context:
{context}

User Question:
{prompt}

Answer:
"""

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=user_message,
    config=genai.types.GenerateContentConfig(
        system_instruction=system_instruction
    )
)
    return response.text.strip()