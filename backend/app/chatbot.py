from google import genai

from app.config import GEMINI_API_KEY
from app.prompt import FITNESS_SYSTEM_PROMPT


client = genai.Client(api_key=GEMINI_API_KEY)


def get_fitness_response(user_message: str) -> str:
    prompt = f"""
{FITNESS_SYSTEM_PROMPT}

User question:
{user_message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text