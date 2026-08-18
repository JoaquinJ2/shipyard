#!/usr/bin/env bash
# Load shipyard from this repo's submodule (project scope).
set -euo pipefail
PLUGIN="${CURSOR_PROJECT_DIR:?}/.cursor/plugins/shipyard"
if [[ -f "$PLUGIN/.cursor-plugin/plugin.json" ]]; then
  python3 -c 'import json, sys; print(json.dumps({"pluginPaths": [sys.argv[1]]}))' "$PLUGIN"
else
  echo '{}'
fi
