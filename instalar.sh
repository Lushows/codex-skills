#!/usr/bin/env bash
# Instala las skills de Lushows en este equipo.
# Uso:  bash instalar.sh
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ORIGEN="$DIR/skills"

if [ ! -d "$ORIGEN" ]; then
  echo "ERROR: no encuentro la carpeta 'skills' junto a este script."
  exit 1
fi

TOTAL=$(find "$ORIGEN" -mindepth 1 -maxdepth 1 -type d | wc -l)
echo ""
echo "Skills encontradas: $TOTAL"
echo ""
echo "  1) Codex       -> ~/.codex/skills"
echo "  2) Claude Code -> ~/.claude/skills"
echo "  3) Los dos"
echo ""
read -r -p "Donde las instalo? (1/2/3) " OPCION

case "$OPCION" in
  1) DESTINOS=("$HOME/.codex/skills") ;;
  2) DESTINOS=("$HOME/.claude/skills") ;;
  3) DESTINOS=("$HOME/.codex/skills" "$HOME/.claude/skills") ;;
  *) echo "Opcion no valida. Cancelado."; exit 1 ;;
esac

for DESTINO in "${DESTINOS[@]}"; do
  mkdir -p "$DESTINO"
  echo ""
  echo "Instalando en $DESTINO"
  for SKILL in "$ORIGEN"/*/; do
    NOMBRE=$(basename "$SKILL")
    if [ -e "$DESTINO/$NOMBRE" ]; then
      rm -rf "$DESTINO/$NOMBRE"
      echo "  reemplazada  $NOMBRE"
    else
      echo "  instalada    $NOMBRE"
    fi
    cp -r "$SKILL" "$DESTINO/$NOMBRE"
  done
done

echo ""
echo "Listo. Cierra y vuelve a abrir Codex (o Claude Code)."
echo ""
