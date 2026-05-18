# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-18

## Sweep Metadata
- **Date:** 2026-05-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Sources Covered | 3 orgs + 8 users |
| Repos Ingested (this sweep) | 310 |
| Total Stars (this sweep) | ~103,362 |
| World Increments Added | 333 |

### GF(3) Trit Distribution (This Sweep)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 110 |
| +1 | PLUS | `#b8bb26` | 112 |
| -1 | MINUS | `#cc241d` | 111 |

GF(3) chain repeats: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`

### Repo Counts by Source

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| plurigrid | org | 100 | 154 | 2026-05-17 |
| bmorphism | user | 100 | 509 | 2026-05-17 |
| kubeflow | org | 48 | 101,796 | 2026-05-17 |
| zubyul | user | 41 | 36 | 2026-04-24 |
| TeglonLabs | org | 4 | 14 | 2026-01-16 |
| migalkin | social | 5 | 829 | 2026-05-07 |
| wasita | social | 4 | 9 | 2026-05-17 |
| AustinCStone | social | 3 | 0 | 2026-02-11 |
| DJedamski | social | 2 | 15 | 2023-04-21 |
| kristinezheng | social | 2 | 0 | 2026-05-14 |
| M1shaaa | social | 2 | 0 | 2026-04-13 |
| **TOTAL** | | **311** | **~103,362** | |

> Social graph users (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) queried via GitHub MCP tools after unauthenticated API rate limit.

### Notable Repos (2026-05-18 Snapshot)
| Repo | Stars | Description |
|------|-------|-------------|
| kubeflow/kubeflow | 15,644 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,140 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,125 | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,099 | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1,682 | Automated Machine Learning on Kubernetes |
| migalkin/NodePiece | 144 | Compositional KG Representations (ICLR'22) |
| migalkin/StarE | 89 | Message Passing for Hyper-Relational KGs |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml SDK for Model Context Protocol |
| bmorphism/Gay.jl | 1 | Wide-gamut color sampling (Pigeons.jl SPI) |
| plurigrid/gorj | 0 | forj + Rama nREPL + GF(3) trit coloring *(this repo)* |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-05-18)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 addresses returned 0.0 APT — coin stores uninitialized or zero balance.

| World | Address | APT |
|-------|---------|-----|
| alice | `0xc793...cc7b` | 0.0 |
| bob | `0x0a3c...512d` | 0.0 |
| A | `0x8699...9d7a` | 0.0 |
| B | `0x3f89...b13` | 0.0 |
| C | `0x38b9...35e` | 0.0 |
| D | `0xf776...dd1` | 0.0 |
| E | `0xdc1d...d36` | 0.0 |
| F | `0x18a1...f71` | 0.0 |
| G | `0x69a3...f32` | 0.0 |
| H | `0xce67...00f` | 0.0 |
| I | `0x070f...c9` | 0.0 |
| J | `0x4d96...f54` | 0.0 |
| K | `0xa732...dc4` | 0.0 |
| L | `0x7c2e...a9` | 0.0 |
| M | `0x6fed...e9` | 0.0 |
| N | `0xe7dd...b2c` | 0.0 |
| O | `0x7325...89d` | 0.0 |
| P | `0x6218...948` | 0.0 |
| Q | `0xac40...a9` | 0.0 |
| R | `0x7ce6...e10` | 0.0 |
| S | `0xb875...386` | 0.0 |
| T | `0x3578...588` | 0.0 |
| U | `0x7586...956` | 0.0 |
| V | `0xb59d...2c3` | 0.0 |
| W | `0x5f32...7b0` | 0.0 |
| X | `0xa95c...47d` | 0.0 |
| Y | `0xd8e3...4c4` | 0.0 |
| Z | `0x7af0...97c` | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)

All 5 pairs probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4...003` | 2 | ✅ |
| A-G | `0xf56c...096` | 2 | ✅ |
| Y-Z | `0xd3ff...883` | 2 | ✅ |
| S-T | `0x3b1c...883` | 2 | ✅ |
| V-W | `0x40fa...b6d` | 2 | ✅ |

All 5 multisig contracts require **2-of-N signatures** and are **healthy**.

### MNX Markets (testnet.mnx.fi)

The MNX testnet site (`https://testnet.mnx.fi`) is a **Next.js SPA**. Probed endpoints:
- `GET /api/markets` → HTML (SPA fallback)
- `GET /api/v1/markets` → HTML (SPA fallback)
- `GET /api/tickers` → HTML (SPA fallback)

**Status:** UNAVAILABLE — market data is loaded client-side only; no accessible JSON API from headless environment. `mnx_snapshots` table has 1 stub row.

---

## DuckDB Tables

```sql
world_increments  — GF(3) trit-colored event log (cumulative across sweeps)
repo_snapshots    — GitHub repo metadata snapshots
aptos_snapshots   — Hamming swarm wallet balances (28 addresses)
multisig_probes   — Aptos multisig contract health (5 pairs, all 2-of-N)
mnx_snapshots     — MNX market stub (SPA unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*  
*Previous sweep: 2026-04-12 | This sweep: 2026-05-18*
