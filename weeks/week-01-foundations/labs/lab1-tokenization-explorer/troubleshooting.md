# Troubleshooting — Lab 1 Tokenization Explorer

---

# Philosophy

Errors are part of inference engineering.

Do not treat failures as:

```text
something is wrong with me
```

Instead treat them as:

```text
signals from the system
```

Professional engineers spend large amounts of time:

* debugging
* profiling
* measuring
* fixing environment issues

This is normal.

---

# Problem: `ModuleNotFoundError`

Example:

```text
ModuleNotFoundError: No module named 'transformers'
```

## Cause

Required Python packages are missing.

## Fix

Install dependencies:

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install transformers torch accelerate
```

---

# Problem: Slow First Run

The first execution may appear frozen.

## Cause

The tokenizer/model is downloading from Hugging Face.

This can take:

* seconds
* minutes

depending on:

* internet speed
* model size
* regional connectivity

## Fix

Wait for the download to complete.

Subsequent runs should be much faster because files are cached locally.

---

# Problem: SSL / Certificate Errors

Example:

```text
SSL certificate verify failed
```

## Cause

Network or certificate configuration issue.

## Possible Fixes

Update certificates:

```bash
sudo apt update
sudo apt install ca-certificates
```

Or upgrade Python packages:

```bash
pip install --upgrade certifi
```

---

# Problem: Hugging Face Authentication Error

Example:

```text
401 Unauthorized
```

## Cause

Some models require authentication.

## Fix

For this lab, ensure you are using:

```text
Qwen/Qwen2.5-0.5B-Instruct
```

which should be publicly accessible.

---

# Problem: Extremely Slow Execution

## Possible Causes

* running on CPU
* low RAM
* background applications
* slow storage
* model downloading during execution

## Fixes

* close browser tabs
* close heavy applications
* rerun after model download finishes
* reduce workload size
* use Google Colab if needed

---

# Problem: Python Version Issues

## Recommended Version

Use:

```text
Python 3.10+
```

Check your version:

```bash
python --version
```

---

# Problem: Virtual Environment Confusion

If package installs are inconsistent:

## Create a clean environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

# Problem: Tokenizer Produces Different Results

Students may compare outputs and notice differences.

## Important

Minor tokenizer differences are normal.

Causes include:

* tokenizer updates
* library versions
* whitespace handling
* hidden Unicode characters

The objective is:

# understanding behavior,

not reproducing identical IDs.

---

# Problem: Weird Emoji Behavior

Example:

```text
😂😂😂😂😂
```

may produce many tokens.

## Explanation

Tokenizers are optimized primarily around:

* common language patterns
* frequent subword structures

Emojis and unusual symbols may tokenize inefficiently.

This is operationally important because:
token-inefficient inputs increase:

* latency
* cost
* context usage

---

# Problem: Code Snippets Split Strangely

Example:

```python
def hello_world():
    print("hello")
```

may tokenize unexpectedly.

## Explanation

Programming syntax introduces:

* punctuation
* indentation
* symbols
* uncommon token patterns

This is one reason code-specialized models sometimes use different tokenization strategies.

---

# Engineering Insight

One of the key lessons of this lab is:

## Tokenization is infrastructure-relevant.

It affects:

* cost
* latency
* context window usage
* memory allocation
* throughput

This is why inference engineers care deeply about tokens.

---

# Diagnostic Commands

Useful commands:

## Check Python version

```bash
python --version
```

## Check installed packages

```bash
pip list
```

## Check GPU

```bash
nvidia-smi
```

## Check RAM

```bash
free -h
```

---

# If Everything Fails

Try:

1. Restart terminal
2. Activate virtual environment again
3. Reinstall dependencies
4. Reboot machine
5. Try Google Colab

Even professional engineers do these regularly.

---

# Final Reminder

The purpose of this lab is not merely:

```text
to run a tokenizer
```

The purpose is to understand:

```text
why tokens are the operational currency of LLM systems
```

That distinction matters enormously in production inference engineering.
