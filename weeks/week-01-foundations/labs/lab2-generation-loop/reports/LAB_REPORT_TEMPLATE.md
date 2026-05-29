# Lab Report Template — Lab 2 Build a Tiny Generation Loop

## Student Information

| Field            | Value |
| ---------------- | ----- |
| Name             |       |
| Date             |       |
| Environment Used |       |
| CPU              |       |
| GPU              |       |
| RAM              |       |

---

# Lab Objective

In your own words, explain:

> What was the purpose of this lab?

Your answer should discuss:

* autoregressive generation
* next-token prediction
* logits
* sequential decoding

Minimum:
150 words.

---

# Environment Setup

Document:

* operating system
* Python version
* CPU or GPU execution
* model used
* installation issues encountered

Example:

```text
Ubuntu 24.04
Python 3.11
CPU execution
Qwen/Qwen2.5-0.5B-Instruct
No installation issues
```

---

# Generation Loop Investigation

## Prompt Used

Write the exact prompt you tested:

```text
_____________________________________
```

---

## Initial Token Count

Record:

```text
____________________
```

---

## Final Token Count

Record:

```text
____________________
```

---

## Tokens Generated

Calculate:

```text
Final Token Count
-
Initial Token Count
```

Result:

```text
____________________
```

---

# Generation Observations

Record at least THREE observations.

---

## Observation 1

What happened?

```text
_____________________________________
_____________________________________
_____________________________________
```

Why does it matter?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

## Observation 2

What happened?

```text
_____________________________________
_____________________________________
_____________________________________
```

Why does it matter?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

## Observation 3

What happened?

```text
_____________________________________
_____________________________________
_____________________________________
```

Why does it matter?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

# Logits Investigation

Answer:

## What are logits?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

## Why does the model output logits instead of words?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

## What does the vocabulary dimension represent?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

# Understanding Autoregressive Generation

Complete the sentence:

```text
A language model generates text by...
```

Minimum:
5 sentences.

```text
_____________________________________
_____________________________________
_____________________________________
_____________________________________
_____________________________________
```

---

# Sequential Dependency Analysis

Answer:

Why can't the model generate all future tokens simultaneously?

Discuss:

* dependency chain
* previous context
* future uncertainty

Minimum:
150 words.

```text
_____________________________________
_____________________________________
_____________________________________
_____________________________________
_____________________________________
```

---

# Engineering Interpretation

Connect this lab to:

## Latency

How does the generation loop affect latency?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

## Throughput

How does repeated decoding affect throughput?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

## KV Cache

Why might KV cache help this generation process?

```text
_____________________________________
_____________________________________
_____________________________________
```

---

# Production Perspective

Imagine:

```text
100,000 users
```

are generating text simultaneously.

Why might this generation loop become expensive?

Discuss:

* compute
* memory
* scheduling
* infrastructure cost

Minimum:
200 words.

```text
_____________________________________
_____________________________________
_____________________________________
_____________________________________
_____________________________________
```

---

# Stretch Challenge Results

If completed:

Describe:

* temperature experiments
* sampling experiments
* alternative prompts
* unexpected behavior

```text
_____________________________________
_____________________________________
_____________________________________
```

---

# Key Takeaways

List FIVE things learned.

### Takeaway 1

```text
_____________________________________
```

### Takeaway 2

```text
_____________________________________
```

### Takeaway 3

```text
_____________________________________
```

### Takeaway 4

```text
_____________________________________
```

### Takeaway 5

```text
_____________________________________
```

---

# Final Reflection

Complete:

```text
Before this lab I thought language models...

After this lab I now understand...
```

Minimum:
150 words.

---

# Instructor Evaluation

| Category                   | Score |
| -------------------------- | ----- |
| Environment Setup          | /10   |
| Technical Accuracy         | /20   |
| Observations               | /20   |
| Engineering Interpretation | /20   |
| Systems Thinking           | /20   |
| Communication Quality      | /10   |

### Total

```text
/100
```

---

# Submission Checklist

* [ ] Lab completed
* [ ] Output recorded
* [ ] Observations documented
* [ ] Reflection completed
* [ ] Engineering analysis included
* [ ] Submitted report

---

# Final Lesson

This lab exists to teach:

```text
Modern language models are repeated next-token prediction systems operating under infrastructure constraints.
```

Understanding that idea is foundational to inference engineering.

---
