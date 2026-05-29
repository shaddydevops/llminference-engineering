import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# ============================================================
# LAB 2 — BUILD A TINY GENERATION LOOP
# STARTER FILE
# ============================================================
#
# Goal:
# Manually implement a simplified autoregressive generation loop.
#
# You will:
# - encode a prompt
# - run a forward pass
# - inspect logits
# - select the next token
# - append that token
# - repeat
#
# This is the core mechanism behind LLM generation.
# ============================================================

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

prompt = "The capital of Ghana is"

max_new_tokens = 20

# ------------------------------------------------------------
# Load tokenizer and model
# ------------------------------------------------------------

print("=" * 80)
print("Loading tokenizer and model...")
print("=" * 80)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()

print(f"Loaded model: {MODEL_NAME}")

# ------------------------------------------------------------
# Encode prompt
# ------------------------------------------------------------

inputs = tokenizer(prompt, return_tensors="pt")
input_ids = inputs["input_ids"]

print("\nOriginal prompt:")
print(prompt)

print("\nInput token IDs:")
print(input_ids)

print("\nInput shape:")
print(input_ids.shape)

# ------------------------------------------------------------
# TODO: Implement generation loop
# ------------------------------------------------------------
#
# Your tasks:
#
# 1. Run the model forward pass:
#
#       outputs = model(input_ids=input_ids)
#
# 2. Inspect logits:
#
#       outputs.logits
#
# 3. Extract logits for the final position:
#
#       next_token_logits = outputs.logits[:, -1, :]
#
# 4. Select the highest-probability token:
#
#       next_token_id = torch.argmax(next_token_logits, dim=-1, keepdim=True)
#
# 5. Append the new token to input_ids:
#
#       input_ids = torch.cat([input_ids, next_token_id], dim=-1)
#
# 6. Decode and print the growing text.
#
# 7. Repeat for max_new_tokens steps.
#
# ------------------------------------------------------------

print("\nTODO: Implement the generation loop below.")
print("Use the comments in this file as your guide.")

# Write your loop here.