# 🧠 ResearchMind: Multi-Agent AI Research System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0-FF4B4B.svg?logo=streamlit)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Integration-gray.svg?logo=langchain)](https://python.langchain.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg?logo=docker)](https://www.docker.com/)

An enterprise-grade, containerized Multi-Agent AI system designed to conduct deep, autonomous web research. Built with a decoupled architecture, ResearchMind leverages a **FastAPI** backend to orchestrate a **LangChain** agent swarm, communicating seamlessly with a sleek **Streamlit** frontend.

---

## 🏗️ System Architecture

The application is fully containerized using **Docker Compose**, ensuring an isolated, reproducible environment across any system.

```text
┌──────────────────────┐        HTTP / REST        ┌───────────────────────┐
│                      │ ◄───────────────────────► │                       │
│    Streamlit UI      │                           │     FastAPI Backend   │
│    (Port: 8501)      │                           │     (Port: 8000)      │
│                      │                           │                       │
└──────────────────────┘                           └───────────┬───────────┘
                                                               │
┌──────────────────────────────────────────────────────────────┴───────────────┐
│                      LangChain Multi-Agent Swarm                             │
│                                                                              │
│  ┌───────────────┐      ┌───────────────┐      ┌──────────────────────────┐  │
│  │ Mistral LLM   │ ◄──► │ Tavily Search │ ◄──► │ Data Synthesis & Output  │  │
│  └───────────────┘      └───────────────┘      └──────────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘

✨ Features
Decoupled Architecture: Clean separation of concerns between the API layer and the Presentation layer.

Multi-Agent Orchestration: Utilizes LangChain to manage autonomous research agents that query, scrape, and synthesize data.

Environment-Agnostic: Packaged into optimized Docker containers (python:3.11-slim) with shared virtual networks.

Defensive Configuration: Strict environment variable management and validation using Pydantic Settings.

Layer Caching: Highly optimized Dockerfiles utilizing multi-stage cache mounting for minimal cloud storage footprint.

🚀 Quick Start (Local Deployment)
1. Prerequisites
Docker Desktop installed and running.

API Keys for Mistral AI and Tavily.

2. Environment Setup
Clone the repository and navigate into the root directory:

Bash
git clone [https://github.com/yourusername/multi-agent-research-system.git](https://github.com/yourusername/multi-agent-research-system.git)
cd multi-agent-research-system
Create a .env file in the root folder to securely store your keys:

Ini, TOML
MISTRAL_API_KEY=your_mistral_key_here
TAVILY_API_KEY=your_tavily_key_here
3. Launch the System
Boot the container matrix using Docker Compose. This command automatically builds the images, establishes the secure network, and spins up both the API and UI containers.

Bash
docker-compose up --build
4. Access the App
Frontend UI: Navigate to http://localhost:8501

Backend API Docs: Navigate to http://localhost:8000/docs to interact with the raw OpenAPI (Swagger) endpoints.

☁️ Cloud Deployment (Docker Hub)
The pre-built, production-ready images for this project have been pushed to Docker Hub. You can pull and run them directly without needing to build from the source code.

Bash
# Pull the pre-compiled images directly from the cloud
docker pull dpk516/researchmind-api:v1
docker pull dpk516/researchmind-ui:v1