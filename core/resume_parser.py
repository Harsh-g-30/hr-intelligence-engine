import pdfplumber
import fitz  # PyMuPDF
import re
from core.resume_enhancer import enhance_resume

from schemas.resume_schema import Resume, Role, CareerGap


SKILL_KEYWORDS = [
    "python", "sql", "machine learning", "deep learning", "statistics",
    "data analysis", "aws", "azure", "gcp", "java", "c++", "nlp"
]


def extract_text_pdfplumber(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def extract_text_pymupdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def extract_text(pdf_path):
    try:
        text = extract_text_pdfplumber(pdf_path)
        if not text.strip():
            raise ValueError("Empty text from pdfplumber")
        return text
    except Exception:
        return extract_text_pymupdf(pdf_path)


def extract_skills(text):
    text_lower = text.lower()
    skills_found = set()

    for skill in SKILL_KEYWORDS:
        if re.search(rf"\b{re.escape(skill)}\b", text_lower):
            skills_found.add(skill)

    return list(skills_found)


def extract_experience_years(text):
    matches = re.findall(r"(\d+\.?\d*)\s*(years?|yrs?)", text.lower())
    years = sum(float(match[0]) for match in matches)
    return round(years, 2) if years > 0 else 0.0


def extract_education(text):
    education_keywords = [
        "b.tech", "bachelor", "master", "m.tech", "phd", "mba"
    ]
    for keyword in education_keywords:
        if keyword in text.lower():
            return keyword.upper()
    return None


def extract_certifications(text):
    certs = []
    known_certs = [
        "aws", "azure", "gcp", "pmp", "scrum", "tensorflow"
    ]
    for cert in known_certs:
        if cert in text.lower():
            certs.append(cert.upper())
    return list(set(certs))


def parse_resume_pdf(pdf_path, candidate_id="UNKNOWN", name="UNKNOWN"):
    text = extract_text(pdf_path)

    resume = Resume(
        candidate_id=candidate_id,
        name=name,
        skills=extract_skills(text),
        experience_years=extract_experience_years(text),
        education=extract_education(text),
        certifications=extract_certifications(text),
        previous_roles=[],
        career_gaps=[]
    )

    # AI-assisted enhancement
    resume = enhance_resume(resume, text)

    return resume
