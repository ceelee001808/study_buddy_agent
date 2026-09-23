"""
STEP 2: A reusable chain with a prompt template.

Goal: define a prompt once with blanks ({level}, {question}),
then pipe it into the model and an output parser.
Run it:  python step2_prompt_chain.py
"""
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from config import MODEL  # the model name lives in config.py
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = init_chat_model(MODEL)

# The template has two "blanks" that get filled in at run time.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a patient tutor. Explain things for a {level} student. "
               "Keep answers under 4 sentences."),
    ("human", "{question}"),
])

# The | pipe sends data left to right:
# template fills blanks -> model answers -> parser turns the reply into a plain string
chain = prompt | model | StrOutputParser()

# Same chain, different inputs. This is why templates are useful.
for level in ["elementary school", "college"]:
    answer = chain.invoke({"level": level, "question": "What is gravity?"})
    print(f"--- Explained for a {level} student ---")
    print(answer)
    print()
