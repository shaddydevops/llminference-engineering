# Expected Output — Lab 1 Tokenization Explorer

---

# Important Note

Your exact outputs may differ depending on:

* tokenizer version
* transformers version
* operating system
* model updates
* whitespace handling

This is normal.

The goal is not exact token matches.

The goal is:

# understanding tokenization behavior.

---

# Example Console Output

You should see outputs similar to:

```text
================================================================================
ORIGINAL TEXT:
Hello world

TOKENS:
['Hello', 'Ġworld']

TOKEN IDS:
[9707, 1879]

TOKEN COUNT:
2
```

---

# Technical Words

Words such as:

```text
microarchitectural
autoregressive
internationalization
```

may split into multiple subword tokens.

Example:

```text
['micro', 'architect', 'ural']
```

or similar variations.

This is expected.

---

# Token Count Differences

You should observe that:

```text
word count != token count
```

Example:

| Text                            | Approx Words | Token Count |
| ------------------------------- | -----------: | ----------: |
| Hello world                     |            2 |           2 |
| microarchitectural optimization |            2 |          5+ |
| 😂😂😂😂😂                      |            1 |    multiple |

---

# Important Observation

Some text styles tokenize inefficiently.

Examples:

* emojis
* code
* mixed languages
* technical terminology
* unusual punctuation

This matters operationally because:
more tokens increase:

* prefill work
* attention computation
* latency
* memory pressure
* serving cost

---

# What Strong Analysis Looks Like

Strong students should write observations such as:

```text
The technical prompt produced significantly more tokens than the simple prompt.
This implies higher prefill latency and greater context window usage during inference.
```

or:

```text
Emoji-heavy text appeared token-inefficient, suggesting multilingual or symbolic content may increase serving cost unexpectedly.
```

---

# Operational Takeaways

Students should leave this lab understanding:

## Tokens are:

* computational units
* billing units
* memory units
* scheduling units

NOT merely preprocessing artifacts.

---

# Common Beginner Misconceptions

## Incorrect Thinking

```text
1 word = 1 token
```

## More Accurate Thinking

```text
Tokens are variable-length subword units whose count directly affects inference economics.
```

---

# Stretch Challenge Expectations

Students attempting the stretch challenge should notice:

| Text Type           | Likely Token Efficiency |
| ------------------- | ----------------------- |
| Simple English      | Efficient               |
| Technical jargon    | Moderate                |
| Emojis              | Often inefficient       |
| Code snippets       | Variable                |
| Mixed-language text | Often inefficient       |

---

# Final Lesson

Modern inference systems do not fundamentally operate on:

```text
language
```

They operate on:

```text
token sequences under hardware constraints
```

That distinction is foundational to inference engineering.
