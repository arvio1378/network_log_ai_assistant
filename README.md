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
| timestamp    | device      | interface | event     | severity | ip          | message          |
|--------------|-------------|-----------|-----------|----------|-------------|------------------|
| 2026-05-06 22:11:52	| router1 | wlan0 | packet_loss | WARNING | 157.208.200.158 | High packet loss detected on router1 (17%) |
| 2026-05-06 22:11:33	| router2	 | eth2 | normal_traffic | INFO | 91.242.8.223	 | router2 normal traffic flow stable |
| 2026-05-06 22:16:23	 | switch2 | wlan0 | cpu_spike	| WARNING	| 207.58.9.129	| switch2 CPU usage at 95% |

## 📈 Result
1. - Question : give me 1 ip with warning severity !
   - Answer : The IP address with a warning severity is 192.107.140.186.
2. - Question : Show all CRITICAL logs.
   - Answer : Here are all the critical (CRITICAL) logs from the provided context:
timestamp: 2026-05-06 22:12:52 | device: switch1 | interface: eth2 | event: interface_down | severity: CRITICAL | ip: 121.91.136.248 | message: switch1 interface eth2 is DOWN
timestamp: 2026-05-06 22:11:56 | device: switch1 | interface: eth1 | event: interface_down | severity: CRITICAL | ip: 37.79.246.251 | message: switch1 interface eth1 is DOWN
3. - Question : When was the last time the eth0 interface was down ?
   - Answer : The last time the eth0 interface was down was on May 6, 2026 at 22:12:28 with IP address 76.253.155.76 from switch2.

## 🏗️ Contribution
Can contribute to anyone. Can help with :
- Real-time log streaming
- larger and more complex datasets
- Network anomaly detection

## 🧑‍💻 About Me
I'm currently studying and building a career in AI/ML. This project is my practice in building a simple Python application. I want to further develop my skills in this field through existing projects.
📫 Connect with me on :
- Linkedin : https://www.linkedin.com/in/arvio-abe-suhendar/
- Github : https://github.com/arvio1378
