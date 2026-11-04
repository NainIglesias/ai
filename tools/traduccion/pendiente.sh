#!/usr/bin/env bash
# Lista lo que ha cambiado en upstream desde el último commit traducido (el del README).
#   tools/traduccion/pendiente.sh [UPSTREAM_REF]      (por defecto upstream/main)
# Salida: líneas "ESTADO<TAB>fichero" de git diff --name-status. Vacía si está al día.
# Variables útiles para scripts: imprime REF y HEAD en stderr.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

target="${1:-upstream/main}"
ref=$(grep -oE 'hasta el commit [0-9a-f]{7,40}' README.md | awk '{print $4}')
[ -n "$ref" ] || { echo "No encuentro 'hasta el commit <sha>' en README.md" >&2; exit 2; }

head=$(git rev-parse "$target")
echo "REF=$ref" >&2
echo "HEAD=$head" >&2

if [ "$(git rev-parse "$ref")" = "$head" ]; then
  exit 0
fi
git diff --name-status "$ref" "$head"
