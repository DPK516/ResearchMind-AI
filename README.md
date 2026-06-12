# 🧠 ResearchMind: Enterprise Multi-Agent AI Research System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B.svg?logo=streamlit)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Integration-gray.svg)](https://python.langchain.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg?logo=docker)](https://www.docker.com/)

ResearchMind is a production-ready Multi-Agent AI Research System that automates web research through a coordinated network of AI agents. The platform combines real-time information retrieval, content analysis, and structured report generation into a unified workflow.

Built with FastAPI, Streamlit, LangChain, and Docker, the system follows a decoupled architecture that separates the presentation layer from backend business logic, making it scalable, maintainable, and deployment-friendly.

---

## ✨ Features

* 🤖 **Multi-Agent Research Workflow** using LangChain
* 🌐 **Real-Time Web Research** powered by Tavily Search
* 📝 **Automated Research Report Generation**
* ⚡ **FastAPI REST Backend**
* 🎨 **Interactive Streamlit Frontend**
* 🐳 **Dockerized Deployment with Docker Compose**
* 🔒 **Environment-Based Configuration Management**
* 📚 **Interactive Swagger API Documentation**

---

## 🏗️ System Architecture

```text
┌──────────────────────┐        HTTP / REST        ┌───────────────────────┐
│                      │ ◄───────────────────────► │                       │
│    Streamlit UI      │                           │     FastAPI Backend   │
│    (Port: 8501)      │                           │     (Port: 8000)      │
│                      │                           │                       │
└──────────────────────┘                           └───────────┬───────────┘
                                                               │
┌──────────────────────────────────────────────────────────────┴───────────────┐
│                      LangChain Multi-Agent Engine                            │
│                                                                              │
│  ┌───────────────┐      ┌───────────────┐      ┌──────────────────────────┐  │
│  │ Mistral LLM   │ ◄──► │ Tavily Search │ ◄──► │ Report Generation        │  │
│  └───────────────┘      └───────────────┘      └──────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Research Workflow

1. User submits a research query through the Streamlit interface.
2. Search agents retrieve relevant information from the web.
3. Research data is analyzed and organized.
4. AI agents synthesize findings into a structured report.
5. Results are returned to the user through the frontend.

---

## 🔧 Technology Stack

| Category         | Technology              |
| ---------------- | ----------------------- |
| Language         | Python 3.11             |
| Backend          | FastAPI                 |
| Frontend         | Streamlit               |
| AI Framework     | LangChain               |
| LLM              | Mistral AI              |
| Search Engine    | Tavily                  |
| Containerization | Docker & Docker Compose |
| Configuration    | Pydantic Settings       |

---

## 📁 Project Structure

```text
📦 ResearchMind
├── 📂 app
│   ├── 📂 agents
│   │   ├── 📄 builder.py
│   │   └── 📄 tools.py
│   ├── 📂 api
│   ├── 📂 core
│   ├── 📂 services
│   └── 📄 main.py
│
├── 📂 frontend
│   └── 📄 streamlit_app.py
│
├── 📄 .env
├── 📄 .gitignore
├── 📄 docker-compose.yml
├── 📄 Dockerfile.backend
├── 📄 Dockerfile.frontend
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🚀 Quick Start

### Prerequisites

* Docker Desktop
* Mistral API Key
* Tavily API Key

### 1. Clone the Repository

```bash
git clone https://github.com/DPK516/ResearchMind-AI.git

cd ResearchMind-AI
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 3. Launch the Application

```bash
docker-compose up --build
```

### 4. Access the Application

**Frontend Dashboard**

```text
http://localhost:8501
```

**Backend API**

```text
http://localhost:8000
```

**Swagger Documentation**

```text
http://localhost:8000/docs
```

---

## ☁️ Docker Hub Images

Pre-built Docker images are available on Docker Hub.

### Backend

```bash
docker pull dpk516/researchmind-api:v1
```

### Frontend

```bash
docker pull dpk516/researchmind-ui:v1
```

---

## 📸 Screenshots

### Dashboard

![ResearchMind Dashboard](assets/dashboard.png)

### Research Results

![Research Results](assets/results.png)

---

## 👨‍💻 Author

**Deepak Kumar Ghadei**


Built to explore scalable Multi-Agent AI systems using FastAPI, Streamlit, LangChain, and Docker.

If you found this project useful, consider giving it a ⭐ on GitHub.
