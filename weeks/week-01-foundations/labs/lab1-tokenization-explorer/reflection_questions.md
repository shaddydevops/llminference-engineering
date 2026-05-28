# Reflection Questions — Lab 1 Tokenization Explorer

---

# Instructions

Answer these questions thoughtfully.

The goal is not memorization.

The goal is:

# developing inference engineering intuition.

Your answers should connect:

* observations
* tokenization behavior
* operational implications
* production systems thinking

Avoid one-line answers.

---

# Question 1

What surprised you most about how the tokenizer split text?

Did any words tokenize differently than expected?

Why do you think that happened?

---

# Question 2

Why is token count more operationally important than word count in LLM systems?

Discuss:

* latency
* cost
* memory usage
* context windows

---

# Question 3

Which text sample appeared least token-efficient?

Why might that matter in production systems?

Consider:

* emojis
* code
* technical jargon
* multilingual text

---

# Question 4

Why do longer prompts generally increase:

* prefill cost
* latency
* memory usage

Explain using concepts from the Week 1 handbook.

---

# Question 5

Suppose an API receives:

```text id="jlwmr1"
10 million prompts/day
```

Why could even a small increase in average token count become economically important?

Discuss:

* infrastructure scaling
* GPU utilization
* serving cost

---

# Question 6

Why are context windows measured in:

```text id="jlwmr2"
tokens
```

instead of:

```text id="jlwmr3"
words
```

What operational problems would occur if engineers ignored token counts?

---

# Question 7

Why might multilingual systems experience different serving costs across languages?

Hint:
Different languages tokenize differently.

---

# Question 8

Why do inference engineers care about token efficiency?

Connect your answer to:

* throughput
* batching
* TTFT
* KV cache growth

---

# Question 9

Suppose two prompts contain the same meaning:

## Prompt A

```text id="jlwmr4"
Explain inference.
```

## Prompt B

```text id="jlwmr5"
Please provide a comprehensive and detailed explanation of transformer-based autoregressive inference systems and their operational infrastructure implications.
```

Why does Prompt B likely cost more operationally?

---

# Question 10

Complete this statement:

```text id="jlwmr6"
Tokens are important because...
```

Write at least:

* 5 sentences
* using engineering reasoning

---

# Stretch Reflection

After completing this lab, how has your understanding changed regarding:

```text id="jlwmr7"
what a language model actually processes
```

compared to what you believed before?

---

# Final Engineering Reflection

This course repeatedly emphasizes:

```text id="jlwmr8"
LLMs are infrastructure systems operating under hardware constraints.
```

Explain how tokenization supports that idea.

Use examples from:

* latency
* memory
* context windows
* serving economics

---
