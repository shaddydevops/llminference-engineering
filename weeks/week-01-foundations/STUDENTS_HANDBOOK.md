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

# The Transformer Forward Pass

At the center of every language model inference system is:

# the forward pass.

The forward pass is the sequence of computations that transforms:

* input token embeddings
  into
* next-token prediction scores.

This process is responsible for most of the computational work during inference.

Understanding the forward pass is essential because nearly every optimization discussed later in this course attempts to improve some aspect of it.

Examples include:

* FlashAttention
* quantization
* batching
* tensor parallelism
* KV caching
* speculative decoding

All exist to optimize the forward pass.

---

# High-Level View

A simplified transformer inference pipeline looks like:

```text
Input Text
    ↓
Tokenization
    ↓
Token IDs
    ↓
Embeddings
    ↓
Transformer Layers
    ↓
Logits
    ↓
Sampling
    ↓
Generated Token
```

The forward pass primarily refers to:

```text
Embeddings → Transformer Layers → Logits
```

This is where:

* GPU computation occurs
* tensor operations dominate
* memory bandwidth becomes critical

---

# Why It Is Called a “Forward” Pass

Neural networks process information directionally.

During inference:
data moves:

* from input
* through layers
* toward predictions

This movement is called:

# forward propagation.

Unlike training:

* no gradients are computed
* no backward pass occurs
* no weight updates happen

Inference therefore performs:

## forward-only computation.

This is one reason inference is cheaper than training.

---

# Embedding Lookup

The first stage of the forward pass is:

# embedding lookup.

Recall:
the tokenizer converted text into integer token IDs.

Example:

```text
[15496, 995]
```

These integers are meaningless by themselves.

The embedding layer maps each token ID to:

# a dense vector representation.

Example:

```text
15496 → vector of dimension 4096
```

These vectors become the numerical representation processed by the transformer.

---

# Why Embeddings Matter

Embeddings allow models to represent:

* semantic relationships
* syntactic structure
* contextual similarities

For example:
tokens with related meanings often occupy nearby regions in embedding space.

Embeddings transform discrete tokens into continuous mathematical representations suitable for neural computation.

This transformation is foundational to modern NLP systems.

---

# Positional Information

Transformers process tokens in parallel.

Unlike recurrent networks:
they do not inherently understand sequence order.

Therefore:
models must inject positional information.

This is typically done using:

* positional embeddings
* rotary positional embeddings (RoPE)
* sinusoidal encodings

Without positional information:
the model would not know whether:

```text
dog bites man
```

differs from:

```text
man bites dog
```

Sequence order matters enormously.

---

# Transformer Layers

After embeddings are created, tensors move through:

# transformer layers.

Modern LLMs may contain:

* dozens
* or even hundreds

of transformer blocks.

Each layer performs:

* attention operations
* feed-forward transformations
* normalization
* residual connections

These layers repeatedly refine token representations.

---

# Self-Attention

The core innovation of transformers is:

# self-attention.

Self-attention allows each token to:

## attend to other relevant tokens in the sequence.

For example:

```text
The cat sat on the mat because it was soft.
```

The token:

```text
it
```

may attend strongly to:

```text
mat
```

because contextual relationships matter.

Attention allows models to dynamically determine:

* what information matters
* what context should influence predictions

---

# Query, Key, and Value

Self-attention operates using:

* Queries (Q)
* Keys (K)
* Values (V)

Each token generates:

* a query vector
* a key vector
* a value vector

The system computes:

## similarity between queries and keys.

These similarity scores determine:
how much attention should be paid to different tokens.

The resulting weighted combinations of values produce contextualized representations.

---

# Why Attention Is Expensive

Attention requires:
tokens to interact with other tokens.

This creates large matrix operations involving:

* sequence length
* hidden dimensions
* multiple attention heads

As sequence length grows:
attention computation becomes increasingly expensive.

This is one reason long-context inference is difficult.

Attention is often one of the most computationally expensive parts of transformer inference.

---

# Multi-Head Attention

Modern transformers use:

# multi-head attention.

Instead of learning a single attention pattern:
the model learns multiple parallel attention patterns simultaneously.

Different heads may specialize in:

* syntax
* long-range dependencies
* factual associations
* code structure
* punctuation relationships

This increases representational capacity.

But it also increases:

