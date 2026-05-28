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


---

# Why Inference Is Expensive

One of the biggest misconceptions in modern AI is the assumption that:
> generating text is computationally cheap.

From the user’s perspective, a language model appears simple:
- type prompt
- receive answer

But underneath that interaction is a highly optimized distributed inference system performing enormous amounts of computation and memory movement.

Modern inference systems are expensive because every generated token requires:
- matrix multiplications
- attention operations
- memory reads/writes
- cache management
- scheduling decisions
- GPU coordination

At scale, these costs compound rapidly.

Understanding where these costs come from is essential for inference engineering.

---

# The Hidden Complexity Behind a Token

A single generated token may require:
- billions of floating point operations
- access to large parameter tensors
- movement of activations across GPU memory
- attention computations over prior context

For small models this is manageable.

For frontier-scale models:
- parameter counts reach hundreds of billions
- context windows become extremely large
- concurrency grows massively

As a result:
## inference becomes an infrastructure problem.

---

# FLOPs and Computational Cost

Inference workloads are dominated by:
# tensor operations.

Particularly:
- matrix multiplications
- attention calculations

These operations are computationally intensive because transformer architectures repeatedly multiply very large matrices.

For example:
- embeddings
- projection matrices
- attention tensors
- feed-forward layers

all require substantial compute.

This is why GPUs dominate inference systems.

---

# Why GPUs Matter

CPUs are optimized for:
- low-latency sequential tasks
- operating system workloads
- branching logic

GPUs are optimized for:
- massive parallelism
- tensor arithmetic
- matrix operations
- high-throughput computation

Transformers map extremely well to GPU architectures because many operations can execute in parallel.

Without GPUs:
- inference latency would become impractical
- throughput would collapse
- serving costs would become enormous

---

# Compute vs Memory

An important realization for inference engineers is:

## inference is often memory-bound rather than compute-bound.

This surprises many beginners.

The issue is not always:
> “the GPU is too slow.”

Often the issue is:
> “memory movement is too expensive.”

Modern GPUs can execute arithmetic extremely quickly.

But repeatedly moving:
- weights
- activations
- KV cache tensors

through memory hierarchies becomes a bottleneck.

This is why:
- memory bandwidth matters enormously
- KV cache optimization matters
- FlashAttention matters
- PagedAttention exists

---

# Memory Bandwidth

Memory bandwidth refers to:
## how quickly data can move through memory systems.

Inference repeatedly transfers:
- parameters
- activations
- attention tensors
- cache states

between:
- VRAM
- caches
- compute units

If memory movement becomes slow:
- GPUs sit idle waiting for data
- throughput drops
- latency increases

This is one of the central engineering challenges in modern inference systems.

---

# VRAM Pressure

Large language models require enormous amounts of memory.

Memory is consumed by:
- model weights
- activations
- KV cache
- batching overhead
- temporary tensors

As context windows increase:
## KV cache memory grows significantly.

As concurrency increases:
## memory pressure increases further.

This creates operational constraints around:
- maximum batch size
- maximum context length
- concurrency limits

Inference engineering is therefore heavily constrained by VRAM capacity.

---

# Why Context Length Is Expensive

Many users assume long prompts are inexpensive.

Operationally:
they are costly.

Longer context means:
- more attention operations
- larger KV caches
- more memory reads
- longer prefill computation

This directly impacts:
- latency
- throughput
- memory usage

As context windows scale into:
- tens of thousands
- or hundreds of thousands of tokens

efficient memory management becomes critical.

---

# Attention Complexity

Attention mechanisms are computationally expensive because:
each token must attend to prior tokens.

Naively:
this scales quadratically with sequence length.

This means:
- doubling context length can dramatically increase computation
- long prompts become increasingly expensive

Modern optimization techniques exist largely to reduce these costs.

Examples include:
- FlashAttention
- KV cache reuse
- sliding window attention
- grouped-query attention

These will appear later in the course.

---

# Why The First Token Is Slow

