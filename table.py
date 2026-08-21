# pip install OpenAI
import os
from typing import Optional
from openai import OpenAI


class Table:
    def __init__(self, name: str):
        self.table_name = name
        self.client = None

    def _set_client(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("Warning: OPENAI_API_KEY not found in environment.")
            return

        try:
            self.client = OpenAI(api_key=api_key)
        except Exception:
            self.client = None
            print("Warning: Failed to initialize OpenAI client. Please check your API key and network connection.")

    def table_names(self):
        if self.client is None:
            return []

        response = self.client.list_tables()
        return [table.name for table in response.data]


table = Table("test")
table._set_client()

print("hi")