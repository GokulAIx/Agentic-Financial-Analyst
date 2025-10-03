from langchain_google_genai import ChatGoogleGenerativeAI
from ingestion.document_loading import Load_Report
from ingestion.text import Splitt
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from database.chroma import Chromaa
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import os

load_dotenv()

Model_API=os.environ["GOOGLE_API_KEY"]

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, api_key=Model_API)

user_Query=input("Enter your financial question: ")


Loaded_Docx=Load_Report("Apple-Report.pdf")
Splitted_Docs=Splitt(Loaded_Docx)

store=Chromaa(Splitted_Docs)

prompt=load_prompt("financial_prompt.json")

parser=StrOutputParser()

retriever=store.as_retriever(search_kwargs={"k":3})

Output_Chain = ({"context" : retriever , "question" : RunnablePassthrough()}
 | prompt | model | parser)


responce=Output_Chain.invoke(user_Query)

print(responce)
