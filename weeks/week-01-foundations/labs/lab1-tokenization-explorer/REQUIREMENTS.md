# Requirements — Lab 1 Tokenization Explorer

## Purpose

This file defines the Python dependencies required for this lab.

The goal is:

* reproducibility
* environment consistency
* easier debugging
* smoother onboarding

Professional inference engineering depends heavily on:

# controlled environments.

---

# Core Dependencies

```text id="4jlwm1"
transformers
torch
accelerate
tabulate
```

---

# Dependency Explanations

## transformers

Provides:

* tokenizer loading
* model loading
* generation APIs
* Hugging Face utilities

This is the primary framework used throughout the course.

---

## torch

PyTorch backend used for:

* tensor computation
* model execution
* GPU acceleration
* inference operations

Modern inference systems heavily depend on tensor frameworks.

---

## accelerate

Helps with:

* device handling
* CPU/GPU execution
* efficient model loading

Useful for inference workflows and future optimization labs.

---

## tabulate

Used for:

* clean console tables
* benchmarking output
* readable engineering reports

Professional engineers present measurements clearly.

---

# Installation

Install dependencies with:

```bash id="4jlwm2"
pip install -r requirements.txt
```

---

# Recommended Environment Setup

Use a virtual environment:

```bash id="4jlwm3"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

This prevents:

* dependency conflicts
* system pollution
* inconsistent environments

---

# GPU Notes

This lab does NOT require:

* large GPU memory
* expensive cloud hardware

CPU execution is acceptable.

However:
future labs may benefit from:

* CUDA support
* Colab GPU
* cloud GPUs

---

# Recommended Python Version

Use:

```text id="4jlwm4"
Python 3.10+
```

Check version:

```bash id="4jlwm5"
python --version
```

---

# Verification

After installation, verify packages:

```bash id="4jlwm6"
pip list
```

You should see:

* transformers
* torch
* accelerate
* tabulate

installed successfully.

---

# Engineering Principle

Dependency management is part of professional engineering.

Strong engineers care about:

* reproducibility
* environment consistency
* deployment reliability
* version control

Environment problems are among the most common real-world engineering issues.

Learning to manage them early is valuable.

---
