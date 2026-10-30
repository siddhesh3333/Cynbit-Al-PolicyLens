# Technical Approach Report — PolicyLens
**Candidate:** Siddhesh Dhande  
**Role:** AI/ML Engineer Intern  
**Date:** October 30, 2026

## 1. Goal

Build a simple demo that checks whether an AI-generated support reply is supported by an official policy, highlights possible conflicts or unsupported claims, and proposes safer wording.

## 2. Architecture

```text
Official policy + customer question + draft reply
                     |
                     v
      Prompt sent to hosted language model
                     |
                     v
       Structured JSON result from the model
                     |
                     v
        Validate fields and allowed status
                     |
                     v
      Streamlit displays result for human review
```

## 3. Technology choices

- **Python:** input validation and API integration.
- **Streamlit:** simple web interface that runs locally and can be deployed.
- **Groq API:** access to a hosted pretrained LLM. Default model ID: `openai/gpt-oss-20b`; change it to an active model if needed.
- **JSON output:** asks the LLM for a predictable set of fields and validates those fields before displaying the result.

This is an API-based proof of concept. It does not train a new model or use embeddings, vector databases, RAG, or an agent framework.

## 4. Input and output

**Inputs:**
- `policy`: official company rules or facts
- `question`: the customer's question
- `draft`: the AI-generated reply

**Output:**
- `status`: Supported, Needs review, or Contradiction
- `reason`: short explanation
- `supported_points`: statements supported by the policy
- `unsupported_claims`: statements with no clear evidence in the policy
- `contradictions`: statements that conflict with the policy
- `safer_reply`: suggested wording that avoids promises not supported by the policy

## 5. Prompt design

The system prompt tells the model to compare the draft only with the supplied policy, avoid inventing rules, select Needs review when evidence is insufficient, and return the required JSON keys. Supplied text is treated as data rather than instructions. This is a defensive prompt design measure, not a complete prompt-injection defence.

## 6. Error handling and security

- Validate that all three text inputs and the model ID are present.
- Limit input length in the prototype.
- Catch API failures and display an error rather than inventing a result.
- Validate JSON syntax, required keys, status values, and list/text field types.
- Load the API key from `GROQ_API_KEY` in the local `.env` file. The key is not shown in the Streamlit UI or written to logs, and `.env` is ignored by Git.
- Do not send confidential customer data to an external service without authorization.

## 7. Test plan

Automated unit tests cover missing inputs, oversized inputs, valid JSON, malformed JSON, invalid statuses, and invalid field types. These tests verify input/output handling only; they do not establish the factual accuracy of LLM judgments.

For a meaningful quality evaluation, prepare 30–50 synthetic policy/question/reply cases and label them with a human reviewer. Include true contradictions, unsupported claims, correct paraphrases, and ambiguous policies. Measure agreement with human labels, precision/recall for contradictions, false-positive rate, response latency, and API cost.

## 8. Limitations and future work

The LLM can make mistakes, and the result depends on the quality and completeness of the supplied policy. The first version handles one reply at a time and uses a human-in-the-loop workflow. Future improvements could include policy version selection, a batch test set, source quotation for each issue, reviewer feedback, and integration into a customer-support product.

## References

- Cynbit internship role: https://www.cynbit.in/careers/ai-ml-engineer-intern
- Cynbit services: https://www.cynbit.in/services
- Groq supported models: https://console.groq.com/docs/models
- Groq API reference: https://console.groq.com/docs/api-reference
