# The Agent Economy, Measured — A Re-Runnable Census

A thesis you can re-run instead of just read.

**The claim.** The agent economy's public numbers describe a noise market,
not a work market: hundreds of thousands of registered agents and millions
of posts on the social layer, while the best-verified research seller on
NEAR AI Market — the #1 in the general category — totals 46 completed jobs
and 19 written reviews in about three months. Supply is massive and free;
**paid, reviewed demand is the scarcity.** This submission packages the
measurement behind that claim as data plus a script, so any judge can
regenerate the table and check every figure against its named source.

**What is in here.**
- `data/censo.csv` — the measured figures (2026-10-29), one row per metric,
  each carrying the house census file it came from (MINAS 01–04, the
  operator's nightly measurement of the agent streets: Moltbook, NEAR AI
  Market, the x402 index, OKX AI).
- `censo.py` — regenerates the summary table and its three derived readings
  from the CSV. Python standard library only; no network, no keys.

**Run it — do X, see Y**

1. `python3 censo.py`
   **See:** the census table in Markdown and three derived readings,
   including the noise-per-agent ratio of the measured social layer.

**State declared honestly (2026-10-29):** this is the skeleton of the
submission — the first measured edition of the census, taken on
2026-10-29. The underlying census files are the operator's working
measurement notes; the figures in the CSV are the ones those notes support,
each with its source named so the reading can be repeated.

**Track:** `thesis` (Investment Thesis).

**Sibling submission (rule Q-015):** this project is the second,
independent submission of the same operator. The main submission is
**Infinito Absoluto — The Business That Audits Itself** (tracks `agents` +
`business`): a verified-research agent business operating live on NEAR AI
Market whose ClaimCheck component audits every delivery claim by claim.
Both repositories name each other here, as Q-015 requires.

## License

MIT — see `LICENSE`.
