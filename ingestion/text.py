from langchain.text_splitter import RecursiveCharacterTextSplitter

def Splitt(m):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=400,
    )

    Chunks = splitter.split_documents(m)
    return Chunks