* compute cost
* memory usage
* tensor complexity

---

# Feed-Forward Networks

After attention, tokens pass through:

# feed-forward networks (FFNs).

These are large neural layers that:

* transform activations
* expand representational capacity
* introduce nonlinearity

FFNs often contain enormous parameter counts.

In many transformers:

## FFNs consume a substantial portion of total compute.

---

# Residual Connections

Transformers use:

# residual connections.

Residual connections allow information to:

* bypass layers
* preserve gradients
* stabilize deep networks

Operationally:
they help transformers train and scale effectively.

Without residual connections:
very deep architectures become difficult to optimize.

---

# Layer Normalization

Transformer layers also use:

# normalization operations.

Normalization stabilizes activations and improves training dynamics.

Although often overlooked:
normalization contributes to:

* numerical stability
* smoother optimization
* more reliable inference behavior

---

# Logits Generation

After tokens pass through all transformer layers:
the model produces:

# logits.

Logits are raw prediction scores for each vocabulary token.

Example:

```text
Vocabulary size = 128,000
```

The model outputs:

```text
128,000 scores
```

for the next token prediction.

These scores are not yet probabilities.

---

# Softmax

The logits pass through:

# softmax.

Softmax converts raw scores into:

## probabilities.

The probabilities across the vocabulary sum to:

```text
1.0
```

This creates the next-token probability distribution.

Sampling strategies then choose the actual output token.

---

# Sampling and Decoding

The final stage of the forward pass pipeline involves:

# decoding.

Common decoding strategies include:

* greedy decoding
* top-k sampling
* top-p sampling
* temperature scaling

These strategies influence:

* determinism
* creativity
* diversity
* stability

Sampling is operationally important because it affects user experience and generation behavior.

---

# The Forward Pass Is Repeated Continuously

One of the most important insights students must understand is:

## inference repeatedly executes forward passes.

For every generated token:
the model performs another forward computation.

This means:
generation cost scales with:

* output length
* sequence length
* concurrency
* context size

This repeated execution is why optimization matters so much.

---

# Why KV Cache Exists

Without optimization:
the model would repeatedly recompute attention over all prior tokens during generation.

This would become prohibitively expensive.

KV cache exists to avoid redundant computation.

Later in this course we will study:

* KV cache structure
* cache growth
* memory implications
* PagedAttention
* cache-aware scheduling

KV cache is one of the most important ideas in modern inference systems.

---

# Forward Pass Bottlenecks

The transformer forward pass is constrained by:

* compute throughput
* memory bandwidth
* VRAM capacity
* tensor movement
* cache efficiency

This is why modern inference engineering focuses heavily on:

* fused kernels
* memory-efficient attention
* quantization
* scheduling optimization

The bottleneck is not merely “running the model.”

The bottleneck is:

## running the model efficiently at scale.

---

# Key Takeaways

Students should now understand:

* the forward pass drives transformer inference
* embeddings convert token IDs into vectors
* positional information preserves sequence order
* transformer layers repeatedly refine token representations
* self-attention enables contextual reasoning
* attention operations are computationally expensive
* feed-forward networks consume substantial compute
* logits represent next-token prediction scores
* softmax converts logits into probabilities
* forward passes repeat continuously during generation
* KV cache exists to avoid redundant computation

The transformer forward pass is the computational engine underlying modern LLM systems.

Understanding it deeply is essential for meaningful inference optimization.

---

# Prefill vs Decode

One of the most important concepts in modern inference engineering is the distinction between:

* prefill
* decode

Students who deeply understand this distinction suddenly understand:

* why the first token is slow
* why KV cache exists
* why batching is difficult
* why vLLM matters
* why speculative decoding is valuable
* why inference optimization is hard

This section is foundational to the rest of the course.

---

# The Two Phases of Inference

Autoregressive generation consists of two fundamentally different computational phases:

```text
1. Prefill Phase
2. Decode Phase
```

Although both involve transformer forward passes, their behavior differs dramatically.

Operationally:
they behave like different workloads.

Understanding this is critical for systems optimization.

---

# High-Level Intuition

A useful mental model is:

## Prefill

> “Read and understand the prompt.”

## Decode

> “Generate tokens one at a time.”

The hardware behavior of these phases differs substantially.

---

# Prefill Phase

The prefill phase processes:

# the entire input prompt.

Example:

