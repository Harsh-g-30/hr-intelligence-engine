from llm.gemini_client import gemini_complete


def enhance_resume(resume, raw_text):
    prompt = f"""
You are an HR assistant.
Given the resume text below, help normalize and infer information.
Rules:
- DO NOT invent skills
- DO NOT exaggerate experience
- If experience duration is unclear, estimate conservatively
- Return ONLY JSON

Resume Text:
{raw_text}

Current Parsed Resume:
{resume.model_dump_json()}

Output JSON format:
{{
  "skills": [],
  "experience_years": number,
  "education": string or null
}}
"""

    response = gemini_complete(prompt)

    try:
        enhanced = eval(response)
        resume.skills = list(set(resume.skills + enhanced.get("skills", [])))
        resume.experience_years = max(
            resume.experience_years,
            enhanced.get("experience_years", resume.experience_years)
        )
        resume.education = resume.education or enhanced.get("education")
    except Exception:
        pass  # Fail-safe: never break pipeline

    return resume
