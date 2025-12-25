from pydantic import BaseModel
from typing import List, Optional


class JobDescription(BaseModel):
    job_id: str
    title: str
    required_skills: List[str]
    optional_skills: List[str] = []
    minimum_experience_years: float
    education_requirement: Optional[str] = None
    responsibilities: List[str] = []
