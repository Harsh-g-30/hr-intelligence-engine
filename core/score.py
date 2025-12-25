from core.skill_extractor import normalize_skills


def score_candidate(resume, jd):
    breakdown = {
        "skill_match": 0,
        "experience_match": 0,
        "education_match": 0,
        "certifications_bonus": 0,
    }

    resume_skills = normalize_skills(resume.skills)
    required_skills = normalize_skills(jd.required_skills)
    optional_skills = normalize_skills(jd.optional_skills)

    matched_required = resume_skills & required_skills
    matched_optional = resume_skills & optional_skills

    # Skill score (50)
    if required_skills:
        breakdown["skill_match"] += int(
            (len(matched_required) / len(required_skills)) * 40
        )

    if optional_skills:
        breakdown["skill_match"] += int(
            (len(matched_optional) / len(optional_skills)) * 10
        )

    # Experience score (25)
    if resume.experience_years >= jd.minimum_experience_years:
        breakdown["experience_match"] = 25
    else:
        breakdown["experience_match"] = int(
            (resume.experience_years / jd.minimum_experience_years) * 25
        )

    # Education score (10, soft)
    if resume.education and jd.education_requirement:
        breakdown["education_match"] = 10

    # Certifications bonus (5)
    if resume.certifications:
        breakdown["certifications_bonus"] = 5

    total_score = sum(breakdown.values())

    return {
        "total_score": min(total_score, 100),
        "breakdown": breakdown,
        "matched_required": list(matched_required),
        "missing_required": list(required_skills - matched_required),
        "missing_optional": list(optional_skills - matched_optional),
    }