```text
"Explain why batching improves transformer inference throughput."
```

Before generation can begin, the model must:

* tokenize the prompt
* compute embeddings
* run attention across all input tokens
* initialize hidden states
* populate KV cache

This is computationally expensive.

---

# What Happens During Prefill

During prefill:
the model processes:

## all prompt tokens simultaneously.

This means:
attention operations occur across the full sequence.

Example:

```text
Input length = 500 tokens
```

The model processes:

```text
500 tokens together
```

This creates:

* large tensor operations
* heavy memory movement
* expensive attention computation

But:

## it is highly parallelizable.

This is extremely important.

---

# Why Prefill Parallelizes Well

During prefill:
all prompt tokens already exist.

Because the entire prompt is known:
the GPU can process many computations in parallel.

This allows:

* high GPU utilization
* efficient tensor operations
* large matrix multiplications

GPUs perform extremely well during prefill.

In many systems:

## prefill achieves very high hardware efficiency.

---

# Decode Phase

Decode begins after the first output token is generated.

At this point:
generation becomes:

# autoregressive.

This means:
each new token depends on previous tokens.

Example:

```text
The capital of Ghana is
```

Model predicts:

```text
Accra
```

Now the next prediction uses:

```text
The capital of Ghana is Accra
```

This repeats sequentially.

---

# Why Decode Is Fundamentally Different

Unlike prefill:
decode operates:

## one token at a time.

Only the newest token is processed during each decode step.

This creates a critical limitation:

# decode is inherently sequential.

The next token cannot be generated until the current token exists.

This dramatically changes hardware behavior.

---

# Decode Parallelism Is Limited

During decode:
future tokens do not yet exist.

Therefore:
the GPU cannot fully parallelize generation across future positions.

This creates:

* lower GPU utilization
* smaller tensor operations
* scheduling inefficiencies
* memory-access bottlenecks

This is one reason inference optimization is difficult.

---

# Why The First Token Is Slow

One of the most visible consequences of prefill is:

# Time To First Token (TTFT)

TTFT measures:

## how long it takes before the first generated token appears.

The first token is slow because:
the entire prefill phase must complete first.

This includes:

* tokenization
* attention over full context
* KV cache initialization
* transformer computation across prompt tokens

Only after prefill finishes can decode begin.

---

# Why Later Tokens Become Faster

After prefill:
decode steps become cheaper because:

* KV cache already exists
* prior computations are reused
* only the newest token is processed

This is why:
token streaming often accelerates after the first token appears.

Operationally:
many systems exhibit:

* slow TTFT
* faster sustained tok/s afterward

This distinction matters enormously in production systems.

---

# GPU Utilization Differences

Prefill and decode stress GPUs differently.

## Prefill

Typically:

* compute-heavy
* highly parallel
* large matrix operations
* efficient GPU occupancy

## Decode

Typically:

* memory-bound
* sequential
* smaller tensor operations
* lower GPU utilization

Modern inference systems must optimize both phases separately.

---

# Why KV Cache Exists

Without KV cache:
every decode step would recompute attention over:

## the entire prior sequence.

This would be catastrophically inefficient.

Instead:
KV cache stores:

* previously computed keys
* previously computed values

This allows decode to reuse prior computations efficiently.

KV cache dramatically reduces decode cost.

But:
it also increases:

* memory usage
* VRAM pressure
* scheduling complexity

Later sections explore this deeply.

---

# Prefill Cost Scales With Prompt Length

Long prompts increase:

* prefill latency
* memory usage
* attention cost

This is because:
attention computation scales with sequence length.

Example:

```text
100-token prompt
```

vs

```text
10,000-token prompt
```

The longer prompt requires dramatically more:

* memory movement
* tensor operations
* attention computation

This is why long-context serving is difficult.

---

# Decode Cost Scales With Output Length

Prefill depends primarily on:

# input size.

Decode depends primarily on:

# output generation length.

Long generations therefore:

* extend inference duration
* increase GPU occupancy time
* consume scheduling resources

At scale:
generation length becomes economically important.

---

# Why Continuous Batching Is Hard

Batching decode requests is difficult because:
different users generate tokens at different speeds.

Some requests:

* finish early
* stall
* generate longer outputs
* use different sampling behaviors

This creates:

# scheduler complexity.

