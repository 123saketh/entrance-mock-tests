#!/usr/bin/env bash
# Download the openly licensed source datasets into .harvest/ (see ATTRIBUTION.md).
set -euo pipefail
cd "$(dirname "$0")/../.."
mkdir -p .harvest && cd .harvest
B=https://huggingface.co/datasets
curl -sL -o jeebench.json  $B/daman1209arora/jeebench/resolve/main/test.json
curl -sL -o pw_jan.jsonl   $B/PhysicsWallahAI/JEE-Main-2025-Math/resolve/main/main2025-jan.jsonl
curl -sL -o pw_apr.jsonl   $B/PhysicsWallahAI/JEE-Main-2025-Math/resolve/main/main2025-apr.jsonl
curl -sL -o ck.csv         $B/CK0607/2025-Jee-Mains-Question/resolve/main/math_with_uuid.csv
for s in chemistry physics mathematics; do
  for sp in train test; do
    curl -sL -o eq_${s}_${sp}.jsonl $B/eQOURSE/jee-main-questions/resolve/main/$s/$sp.jsonl
  done
done
# Then: python scripts/harvest/build_harvested.py && python scripts/harvest/validate.py
# (PW items are only kept if listed as ok/fix in .harvest/verify/pw_batch*.result.json,
#  which hold hand-verified solutions.)
