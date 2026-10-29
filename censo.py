#!/usr/bin/env python3
"""
Censo de la economía de agentes — modelo re-ejecutable (esqueleto).

Reads data/censo.csv (figures measured by the house on 2026-10-29, each row
carrying its source) and regenerates the summary table. The census is a
living measurement, not an essay: re-run the measurement, replace the CSV,
re-run this script, and the table — the thesis — updates itself.

Run:  python3 censo.py
Out:  the census table in Markdown, plus the three derived readings.
"""
import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "data", "censo.csv"), newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print("| Métrica | Valor | Ámbito | Fuente |")
    print("|---|---:|---|---|")
    for r in rows:
        print(f"| {r['metrica']} | {int(r['valor']):,} | {r['ambito']} | {r['fuente']} |")

    by = {r["metrica"]: int(r["valor"]) for r in rows}
    posts_per_agent = by["Posts en Moltbook"] / by["Agentes verificados en Moltbook (portada, en vivo)"]
    print()
    print("Lecturas derivadas (se recalculan solas al actualizar el CSV):")
    print(f"- Ruido por agente en la red social medida: {posts_per_agent:.1f} posts por agente verificado.")
    print(f"- El campeón de la categoría general en NEAR suma {by['Trabajos completados del n.º 1 de Web Research en NEAR']} trabajos y {by['Reseñas escritas del n.º 1 de Web Research en NEAR (todas positivas)']} reseñas: la reputación, no el registro, es el foso.")
    print(f"- El índice x402 lista {by['Recursos en el índice x402 de CDP']:,} recursos: la oferta es masiva; la demanda pagada es la escasez.")


if __name__ == "__main__":
    main()
