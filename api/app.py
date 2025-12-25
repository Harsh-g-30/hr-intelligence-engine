from fastapi import FastAPI, UploadFile, File, Form
import shutil
import uuid
import os

from schemas.jd_schema import JobDescription
from schemas.output_schema import EvaluationResult, DecisionExplanation
from core.resume_parser import parse_resume_pdf
from core.score import score_candidate
from core.bias_checker import detect_bias_flags
from core.explainability import generate_explanations

app = FastAPI(
    title="HR Intelligence Engine",
    description="AI-powered, explainable resume screening API",
    version="1.0.0"
)

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_uploaded_file(upload_file: UploadFile) -> str:
    filename = f"{uuid.uuid4()}_{upload_file.filename}"
    path = os.path.join(UPLOAD_DIR, filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return path


@app.post("/evaluate/hr", response_model=EvaluationResult)
async def evaluate_hr(
    resume: UploadFile = File(...),
    job_title: str = Form(...),
    required_skills: str = Form(...),
    optional_skills: str = Form(""),
    min_experience: float = Form(...),
    education_requirement: str = Form(None),
):
    resume_path = save_uploaded_file(resume)

    parsed_resume = parse_resume_pdf(
        pdf_path=resume_path,
        candidate_id="HR_UPLOAD",
        name="Candidate"
    )

    jd = JobDescription(
        job_id="JD_API",
        title=job_title,
        required_skills=[s.strip() for s in required_skills.split(",")],
        optional_skills=[s.strip() for s in optional_skills.split(",") if s.strip()],
        minimum_experience_years=min_experience,
        education_requirement=education_requirement
    )

    score_data = score_candidate(parsed_resume, jd)
    bias_flags = detect_bias_flags(parsed_resume, jd)
    why_selected, why_rejected = generate_explanations(score_data)

    return EvaluationResult(
        fit_score=score_data["total_score"],
        score_breakdown=score_data["breakdown"],
        matched_skills=score_data["matched_required"],
        missing_required_skills=score_data["missing_required"],
        missing_optional_skills=score_data["missing_optional"],
        decision_explanation=DecisionExplanation(
            why_selected=why_selected,
            why_rejected=why_rejected
        ),
        bias_flags=bias_flags,
        candidate_suggestions=[
            "Strengthen missing required skills",
            "Add relevant certifications"
        ]
    )
