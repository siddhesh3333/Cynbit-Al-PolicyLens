# AI Opportunity Report — PolicyLens
**Candidate:** Siddhesh Dhande  
**Role:** AI/ML Engineer Intern  
**Date:** October 30, 2026

## 1. Summary

PolicyLens is a small prototype that checks whether an AI-generated customer-support reply agrees with a company's approved policy. A support team provides the policy, the customer's question, and the AI draft. The tool returns a simple review label, explains potentially unsupported or contradictory claims, and suggests safer wording.

The idea targets a practical risk in AI-assisted customer support: a reply may sound fluent while promising something the company does not actually offer.

## 2. Why this is relevant

Cynbit's public AI/ML internship description includes building chatbots and virtual assistants, prompt engineering, document processing, and integrating AI/ML technologies. Its services page describes autonomous agents, LLM automation, and AI-stack integration. A policy-checking step is a plausible supporting capability for AI assistants that answer customer questions.

Sources:
- https://www.cynbit.in/careers/ai-ml-engineer-intern
- https://www.cynbit.in/services

This is an opportunity proposed from public information. It is **not** a claim that Cynbit currently has this problem or needs this exact tool.

## 3. Problem and proposed workflow

**Example:** The approved policy says returns are accepted within 14 days. A chatbot tells a customer they have 30 days. The statement could create an avoidable support issue.

PolicyLens follows five simple steps:
1. Receive the official policy, customer question, and AI draft.
2. Send those texts to a hosted language model with instructions to judge the draft only against the supplied policy.
3. Request a structured JSON result.
4. Validate the returned fields and show one of three labels: Supported, Needs review, or Contradiction.
5. Show the claims to check and a safer suggested reply for a human reviewer.

## 4. Opportunity comparison

| Opportunity | Potential value | Why it was not selected for this first prototype |
|---|---|---|
| Invoice field extraction | Reduce manual data entry | Many standard examples exist; requires robust handling of varied layouts and OCR |
| Customer enquiry classification | Route requests to teams | Common baseline problem with a less distinctive demonstration |
| AI reply policy checking | Help detect unsupported promises before a reply is sent | Selected because the workflow is easy to understand and can be demonstrated with synthetic policy text |

The selected idea is not claimed to be globally novel. Its value for this assessment is a focused implementation of a specific AI quality-control step.

## 5. Expected value and how to measure it

Potential benefits are fewer unsupported promises, more consistent reply review, and a reusable policy-check workflow. These are hypotheses until tested.

For a first evaluation, create 30–50 synthetic test cases with human labels. Include supported replies, changed dates or amounts, unsupported guarantees, missing policy information, and ambiguous cases. Compare PolicyLens results with human reviewers and track:

- Agreement with human labels
- Precision and recall for policy contradictions
- False alarms on correct replies
- Percentage of cases marked Needs review
- Average API response time and cost per check

Do not claim accuracy or time savings until these measurements have been completed.

## 6. Risks and safeguards

- **Model errors:** the LLM can miss a contradiction or flag a harmless statement. Human review remains necessary.
- **Incomplete policy:** if the supplied policy is missing, outdated, or ambiguous, the result can be misleading.
- **Privacy:** the submitted text and the API request are sent to Groq. The API key is loaded from the local `.env` file and is not shown in the Streamlit UI. Use synthetic data in the public demo and obtain authorization before using customer information.
- **Prompt injection:** the evaluator is instructed to treat policy, question, and draft as data, not as instructions. This reduces but does not eliminate risk.
- **Overreliance:** the result is advisory and must not automatically approve or reject customer requests.

## 7. Recommendation

Start with a small, human-labelled test set in a non-production environment. If agreement and false-positive rates are acceptable, a future version could be integrated into a support workflow as a pre-send review step. Production use would need access control, policy versioning, audit logs, privacy review, and monitoring.
