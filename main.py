import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

tweet_prompt = PromptTemplate.from_template("""
    You're customer service. Write me an acurate answer on the following question.
    Do not make up answers, stick to the facts {question}.
    """)

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

if __name__=="__main__":
    question = ""
    resp = tweet_chain.run(topic=question)
    print(resp)
