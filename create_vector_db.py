import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

all_docs = []

pdf_folder = "data"

for file in os.listdir(pdf_folder):

    if file.endswith(".pdf"):

        pdf_path = os.path.join(pdf_folder, file)

        loader = PyPDFLoader(pdf_path)

        docs = loader.load()

        all_docs.extend(docs)

print("Total Pages Loaded:", len(all_docs))

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(all_docs)

print("Total Chunks:", len(chunks))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vectorstore"
)

print("Vector Database Created Successfully!")