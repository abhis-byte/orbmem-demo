# ORBYNT Cognitive Database (OCDB)

> **The world’s first AI-native cognitive database for autonomous agents.**

OCDB is a new category of database designed not for static CRUD operations, but for **cognitive reasoning, memory, and safety intelligence**.  
It introduces a four-layer architecture that enables autonomous agents to store, recall, reason, and self-correct in ways traditional databases (like SQLite) cannot.

---

## 🌟 Key Features

### Layer 1 — Memory Engine
- Key–Value + JSON + Temporal Memory
- Session-based memory
- Automatic forgetting (TTL)
- Stores agent state, user preferences, environment memory

### Layer 2 — Vector Engine
- Semantic search + embeddings
- Cosine similarity retrieval
- Conceptual matching for RAG pipelines
- Pure NumPy implementation

### Layer 3 — Reasoning Graph Engine
- Graph DB + Planning Tree
- Nodes = reasoning steps, edges = transitions
- Track self-correction and hallucinations
- Visualize agent reasoning paths

### Layer 4 — Safety + Correction Memory
- Pattern history DB
- Stores unsafe attempts, flagged text, corrections
- Learns safety fingerprints over time
- Enables agents to avoid repeated mistakes

---

## 🏗️ Architecture Diagram

![alt text](OCDB.png)


---

## 🚀 Quickstart

### 1. Install dependencies
```bash
pip install numpy networkx
```

---

### 2. Run the demo
```bash
python demo.py
```

---

### 3. Expected Output

- Memory Engine stores/retrieves agent state and preferences.
- Vector Engine returns semantic matches with similarity scores.
- Reasoning Graph exports nodes/edges and analyzes hallucinations.
- Safety Engine flags unsafe text and learns correction patterns.
- Cohesion loop ties all layers together.

---

### 📂 Project Structure
```bash
ocdb/                      ← main package folder
│
├── __init__.py            ← makes this a Python package
├── memory_engine.py       ← Layer 1: temporal KV + JSON + TTL
├── vector_engine.py       ← Layer 2: embeddings + semantic search
├── graph_engine.py        ← Layer 3: reasoning graph + planning/
├── safety_engine.py       ← Layer 4: safety + correction memory
└── ocdb.py                ← unified facade (ties all layers together)

demo.py                    ← advanced demo script
```
---

### 🌍 Vision

OCDB is not just a database — it’s cognitive infrastructure.
By enabling agents to remember, reason, and self-correct, OCDB lays the foundation for safer, more autonomous AI systems.
This project is open-source to encourage collaboration and global recognition.
We believe OCDB will become the gold standard for cognitive agent databases.

---

### 📜 License

Released under the MIT License.
You are free to use, modify, and distribute OCDB with attribution.

---

### ✨ Recognition

*OCDB is designed to be cited in:*

- Research papers
- AI labs (Google, OpenAI, DeepMind)
- Industry applications
- Kaggle and Dev.to projects

---

### 🤝 Contributing

Contributions are welcome!

- Fork the repo
- Add new features (e.g., persistence, visualization, API endpoints)
- Submit a pull request

Together, we can make OCDB the backbone of autonomous agent cognition.



