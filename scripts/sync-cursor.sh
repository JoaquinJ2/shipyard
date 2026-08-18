#!/usr/bin/env bash
# Materialize shipyard kernel + packs into a consuming repo's .cursor/.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec python3 "$ROOT/scripts/sync-cursor.py" "$@"
