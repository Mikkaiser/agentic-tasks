from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
openai = OpenAI()

def call_llm(reply, message_history):
