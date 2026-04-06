# World-Increment Sweep + Hamming Snapshot

**Sweep Timestamp:** 2026-04-06T12:30:00Z
**Agent:** world-increment-sweep (autonomous two-job agent)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots (unique) | ~164 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Status | Unavailable (HTML only) |

---

## GitHub Social Graph Sweep

### Repos Collected Per Source

| Source       | Type | Repos Fetched | Top Repo (Stars)                         |
|--------------|------|---------------|------------------------------------------|
| plurigrid    | org  | 28            | asi (16 stars)                           |
| kubeflow     | org  | 30            | kubeflow/kubeflow (15,553 stars)         |
| TeglonLabs   | org  | 3             | mathpix-gem (2 stars)                    |
| bmorphism    | user | 30            | ocaml-mcp-sdk (60 stars)                 |
| zubyul       | user | 5 public      | gay-world (1 star)                       |
| migalkin     | user | 19            | NodePiece (143 stars)                    |
| DJedamski    | user | 6             | Kaggle (1 star)                          |
| wasita       | user | 9             | magic-garden (1 star)                    |
| kristinezheng| user | 6             | kristinezheng.github.io (0 stars)        |
| M1shaaa      | user | 8             | M1shaaa profile (0 stars)                |
| AustinCStone | user | 20            | TextGAN (92 stars)                       |

### Notable Repos

- **kubeflow/kubeflow** — 15,553 stars, 2,627 forks — ML Toolkit for Kubernetes
- **kubeflow/pipelines** — 4,118 stars, 1,983 forks — ML Pipelines
- **kubeflow/spark-operator** — 3,111 stars — Kubernetes operator for Apache Spark
- **kubeflow/trainer** — 2,074 stars — Distributed AI Model Training + LLM Fine-Tuning
- **migalkin/NodePiece** — 143 stars — Knowledge Graph representations (ICLR'22)
- **AustinCStone/TextGAN** — 92 stars — TensorFlow text GAN
- **bmorphism/ocaml-mcp-sdk** — 60 stars — OCaml SDK for MCP (Jane Street oxcaml_effect)
- **plurigrid/asi** — 16 stars — topological chemputer (actively developed)
- **plurigrid/gorj** — 105 open issues — forj + GF(3) REPL orchestration (this repo)

---

## GF(3) Color Chain — World Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Hamming Swarm Snapshot (Aptos Mainnet)

**RPC:** https://fullnode.mainnet.aptoslabs.com

### Aptos Wallet Balances

All 28 wallets returned 0.0 APT (CoinStore resource returned 0 — accounts may use FA coin standard or are unfunded).

| World | Address (short)    | Balance APT |
|-------|--------------------|-------------|
| alice | 0xc793...cc7b      | 0.0         |
| bob   | 0x0a3c...2d5d      | 0.0         |
| A     | 0x8699...9d7a      | 0.0         |
| B     | 0x3f89...b13       | 0.0         |
| C     | 0x38b9...35e       | 0.0         |
| D     | 0xf776...dd1       | 0.0         |
| E     | 0xdc1d...d36       | 0.0         |
| F     | 0x18a1...f71       | 0.0         |
| G     | 0x69a3...f32       | 0.0         |
| H     | 0xce67...00f       | 0.0         |
| I     | 0x070f...c9        | 0.0         |
| J     | 0x4d96...f54       | 0.0         |
| K     | 0xa732...dc4       | 0.0         |
| L     | 0x7c2e...ba9       | 0.0         |
| M     | 0x6fed...2e9       | 0.0         |
| N     | 0xe7dd...b2c       | 0.0         |
| O     | 0x7325...89d       | 0.0         |
| P     | 0x6218...948       | 0.0         |
| Q     | 0xac40...a9        | 0.0         |
| R     | 0x7ce6...e10       | 0.0         |
| S     | 0xb875...386       | 0.0         |
| T     | 0x3578...588       | 0.0         |
| U     | 0x7586...956       | 0.0         |
| V     | 0xb59d...2c3       | 0.0         |
| W     | 0x5f32...b0        | 0.0         |
| X     | 0xa95c...47d       | 0.0         |
| Y     | 0xd8e3...4c4       | 0.0         |
| Z     | 0x7af0...97c       | 0.0         |

---

## Multisig Contract Probes

All 5 multisig contracts healthy — all require **2-of-N signatures**.

| Pair | Address (short)    | Sigs Required | Healthy |
|------|--------------------|---------------|---------|
| A-B  | 0x0da4...003       | 2             | YES     |
| A-G  | 0xf56c...096       | 2             | YES     |
| Y-Z  | 0xd3ff...883       | 2             | YES     |
| S-T  | 0x3b1c...883       | 2             | YES     |
| V-W  | 0x40fa...b6d       | 2             | YES     |

---

## MNX Markets Status

**Status: UNAVAILABLE (no JSON API)**
Both `https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/v1/markets` return the Next.js frontend HTML. MNX testnet market data API is not publicly exposed as JSON.

---

## GF(3) Color Chain Legend

| id % 3 | Trit | Color   | Hex Code | Name     |
|--------|------|---------|----------|----------|
| 0      | 0    | Pink    | #d3869b  | ERGODIC  |
| 1      | +1   | Green   | #b8bb26  | PLUS     |
| 2      | -1   | Red     | #cc241d  | MINUS    |

**GF(3) Assignment Rule:**
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

The GF(3) color chain encodes Galois Field(3) trit conservation across world-increment rows. Trits cycle PLUS→MINUS→ERGODIC deterministically, providing a chromatic identity for each data source in the sweep.

---

## DuckDB Tables

- `world_increments` — 11 source increment rows
- `repo_snapshots` — 164 unique repos tracked across 11 sources
- `aptos_snapshots` — 28 Hamming swarm wallet snapshots
- `multisig_probes` — 5 contract health probes (all healthy, 2-of-N)
- `mnx_snapshots` — 1 status row (API unavailable)

---

*Generated by autonomous world-increment sweep agent — 2026-04-06*
*plurigrid/gorj :: packages/world-increment/ducklake/*
