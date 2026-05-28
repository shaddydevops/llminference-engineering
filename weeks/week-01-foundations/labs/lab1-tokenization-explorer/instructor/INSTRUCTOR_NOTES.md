# Instructor Notes — Lab 1 Tokenization Explorer

---

# Instructor Overview

This is the first practical lab of the course.

Its purpose is NOT merely to teach:

```text id="jlwmi1"
how to use a tokenizer
```

Its purpose is to fundamentally change how students think about:

* prompts
* inference
* cost
* latency
* memory
* context windows

This lab establishes one of the most important ideas in the entire course:

# tokens are the operational currency of LLM systems.

---

# Teaching Goals

By the end of this lab, students should understand:

* LLMs process tokens, not words
* token count directly affects inference economics
* tokenization behavior varies significantly
* prompt design changes system cost
* inference systems operate under token constraints

Students should begin thinking operationally.

---

# Recommended Session Flow

## Part 1 — Concept Introduction (10–15 min)

Before running code:

Ask students:

> What exactly does a language model receive when you send a prompt?

Most beginners answer:

```text id="jlwmi2"
words
```

This misconception is important.

Introduce:

* tokenization
* token IDs
* subword splitting
* token count economics

---

## Part 2 — Live Demonstration (15–20 min)

Run:

```bash id="jlwmi3"
python code/starter.py
```

Pause frequently.

Do NOT rush.

Ask students:

* Why did this split happen?
* Why are emojis inefficient?
* Why are technical words expensive?
* Why might multilingual systems differ?

The discussion matters more than the code.

---

## Part 3 — Production Framing (10 min)

Connect tokenization to:

* API billing
* context windows
* prefill latency
* KV cache growth
* throughput
* serving cost

Students should realize:

# tokenization affects infrastructure economics.

---

## Part 4 — Student Investigation (20–30 min)

Students should modify prompts themselves.

Encourage experimentation with:

* emojis
* code
* Ghanaian names
* repeated punctuation
* mixed languages
* whitespace
* very long prompts

Curiosity is important.

---

# Key Misconceptions To Correct

## Misconception 1

```text id="jlwmi4"
1 word = 1 token
```

Correct this immediately.

---

## Misconception 2

```text id="jlwmi5"
Tokenization is just preprocessing.
```

Explain that tokenization affects:

* latency
* memory
* cost
* batching
* context utilization

---

## Misconception 3

```text id="jlwmi6"
Long prompts only affect generation length.
```

Clarify:
long prompts increase:

* prefill cost
* attention computation
* KV cache initialization

before generation even begins.

---

# Important Engineering Insight

Students often think:

```text id="jlwmi7"
AI performance depends only on model intelligence.
```

This lab begins teaching:

```text id="jlwmi8"
AI systems are constrained by infrastructure realities.
```

That mindset shift is essential.

---

# Suggested Discussion Prompts

Use questions like:

* Why might emojis increase serving cost?
* Why are tokens a better operational metric than words?
* Why do APIs bill by tokens?
* Why do context windows use token counts?
* Why might multilingual systems be more difficult to optimize?

These discussions elevate the lab from:

```text id="jlwmi9"
coding exercise
```

to:

```text id="jlwmia"
systems reasoning exercise
```

---

# What Strong Students Usually Notice

Advanced students often realize:

* tokenization is inconsistent across text styles
* code tokenization behaves differently
* punctuation affects splitting
* long prompts quickly consume context windows
* token inefficiency scales operational cost

Encourage these observations.

---

# Expected Student Difficulty

Students may struggle with:

* understanding subword tokenization
* distinguishing words vs tokens
* interpreting token IDs
* connecting tokenization to infrastructure

This is normal.

Do not over-focus on exact tokenizer internals.

Focus on:

# operational implications.

---

# Assessment Guidance

Strong submissions should include:

* measured token counts
* comparisons between prompts
* operational reasoning
* production interpretation

Weak submissions usually:

* only paste output
* avoid interpretation
* ignore infrastructure implications

Reward reasoning, not merely execution.

---

# Stretch Challenge Suggestions

Advanced students can investigate:

* multilingual tokenization
* tokenizer differences across models
* token efficiency benchmarking
* code vs natural language tokenization
* prompt compression techniques

These naturally connect to:

* context optimization
* serving efficiency
* inference cost reduction

---

# Connection To Future Weeks

This lab prepares students for:

## Week 2

GPU profiling and throughput analysis

## Week 3

Batching systems

## Week 4

KV cache behavior

## Week 5

Quantization

## Week 6

Speculative decoding

## Week 7

PagedAttention and vLLM

Students should repeatedly connect future concepts back to:

# tokens and context growth.

---

# Instructor Reminder

Do not let students leave believing:

```text id="jlwmib"
tokenization is trivial preprocessing
```

They should leave understanding:

```text id="jlwmic"
tokenization shapes the economics and performance of inference systems.
```

That realization is foundational to the rest of the course.

---
