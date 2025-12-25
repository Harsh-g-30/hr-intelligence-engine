from pydantic import BaseModel
from typing import List, Optional


class Role(BaseModel):
    title: str
    duration_years: float


class CareerGap(BaseModel):
    duration_months: int
    reason: Optional[str] = None


class Resume(BaseModel):
    candidate_id: str
    name: str
    skills: List[str]
    experience_years: float
    education: Optional[str] = None
    previous_roles: List[Role] = []
    certifications: List[str] = []
    career_gaps: List[CareerGap] = []
