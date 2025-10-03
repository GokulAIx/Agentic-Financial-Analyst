from langchain_community.document_loaders import PyPDFLoader


def Load_Report(n):
    loader=PyPDFLoader(n)

    return loader.load()