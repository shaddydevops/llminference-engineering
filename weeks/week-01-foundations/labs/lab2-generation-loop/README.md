# Lab 2 — Build a Tiny Generation Loop

## Week 1: Foundations of LLM Inference

---

# Lab Goal

In this lab, you will manually implement a simplified token-by-token generation loop.

This is one of the most important labs in the course because students finally see:

# how language models actually generate text.

Most people interact with LLMs through:

* chat interfaces
* APIs
* frameworks

Very few understand the actual mechanics underneath.

This lab removes the abstraction.

---

# Why This Lab Matters

Modern language models are:

# autoregressive systems.

They generate:

* one token at a time
* sequentially
* repeatedly

This repeated generation loop drives:

* latency
* throughput
* GPU utilization
* scheduler complexity
* KV cache behavior

Understanding the generation loop is foundational to:

* inference optimization
* speculative decoding
* batching systems
* production serving

---

# Core Concepts

You will practice:

* running forward passes manually
* inspecting logits
* selecting next tokens
* appending generated tokens
* understanding autoregressive decoding
* observing sequential generation behavior

---

# What Is Actually Happening During Generation?

Suppose the prompt is:

```text id="djlwm2"
The capital of Ghana is
```

The model predicts:

```text id="djlwm3"
Accra
```

Now the sequence becomes:

```text id="djlwm4"
The capital of Ghana is Accra
```

The model then predicts:
the NEXT token.

This repeats:

* token
* by
* token

until stopping conditions are reached.

This loop is the core of transformer inference.

---

# Important Realization

The model does NOT:

```text id="djlwm5"
generate the whole sentence at once
```

Instead:
it repeatedly performs:

# next-token prediction.

This is one reason decode is difficult to parallelize.

Future tokens do not yet exist.

---

# Files In This Lab

```text id="djlwm6"
lab2-generation-loop/
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

# Recommended Environment

This lab can run on:

* CPU
* local Ubuntu laptop
* Google Colab

GPU is helpful but not required.

A small model is intentionally used.

---

# Default Model

We use:

```text id="djlwm7"
Qwen/Qwen2.5-0.5B-Instruct
```

Why?

* lightweight enough for beginner hardware
* modern architecture
* fast experimentation
* aligned with later course sections

---

# Setup

Install dependencies:

```bash id="djlwm8"
pip install -r requirements.txt
```

---

# Lab Overview

You will:

1. Load tokenizer and model
2. Encode a prompt
3. Run a forward pass
4. Extract logits
5. Select next token
6. Append token to sequence
7. Repeat generation loop

This recreates the core logic underlying LLM text generation.

---

# Task 1 — Load Model and Tokenizer

Students should:

* load tokenizer
* load causal language model
* inspect vocabulary size
* inspect model type

Goal:
understand the inference stack components.

---

# Task 2 — Encode Prompt

Convert raw text into:

* token IDs
* tensors

This demonstrates how text becomes model input.

---

# Task 3 — Run Forward Pass

Run the model manually:

```python id="djlwm9"
outputs = model(input_ids=input_ids)
```

This is the transformer forward pass.

Students should inspect:

* logits shape
* tensor dimensions
* output structure

---

# Task 4 — Extract Next-Token Logits

The model outputs:

# probability scores for every vocabulary token.

Students should inspect:

```python id="djlwm10"
outputs.logits
```

and identify:

* vocabulary dimension
* sequence dimension

---

# Task 5 — Select Next Token

Use:

```python id="djlwm11"
torch.argmax(...)
```

to select the most likely token.

This implements:

# greedy decoding.

Students should realize:
generation is fundamentally:

## repeated probability selection.

---

# Task 6 — Append Generated Token

Append the generated token back into:

```text id="djlwm12"
input_ids
```

This grows the sequence.

The model then uses:

* previous prompt
* newly generated tokens

to predict the next token.

---

# Task 7 — Repeat Generation Loop

Repeat:

* forward pass
* logits extraction
* token selection
* append

multiple times.

Students should watch:

# text emerge progressively.

This is one of the most important moments in the course.

---

# Important Engineering Insight

The model repeatedly performs:

# full forward passes during generation.

This explains why inference is expensive.

Even short responses may require:

* dozens
* hundreds
* thousands

of forward computations.

---

# Why This Matters Operationally

This generation loop drives:

* decode latency
* throughput bottlenecks
* scheduler complexity
* KV cache usage

Every optimization later in the course attempts to improve:

# this loop.

---

# Key Concept: Sequential Dependency

Token generation is sequential because:

```text id="djlwm13"
future tokens depend on previous tokens
```

This creates:

* decode bottlenecks
* limited parallelism
* scheduling challenges

This is why speculative decoding becomes valuable later.

---

# Expected Student Outcome

Students should leave this lab understanding:

* how logits drive generation
* how next-token prediction works
* why decoding is sequential
* why forward passes repeat continuously
* why inference optimization is difficult

This conceptual breakthrough is essential.

---

# Stretch Challenge

Students can experiment with:

* temperature sampling
* top-k sampling
* top-p sampling
* longer prompts
* different decoding strategies

Observe how generation changes.

---

# Deliverable

Submit:

```text id="djlwm14"
reports/lab2_report.md
```

including:

* screenshots/output
* observations
* operational reasoning
* reflection answers

---

# Final Lesson

Modern language models fundamentally operate through:

# repeated next-token prediction loops.

Understanding that loop is one of the most important conceptual milestones in inference engineering.

---
