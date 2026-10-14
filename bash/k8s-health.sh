#!/usr/bin/env bash
set -euo pipefail
NAMESPACE="${NAMESPACE:-default}"
kubectl get pods -n "$NAMESPACE"
kubectl get events -n "$NAMESPACE" --sort-by=.lastTimestamp | tail -20
