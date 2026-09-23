"""
STEP 5 (FINAL PROJECT): An interactive study buddy in your terminal.

Combines everything: model + prompt + tools + memory, in a chat loop.
Run it:  python step5_chat_app.py      (type 'quit' to exit)
"""
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from config import MODEL  # the model name lives in config.py
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()
model = init_chat_model(MODEL)


def calculate(expression: str) -> str:
    """Evaluate a basic math expression like '12 * 7' or '0.15 * 240'."""
    try:
        return str(eval(expression, {"__builtins__": {}}))
    except Exception as e:
        return f"Could not calculate that: {e}"


def make_flashcard(term: str, definition: str) -> str:
    """Create a study flashcard from a term and its definition."""
    return f"FRONT: {term}\nBACK: {definition}"


agent = create_agent(
    model=model,
    tools=[calculate, make_flashcard],
    system_prompt=(
        "You are a friendly study buddy. Explain clearly and briefly, "
        "quiz the student when asked, and use your tools when they help."
    ),
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": "main-session"}}

print("Study Buddy is ready! Type 'quit' to exit.\n")
while True:
    user_text = input("You: ").strip()
    if user_text.lower() in {"quit", "exit"}:
        print("Good luck studying!")
        break
    if not user_text:
        continue
    result = agent.invoke({"messages": [{"role": "user", "content": user_text}]}, config)
    print("Buddy:", result["messages"][-1].content, "\n")
