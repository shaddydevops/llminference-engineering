# Reflection Questions — Lab 2 Build a Tiny Generation Loop

---

# Instructions

Answer these questions thoughtfully.

The purpose is not simply to verify that you ran the code.

The purpose is to develop:

# inference engineering intuition.

Connect your answers to:

* autoregressive generation
* forward passes
* latency
* throughput
* KV cache
* production serving

Avoid one-sentence responses.

---

# Question 1

Before this lab, how did you think language models generated text?

After completing the lab, what changed?

Minimum:
100 words.

---

# Question 2

Why is language generation called:

```text
next-token prediction
```

instead of:

```text
sentence generation
```

Explain using examples from the lab.

---

# Question 3

Why does every generated token require another forward pass?

Discuss:

* logits
* token selection
* sequence growth

---

# Question 4

Suppose a model generates:

```text
500 tokens
```

How many decoding iterations are required?

Why is this operationally important?

---

# Question 5

Why is decoding fundamentally sequential?

Explain why:

```text
Token N + 1
```

depends on:

```text
Token N
```

---

# Question 6

Why can't a model simply generate all future tokens simultaneously?

Discuss:

* uncertainty
* probability distributions
* context dependence

---

# Question 7

During the lab you observed:

```text
input_ids
```

growing continuously.

Why does sequence growth matter?

Discuss:

* context length
* memory usage
* compute requirements

---

# Question 8

How does this generation loop help explain:

* latency
* throughput bottlenecks

in production systems?

---

# Question 9

Why might repeated forward passes become expensive when:

```text
100,000 users
```

are generating text simultaneously?

Discuss:

* GPU utilization
* memory pressure
* scheduling complexity

---

# Question 10

How does this lab help justify the existence of:

* KV cache
* speculative decoding
* batching systems
* vLLM

Even if you do not fully understand those technologies yet.

---

# Systems Thinking Challenge

Complete:

```text
A language model is not primarily a chatbot.
It is...
```

Minimum:
5 sentences.

---

# Production Scenario

Imagine you are serving:

```text
10 million requests per day
```

Why would understanding the generation loop be important for:

* infrastructure cost
* scalability
* latency optimization

Minimum:
150 words.

---

# Final Reflection

Complete the statement:

```text
The single most important thing I learned from this lab was...
```

Explain why.

Minimum:
100 words.

---

# Key Lesson

This lab is successful if you leave understanding:

```text
Every generated token requires another prediction step.
```

That simple idea explains a large portion of modern inference engineering.

---
