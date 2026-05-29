# ============================================================
# LAB 2 — GENERATION LOOP UTILITIES
# ============================================================
#
# Shared helper functions used throughout the lab.
#
# These utilities separate reusable logic from the
# main notebook/scripts and introduce students to
# cleaner engineering practices.
#
# ============================================================

import torch

# ------------------------------------------------------------
# Pretty Divider
# ------------------------------------------------------------

def divider(width: int = 80):
    """
    Create a visual separator.
    """

    return "=" * width

# ------------------------------------------------------------
# Decode Token
# ------------------------------------------------------------

def decode_token(
    tokenizer,
    token_id
):
    """
    Decode a single token ID.
    """

    return tokenizer.decode(token_id)

# ------------------------------------------------------------
# Decode Sequence
# ------------------------------------------------------------

def decode_sequence(
    tokenizer,
    input_ids
):
    """
    Decode full sequence.
    """

    return tokenizer.decode(
        input_ids[0],
        skip_special_tokens=True
    )

# ------------------------------------------------------------
# Extract Next Token Logits
# ------------------------------------------------------------

def get_next_token_logits(
    outputs
):
    """
    Extract logits corresponding
    to the final sequence position.
    """

    return outputs.logits[:, -1, :]

# ------------------------------------------------------------
# Greedy Decoding
# ------------------------------------------------------------

def greedy_decode(
    next_token_logits
):
    """
    Select highest probability token.
    """

    return torch.argmax(
        next_token_logits,
        dim=-1,
        keepdim=True
    )

# ------------------------------------------------------------
# Append Token
# ------------------------------------------------------------

def append_token(
    input_ids,
    next_token_id
):
    """
    Append generated token
    to existing sequence.
    """

    return torch.cat(
        [input_ids, next_token_id],
        dim=-1
    )

# ------------------------------------------------------------
# Logits Information
# ------------------------------------------------------------

def describe_logits(
    logits
):
    """
    Return shape information.
    """

    batch_size = logits.shape[0]
    sequence_length = logits.shape[1]
    vocab_size = logits.shape[2]

    return {
        "batch_size": batch_size,
        "sequence_length": sequence_length,
        "vocab_size": vocab_size
    }

# ------------------------------------------------------------
# Top-K Inspection
# ------------------------------------------------------------

def top_k_predictions(
    tokenizer,
    next_token_logits,
    k=5
):
    """
    Inspect top-k candidate tokens.
    Useful for understanding model uncertainty.
    """

    probs = torch.softmax(
        next_token_logits,
        dim=-1
    )

    values, indices = torch.topk(
        probs,
        k=k
    )

    predictions = []

    for prob, idx in zip(
        values[0],
        indices[0]
    ):

        predictions.append({
            "token_id": idx.item(),
            "token": tokenizer.decode([idx.item()]),
            "probability": round(
                prob.item(),
                6
            )
        })

    return predictions

# ------------------------------------------------------------
# Generation Statistics
# ------------------------------------------------------------

def generation_stats(
    initial_length,
    final_length
):
    """
    Basic generation metrics.
    """

    generated_tokens = (
        final_length -
        initial_length
    )

    return {
        "initial_tokens": initial_length,
        "final_tokens": final_length,
        "generated_tokens": generated_tokens
    }

# ------------------------------------------------------------
# Engineering Explanation
# ------------------------------------------------------------

def engineering_takeaway():
    """
    Return summary insight.
    """

    return """
Generation is a repeated next-token prediction loop.

Each generated token requires:
- a forward pass
- logits computation
- token selection
- sequence growth

This sequential dependency is one of the
core reasons inference optimization is difficult.
"""

# ============================================================
# END
# ============================================================