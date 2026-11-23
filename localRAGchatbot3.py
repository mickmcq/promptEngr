import ollama
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_ollama import OllamaEmbeddings
from chromadb.config import Settings
from chromadb import Client
from langchain_chroma import Chroma
import gradio as gr
import re
from concurrent.futures import ThreadPoolExecutor


# Step 1: Load the document using PyMuPDFLoader
loader = PyMuPDFLoader("Xiao2025.pdf")
documents = loader.load()

# Step 2: Split text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# Step 3: Initialize Ollama embeddings
embedding_function = OllamaEmbeddings(model="nomic-embed-text")


# Step 4: Parallelize embedding generation
def generate_embedding(chunk):
    return embedding_function.embed_query(chunk.page_content)


with ThreadPoolExecutor() as executor:
    embeddings = list(executor.map(generate_embedding, chunks))

# Step 5: Recreate the collection
client = Client(Settings())
# . client.delete_collection(
# .     name="foundations_of_llms"
# . )  # Delete any existing collection if needed
collection = client.create_collection(name="foundations_of_llms")

# Step 6: Add documents and embeddings to Chroma
for idx, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk.page_content],
        metadatas=[{"id": idx}],
        embeddings=[embeddings[idx]],
        ids=[str(idx)],  # Ensure IDs are strings
    )

print("Embeddings stored successfully!")

# initialize retriever using chroma collection

retriever = Chroma(
    collection_name="foundations_of_llms",
    client=client,
    embedding_function=embedding_function,
).as_retriever()


def retrieve_context(question):
    results = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in results])
    return context


def query_qwen(question, context):

    # Format the input as a structured prompt
    formatted_promt = f"Question: {question}\n\nContext: {context}"

    # Send the prompt to qwen using Ollama
    response = ollama.chat(
        model="qwen3.5:9b", messages=[{"role": "user", "content": formatted_promt}]
    )

    # Extract and clean the response
    response_content = response["message"]["content"]
    final_answer = re.sub(
        r"<think>.*?</think>", "", response_content, flags=re.DOTALL
    ).strip()
    return final_answer


def rag_pipeline(question):

    # Retrieve context from the vector store
    context = retrieve_context(question)

    # Generate an answer using Qwen 3.5:9b
    answer = query_qwen(question, context)
    return answer


def ask_question(question):
    # Run the RAG pipeline
    return rag_pipeline(question)


# Create a Gradio interface
interface = gr.Interface(
    fn=ask_question,
    inputs="text",
    outputs="text",
    title="RAG Chatbot: Foundations of LLMs",
    description="Ask any question about the Foundations of LLMs book. Powered by Qwen 3.5:9b.",
)

# Launch the Gradio app
interface.launch(debug=True)
