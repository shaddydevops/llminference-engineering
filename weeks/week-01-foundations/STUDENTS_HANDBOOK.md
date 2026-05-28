# Week 1 — Foundations of LLM Inference
## Production LLM Inference Engineering

---

# Introduction

Most people interact with large language models through polished chat interfaces.

A user types a message.

A response appears.

The process feels instantaneous, intelligent, and almost magical.

But underneath that interaction is one of the most computationally demanding software systems ever deployed at scale.

Modern language models are not “thinking.”

They are executing massive probabilistic inference workloads across highly optimized GPU systems under strict latency and memory constraints.

This course is about understanding those systems.

Not from the perspective of:
- prompt engineering
- chatbot wrappers
- AI hype
- productivity tooling

but from the perspective of:
- inference infrastructure
- GPU execution
- memory systems
- scheduling
- optimization
- production engineering

---

# Why This Course Exists

Most AI education today focuses on model usage.

Very little focuses on:
- how inference actually works
- why serving models is expensive
- how modern inference stacks are optimized
- why systems like vLLM exist
- why KV cache matters
- why batching changes economics
- why latency engineering dominates production deployments

As a result, many developers can call an API but cannot explain:
- why the first token is slow
- why context length affects memory
- why throughput and latency conflict
- why GPUs run out of memory
- why quantization matters
- why serving infrastructure is difficult

This course addresses that gap.

---

# The Central Thesis of This Course

Large language model inference is fundamentally:
## a systems engineering problem.

Not a prompting problem.

Not a frontend problem.

Not a wrapper-framework problem.

Inference engineering sits at the intersection of:
- distributed systems
- GPU architecture
- memory management
- scheduling theory
- probabilistic modeling
- infrastructure optimization

The goal of this course is to help students think like inference engineers.

---

# What Students Will Learn

By the end of this course, students should understand:

## Conceptually
- how transformer inference works
- why token generation is autoregressive
- how KV cache changes computational complexity
- why memory bandwidth matters
- why batching improves throughput
- why latency optimization is difficult

## Practically
- benchmark inference systems
- deploy vLLM servers
- profile GPU workloads
- optimize inference pipelines
- implement quantization workflows
- evaluate speculative decoding systems
- interpret serving metrics

## Professionally
- reason about infrastructure tradeoffs
- debug inference bottlenecks
- evaluate deployment architectures
- understand production serving constraints
- communicate performance findings clearly

---

# How This Course Is Structured

This course progresses from:
## conceptual foundations
to
## production-grade infrastructure engineering.

The sequence is intentional.

Students first learn:
- what inference is
- how token generation works
- why latency exists
- how memory behaves

before moving into:
- batching
- scheduling
- vLLM
- quantization
- FlashAttention
- speculative decoding

This mirrors how professional understanding develops.

---

# A Different Way To Think About LLMs

Most people describe language models as:
> “AI systems that generate text.”

This course instead frames them as:

> Large-scale probabilistic token inference systems optimized under memory and latency constraints.

That framing matters.

Because once inference is viewed as a systems problem, many engineering decisions begin to make sense:
- why GPUs dominate
- why memory becomes the bottleneck
- why batching matters
- why KV cache exists
- why quantization reduces costs
- why inference infrastructure is expensive

---

# The Real Cost of a Token

One of the most important realizations students should develop is this:

## Tokens are not free.

Every generated token requires:
- GPU computation
- memory reads/writes
- attention operations
- scheduling decisions
- cache management
- network overhead
- infrastructure coordination

At scale, even small inefficiencies become extremely expensive.

A 5% improvement in inference efficiency can translate into millions of dollars in infrastructure savings for large deployments.

This is why inference optimization matters.

---

# What Week 1 Focuses On

Week 1 builds the conceptual foundation for the rest of the course.

Students will learn:
- what inference actually means
- how tokenization works
- how generation loops operate
- why prefill and decode differ
- how latency emerges
- why memory dominates serving systems

These ideas are foundational.

Without them:
- vLLM becomes confusing
- batching becomes abstract
- FlashAttention becomes meaningless
- quantization feels arbitrary

Week 1 therefore establishes the mental models required for the entire course.

---

# Engineering Mindset

Throughout this course, students should repeatedly ask:

## What is the bottleneck?
## What resource is constrained?
## What tradeoff is being made?
## What metric is being optimized?
## What operational cost exists?

These questions define inference engineering.

---

# Important Philosophy

This course prioritizes:
- depth over hype
- understanding over memorization
- systems thinking over tooling familiarity
- engineering reasoning over copy-paste workflows

Students are encouraged to:
- investigate
- benchmark
- profile
- experiment
- debug
- question assumptions

That mindset is essential for becoming a strong infrastructure engineer.

---

# Final Thought

Modern AI systems are often presented as magic.

But behind every generated token is:
- infrastructure
- optimization
- scheduling
- memory management
- GPU execution
- engineering tradeoffs

Understanding those systems is what this course is about.

Welcome to Production LLM Inference Engineering.



---

# What Is Inference?

The word “inference” is used constantly in AI discussions, but it is often poorly understood.

In practical terms, inference refers to:
## using a trained model to produce predictions.

For large language models, inference means:
> taking input tokens and generating output tokens.

That sounds simple.

Operationally, it is not.

Modern inference systems execute billions or trillions of mathematical operations while attempting to satisfy strict production constraints around:
- latency
- throughput
- memory usage
- concurrency
- reliability
- infrastructure cost

Understanding inference is the foundation of this course.

---

# Training vs Inference

One of the most important distinctions in machine learning systems is the difference between:
- training
- inference

These workloads behave very differently.

---

# Training

Training is the process of:
## adjusting model parameters.

During training:
- gradients are computed
- weights are updated
- backpropagation occurs
- optimization algorithms run repeatedly

Training is computationally expensive because the system must:
- store activations
- compute gradients
- propagate errors backward
- update billions of parameters

Training is about:
## learning.

---

# Inference

Inference is different.

During inference:
- weights are fixed
- gradients are not computed
- no learning occurs
- the model only performs forward passes

Inference is about:
## prediction.

The system receives:
- a prompt
- input tokens
- prior context

and predicts:
- the next token probability distribution.

That process repeats autoregressively until generation stops.

---

# Why Inference Matters More Than Most People Realize

Many people assume training is the primary engineering challenge in AI.

In reality:
## inference often dominates operational cost.

Why?

Because training may happen:
- once
- occasionally
- periodically

But inference happens:
- continuously
- for every user
- at production scale
- under latency constraints

For large consumer systems:
- millions of inference requests occur daily
- latency directly affects user experience
- infrastructure costs scale with usage

As a result:
## efficient inference becomes economically critical.

---

# The Core Inference Loop

At a high level, language model inference follows this cycle:

```text
Input Prompt
    ↓
Tokenization
    ↓
Transformer Forward Pass
    ↓
Logits Generation
    ↓
Sampling
    ↓
Next Token Selection
    ↓
Append Token To Context
    ↓
Repeat
