from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vector_db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings
)

def ask_question(question):

    docs = vector_db.similarity_search(
        question,
        k=3
    )

    if not docs:
        return "No relevant scheme information found."

    answer = ""

    for i, doc in enumerate(docs, start=1):
        answer += f"\n\n{i}. {doc.page_content}"

    return answer