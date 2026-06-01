import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_google_genai import ChatGoogleGenerativeAI

# Load Environment Variables
load_dotenv()

# ==========================
# STEP 1: LOAD PDF DOCUMENTS
# ==========================

all_docs = []

for file in os.listdir("data"):
    if file.endswith(".pdf"):

        pdf_path = os.path.join("data", file)

        loader = PyPDFLoader(pdf_path)
        docs = loader.load()

        # IMPORTANT
        all_docs.extend(docs)

        print("\n====================")
        print(file)
        print("====================")
        print(docs[0].page_content[:500])

print("\nTotal Pages Loaded:", len(all_docs))

# ==========================
# STEP 2: CHUNK DOCUMENTS
# ==========================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(all_docs)

print("Total Chunks Created:", len(chunks))

# ==========================
# STEP 3: CREATE EMBEDDINGS
# ==========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ==========================
# STEP 4: CREATE VECTOR DB
# ==========================

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vectorstore"
)

print("\nVector Database Ready!")
print("Government Scheme Advisor Ready!")

# ==========================
# STEP 5: LOAD GEMINI MODEL
# ==========================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# ==========================
# STEP 6: CHAT LOOP
# ==========================

while True:

    question = input("\nAsk a Question: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Retrieve relevant chunks
    docs = vector_db.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an AI Government Scheme Advisor.

Answer ONLY using the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    print("\nAI Answer:\n")
    print(response.content)