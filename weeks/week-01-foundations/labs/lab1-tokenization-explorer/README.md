# Lab 1 — Tokenization Explorer

## Week 1: Foundations of LLM Inference

---

## Lab Goal

In this lab, you will investigate how raw text becomes tokens, token IDs, and model-ready numerical input.

This lab answers one of the most important questions in LLM inference:

> What exactly does a model receive when a user sends a prompt?

By the end, you should understand why tokens are the real operational unit of LLM systems.

---

## Why This Lab Matters

Most beginners think language models process words.

They do not.

Language models process tokens.

This distinction matters because token count affects:

* latency
* memory usage
* context window pressure
* API cost
* throughput
* batching behavior
* KV cache growth

In production inference systems, token count is not a minor detail.

It is one of the most important cost and performance drivers.

---

## Production Context

Imagine you operate an inference API.

Two users send prompts:

### Prompt A

```text
Summarize this email.
```

### Prompt B

```text
Please carefully analyze the following 40-page contract and identify every clause that creates legal, financial, operational, or reputational risk.
```

Even before generation begins, Prompt B is more expensive.

Why?

Because it creates more input tokens.

More input tokens mean:

* longer prefill
* larger KV cache
* more attention computation
* higher memory pressure
* slower TTFT

This lab helps you see that directly.

---

## Core Concepts

You will practice:

* loading a tokenizer
* converting text into tokens
* converting text into token IDs
* counting tokens
* comparing token-to-word ratios
* identifying subword splits
* reasoning about cost and latency

---

## Files In This Lab

```text
lab1-tokenization-explorer/
├── README.md
├── code/
│   ├── starter.py
│   ├── solution.py
│   └── utils.py
├── expected_output.md
├── troubleshooting.md
├── reflection_questions.md
├── reports/
│   └── LAB_REPORT_TEMPLATE.md
├── instructor/
│   └── INSTRUCTOR_NOTES.md
└── requirements.txt
```

---

## Recommended Environment

This lab is safe to run on:

* your Ubuntu laptop
* Google Colab
* CPU-only machine

No large GPU is required.

---

## Default Model

We use:

```text
Qwen/Qwen2.5-0.5B-Instruct
```

Why?

* small enough for beginner experiments
* modern tokenizer
* aligned with our future Qwen-based capstone
* easier to run on limited hardware

---

## Setup

From this lab folder:

```bash
pip install -r requirements.txt
```

Or from the Week 1 root if you use a shared environment:

```bash
pip install -r labs/requirements.txt
```

---

## Task 1 — Basic Tokenization

Run:

```bash
python code/starter.py
```

Observe:

* original text
* token list
* token IDs
* token count

Do not just look for whether the script worked.

Ask:

> What surprised me about how the text was split?

---

## Task 2 — Compare Words vs Tokens

Modify the starter code to calculate:

```text
number of words
number of tokens
tokens per word
```

You should notice that:

```text
word count != token count
```

This matters because production systems bill, schedule, and allocate memory based on tokens.

---

## Task 3 — Study Subword Splitting

Add technical words such as:

```text
microarchitectural
quantization
autoregressive
internationalization
```

Observe how they split.

Rare or complex words often become multiple tokens.

This shows why tokenization is not equivalent to word splitting.

---

## Task 4 — Compare Prompt Styles

Compare:

```text
Explain inference.
```

with:

```text
Please provide a detailed technical explanation of transformer inference, including tokenization, prefill, decode, KV cache, latency, throughput, and production serving tradeoffs.
```

Ask:

* Which prompt produces more tokens?
* Why does that matter?
* What would happen at scale?

---

## Task 5 — Operational Interpretation

For each text sample, write one sentence explaining the production implication.

Example:

```text
This prompt has 92 tokens, so it will create more prefill work and consume more context window space than the shorter prompt.
```

This is the type of reasoning expected throughout the course.

---

## Expected Student Output

You should produce:

1. A tokenization table.
2. Token count comparisons.
3. At least three observations.
4. A short lab report.
5. Answers to reflection questions.

---

## Engineering Standard

A weak answer says:

```text
The tokenizer split the sentence.
```

A strong answer says:

```text
The longer prompt produced 5x more tokens, which implies higher prefill latency, larger KV cache allocation, and higher serving cost in production.
```

That is the level of thinking this course is designed to develop.

---

## Stretch Challenge

Test text in different styles:

* English
* Ghanaian names
* code snippets
* emojis
* punctuation-heavy text
* repeated whitespace
* mixed language text

Observe how tokenization changes.

Then answer:

> Which text type appears least token-efficient, and why might that matter in a production multilingual AI system?

---

## Deliverable

Submit:

```text
reports/lab1_report.md
```

using the provided report template.

Your report should include:

* tokenization results
* observations
* production interpretation
* reflection answers

---

## Key Lesson

Tokens are not just a preprocessing detail.

Tokens are the economic, computational, and memory unit of LLM inference systems.
