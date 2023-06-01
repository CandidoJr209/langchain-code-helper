#!/usr/bin/env python
import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(temperature=0.4)


prompt = PromptTemplate(
    input_variables=["model"],
    template="Generate a django model that represents a {model}",
)

print(prompt.format(model="user"))
code = llm(prompt.format(model="user"))

file_name = "models.py"
current_path = os.getcwd()
full_path = current_path + f"/generated_code/{file_name}"

directory = os.path.dirname(full_path)
if not os.path.exists(directory):
    os.makedirs(directory)

with open(full_path, "w") as file:
    file.write(code)