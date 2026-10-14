#!/usr/bin/env bash
set -euo pipefail
for cmd in aws kubectl docker; do
  command -v "$cmd" >/dev/null || { echo "$cmd missing"; exit 1; }
done
aws sts get-caller-identity >/dev/null
kubectl version --client >/dev/null
docker version >/dev/null
echo "Infrastructure preflight passed."
