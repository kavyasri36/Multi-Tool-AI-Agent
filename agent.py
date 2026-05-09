import pandas as pd
import json
from sales_analysis import SalesAnalyzer

from langchain_ollama import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate

# 1. Initialize Local LLM
llm = OllamaLLM(
    model="llama3.2:1b",
    temperature=0
)

search = DuckDuckGoSearchRun()

def fetch_benchmarks():
    return search.run(
        "average ecommerce order value benchmark"
    )
    
def run_analysis():
    # Update this path to where your actual sales.csv lives
    sales = SalesAnalyzer("D:\\AI Agent\\Multi-Tool-AI-Agent\\sales.csv")
    metrics = sales.analyze()
    benchmarks = fetch_benchmarks()

    print("\nDEBUG: METRICS USED\n")
    print(json.dumps(metrics, indent=2))

    return metrics, benchmarks


writer_prompt = PromptTemplate.from_template("""
You are a business analyst.

RULES:
- Use ONLY the numbers provided
- Do NOT invent values
- Do NOT assume currency
- Do NOT recalculate

METRICS (JSON):
{metrics}

INDUSTRY CONTEXT:
{benchmarks}

Write 3 insights and 3 recommendations.
""")

# 6. MAIN EXECUTION
if __name__ == "__main__":
    # Gather data from our tools
    metrics, benchmarks = run_analysis()

    # Pass the data to the LLM
    response = llm.invoke(
        writer_prompt.format(
            metrics=json.dumps(metrics, indent=2),
            benchmarks=benchmarks
        )
    )

    print("\nFINAL OUTPUT:\n")
    print(response)