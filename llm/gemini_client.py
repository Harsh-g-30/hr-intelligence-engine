import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment")

client = genai.Client(api_key=api_key)

MODEL_ID = "gemini-2.5-flash"


def gemini_complete(prompt: str) -> str:
    """
    Safe text generation wrapper for Gemini 2.5 Flash.
    """
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config={
            "temperature": 0.2,
            "max_output_tokens": 500,
        },
    )

    return response.text.strip()