Continuous batching systems like vLLM exist largely to optimize decode efficiency under these constraints.

---

# Why Speculative Decoding Matters

Decode is slow partly because:
generation is sequential.

Speculative decoding attempts to reduce this bottleneck by:

* generating draft tokens
* verifying them efficiently

The goal is:

## increasing effective decode throughput.

This technique exists specifically because decode is difficult to parallelize.

---

# Operational Implications

Production inference systems must balance:

* prefill efficiency
* decode efficiency
* memory usage
* latency
* throughput

Optimizing one phase may worsen another.

For example:

* aggressive batching may improve throughput
* but worsen TTFT

These are real engineering tradeoffs.

---

# Mental Model

Students should think of:

## prefill

as:

```text
large parallel computation
```

and:

## decode

as:

```text
sequential token streaming
```

These are fundamentally different workload patterns.

Most inference optimizations exist to manage this tension.

---

# Why This Concept Is Foundational

Prefill vs decode explains:

* TTFT
* KV cache
* batching difficulty
* scheduler design
* throughput bottlenecks
* memory growth
* streaming latency
* speculative decoding
* vLLM architecture decisions

This is one of the most important concepts in modern inference engineering.

Students should revisit it repeatedly throughout the course.

---

# Key Takeaways

Students should now understand:

* inference consists of prefill and decode phases
* prefill processes the full prompt simultaneously
* prefill parallelizes efficiently
* decode generates tokens sequentially
* decode is inherently difficult to parallelize
* TTFT is dominated by prefill cost
* sustained generation speed differs from TTFT
* KV cache exists to optimize decode
* long prompts increase prefill cost
* long outputs increase decode cost
* continuous batching exists largely because decode is difficult

This distinction forms the conceptual bridge into:

* KV cache systems
* batching architectures
* vLLM
* PagedAttention
* speculative decoding

Without understanding prefill vs decode deeply, modern inference systems remain difficult to reason about.

---


# KV Cache Introduction

One of the most important optimizations in modern language model inference is:

# KV cache.

Without KV cache:
modern autoregressive generation would become prohibitively expensive.

KV cache exists because repeatedly recomputing attention over previous tokens during decoding is computationally wasteful.

This section introduces:

* what KV cache is
* why it exists
* why it matters
* how it changes inference economics
* why it creates new memory problems

Understanding KV cache is essential for:

* vLLM
* PagedAttention
* batching systems
* speculative decoding
* long-context serving

KV cache is one of the foundational concepts of modern inference engineering.

---

# The Core Problem

Recall from the previous section:

During autoregressive generation:
new tokens are generated one at a time.

Example:

```text
The capital of Ghana is
```

Model predicts:

```text
Accra
```

Now the model must generate the next token using:

```text
The capital of Ghana is Accra
```

Then:

```text
The capital of Ghana is Accra .
```

Then:

```text
The capital of Ghana is Accra . It
```

This process continues repeatedly.

---

# The Naive Approach

Without optimization:
each decode step would recompute:

## attention over the entire sequence.

Example:

Step 1:

```text
5 tokens
```

Step 2:

```text
6 tokens
```

Step 3:

```text
7 tokens
```

The model would repeatedly recompute attention for:

* old tokens
* unchanged tokens
* previously processed context

This is extremely inefficient.

---

# Why Recomputing Attention Is Wasteful

Most prior tokens do not change during generation.

Only:

## the newest token

changes.

Yet naive decoding would repeatedly recompute:

* queries
* keys
* values
* attention interactions

for all previous tokens.

This creates:

* unnecessary compute
* wasted memory movement
* increased latency
* reduced throughput

KV cache exists to eliminate this redundancy.

---

# What KV Cache Stores

KV cache stores:

* Keys (K)
* Values (V)

generated during previous attention computations.

Instead of recomputing these tensors every decode step:
the system reuses them.

Hence the name:

# KV cache.

---

# Why Queries Are Not Cached

During generation:
the newest token produces:

* a new query
* a new key
* a new value

The query changes every step because:
the current token changes every step.

However:
previous keys and values remain valid.

Therefore:

* queries are recomputed
* keys and values are cached

This dramatically reduces redundant computation.

---

# High-Level Decode Flow With KV Cache

Without KV cache:

```text
Recompute full sequence attention every step
```

With KV cache:

