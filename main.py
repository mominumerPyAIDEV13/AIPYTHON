# Local-AI-RAG: Production-Grade Semantic Search Pipeline

A lightweight, high-performance Retrieval-Augmented Generation (RAG) pipeline built using Python. This project demonstrates how to chunk unstructured corporate documentation, generate vector embeddings, compute cosine similarity metrics for semantic search, and feed relevant contexts into a locally deployed Large Language Model (LLM) for precise extraction.

## 🚀 Key Features
* **Zero-Cloud Architecture:** Operates completely offline using local compute resources to preserve absolute data privacy.
* **Vector Embeddings Execution:** Leverages mathematical vector mapping via the `nomic-embed-text` structure to parse raw datasets.
* **Semantic Retrieval Engine:** Utilizes matrix-based Cosine Similarity computations to isolate exact document matching.
* **Deterministic Inference:** Configured with a `0.0 temperature` setting to ensure highly factual, hallucination-free AI responses.

## 🛠️ Tech Stack & Dependencies
* **Core Language:** Python 3.10+
* **LLM Orchestration:** OpenAI API Specification (Local Interfacing Client)
* **Mathematical Operations:** NumPy
* **Vector Analytics:** Scikit-Learn

## 📋 Repository Structure
```text
├── main.py          # Primary execution pipeline & retrieval script
├── requirements.txt # Project package dependencies
├── document.txt     # Raw unstructured target text dataset
└── README.md        # Technical project documentation
```

## ⚙️ How to Deploy & Run (Local Environment Setup)

### 1. Initialize the Environment
Clone this repository and install the required numerical computing packages:
```bash
git clone https://github.com
cd YOUR_REPO_NAME
pip install -r requirements.txt
```

### 2. Configure the Local LLM Gateway
Ensure you have **Ollama** installed on your host machine. Pull the required models via your terminal:
```bash
ollama pull nomic-embed-text
ollama pull llama3
```

### 3. Run the Inference Pipeline
Execute the main script to parse `document.txt` and generate the context-aware query output:
```bash
python main.py
```

## 🤝 Open For Technical Collaboration
I specialize in constructing private LLM orchestration mechanisms, agentic systems, and highly optimized API microservices. If your development team requires a remote contractor to build custom AI workflows, deploy RAG pipelines, or optimize FastAPI backend infrastructure, feel free to review my open-source codebases or initiate contact.