One of the most important operational metrics is:
# Time To First Token (TTFT)

The first generated token is often significantly slower than subsequent tokens.

Why?

Because before generation begins, the system must:
- tokenize the prompt
- run prefill computation
- initialize attention states
- populate KV cache
- process the full input context

This initial computation is expensive.

Later decode steps become cheaper because:
- KV cache avoids recomputation
- only the newest token is processed

This distinction becomes foundational later in the course.

---

# Throughput vs Latency

Inference systems constantly balance:
- latency
- throughput

These metrics often conflict.

For example:
- larger batches improve throughput
- but increase waiting time for individual users

This creates engineering tradeoffs.

Production serving systems therefore optimize carefully depending on:
- workload type
- concurrency patterns
- SLA requirements
- infrastructure costs

There is rarely a perfect configuration.

---

# Why Inference Optimization Exists

Inference optimization techniques exist because:
## naive inference is economically inefficient.

Without optimization:
- GPUs are underutilized
- memory is wasted
- latency becomes excessive
- throughput remains low
- serving costs increase dramatically

Modern systems therefore rely on:
- batching
- KV caching
- quantization
- speculative decoding
- optimized attention kernels
- scheduling algorithms

This course explores each of these deeply.

---

# The Economics of Inference

At production scale:
small inefficiencies become extremely expensive.

Consider:
- millions of users
- billions of generated tokens
- thousands of GPUs

A small improvement in:
- latency
- memory efficiency
- throughput

can save enormous amounts of money.

This is why companies invest heavily in inference optimization research.

Inference engineering is not merely academic.

It has direct economic impact.

---

# Operational Reality

Production inference systems must simultaneously manage:
- hardware limits
- user demand
- latency expectations
- reliability
- scaling
- infrastructure cost

This is why inference engineering increasingly resembles:
# distributed systems engineering.

The challenge is not simply generating text.

The challenge is generating text:
- quickly
- reliably
- cheaply
- at scale

---

# Key Takeaways

Students should now understand:

- inference is computationally expensive
- GPUs dominate because transformers require massive parallel computation
- memory movement is often the real bottleneck
- VRAM capacity constrains serving systems
- long context windows increase operational cost
- attention operations are expensive
- TTFT emerges from expensive prefill computation
- latency and throughput often conflict
- optimization exists because naive inference is inefficient

These ideas form the operational foundation for everything later in the course.

---


# Tokenization

Before a language model can process text, the text must first be transformed into a numerical representation.

Language models do not directly understand:

* words
* sentences
* grammar
* meaning

They operate on:

# tokens.

Tokenization is the process of converting raw text into these token units.

This step is foundational to modern language model systems.

---

# Why Tokenization Exists

Neural networks operate on numbers.

Not raw language.

Therefore:
human-readable text must first be transformed into discrete numerical representations before inference can occur.

This transformation pipeline typically looks like:

```text
Raw Text
    ↓
Tokenization
    ↓
Token IDs
    ↓
Embeddings
    ↓
Transformer Processing
```

Without tokenization:
transformers cannot operate on language.

---

# What Is a Token?

A token is a unit of text representation used by the model.

Depending on the tokenizer, a token may represent:

* an entire word
* part of a word
* punctuation
* whitespace
* symbols
* even fragments of words

For example:

```text
"unbelievable"
```

might tokenize into:

```text
["un", "believ", "able"]
```

Different tokenizers may split text differently.

This matters operationally.

---

# Tokens vs Words

One of the most common beginner mistakes is assuming:

> 1 token = 1 word.

This is incorrect.

In practice:

* some words become multiple tokens
* some tokens represent punctuation
* some tokens represent spaces
* some tokens are extremely short fragments

For English:
a rough approximation is:

```text
1 token ≈ 0.75 words
```

But this varies significantly.

---

# Why Token Count Matters

In production systems:

## tokens are the real computational unit.

Not words.

Inference cost scales largely with:

* input token count
* output token count
* context length

This means:
longer prompts cost more.

Every additional token increases:

