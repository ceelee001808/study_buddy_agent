# Study Buddy: A Beginner LangChain Project

You'll build an AI study assistant in 5 small steps. Each step is its own file,
so you can run them one at a time and see exactly what each new idea adds.

| File | What you learn |
|---|---|
| `config.py` | Where the model name is set (shared by every step) |
| `step1_basic_call.py` | Sending a message to a model |
| `step2_prompt_chain.py` | Prompt templates and the `|` pipe (chains) |
| `step3_agent_tools.py` | Agents that call your Python functions (tools) |
| `step4_memory.py` | Remembering the conversation (threads) |
| `step5_chat_app.py` | The finished app: an interactive chat in your terminal |

---

## Part A: One-time setup (about 10 minutes)

### 1. Install the tools
- **Python 3.10 or newer**: https://www.python.org/downloads/
  (On Windows, tick **"Add Python to PATH"** during install.)
- **VS Code**: https://code.visualstudio.com/
- In VS Code, open the Extensions panel (the four-squares icon on the left),
  search **"Python"**, and install the one published by Microsoft.

### 2. Get a FREE API key (Google Gemini)
1. Go to https://aistudio.google.com/apikey and sign in with a Google account.
2. Click **Create API key** and copy it somewhere safe.
3. No credit card needed. The free tier is rate-limited, which is fine for learning.

> Heads up: on Google's free tier, your prompts may be used to improve Google's products,
> so don't type anything private into the app.

### 3. Open the project in VS Code
1. Unzip `study-buddy.zip`.
2. In VS Code: **File > Open Folder...** and pick the `study-buddy` folder.

### 4. Open the terminal
**Terminal > New Terminal** (or press Ctrl+` ). A panel opens at the bottom.
Every command below gets typed there.

### 5. Create a virtual environment
A "venv" keeps this project's packages separate from everything else.

Mac / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

You'll know it worked when you see `(.venv)` at the start of the terminal line.

> Windows error about "running scripts is disabled"? Run this once, then try again:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

If VS Code pops up asking "select this environment for the workspace?", click **Yes**.
Otherwise press Ctrl+Shift+P, type **Python: Select Interpreter**, and choose the one with `.venv`.

### 6. Install the packages
```bash
pip install -r requirements.txt
```

### 7. Add your API key
1. In the file list on the left, right-click `.env.example` > **Copy**, then **Paste**.
2. Rename the copy to exactly `.env`
3. Open `.env` and replace `your-key-here` with your real key. Save.

> Never share `.env` or upload it to GitHub. The included `.gitignore` already hides it.

---

## Part B: Run each step

Run each file from the terminal (with `(.venv)` showing), in order.
You can also open a file and click the play button in the top-right corner.

### Step 1: Talk to a model
```bash
python step1_basic_call.py
```
**Expected:** `MODEL SAYS:` followed by one sentence about photosynthesis.
**Key idea:** `init_chat_model(...)` creates a model; `.invoke()` sends a message.

### Step 2: Prompt template + chain
```bash
python step2_prompt_chain.py
```
**Expected:** Two explanations of gravity, one simple and one more advanced.
**Key idea:** `prompt | model | parser` pipes data left to right. One template, many inputs.

### Step 3: Agent with tools
```bash
python step3_agent_tools.py
```
**Expected:** A step-by-step printout showing:
1. Your question (Human Message)
2. The model deciding to call `calculate` (Ai Message with a tool call)
3. The result `36.0` (Tool Message)
4. The model calling `make_flashcard` (Ai Message)
5. The flashcard text (Tool Message)
6. The final answer

The exact wording and order may vary a little each run. That's normal: the model decides.
**Key idea:** The model reads your function docstrings and chooses when to call them.

### Step 4: Memory
```bash
python step4_memory.py
```
**Expected:**
- Thread 1 remembers you're studying cell biology and makes a flashcard about it.
- Thread 2 says it doesn't know your topic, because it's a separate conversation.

**Key idea:** A `checkpointer` stores history; the `thread_id` picks which conversation.

### Step 5: The finished app
```bash
python step5_chat_app.py
```
Chat with it! Things to try:
- `I'm studying the French Revolution. Give me a 3-question quiz.`
- `What's 17.5% of 380?`
- `Make flashcards for the three terms you just quizzed me on.`
- `quit` to exit

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | Your venv isn't active. Re-run the activate command from Part A step 5, then `pip install -r requirements.txt`. |
| Authentication / API key error | Check the file is named exactly `.env` (not `.env.txt`), is in the `study-buddy` folder, and has your real key with no quotes or spaces. |
| `429` / "quota exceeded" / "resource exhausted" | You hit the free tier's rate limit. Wait a minute and try again. |
| Model not found error | Free models change over time. Check which models are free in Google AI Studio, then update `MODEL` in `config.py`. |
| `python` not found (Mac) | Use `python3` instead. |

## Using a different provider
The model name lives in ONE place: `config.py`. To switch, e.g. to Claude (paid):
`pip install "langchain[anthropic]"`, put `ANTHROPIC_API_KEY=...` in `.env`,
and set `MODEL = "anthropic:claude-sonnet-4-5"` in `config.py`.

## Challenges once it all works
1. Add a third tool, e.g. `define_word(word: str) -> str` that returns a fake dictionary entry.
2. Change the system prompt in step 5 to make the buddy talk like a pirate, then a strict professor.
3. Make step 5 save every flashcard to a `flashcards.txt` file.