```text
Reuse previous keys/values
+
Compute only newest token attention
```

This changes decode economics dramatically.

---

# Operational Impact

KV cache significantly improves:

* decode speed
* throughput
* latency
* GPU utilization

Without KV cache:
autoregressive decoding becomes far slower.

Modern LLM serving systems rely heavily on KV cache efficiency.

---

# The Tradeoff

KV cache improves compute efficiency.

But:
it increases:

# memory usage.

This tradeoff is extremely important.

As generation continues:
KV cache grows.

As context length increases:
KV cache grows further.

As concurrency increases:
memory pressure increases massively.

Inference engineering becomes:

## a memory management problem.

---

# KV Cache Growth

Each generated token adds:

* new key tensors
* new value tensors

to the cache.

Therefore:
KV cache size scales roughly with:

* sequence length
* number of layers
* hidden dimensions
* batch size
* concurrency

Large context windows can therefore consume enormous amounts of VRAM.

---

# Why Long Context Is Difficult

Many people assume:
larger context windows are “just software improvements.”

Operationally:
they are memory-intensive infrastructure challenges.

Longer contexts mean:

* larger KV caches
* more VRAM pressure
* more memory fragmentation
* harder scheduling

This is one reason long-context inference is expensive.

---

# Memory Fragmentation

In production systems:
requests:

* start at different times
* finish at different times
* generate different output lengths

This creates irregular KV cache allocation patterns.

Over time:
memory becomes fragmented.

This creates:

* inefficient VRAM usage
* wasted memory regions
* scheduling difficulties

Modern serving systems like vLLM were designed largely to address this problem.

---

# KV Cache and Time To First Token

KV cache also influences:

# TTFT.

During prefill:
the model computes initial KV states for the prompt.

This initialization contributes to:

* prefill latency
* memory allocation cost

Afterward:
decode becomes cheaper because cached states are reused.

---

# Why KV Cache Matters Operationally

KV cache directly affects:

* maximum concurrency
* maximum context length
* throughput
* serving cost
* GPU memory usage

In many production systems:
KV cache memory becomes:

# the dominant VRAM consumer.

This surprises many beginners.

They assume:
model weights dominate memory usage.

But during large-scale serving:
KV cache can become equally important or even larger.

---

# KV Cache and Batching

Batching complicates KV cache management.

Different requests:

* have different lengths
* generate at different speeds
* terminate unpredictably

The serving system must:

* allocate cache memory dynamically
* reuse memory efficiently
* avoid fragmentation
* schedule requests intelligently

This becomes a systems engineering challenge.

---

# Why PagedAttention Exists

Traditional KV cache allocation strategies often waste VRAM.

PagedAttention improves this by:

* managing cache memory in blocks/pages
* reducing fragmentation
* improving allocation efficiency
* enabling larger effective batch sizes

This is one of the core innovations behind vLLM.

Students will study this deeply later in the course.

---

# KV Cache Is a Fundamental Optimization

Students should understand:

KV cache is not:

## an optional optimization.

It is:

## a foundational requirement for efficient autoregressive inference.

Without KV cache:
modern LLM serving would be dramatically slower and more expensive.

---

# Mental Model

Students should think of KV cache as:

```text
Reusable memory of previous attention computations
```

The system remembers prior attention state so it does not need to recompute everything repeatedly.

This is conceptually similar to:

* caching in databases
* memoization in algorithms
* reuse in compiler optimization

The principle is:

## avoid redundant work.

---

# Engineering Perspective

KV cache transforms inference from:

## primarily compute-bound

into

## heavily memory-constrained.

This is a major shift.

Once KV cache enters the picture:
inference optimization increasingly becomes about:

* memory allocation
* fragmentation
* scheduling
* cache efficiency
* VRAM utilization

This is why modern inference engineering resembles systems engineering.

---

# Key Takeaways

Students should now understand:

* KV cache stores previous keys and values
* KV cache avoids redundant attention computation
* decode becomes much cheaper with caching
* KV cache improves throughput and latency
* KV cache increases VRAM usage
* cache size grows with sequence length
* long-context inference is memory-intensive
* batching complicates cache management
* fragmentation becomes a serious systems problem
* PagedAttention exists largely to optimize KV cache allocation

KV cache is one of the most important ideas in modern inference systems.

Many later optimizations in this course build directly on this concept.

---