* memory usage
* attention computation
* latency
* infrastructure cost

This is why:
token efficiency matters operationally.

---

# Vocabulary

Every tokenizer has a:

# vocabulary.

The vocabulary is the set of all tokens recognized by the model.

Modern vocabularies may contain:

* tens of thousands
* or hundreds of thousands

of token entries.

For example:
a tokenizer may contain tokens for:

* common words
* punctuation
* programming syntax
* multilingual text
* whitespace patterns

Each token is assigned:

# a unique integer ID.

---

# Token IDs

After tokenization, tokens are converted into:

# token IDs.

Example:

```text
"Hello world"
```

might become:

```text
[15496, 995]
```

These IDs are what actually enter the neural network.

The model never directly sees:

```text
Hello world
```

It only sees:

```text
[15496, 995]
```

This distinction is extremely important.

---

# Embeddings

Token IDs themselves are not meaningful to the transformer.

They are first converted into:

# embeddings.

Embeddings are dense numerical vector representations.

These vectors capture:

* semantic relationships
* syntactic structure
* contextual information

The embedding layer maps:

```text
Token ID → High-dimensional vector
```

This becomes the starting point for transformer computation.

---

# Byte Pair Encoding (BPE)

Many modern tokenizers use:

# Byte Pair Encoding (BPE)

BPE works by:

* identifying common text patterns
* merging frequently occurring sequences
* constructing reusable subword units

This allows models to:

* handle rare words efficiently
* reduce vocabulary explosion
* generalize better across language patterns

BPE is one reason models can process:

* misspellings
* code
* multilingual text
* uncommon names

without requiring every possible word in the vocabulary.

---

# Why Subword Tokenization Matters

Subword tokenization provides important operational advantages.

Instead of requiring:

```text
every possible word
```

the tokenizer can compose words from smaller pieces.

For example:

```text
"microarchitectural"
```

may be split into reusable fragments.

This dramatically reduces:

* vocabulary size
* memory requirements
* out-of-vocabulary failures

while preserving flexibility.

---

# Tokenization Is Not Neutral

Tokenization choices affect:

* efficiency
* context length
* multilingual performance
* code generation quality
* inference cost

Poor tokenization can:

* inflate token counts
* waste context window space
* increase latency

For example:
some languages require more tokens per sentence than others.

This creates:

# unequal inference costs across languages.

---

# Context Windows

Language models operate within finite:

# context windows.

The context window defines:

## the maximum number of tokens the model can process simultaneously.

Examples:

* 4K tokens
* 8K tokens
* 32K tokens
* 128K tokens

Everything inside the context window contributes to:

* memory usage
* attention computation
* latency

As token counts increase:
inference becomes more expensive.

---

# Tokenization and Economics

Tokenization directly impacts:

# operational economics.

More tokens mean:

* more GPU compute
* more attention operations
* more memory movement
* more infrastructure cost

This is why API providers bill by:

# token usage.

Tokens are effectively the currency of inference systems.

---

# Tokenization and Prompt Engineering

Many prompt engineering practices are actually:

# token optimization practices.

Examples:

* concise prompts
* compressed instructions
* reduced redundancy

can significantly reduce:

* latency
* inference cost
* context pressure

Efficient prompting therefore has infrastructure implications.

---

# Important Engineering Insight

Students should begin thinking of prompts not as:

```text
human language
```

but as:

```text
token sequences consuming finite system resources
```

This mindset becomes essential later when discussing:

* batching
* KV cache growth
* long-context serving
* throughput optimization

---

# Key Takeaways

Students should now understand:

* transformers operate on tokens, not raw text
* tokenization converts text into token IDs
* tokens are not equivalent to words
* vocabularies map tokens to integers
* embeddings convert token IDs into vectors
* BPE enables flexible subword representations
* token counts directly affect inference cost
* context windows constrain inference systems
* tokens are the operational currency of LLM serving

Tokenization may appear simple, but it has profound implications for:

* latency
* memory usage
* serving economics
* infrastructure scaling

---
