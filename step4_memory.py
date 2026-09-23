"""
STEP 4: Add memory.

Goal: the agent remembers earlier messages in the same conversation ("thread").
Run it:  python step4_memory.py
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
    return str(eval(expression, {"__builtins__": {}}))


def make_flashcard(term: str, definition: str) -> str:
    """Create a study flashcard from a term and its definition."""
    return f"FRONT: {term}\nBACK: {definition}"


# The checkpointer is what stores the conversation history.
agent = create_agent(
    model=model,
    tools=[calculate, make_flashcard],
    system_prompt="You are a helpful study buddy. Use your tools when they help.",
    checkpointer=InMemorySaver(),
)


def ask(text: str, thread_id: str) -> str:
    config = {"configurable": {"thread_id": thread_id}}
    result = agent.invoke({"messages": [{"role": "user", "content": text}]}, config)
    return result["messages"][-1].content


# Thread 1: tell it a topic, then refer back to it.
print("[Thread 1] You: I'm studying cell biology.")
print("Buddy:", ask("I'm studying cell biology.", "thread-1"), "\n")

print("[Thread 1] You: Make me one flashcard on my topic.")
print("Buddy:", ask("Make me one flashcard on my topic.", "thread-1"), "\n")

# Thread 2: a brand-new conversation, so it should NOT know your topic.
print("[Thread 2] You: What topic am I studying?")
print("Buddy:", ask("What topic am I studying?", "thread-2"))
