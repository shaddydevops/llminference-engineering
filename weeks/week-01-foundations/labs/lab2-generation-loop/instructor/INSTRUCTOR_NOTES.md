# Instructor Notes — Lab 2 Build a Tiny Generation Loop

---

# Instructor Overview

This is one of the most important labs in the entire course.

Students move from:

```text
LLMs feel magical
```

to:

```text
LLMs are repeated next-token prediction systems
```

This shift is foundational.

Many future concepts become dramatically easier once students understand:

* autoregressive generation
* forward passes
* logits
* sequence growth
* sequential dependency

---

# Teaching Goal

The primary objective is NOT:

```text
learning PyTorch code
```

The primary objective is:

```text
understanding how language models actually generate text
```

Students should leave understanding:

* why decoding is sequential
* why generation is expensive
* why latency exists
* why KV cache matters
* why speculative decoding exists

---

# Learning Outcomes

By the end of this lab, students should be able to explain:

## Conceptually

* what a forward pass is
* what logits are
* how next-token prediction works
* how generation loops operate

## Operationally

* why generation creates latency
* why long outputs are expensive
* why decode scales poorly
* why inference optimization is difficult

---

# Recommended Teaching Flow

## Part 1 — Prediction Exercise (10 minutes)

Before running any code:

Ask:

> How does ChatGPT generate a response?

Most students answer:

```text
It writes a sentence.
```

or

```text
It predicts the answer.
```

Keep asking:

```text
How?
```

until someone reaches:

```text
It predicts the next word.
```

Then introduce:

```text
token
```

instead of:

```text
word
```

This sets up the lab perfectly.

---

## Part 2 — Demonstration (15 minutes)

Run:

```bash
python code/solution.py
```

Pause frequently.

After every generation step ask:

```text
What just happened?
```

Students should eventually answer:

```text
The model predicted one token.
```

Repeat this idea continuously.

---

# Important Teaching Moment

When students see:

```python
outputs = model(input_ids=input_ids)
```

stop.

Explain:

This single line represents:

* embeddings
* attention
* feed-forward layers
* logits generation

This is:

# the transformer forward pass.

Many students miss how significant this line is.

---

# Explaining Logits

Students often struggle here.

Use this analogy:

Imagine:

```text
150,000 possible next tokens
```

The model assigns a score to each one.

Example:

| Token  | Score |
| ------ | ----- |
| Accra  | 9.8   |
| Kumasi | 7.1   |
| Banana | -3.2  |

Those scores are:

```text
logits
```

The model has not chosen yet.

It is evaluating possibilities.

---

# Explaining Greedy Decoding

Show:

```python
torch.argmax(...)
```

Explain:

```text
Choose the highest-scoring candidate.
```

Then discuss limitations:

* repetitive outputs
* lack of creativity
* deterministic behavior

This creates a natural bridge to:

* temperature
* top-k
* top-p

later.

---

# Critical Insight

Students should notice:

```text
forward pass
→ token

forward pass
→ token

forward pass
→ token
```

This repetition is the heart of inference.

Write this on a whiteboard if teaching live.

---

# Common Student Misconceptions

## Misconception 1

```text
The model generates sentences.
```

Correction:

```text
The model generates tokens.
```

---

## Misconception 2

```text
Generation happens all at once.
```

Correction:

```text
Generation happens sequentially.
```

---

## Misconception 3

```text
Future tokens already exist.
```

Correction:

Future tokens are unknown.

They must be predicted.

---

## Misconception 4

```text
More compute automatically solves inference.
```

Correction:

Sequential dependency limits scaling.

This becomes important later.

---

# Discussion Prompts

Ask:

### Question

Why can't the model generate:

```text
Token 500
```

before generating:

```text
Token 1
```

---

### Question

Why might this be expensive at scale?

---

### Question

Why might caching become useful?

---

### Question

Why might batching become difficult?

---

# Connecting To Future Weeks

This lab lays the foundation for:

## Week 2

Benchmarking

Students now understand what they are measuring.

---

## Week 3

Batching

Students understand generation workloads.

---

## Week 4

KV Cache

Students understand repeated computation.

---

## Week 5

Quantization

Students understand forward pass cost.

---

## Week 6

Speculative Decoding

Students understand decode bottlenecks.

---

## Week 7

vLLM + PagedAttention

Students understand why serving systems exist.

---

# Assessment Guidance

Strong students explain:

```text
why
```

Weak students explain:

```text
what happened
```

Reward:

* reasoning
* interpretation
* systems thinking

more than:

* copied output

---

# Stretch Challenge Ideas

Advanced students can:

## Compare

* greedy decoding
* temperature sampling

---

## Measure

* generation speed
* prompt length effects

---

## Investigate

* logits distribution
* token probabilities
* confidence levels

---

# Instructor Checklist

By the end of class students should understand:

* [ ] next-token prediction
* [ ] logits
* [ ] forward passes
* [ ] sequence growth
* [ ] autoregressive generation
* [ ] sequential dependency
* [ ] why decoding is expensive

If students understand these concepts:

# the lab succeeded.

---

# Final Teaching Message

The most important lesson from this lab is:

```text
Modern language models are repeated next-token prediction engines.
```

Everything else:

* latency
* throughput
* KV cache
* speculative decoding
* batching
* vLLM

exists because of that simple reality.

---
