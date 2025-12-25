# 🧠 HR Intelligence Engine

**AI-powered, explainable, and bias-aware resume screening platform**

---

## 📌 Overview

The **HR Intelligence Engine** is a production-ready AI system that evaluates **resume–job description fit** using a **hybrid architecture**:

- **Deterministic rule-based scoring** for fairness and auditability  
- **Gemini 2.5 Flash (LLM)** for safe parsing enhancement and human-readable explanations  

The system supports:

- PDF resume ingestion  
- Explainable fit scoring (0–100)  
- Skill gap analysis  
- Bias-aware hiring signals  
- CLI execution  
- REST APIs via FastAPI  

This project is designed with **real-world HR workflows** in mind, prioritizing **transparency, reliability, and ethical AI usage**.

---

## ✨ Key Features

- 📄 Resume PDF Parsing  
- 📋 Job Description Analysis  
- 🎯 Explainable Fit Scoring  
- 🧩 Skill Match & Gap Detection  
- ⚖️ Bias-Aware Evaluation  
- 🤖 Gemini AI for Parsing & Explanations  
- 🖥️ CLI Interface  
- 🌐 FastAPI Backend with Swagger UI  

---

## 🧠 Architecture

### High-Level Flow

[ CLI / Web UI ]
↓
[ FastAPI Backend ]
↓
[ Resume PDF Parser ]
↓
[ Gemini AI Enhancer ]
↓
[ Deterministic Scoring Engine ]
↓
[ Explainability & Bias Detection ]
↓
[ JSON Response / UI Output ]


---

### Design Principles

#### Hybrid AI Architecture
- AI assists, but never decides  
- Scoring is deterministic and testable  

#### Explainability First
- Every score is traceable  

#### Bias Awareness
- Career gaps and education treated fairly  

#### Production Safety
- Graceful fallbacks if AI fails  

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|-----------|
| Backend | Python, FastAPI |
| AI Model | Gemini 2.5 Flash (`google.genai`) |
| Parsing | pdfplumber, PyMuPDF |
| Schemas | Pydantic |
| API Server | Uvicorn |
| CLI | argparse |
| Testing | Pytest |

---

## 📁 Project Structure

hr-intelligence-engine/
│
├── api/ # FastAPI backend
│ └── app.py
│
├── core/ # Core engine logic
│ ├── resume_parser.py
│ ├── scorer.py
│ ├── explainability.py
│ └── bias_checker.py
│
├── llm/ # Gemini integration
│ └── gemini_client.py
│
├── schemas/ # Pydantic schemas
│ ├── resume_schema.py
│ ├── jd_schema.py
│ └── output_schema.py
│
├── data/
│ ├── samples/
│ └── uploads/
│
├── main.py # CLI entry point
├── requirements.txt
└── README.md


---


