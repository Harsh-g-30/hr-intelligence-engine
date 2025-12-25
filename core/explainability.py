from llm.gemini_client import gemini_complete
import json


def generate_explanations(score_data):
    base_selected = []
    base_rejected = []

    if score_data["matched_required"]:
        base_selected.append(
            f"Matched required skills: {', '.join(score_data['matched_required'])}"
        )

    if score_data["missing_required"]:
        base_rejected.append(
            f"Missing required skills: {', '.join(score_data['missing_required'])}"
        )

    prompt = f"""
You are an HR system.
Rewrite the explanations below.

RULES:
- Return STRICT JSON only
- No markdown
- No headings
- No extra text
- Keep meaning exactly the same

Input:
{{
  "why_selected": {base_selected},
  "why_rejected": {base_rejected}
}}

Output JSON format:
{{
  "why_selected": ["..."],
  "why_rejected": ["..."]
}}
"""

    try:
        response = gemini_complete(prompt)

        # Extract JSON safely
        start = response.find("{")
        end = response.rfind("}") + 1
        json_text = response[start:end]

        parsed = json.loads(json_text)

        return (
            parsed.get("why_selected", base_selected),
            parsed.get("why_rejected", base_rejected),
        )

    except Exception:
        # Absolute safety fallback
        return base_selected, base_rejected
