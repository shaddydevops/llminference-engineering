# ============================================================
# LAB 1 — TOKENIZATION UTILITIES
# ============================================================
#
# Shared helper functions for tokenization experiments.
#
# These utilities are intentionally separated from the main
# scripts to encourage cleaner engineering structure.
#
# ============================================================

from typing import Dict, List

# ------------------------------------------------------------
# Basic word count
# ------------------------------------------------------------

def get_word_count(text: str) -> int:
    """
    Approximate word count using whitespace splitting.
    """

    return len(text.split())

# ------------------------------------------------------------
# Tokens per word ratio
# ------------------------------------------------------------

def tokens_per_word(
    token_count: int,
    word_count: int
) -> float:
    """
    Calculate token-to-word ratio safely.
    """

    if word_count == 0:
        return 0.0

    return token_count / word_count

# ------------------------------------------------------------
# Simple operational interpretation
# ------------------------------------------------------------

def operational_interpretation(
    token_count: int
) -> str:
    """
    Return a simple production interpretation
    based on token count.
    """

    if token_count > 50:
        return (
            "High token count: likely higher prefill latency, "
            "larger KV cache allocation, and increased serving cost."
        )

    elif token_count > 20:
        return (
            "Moderate token count: noticeable impact on "
            "latency and context window utilization."
        )

    else:
        return (
            "Relatively token-efficient prompt with lower "
            "prefill overhead."
        )

# ------------------------------------------------------------
# Pretty divider
# ------------------------------------------------------------

def divider(
    width: int = 80
) -> str:
    """
    Generate divider line for cleaner console output.
    """

    return "=" * width

# ------------------------------------------------------------
# Structured text analysis
# ------------------------------------------------------------

def build_analysis_dict(
    text: str,
    tokens: List[str],
    token_ids: List[int]
) -> Dict:
    """
    Build structured analysis dictionary.
    """

    word_count = get_word_count(text)
    token_count = len(token_ids)

    return {
        "text": text,
        "word_count": word_count,
        "token_count": token_count,
        "tokens_per_word": round(
            tokens_per_word(token_count, word_count),
            2
        ),
        "tokens": tokens,
        "token_ids": token_ids,
        "interpretation": operational_interpretation(
            token_count
        )
    }

# ============================================================
# END
# ============================================================