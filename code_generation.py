#!/usr/bin/env python

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(temperature=0.9)


prompt = PromptTemplate(
    input_variables=["model"],
    template="Generate a django model that represents a {model}",
)

print(prompt.format(model="user"))
code = llm(prompt.format(model="user"))

file_name = "generated_code.py"

with open(file_name, "w") as file:
    file.write(code)