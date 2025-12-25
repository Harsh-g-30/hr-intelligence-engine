🧠 HR Intelligence Engine

AI-powered, explainable, and bias-aware resume screening platform

📌 Overview

The HR Intelligence Engine is a production-ready AI system that evaluates resume–job description fit using a hybrid architecture:

Deterministic rule-based scoring for fairness and auditability

Gemini 2.5 Flash (LLM) for safe parsing enhancement and human-readable explanations

The system supports:

PDF resume ingestion

Explainable fit scoring (0–100)

Skill gap analysis

Bias-aware hiring signals

CLI execution

REST APIs via FastAPI

This project is designed with real-world HR workflows in mind, prioritizing transparency, reliability, and ethical AI usage.

✨ Key Features

📄 Resume PDF Parsing

📋 Job Description Analysis

🎯 Explainable Fit Scoring

🧩 Skill Match & Gap Detection

⚖️ Bias-Aware Evaluation

🤖 Gemini AI for Parsing & Explanations

🖥️ CLI Interface

🌐 FastAPI Backend with Swagger UI

🧠 Architecture
High-Level Flow
[ CLI / Web UI ]
        |
        v
[ FastAPI Backend ]
        |
        v
[ Resume PDF Parser ]
        |
        v
[ Gemini AI Enhancer ]
        |
        v
[ Deterministic Scoring Engine ]
        |
        v
[ Explainability & Bias Detection ]
        |
        v
[ JSON Response / UI Output ]

Design Principles

Hybrid AI Architecture

AI assists, but never decides

Scoring is deterministic and testable

Explainability First

Every score is traceable

Bias Awareness

Career gaps and education treated fairly

Production Safety

Graceful fallbacks if AI fails

🛠️ Tech Stack
Layer	Technology
Backend	Python, FastAPI
AI Model	Gemini 2.5 Flash (google.genai)
Parsing	pdfplumber, PyMuPDF
Schemas	Pydantic
API Server	Uvicorn
CLI	argparse
Testing	Pytest
📁 Project Structure
hr-intelligence-engine/
│
├── api/                # FastAPI backend
│   └── app.py
│
├── core/               # Core engine logic
│   ├── resume_parser.py
│   ├── scorer.py
│   ├── explainability.py
│   └── bias_checker.py
│
├── llm/                # Gemini integration
│   └── gemini_client.py
│
├── schemas/            # Pydantic schemas
│   ├── resume_schema.py
│   ├── jd_schema.py
│   └── output_schema.py
│
├── data/
│   ├── samples/
│   └── uploads/
│
├── main.py             # CLI entry point
├── requirements.txt
└── README.md

🚀 Getting Started
1️⃣ Clone Repository
git clone https://github.com/Harsh-g-30/hr-intelligence-engine.git
cd hr-intelligence-engine

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables

Create a .env file:

GEMINI_API_KEY=your_gemini_api_key_here

🖥️ CLI Usage
python main.py --resume resume.pdf --jd jd.txt --mode hr


Modes supported:

hr

candidate

🌐 API Usage (FastAPI)
Start Server
python -m uvicorn api.app:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

🔹 POST /evaluate/hr

Description:
Evaluate resume–JD fit from an HR perspective.

Inputs (form-data):

resume (PDF)

job_title

required_skills (comma-separated)

optional_skills

min_experience

education_requirement

Response:

{
  "fit_score": 23,
  "matched_skills": ["python"],
  "missing_required_skills": ["machine learning", "statistics"],
  "decision_explanation": {
    "why_selected": ["Matched required skills: python"],
    "why_rejected": ["Missing required skills: machine learning, statistics"]
  }
}

🧪 Testing
pytest tests/

⚠️ AI Safety & Ethics

AI never assigns scores

AI never rejects candidates

All decisions are deterministic

AI output is strictly structured and validated

📌 Use Cases

HR resume screening

Candidate self-assessment

Hiring pipeline analysis

Fair hiring experimentation

AI explainability demonstrations
