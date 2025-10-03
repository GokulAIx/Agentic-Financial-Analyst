from langchain_core.prompts import PromptTemplate

prompt=PromptTemplate(
    template="""
    You are a financial analyst. Based on the following context, answer the question at the end.
    Context: {context}
    Question: {question}""",

    input_variables=["context","question"]
)

prompt.save("financial_prompt.json")