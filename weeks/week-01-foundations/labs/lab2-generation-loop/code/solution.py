import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# ============================================================
# LAB 2 — BUILD A TINY GENERATION LOOP
# SOLUTION
# ============================================================
#
# This solution demonstrates:
#
# - autoregressive generation
# - forward passes
# - logits inspection
# - greedy decoding
# - sequence growth
#
# ============================================================

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

prompt = "The capital of Ghana is"

max_new_tokens = 20

# ------------------------------------------------------------
# Load tokenizer and model
# ------------------------------------------------------------

print("=" * 80)
print("LOADING MODEL")
print("=" * 80)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

# ------------------------------------------------------------
# Encode prompt
# ------------------------------------------------------------

input_ids = tokenizer(
    prompt,
    return_tensors="pt"
).input_ids

print("\nOriginal Prompt:")
print(prompt)

print("\nInitial Input Shape:")
print(input_ids.shape)

print("\nInitial Token Count:")
print(input_ids.shape[-1])

# ------------------------------------------------------------
# Generation Loop
# ------------------------------------------------------------

print("\n" + "=" * 80)
print("STARTING GENERATION")
print("=" * 80)

with torch.no_grad():

    for step in range(max_new_tokens):

        # ----------------------------------------------------
        # Forward Pass
        # ----------------------------------------------------

        outputs = model(input_ids=input_ids)

        # ----------------------------------------------------
        # Logits
        # ----------------------------------------------------

        logits = outputs.logits

        if step == 0:

            print("\nLogits Tensor Shape:")
            print(logits.shape)

            print("""
Shape Explanation:

(batch_size,
 sequence_length,
 vocabulary_size)
""")

        # ----------------------------------------------------
        # Extract final token logits
        # ----------------------------------------------------

        next_token_logits = logits[:, -1, :]

        # ----------------------------------------------------
        # Greedy Decoding
        # ----------------------------------------------------

        next_token_id = torch.argmax(
            next_token_logits,
            dim=-1,
            keepdim=True
        )

        # ----------------------------------------------------
        # Append token
        # ----------------------------------------------------

        input_ids = torch.cat(
            [input_ids, next_token_id],
            dim=-1
        )

        # ----------------------------------------------------
        # Decode growing sequence
        # ----------------------------------------------------

        generated_text = tokenizer.decode(
            input_ids[0],
            skip_special_tokens=True
        )

        print("\n" + "-" * 80)
        print(f"STEP {step + 1}")

        print("\nNew Token ID:")
        print(next_token_id.item())

        print("\nCurrent Sequence Length:")
        print(input_ids.shape[-1])

        print("\nGenerated Text:")
        print(generated_text)

# ------------------------------------------------------------
# Final Output
# ------------------------------------------------------------

print("\n" + "=" * 80)
print("FINAL OUTPUT")
print("=" * 80)

final_text = tokenizer.decode(
    input_ids[0],
    skip_special_tokens=True
)

print(final_text)

# ------------------------------------------------------------
# Engineering Interpretation
# ------------------------------------------------------------

print("\n" + "=" * 80)
print("ENGINEERING INSIGHTS")
print("=" * 80)

print("""
1. The model generates one token at a time.

2. Every generated token requires another forward pass.

3. Future tokens cannot be generated until previous
   tokens exist.

4. This creates a sequential bottleneck.

5. Decode therefore parallelizes poorly.

6. Many modern inference optimizations exist to
   improve this generation loop.

7. KV cache exists largely because recomputing
   attention repeatedly would be extremely expensive.
""")