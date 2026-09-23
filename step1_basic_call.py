"""
STEP 1: Talk to a model.

Goal: send one message to an AI model and print its reply.
Run it:  python step1_basic_call.py
"""
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from config import MODEL  # the model name lives in config.py

# Reads API key from the .env file so you don't hardcode it.
load_dotenv()

# One line to create a chat model. To switch providers, edit MODEL in config.py.
model = init_chat_model(MODEL)

# .invoke() sends a message and waits for the reply.
response = model.invoke("Explain photosynthesis in one sentence.")

# The reply is an AIMessage object; the text lives in .content
print("MODEL SAYS:")
print(response.content)
