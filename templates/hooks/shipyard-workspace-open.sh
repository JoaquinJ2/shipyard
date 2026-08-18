#!/usr/bin/env bash
# Load shipyard from this repo's submodule (project scope).
set -euo pipefail
input=$(cat || true)
root="${CURSOR_PROJECT_DIR:-}"
if [[ -z "$root" ]]; then
  root=$(printf '%s' "$input" | python3 -c 'import json,sys; d=json.load(sys.stdin); print((d.get("workspace_roots") or [""])[0])')
fi
PLUGIN="${root}/.cursor/plugins/shipyard"
if [[ -n "$root" && -f "$PLUGIN/.cursor-plugin/plugin.json" ]]; then
  python3 -c 'import json, sys; print(json.dumps({"pluginPaths": [sys.argv[1]]}))' "$PLUGIN"
else
  echo '{}'
fi
