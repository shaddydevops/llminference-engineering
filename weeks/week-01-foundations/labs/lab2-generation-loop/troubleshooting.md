# Troubleshooting — Lab 2 Build a Tiny Generation Loop

---

# Philosophy

This lab intentionally exposes students to the mechanics of inference.

Because we are working closer to the model internals, students may encounter:

* memory issues
* slow execution
* tensor shape confusion
* decoding mistakes

These are valuable learning opportunities.

Inference engineering is often:

# understanding why systems behave the way they do.

---

# Problem: Model Loading Is Slow

Example:

```text
Loading checkpoint shards...
```

appears to take a long time.

## Cause

The model is downloading from Hugging Face or loading weights into memory.

## Fix

Wait for the initial load.

Subsequent runs should be significantly faster because:

* files are cached
* weights are stored locally

---

# Problem: Out of Memory (OOM)

Example:

```text
CUDA out of memory
```

## Cause

Insufficient GPU memory.

Even small models require:

* model weights
* activations
* temporary tensors

## Fix Options

### Run on CPU

```python
device = "cpu"
```

### Reduce Generation Length

Reduce:

```python
max_new_tokens = 20
```

to:

```python
max_new_tokens = 5
```

### Close Other Applications

Check:

```bash
nvidia-smi
```

and terminate unnecessary GPU workloads.

---

# Problem: Tensor Shape Confusion

Students often see:

```python
outputs.logits.shape
```

and become confused.

Example:

```text
torch.Size([1, 5, 151936])
```

## Interpretation

```text
Dimension 1:
Batch Size

Dimension 2:
Sequence Length

Dimension 3:
Vocabulary Size
```

Think:

```text
(batch,
 tokens,
 vocabulary)
```

---

# Problem: Model Generates Repetitive Text

Example:

```text
The capital of Ghana is Accra Accra Accra Accra...
```

## Cause

Greedy decoding always selects:

```python
torch.argmax(...)
```

which may repeatedly choose the same token.

## Why This Happens

Greedy decoding prioritizes:

* certainty
* determinism

but sacrifices:

* diversity
* creativity

This behavior is expected.

---

# Problem: Generated Text Looks Strange

Example:

```text
The capital of Ghana is . . . . .
```

## Cause

Small models may:

* make mistakes
* generate repetitive punctuation
* produce unstable continuations

Remember:

This lab focuses on:

# generation mechanics

not model quality.

---

# Problem: Sequence Length Keeps Growing

Students often ask:

```text
Why does the sequence keep getting longer?
```

## Explanation

Every generated token becomes part of future context.

Example:

```text
Prompt:
The capital of Ghana is
```

After generation:

```text
The capital of Ghana is Accra
```

Now:

```text
Accra
```

becomes part of the next prediction.

This is autoregressive generation.

---

# Problem: Generation Feels Slow

Students often expect:

```text
The model should generate everything instantly.
```

## Reality

Generation works like:

```text
Forward Pass
→ Next Token

Forward Pass
→ Next Token

Forward Pass
→ Next Token
```

This repeats continuously.

Even short outputs require many computations.

---

# Problem: Why Can't The Model Generate All Tokens At Once?

This is one of the most important questions in the course.

## Explanation

Future tokens do not yet exist.

Example:

```text
The capital of Ghana is
```

Before predicting:

```text
Accra
```

the model cannot know:

```text
Accra
```

exists.

Generation therefore depends on:

# previous outputs.

This creates a sequential dependency.

---

# Problem: Why Is Decode Hard To Parallelize?

Because generation depends on:

```text
Token N
```

before producing:

```text
Token N+1
```

This dependency chain limits parallelism.

Many modern inference optimizations attempt to reduce this bottleneck.

---

# Problem: CPU Execution Is Extremely Slow

## Cause

Transformers contain:

* billions of operations
* large matrix multiplications
* heavy memory movement

CPUs can run inference.

GPUs run inference much faster.

## Fix

Use:

* local GPU
* Google Colab GPU
* cloud GPU

when available.

---

# Diagnostic Commands

Check GPU:

```bash
nvidia-smi
```

Check RAM:

```bash
free -h
```

Check Python:

```bash
python --version
```

Check installed packages:

```bash
pip list
```

---

# Engineering Insight

This lab intentionally exposes:

```text
the inner generation loop
```

that powers all modern LLMs.

The purpose is not merely to generate text.

The purpose is to understand:

* why decoding is sequential
* why inference is expensive
* why KV cache exists
* why speculative decoding matters

---

# If Everything Fails

Try:

1. Restart Python kernel
2. Recreate virtual environment
3. Reinstall dependencies
4. Reduce model size
5. Use CPU temporarily
6. Try Google Colab

Professional engineers do these routinely.

---

# Final Lesson

If students leave this lab understanding:

```text
LLMs generate text one token at a time through repeated forward passes
```

then the lab has succeeded.

That single idea explains a huge portion of modern inference engineering.

---
