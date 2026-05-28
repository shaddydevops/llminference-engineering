#!/bin/bash

set -e

echo "Creating Week 1 lab folder structure..."

LABS_DIR="labs"

mkdir -p "$LABS_DIR"

labs=(
  "lab1-tokenization-explorer"
  "lab2-generation-loop"
  "lab3-latency-benchmarking"
  "lab4-memory-analysis"
  "lab5-prefill-vs-decode"
)

for lab in "${labs[@]}"; do
  echo "Creating $lab..."

  mkdir -p "$LABS_DIR/$lab/code"
  mkdir -p "$LABS_DIR/$lab/notebooks"
  mkdir -p "$LABS_DIR/$lab/data"
  mkdir -p "$LABS_DIR/$lab/outputs"
  mkdir -p "$LABS_DIR/$lab/reports"
  mkdir -p "$LABS_DIR/$lab/instructor"

  touch "$LABS_DIR/$lab/README.md"
  touch "$LABS_DIR/$lab/code/starter.py"
  touch "$LABS_DIR/$lab/code/solution.py"
  touch "$LABS_DIR/$lab/code/utils.py"
  touch "$LABS_DIR/$lab/notebooks/README.md"
  touch "$LABS_DIR/$lab/expected_output.md"
  touch "$LABS_DIR/$lab/troubleshooting.md"
  touch "$LABS_DIR/$lab/reflection_questions.md"
  touch "$LABS_DIR/$lab/reports/LAB_REPORT_TEMPLATE.md"
  touch "$LABS_DIR/$lab/instructor/INSTRUCTOR_NOTES.md"
  touch "$LABS_DIR/$lab/requirements.txt"
done

cat > "$LABS_DIR/README.md" << 'EOF'
# Week 1 Labs — Foundations of LLM Inference

These labs turn the Week 1 handbook into practical engineering investigations.

## Labs

1. Tokenization Explorer
2. Generation Loop
3. Latency Benchmarking
4. Memory Analysis
5. Prefill vs Decode

## Philosophy

Students should not only run code.

They should:
- observe behavior
- measure performance
- explain implications
- connect results to production inference systems

## Recommended Flow

Run the labs in order.
EOF

cat > "$LABS_DIR/requirements.txt" << 'EOF'
transformers
torch
accelerate
psutil
tabulate
pandas
matplotlib
jupyter
EOF

echo ""
echo "Week 1 lab structure created successfully."
echo ""
find "$LABS_DIR" -maxdepth 3 -type f | sort
