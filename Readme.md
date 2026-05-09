# 🤖 Multi-Tool AI Agent

A local AI-powered sales analysis agent that uses **LLaMA 3.2** (via Ollama) to analyze sales data, fetch live industry benchmarks from the web, and generate actionable business insights — all running **100% locally** with no cloud API costs.

---

## 🧠 How It Works

```
sales.csv → SalesAnalyzer → metrics (JSON)
                                        ↘
                                         LLM (LLaMA 3.2) → Insights & Recommendations
                                        ↗
DuckDuckGo Search → industry benchmarks
```

1. **SalesAnalyzer** reads your `sales.csv` and computes key metrics
2. **DuckDuckGoSearchRun** fetches live ecommerce benchmark data
3. **LLaMA 3.2** (running locally via Ollama) analyzes both and writes insights

---

## 📁 Project Structure

```
Multi-Tool-AI-Agent/
├── agent.py            # Main entry point
├── sales_analysis.py   # SalesAnalyzer class
├── sales.csv           # Your sales data (not tracked)
├── requirements.txt    # Python dependencies
└── .gitignore
```

---

## ⚙️ Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/download) installed and running
- LLaMA 3.2 model pulled:
  ```bash
  ollama pull llama3.2:1b
  ```

---

## 🚀 Setup

**1. Clone the repo**
```bash
git clone https://github.com/kavyasri36/Multi-Tool-AI-Agent.git
cd Multi-Tool-AI-Agent
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your sales data**

Place your `sales.csv` in the project root. It should have these columns:

| Column | Description |
|--------|-------------|
| `quantity` | Units sold |
| `unit_price` | Price per unit |
| `discount_percent` | Discount applied (0-100) |
| `product_category` | Category name |
| `region` | Sales region |
| `payment_method` | Payment type |

---

## ▶️ Run

```bash
python agent.py
```

**Sample output:**
```
DEBUG: METRICS USED
{
  "total_revenue": 48200.5,
  "average_order_value": 241.0,
  ...
}

FINAL OUTPUT:
Insight 1: ...
Recommendation 1: ...
```

---

## 📦 Dependencies

```
langchain
langchain-core
langchain-community
langchain-ollama
pandas
duckduckgo-search
ddgs
```

---

## 🔧 Configuration

To change the LLM model, update `agent.py`:
```python
llm = OllamaLLM(
    model="llama3.2:1b",  # change model here
    temperature=0
)
```

---

## 📄 License

MIT