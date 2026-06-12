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