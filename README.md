# Network Log AI Assistant

## 📋 Description
Network Log AI Assistant is an AI-powered log analysis system built with Retrieval-Augmented Generation (RAG). The project helps analyze, search, and understand network logs using Large Language Models (LLMs), vector databases, and semantic search.

## 🚀 Features
- Upload CSV network log files
- Automatic document creation from logs
- Streamlit web interface
- GPU/CUDA support (optional)
- AI-powered question answering

## 🧠 Tools & Library
- Python
- Streamlit
- Faiss
- Pandas
- LLM Model : Qwen/Qwen2.5-1.5B-Instruct
- Embedding Model : sentence-transformers/all-MiniLM-L6-v2

## 📁 Folder Structures
- NETWORK LOG AI ASSISTANT
  - data
      - network_logs.csv
      - data_generator.py
  - src
      - app.py
  - vector_store
      - faiss_index.idx
  - test.ipynb
  - requirements.txt
  - README.md
 
 ## 🛠️ Architecture
  - CSV Log File
  - Data Preprocessing
  - Document Creation
  - Embedding Model
  - FAISS Vector Store
  - User Question
  - Similarity Search
  - LLM Response
  - Final Answer
 
## 🖥️ How to Run the Program
1. Clone repositori
```bash
git clone https://github.com/arvio1378/network_log_ai_assistant.git
cd NETWORK LOG AI ASSISTANT
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Run the program
```bash
streamlit run src/app.py
```

## 📊 Dataset
Example CSV structure :
| timestamp    | device      | interface | event | severity | ip | message |
|-------------|-------------|-------------|-------------||-------------|-------------|-------------|
