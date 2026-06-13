# ⬛ ResearchMind

### Enterprise Multi-Agent AI Research Platform for Deep Intelligence and Insight Generation

A containerized multi-agent AI research tool built with LangChain, FastAPI, and Streamlit to automate deep internet research and analysis.

**What does this actually do?** Think of ResearchMind as your own personal team of expert analysts. You type in any topic, and a swarm of AI agents instantly searches the live internet, reads multiple sources, filters out biased information, and writes a highly detailed, professional research report and risk assessment for you in seconds.

---

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?style=flat-square&logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=flat-square&logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/LangChain-Agents-1C3C3C?style=flat-square" alt="LangChain">
  <img src="https://img.shields.io/badge/AWS-EC2%20Deployed-FF9900?style=flat-square&logo=amazonaws" alt="AWS EC2">
  <img src="https://img.shields.io/badge/License-MIT-black?style=flat-square" alt="License">
</div>

<br />

## 🖥️ Platform Overview

### Live Dashboard
![ResearchMind Dashboard](assets/dashboard.png)

### Intelligence Payload Generation
![Research Results](assets/results.png)

---

## 📖 Table of Contents

* [🎯 The Value Proposition](#-the-value-proposition)
* [⚙️ System Architecture](#️-system-architecture)
* [🧠 The AI Research Pipeline](#-the-ai-research-pipeline)
* [💻 Developer Experience (Quick Start)](#-developer-experience-quick-start)
* [☁️ Production Deployment (AWS EC2)](#️-production-deployment-aws-ec2)
* [📝 Environment Configuration](#-environment-configuration)
* [📄 License](#-license)

---

## 🎯 The Value Proposition

Traditional single-prompt LLM interactions fail when executing extensive market research or strategic intelligence gathering. They lack iterative verification mechanisms, often hallucinate facts, and cannot access real-time data.

ResearchMind solves this by treating research as an automated, multi-stage software engineering pipeline powered by **LangChain**:
1. **Context Acquisition:** Utilizes **Tavily AI** to perform live, deep-web knowledge graph queries.
2. **Bias Filtering:** Re-evaluates text resources through specialized agent loops to filter out noise and promotional content.
3. **Risk Assessment:** Employs a dedicated Critic Agent to identify logical gaps and generate adjacent risk appraisals.
4. **Payload Generation:** Synthesizes disparate data points into cohesive, analytical enterprise documentation.

---

## ⚙️ System Architecture

ResearchMind is engineered as a decoupled containerized application. The frontend and backend run in completely isolated Docker container environments, connected via an internal network bridge.

```text
        [ User Web Browser ]
               ▲  │
      Response │  │ HTTP Request (Port 8501)
               │  ▼
┌───────────────────────────────────────────┐
│      AWS Cloud / Docker Environment       │
│                                           │
│             [ Streamlit UI ]              │
│                    ▲  │                   │
│      JSON Response │  │ Internal Network  │
│                    │  ▼ (Port 8000)       │
│                                           │
│            [ FastAPI Backend ]            │
│                    ▲  │                   │
│                    │  ▼                   │
│        ┌─────────────────────────┐        │
│        │ LangChain Orchestrator  │        │
│        │  (The Action Pipeline)  │        │
│        └──────┬──▲─────────┬──▲──┘        │
└───────────────┼──┼─────────┼──┼───────────┘
                │  │         │  │
                │  │         │  │ 
                │  │         │  │    
                ▼  │         ▼  │
         [ Mistral AI ]  [ Tavily AI ]

📂 Project Structure

    ResearchMind/
    ├── app/
    │   ├── agents/
    │   │   ├── builder.py          
    │   │   └── tools.py            
    │   ├── api/
    │   │   └── routes.py           
    │   ├── core/
    │   │   └── config.py           
    │   ├── services/
    │   │   └── research.py         
    │   └── main.py                 
    ├── frontend/
    │   └── streamlit_app.py        
    ├── assets/                     
    ├── .env                        
    ├── docker-compose.yml          
    ├── Dockerfile.backend          
    ├── Dockerfile.frontend         
    ├── LICENSE                     
    ├── README.md                  
    └── requirements.txt
```
---
## 🧠 The AI Research Pipeline

ResearchMind processes user queries through a strictly orchestrated, four-step LangChain execution pipeline. By decoupling the agents into specialized roles, the system ensures high-quality data extraction and rigorous risk assessment.

### 1️⃣ Initial Web Search
* **Engine:** LangChain Search Agent (`create_tool_calling_agent`) + Tavily API
* **Action:** Receives the target topic and autonomously executes optimal internet searches to gather recent, reliable information, returning titles, URLs, and snippet context.

### 2️⃣ Deep-Dive URL Scraping
* **Engine:** LangChain Reader Agent + Custom Web Scraper (`BeautifulSoup` & `aiohttp`)
* **Action:** Analyzes the initial search results, identifies the most highly relevant URL, and performs a deep scrape of the webpage. It automatically sanitizes the DOM (stripping scripts, navbars, and footers) to extract pure text context.

### 3️⃣ Report Synthesis
* **Engine:** Mistral AI Writer Chain
* **Action:** Merges the broad search snippets with the deep-scraped text payload. It processes this combined context to draft a cohesive, highly structured intelligence report (Introduction, Findings, Conclusion, Sources).

### 4️⃣ Strategic Risk Assessment
* **Engine:** Mistral AI Risk Analyst Chain
* **Action:** Acts as an independent Enterprise Risk Analyst. It reviews the generated draft—not to grade the writing, but to provide a strictly professional disclaimer identifying potential source biases, unverified assumptions, and external market risks.

### ⚙️ Execution Flow

```text
        [ FastAPI Endpoint ]
                 │
                 ▼ (User Topic)
   ┌───────────────────────────────────┐
   │ 1️⃣  Initial Web Search           │
   │     (LangChain + Tavily API)      │
   └─────────────┬─────────────────────┘
                 │ Returns URLs & Snippets
                 ▼ 
   ┌───────────────────────────────────┐
   │ 2️⃣  Deep-Dive URL Scraping       │
   │     (LangChain + BeautifulSoup)   │
   └─────────────┬─────────────────────┘
                 │ Returns Cleaned DOM Text
                 ▼ 
   ┌───────────────────────────────────┐
   │ 3️⃣  Report Synthesis             │
   │     (Mistral AI Writer Chain)     │
   └─────────────┬─────────────────────┘
                 │ Returns Draft Markdown Report
                 ▼ 
   ┌───────────────────────────────────┐
   │ 4️⃣  Strategic Risk Assessment    │
   │     (Mistral AI Risk Chain)       │
   └─────────────┬─────────────────────┘
                 │ Returns Bias & Risk Feedback
                 ▼ 
    [ Final Structured JSON Payload ]
```
---
## 💻 Developer Experience (Quick Start)

### Prerequisites
* Python 3.10+
* Docker & Docker Compose
* API Keys for Mistral AI and Tavily AI

### Method-1 One-Click Local Deploy (Docker Compose)
The fastest way to test the environment locally is via our multi-container setup:

**1. Clone the repository and configure environment variables:**
```bash
git clone [https://github.com/dpk516/researchmind.git](https://github.com/dpk516/researchmind.git)
cd researchmind

# Create the .env file
echo "MISTRAL_API_KEY=your_actual_key_here" >> .env
echo "TAVILY_API_KEY=your_actual_key_here" >> .env
```
**2. Spin up the cluster:**
```bash
docker-compose up -d --build
```
Access the application immediately at: http://localhost:8501

### Method-2 Standard Local Setup
If you prefer running the Python environments manually:

**1. Start the FastAPI Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
**2. Start the Streamlit Frontend:**
Open a new terminal session:
```bash
cd frontend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
export API_URL=[http://127.0.0.1:8000/api/research](http://127.0.0.1:8000/api/research)  # Windows: set API_URL=...
streamlit run streamlit_app.py --server.port 8501
```
---

## ☁️ Production Deployment (AWS EC2)

ResearchMind is optimized for deployment on Linux cloud instances (e.g., Ubuntu EC2).

**1. Establish the internal container network:**
```bash
docker network create research-net
```
**2. Deploy the Backend Engine (injecting safe variables):**
```bash
docker run -d \
  --name api \
  --network research-net \
  -p 8000:8000 \
  --env-file .env \
  dpk516/researchmind-api:v1
```
**3. Deploy the UI connected to the Backend Bridge:**
```bash
docker run -d \
  --name ui \
  --network research-net \
  -p 8501:8501 \
  -e API_URL=http://api:8000/api/research \
  dpk516/researchmind-ui:v1
```
---

## 📝 Environment Configuration

Configure the following environment variables to connect the backend application to the required external APIs.

| Variable          | Location           | Purpose                                              |
| :---              | :---               | :---                                                 |
| `MISTRAL_API_KEY` | Backend Container  | API key for Mistral AI to power the LLM reasoning.   |
| `TAVILY_API_KEY`  | Backend Container  | API key for Tavily AI to perform live web searches.  |

> **Note:** Do not use quotation marks around your API keys in the `.env` file (e.g., avoid `MISTRAL_API_KEY="xyz123"`). Docker reads the quotes as part of the actual key, which will cause authentication errors.
---
## 📄 License

Distributed under the MIT License. See the `LICENSE` file for more information.

---
<div align="center">
  <sub>Maintained  by <a href="https://github.com/dpk516">Deepak</a>
</div>
