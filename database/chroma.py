from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


embedder=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
def Chromaa(k):
    vectorstore=Chroma.from_documents(
        documents=k,
        embedding=embedder,
        persist_directory="database/chroma"
    )
    return vectorstore