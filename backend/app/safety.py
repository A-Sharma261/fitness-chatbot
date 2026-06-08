RISKY_KEYWORDS = [
    "chest pain",
    "fainting",
    "passed out",
    "dizzy",
    "injury",
    "injured",
    "pain",
    "pregnant",
    "pregnancy",
    "eating disorder",
    "anorexia",
    "bulimia",
    "steroids",
    "sarms",
    "extreme weight loss",
]


def is_risky_message(message: str) -> bool:
    lowered_message = message.lower()
    return any(keyword in lowered_message for keyword in RISKY_KEYWORDS)


def get_safety_response() -> str:
    return (
        "This sounds like it may involve health, injury, or medical concerns. "
        "I can give general fitness education, but I cannot diagnose or treat medical issues. "
        "Please speak with a qualified health professional for advice specific to your situation."
    )