# cynbit PolicyLens — AI Reply Checker

**A small AI tool that checks whether a draft customer-support reply follows the official company policy.**
 **[Access the Live Application Here](https://cynbit.streamlit.app/)**
## The problem

A customer-support chatbot might promise a 30-day return window even though the real policy allows returns only within 14 days. That answer may sound confident but be wrong.

## What PolicyLens does

1. Paste the official policy.
2. Enter the customer's question.
3. Paste the AI-generated draft reply.
4. Copy `.env.example` to `.env` and replace `your_groq_api_key_here` with your Groq API key.
5. Click **Check reply**.
6. Review one of three labels — **Supported**, **Needs review**, or **Contradiction** — plus the reason, claims to check, and a safer suggested reply.

This is a focused policy-grounding checker, not another general chatbot, invoice extractor, or document parser.

## Technology

- **Python** for the checking logic.
- **Streamlit** for the web interface.
- **Groq API + a hosted pretrained LLM** to compare the draft with the supplied policy.
- **JSON output validation** so the application checks that the model returned the expected fields.

The prototype does not train a model from scratch. It uses a hosted pretrained language model through an API.

## Run it on Windows PowerShell

1. Download and extract the ZIP, then open the extracted `cynbit_policylens_updated` folder in VS Code.
2. In the VS Code terminal, run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m unittest discover -s tests -v
streamlit run app.py
```

3. Create an API key in your [Groq Console](https://console.groq.com/keys).
4. Copy `.env.example` to `.env` and replace `your_groq_api_key_here` with your Groq API key.
5. Keep the default model ID or enter another model ID available to your Groq account.
6. Click **Check reply**. The included default text is a sample scenario you can run first.

If PowerShell blocks virtual-environment activation, run the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## API key handling — important

The app loads the Groq API key from `GROQ_API_KEY` in the local `.env` file. Users do not enter or see the key in the Streamlit UI.

- The `.env` file is ignored by Git and must never be committed.
- `.env.example` documents the required variable without containing a real key.
- Never commit a real API key or screenshot showing a key to GitHub.

The text you submit for checking is sent to Groq. Use fictional data for the public demo; do not submit confidential customer information without authorization. For a deployed application used by multiple people, add proper server-side secret management, authentication, and access controls.

## Default model

The default model ID is `openai/gpt-oss-20b`. Groq's model catalogue can change, so check the [current supported models](https://console.groq.com/docs/models) if the request reports that the model is unavailable.

## Sample scenario

**Official policy:** Returns are allowed within 14 days of delivery. Items must be unused and in their original packaging. Approved refunds take 5–7 business days.

**Customer:** “I received my headphones 20 days ago. Can I return them and get a refund tomorrow?”

**Draft AI reply:** “Yes, you can return the headphones within 30 days, even if they have been used. Your refund will arrive tomorrow.”

PolicyLens should flag the 30-day window and next-day refund promise as potential contradictions to investigate. The actual output comes from the LLM and may vary.

## Limitations

- The review can be wrong or incomplete because language models can misread text or miss contradictions.
- The result depends on the policy text provided. Missing or outdated policy text can lead to a misleading verdict.
- A verdict is a review aid, not an automatic approval/rejection decision.
- The sample tests validate input and output handling; they do **not** prove that the model's judgments are accurate.

## Public research used for the opportunity framing

Cynbit's public AI/ML internship page mentions AI chatbots, prompt engineering, document pipelines, and AI/ML integration. Its services page describes AI automation, autonomous agents, LLM automation, and AI-stack integration. PolicyLens is a proposed supporting QA tool for such AI-powered workflows, not a claim about an existing internal Cynbit problem.

- [Cynbit — AI/ML Engineer Intern](https://www.cynbit.in/careers/ai-ml-engineer-intern)
- [Cynbit — Services](https://www.cynbit.in/services)
- [Groq — Supported models](https://console.groq.com/docs/models)
- [Groq — API keys](https://console.groq.com/keys)
