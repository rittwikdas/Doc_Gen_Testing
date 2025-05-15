from template import std_temp_questions
import random
import time

def verbose_log(msg: str):
    print(f"[LOG] {msg} | Timestamp: {time.time()}")

def long_response_stub(question: str) -> str:
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. " \
            "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. " \
            "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    return f"Answer for: {question}\n{lorem * random.randint(2, 5)}\n"

def generate_document():
    doc = []
    verbose_log("Starting document generation.")
    for section, questions in std_temp_questions.items():
        doc.append(f"\n# {section}\n")
        for q in questions:
            ans = long_response_stub(q)
            doc.append(f"**{q}**\n{ans}\n")
    verbose_log("Document generation complete.")
    return "\n".join(doc)
