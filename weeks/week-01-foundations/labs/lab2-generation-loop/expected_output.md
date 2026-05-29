# Expected Output — Lab 2 Build a Tiny Generation Loop

---

# Important Note

Your generated text will NOT match other students exactly.

Why?

Because generation depends on:

* model version
* decoding strategy
* temperature
* tokenizer version
* random seed
* hardware environment

The goal is NOT identical output.

The goal is:

# understanding autoregressive generation.

---

# What Success Looks Like

A successful run should:

1. Load tokenizer and model
2. Encode the prompt
3. Run repeated forward passes
4. Generate tokens one at a time
5. Grow the sequence continuously
6. Produce readable output

---

# Example Console Output

You should see something similar to:

```text
================================================================================
LOADING MODEL
================================================================================

Original Prompt:
The capital of Ghana is

Initial Input Shape:
torch.Size([1, 5])

Initial Token Count:
5
```

---

# First Forward Pass

Example:

```text
Logits Tensor Shape:

torch.Size([1, 5, 151936])
```

Interpretation:

```text
Batch Size = 1
Sequence Length = 5
Vocabulary Size = 151936
```

The exact vocabulary size may differ.

---

# Example Generation Loop

```text
--------------------------------------------------------------------------------
STEP 1

New Token ID:
10234

Current Sequence Length:
6

Generated Text:
The capital of Ghana is Accra
```

---

```text
--------------------------------------------------------------------------------
STEP 2

New Token ID:
534

Current Sequence Length:
7

Generated Text:
The capital of Ghana is Accra .
```

---

```text
--------------------------------------------------------------------------------
STEP 3

Generated Text:
The capital of Ghana is Accra . It
```

The exact text will vary.

What matters is that:

# sequence length increases every iteration.

---

# Key Observation

Students should notice:

```text
Every generated token requires another forward pass.
```

This is one of the most important lessons in the course.

---

# Sequence Growth

Example:

| Step           | Sequence Length |
| -------------- | --------------: |
| Initial Prompt |               5 |
| Step 1         |               6 |
| Step 2         |               7 |
| Step 3         |               8 |
| Step 10        |              15 |
| Step 20        |              25 |

Notice:

```text
1 generated token
=
1 additional sequence position
```

---

# Why This Matters

Every additional token requires:

* another forward pass
* another logits computation
* another token selection step

This creates:

```text
Sequential dependency
```

which limits parallelism.

---

# Engineering Insight #1

Students should realize:

```text
The model is not writing sentences.
```

Instead:

```text
The model repeatedly predicts the next token.
```

Everything else emerges from this process.

---

# Engineering Insight #2

Generation is expensive because:

```text
Forward Pass
→ Next Token
→ Forward Pass
→ Next Token
→ Forward Pass
→ Next Token
```

This repeats continuously.

Even short responses may require dozens of forward passes.

---

# Engineering Insight #3

This generation loop explains:

* decode latency
* throughput bottlenecks
* scheduler complexity
* KV cache importance

Most later optimizations exist to improve:

# this loop.

---

# Common Student Observations

Students often notice:

## Observation 1

```text
Generation feels repetitive.
```

Correct.

The system is repeating the same process continuously.

---

## Observation 2

```text
The sequence keeps getting longer.
```

Correct.

Every generated token becomes part of future context.

---

## Observation 3

```text
Generation is slower than expected.
```

Correct.

Each token requires:

* compute
* memory movement
* attention operations

---

# Stretch Challenge Expectations

Students experimenting with:

## Temperature

Should notice:

```text
Higher temperature
=
more randomness
```

---

## Greedy Decoding

Should notice:

```text
More deterministic output
```

---

## Longer Prompts

Should notice:

```text
More prefill work
```

before generation begins.

---

# What Strong Analysis Looks Like

Strong answer:

```text
The generation loop revealed that every token requires another forward pass.
This explains why decoding is sequential and why inference systems invest heavily in KV caching and speculative decoding.
```

Weak answer:

```text
The model generated text.
```

---

# Operational Takeaway

Modern inference systems are fundamentally:

```text
Repeated next-token prediction engines.
```

Understanding that idea is essential for:

* batching
* scheduling
* speculative decoding
* KV cache systems
* vLLM
* production inference optimization

---

# Final Lesson

The most important realization from this lab is:

```text
Language models do not generate responses all at once.
```

They generate:

```text
one token
at a time
through repeated forward passes
```

This simple fact drives many of the challenges and innovations in modern inference engineering.

---
