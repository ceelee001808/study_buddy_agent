"""
STEP 3: An agent that can use tools.

Goal: give the model two Python functions it can decide to call on its own.
Run it:  python step3_agent_tools.py
"""
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from config import MODEL  # the model name lives in config.py
from langchain.agents import create_agent

load_dotenv()
model = init_chat_model(MODEL)


# ---- TOOLS ----
# The docstring and type hints are what the model reads to decide
# WHEN and HOW to call each tool, so write them clearly.

def calculate(expression: str) -> str:
    """Evaluate a basic math expression like '12 * 7' or '0.15 * 240'."""
    # Restricted eval: fine for learning, NOT safe for untrusted input.
    return str(eval(expression, {"__builtins__": {}}))


def make_flashcard(term: str, definition: str) -> str:
    """Create a study flashcard from a term and its definition."""
    return f"FRONT: {term}\nBACK: {definition}"


# ---- AGENT ----
agent = create_agent(
    model=model,
    tools=[calculate, make_flashcard],
    system_prompt="You are a helpful study buddy. Use your tools when they help.",
)

question = "What's 15% of 240? Then make a flashcard for the word 'percent'."
result = agent.invoke({"messages": [{"role": "user", "content": question}]})

# Print every step so you can SEE the agent's loop:
# your question -> tool call -> tool result -> tool call -> ... -> final answer
print("=== EVERY STEP THE AGENT TOOK ===")
for msg in result["messages"]:
    msg.pretty_print()

print("\n=== FINAL ANSWER ONLY ===")
print(result["messages"][-1].content)
