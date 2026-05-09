import pandas as pd
import json

from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate

# 1. Initialize Local LLM
llm = OllamaLLM(
    model="llama3",
    temperature=0
)