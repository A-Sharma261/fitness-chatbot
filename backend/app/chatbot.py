from google import genai

from app.config import GEMINI_API_KEY
from app.prompt import FITNESS_SYSTEM_PROMPT
from app.schemas import ChatMessage


client = genai.Client(api_key=GEMINI_API_KEY)


def format_history(history: list[ChatMessage]) -> str:
    if not history:
        return "No previous conversation."

    formatted_messages = []

    for message in history[-10:]:
        role = "User" if message.role == "user" else "Assistant"
        formatted_messages.append(f"{role}: {message.content}")

    return "\n".join(formatted_messages)


def get_fitness_response(user_message: str, history: list[ChatMessage] | None = None) -> str:
    conversation_history = format_history(history or [])

    prompt = f"""
{FITNESS_SYSTEM_PROMPT}

Previous conversation:
{conversation_history}

Current user question:
{user_message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    return response.text