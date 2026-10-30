# Test Plan — PolicyLens

## Automated tests

Run:

```powershell
python -m unittest discover -s tests -v
```

The current unit tests check required input validation, maximum field size, valid JSON parsing, malformed JSON, allowed status labels, and expected field types.

## Manual functional checks

Copy `.env.example` to `.env`, set a valid `GROQ_API_KEY`, and run `streamlit run app.py`:

1. Run the default sample. The policy says returns are accepted within 14 days, while the draft claims 30 days and a next-day refund.
2. Change the draft to a reply that accurately reflects the policy and check whether the status is Supported or Needs review.
3. Remove `GROQ_API_KEY` from `.env` and confirm the app asks for it before making an API call.
4. Remove the policy text and confirm the app asks for it before making an API call.
5. Use an invalid model ID and confirm a safe API error is shown without exposing the key or crashing the app.
6. Confirm the API key is not displayed anywhere in the sidebar or page.
7. Check that the JSON download includes the status and explanation.

LLM outputs can vary. These manual checks are for functional behavior, not proof of accuracy.

## Credential handling checks

- Search the source for `load_dotenv` and `GROQ_API_KEY`; the app should load the key from `.env`.
- Confirm `.env` and local secrets files are ignored by Git, while `.env.example` is included.
- Never use a real API key in automated tests or commit history.
