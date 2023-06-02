#!/usr/bin/env python
import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()



class DjangoCodeGenerator:
    def __init__(self, **kwargs):
        self.llm = OpenAI(temperature=kwargs.get("temperature",0.4))
        self.path = kwargs.get("path")
        self.file_name = kwargs.get("file_name")

    @property
    def full_path(self):
        current_path = os.getcwd()
        return current_path + self.path + self.file_name

    def _directory_check_or_create(self):
        directory = os.path.dirname(self.full_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def _write_code_from_prompt(self, formatted_prompt):
        code = self.llm(formatted_prompt)
        with open(self.full_path, "w") as file:
            file.write(code)

    def _generate_prompt(self):
        raise NotImplementedError

    def generate(self):
        self._directory_check_or_create()
        prompt = self._generate_prompt()
        self._write_code_from_prompt(prompt)




class DjangoModelCodeGenerator(DjangoCodeGenerator):
    def __init__(self, **kwargs):
        super().__init__(file_name="models.py", **kwargs)

    def _generate_prompt(self):
        prompt = PromptTemplate(
            input_variables=["model"],
            template="Generate a django model that represents a {model}",
        )
        return prompt.format(model="house")
