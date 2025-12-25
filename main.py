from schemas.jd_schema import JobDescription
from schemas.output_schema import EvaluationResult, DecisionExplanation

from core.score import score_candidate
from core.bias_checker import detect_bias_flags
from core.explainability import generate_explanations
from core.resume_parser import parse_resume_pdf


def main():
    resume = parse_resume_pdf(
        pdf_path="data/samples/sample_resume.pdf",
        candidate_id="C001",
        name="John Doe"
    )

    jd = JobDescription(
        job_id="J001",
        title="Data Scientist",
        required_skills=["Python", "Statistics", "Machine Learning"],
        optional_skills=["AWS", "Deep Learning"],
        minimum_experience_years=2,
        education_requirement="Bachelor's degree"
    )

    score_data = score_candidate(resume, jd)
    bias_flags = detect_bias_flags(resume, jd)
    why_selected, why_rejected = generate_explanations(score_data)

    result = EvaluationResult(
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

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
