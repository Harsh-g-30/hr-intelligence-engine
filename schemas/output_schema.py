from pydantic import BaseModel
from typing import List, Dict


class DecisionExplanation(BaseModel):
    why_selected: List[str]
    why_rejected: List[str]


class EvaluationResult(BaseModel):
    fit_score: int
    score_breakdown: Dict[str, int]
    matched_skills: List[str]
    missing_required_skills: List[str]
    missing_optional_skills: List[str]
    decision_explanation: DecisionExplanation
    bias_flags: List[str]
    candidate_suggestions: List[str]
