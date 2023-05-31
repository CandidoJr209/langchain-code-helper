import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))