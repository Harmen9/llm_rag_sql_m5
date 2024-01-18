import os

from dotenv import load_dotenv
from langchain_openai import OpenAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_ENDPOINT  = os.getenv("API_ENDPOINT ")


llm = OpenAI(openai_api_key=OPENAI_API_KEY)

customer_prompt = PromptTemplate.from_template("""
    You're customer service. Write me an acurate answer on the following question.
    Do not make up answers, stick to the facts {question}.
    """)

customer_chain = LLMChain(llm=llm, prompt=customer_prompt, verbose=True)

if __name__=="__main__":
    question = "What is 1+1?"
    resp = customer_chain.run(question=question)
    print(resp)
