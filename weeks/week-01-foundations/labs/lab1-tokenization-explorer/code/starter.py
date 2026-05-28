from transformers import AutoTokenizer

# ============================================================
# LAB 1 — TOKENIZATION EXPLORER
# ============================================================
# Goal:
# Understand how raw text becomes tokens and token IDs.
#
# This starter file intentionally leaves analysis tasks for
# the student to complete.
# ============================================================

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

# ------------------------------------------------------------
# Text samples
# ------------------------------------------------------------

texts = [
    "Hello world",
    "The capital of Ghana is Accra.",
    "Inference engineering is about systems, memory, latency, and cost.",
    "microarchitectural optimization",
    "Akwaaba! How are you doing today?",
]

# ------------------------------------------------------------
# Load tokenizer
# ------------------------------------------------------------

print("=" * 80)
print("Loading tokenizer...")
print("=" * 80)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print(f"Loaded tokenizer for: {MODEL_NAME}")

# ------------------------------------------------------------
# Basic tokenization loop
# ------------------------------------------------------------

for text in texts:

    print("\n" + "=" * 80)

    # --------------------------------------------------------
    # Original text
    # --------------------------------------------------------

    print("ORIGINAL TEXT:")
    print(text)

    # --------------------------------------------------------
    # Tokenization
    # --------------------------------------------------------

    tokens = tokenizer.tokenize(text)

    print("\nTOKENS:")
    print(tokens)

    # --------------------------------------------------------
    # Token IDs
    # --------------------------------------------------------

    token_ids = tokenizer.encode(text)

    print("\nTOKEN IDS:")
    print(token_ids)

    # --------------------------------------------------------
    # Token count
    # --------------------------------------------------------

    print("\nTOKEN COUNT:")
    print(len(token_ids))

    # --------------------------------------------------------
    # TODO SECTION
    # --------------------------------------------------------
    #
    # STUDENT TASKS:
    #
    # 1. Calculate word count
    # 2. Compare words vs tokens
    # 3. Calculate tokens-per-word ratio
    # 4. Identify which text splits most aggressively
    # 5. Explain WHY that matters operationally
    #
    # Example operational reasoning:
    #
    # "More tokens increase prefill cost and consume more
    # context window space."
    #
    # --------------------------------------------------------

print("\n" + "=" * 80)
print("LAB COMPLETE")
print("=" * 80)

# ============================================================
# REFLECTION QUESTIONS
# ============================================================
#
# 1. Which text produced the most tokens?
#
# 2. Did any token splits surprise you?
#
# 3. Why might technical words produce more tokens?
#
# 4. Why do token counts matter operationally?
#
# 5. Why are tokens a better metric than words for
#    inference systems?
#
# ============================================================