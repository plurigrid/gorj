# World-Increment Sweep — 2026-04-01

## Sweep Metadata
- **Date:** 2026-04-01T00:00:00Z
- **Agent:** world-increment-sweep + hamming snapshot
- **DuckDB:** `/packages/world-increment/ducklake/world.duckdb`
- **Session:** https://claude.ai/code/session_01Y893C4ZATEdr9veeNwx5HR

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 49 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GitHub Sweep Summary

| Source Type | Source Name   | Repos Discovered |
|-------------|---------------|-----------------|
| org         | plurigrid     | 93              |
| org         | kubeflow      | 46              |
| org         | TeglonLabs    | 3               |
| user        | bmorphism     | 97              |
| user        | zubyul        | 44              |
| user        | migalkin      | 19              |
| user        | DJedamski     | 6               |
| user        | wasita        | 9               |
| user        | kristinezheng | 6               |
| user        | M1shaaa       | 8               |
| user        | AustinCStone  | 40              |
| **TOTAL**   |               | **371**         |

Notable repos by stars:
- `kubeflow/kubeflow` — 15,549 stars (ML Toolkit for Kubernetes)
- `kubeflow/pipelines` — 4,118 stars (ML Pipelines)
- `kubeflow/spark-operator` — 3,110 stars
- `migalkin/NodePiece` — 143 stars (ICLR'22 KG embeddings)
- `AustinCStone/TextGAN` — 92 stars (TensorFlow text GAN)
- `bmorphism/ocaml-mcp-sdk` — 60 stars (OCaml MCP SDK)
- `plurigrid/asi` — 14 stars (topological chemputer)

---

## GF(3) Color Chain — World Increments

| ID | Source Type | Source       | GF3 Trit | Color   | Name    |
|----|-------------|--------------|----------|---------|---------|
| 1  | org         | plurigrid    | +1       | #b8bb26 | PLUS    |
| 2  | org         | kubeflow     | -1       | #cc241d | MINUS   |
| 3  | org         | TeglonLabs   | 0        | #d3869b | ERGODIC |
| 4  | user        | bmorphism    | +1       | #b8bb26 | PLUS    |
| 5  | user        | zubyul       | -1       | #cc241d | MINUS   |
| 6  | user        | migalkin     | 0        | #d3869b | ERGODIC |
| 7  | user        | DJedamski    | +1       | #b8bb26 | PLUS    |
| 8  | user        | wasita       | -1       | #cc241d | MINUS   |
| 9  | user        | kristinezheng| 0        | #d3869b | ERGODIC |
| 10 | user        | M1shaaa      | +1       | #b8bb26 | PLUS    |
| 11 | user        | AustinCStone | -1       | #cc241d | MINUS   |

---

## Aptos Hamming Swarm Snapshot

All 28 addresses probed via Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`).
All accounts returned 0.0 APT — unfunded or no CoinStore resource on mainnet.

| World | Address (truncated)  | Balance APT |
|-------|----------------------|-------------|
| alice | 0xc793...4cc7b       | 0.0         |
| bob   | 0x0a3c...512d5d      | 0.0         |
| A     | 0x8699...be9d7a      | 0.0         |
| B     | 0x3f89...cb13        | 0.0         |
| C     | 0x38b9...1535e       | 0.0         |
| D     | 0xf776...cfdd1       | 0.0         |
| E     | 0xdc1d...8d36        | 0.0         |
| F     | 0x18a1...3cf71       | 0.0         |
| G     | 0x69a3...c7f32       | 0.0         |
| H     | 0xce67...5300f       | 0.0         |
| I     | 0x070f...1fc9        | 0.0         |
| J     | 0x4d96...87f54       | 0.0         |
| K     | 0xa732...25dc4       | 0.0         |
| L     | 0x7c2e...eba9        | 0.0         |
| M     | 0x6fed...7f2e9       | 0.0         |
| N     | 0xe7dd...51b2c       | 0.0         |
| O     | 0x7325...a89d        | 0.0         |
| P     | 0x6218...c948        | 0.0         |
| Q     | 0xac40...c89a9       | 0.0         |
| R     | 0x7ce6...76e10       | 0.0         |
| S     | 0xb875...d0386       | 0.0         |
| T     | 0x3578...f4588       | 0.0         |
| U     | 0x7586...f9956       | 0.0         |
| V     | 0xb59d...af2c3       | 0.0         |
| W     | 0x5f32...c7b0        | 0.0         |
| X     | 0xa95c...3047d       | 0.0         |
| Y     | 0xd8e3...444c4       | 0.0         |
| Z     | 0x7af0...197c        | 0.0         |

---

## Multisig Probe Results

All 5 contracts probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated)        | Sigs Required | Healthy |
|------|----------------------------|---------------|---------|
| A-B  | 0x0da4f428...4987003       | 2             | true    |
| A-G  | 0xf56c4a1c...fbc0096       | 2             | true    |
| Y-Z  | 0xd3ffe181...75b883        | 2             | true    |
| S-T  | 0x3b1c3ae9...ed7883        | 2             | true    |
| V-W  | 0x40fad7b4...80eb6d        | 2             | true    |

All contracts healthy. Each requires 2-of-N multisig.

---

## MNX Markets

**Status: unavailable**

All three endpoints tested (`/api/markets`, `/api/v1/markets`, `/api/tickers`) at `https://testnet.mnx.fi` return HTML (Next.js SPA). No machine-readable market data API accessible. No rows in `mnx_snapshots`.

---

## GF(3) Assignment Rule

| id % 3 | Trit | Hex     | Name    |
|--------|------|---------|---------|
| 0      | 0    | #d3869b | ERGODIC |
| 1      | +1   | #b8bb26 | PLUS    |
| 2      | -1   | #cc241d | MINUS   |

The GF(3) chain encodes the ergodic / additive / subtractive triad cycling through each source sweep as a Hamming-distance coloring.

---

*Generated by Claude Code world-increment sweep agent — 2026-04-01*
*Session: https://claude.ai/code/session_01Y893C4ZATEdr9veeNwx5HR*
