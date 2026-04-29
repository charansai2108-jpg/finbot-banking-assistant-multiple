# 🏦 FinBot — AI Banking Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Groq](https://img.shields.io/badge/Groq-API-orange)
![LLaMA](https://img.shields.io/badge/LLaMA-3.3_70B-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

An AI-powered multi-turn customer support chatbot 
for HDFC Bank, specialized in NEFT, RTGS, and 
SFMS payment queries.

Built in Week 1 of AI Career Accelerator Program 🚀

---

## 🎯 Features

- Multi-turn conversation with memory
- Answers NEFT/RTGS/SFMS banking questions  
- Checks transaction status using UTR/Transaction ID
- Handles failed transactions with escalation flow
- Prompt guardrails — refuses out-of-scope queries
- Never discloses sensitive customer data
- Graceful exit with goodbye message

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| Groq API | LLM API provider |
| LLaMA 3.3 70B | AI language model |
| Prompt Engineering | System prompts + Guardrails |
| Google Colab | Development environment |

---

## 💡 Prompt Engineering Techniques

- **System Prompts** — Defined FinBot persona, 
  rules, tone and restrictions
- **Prompt Guardrails** — Restricted scope to 
  banking topics only
- **Few-Shot Style** — Edge case handling built 
  into instructions
- **Chain-of-Thought** — Step-by-step transaction 
  validation logic

---

## 📋 Sample Conversation
