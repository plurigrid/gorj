# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-06

## Sweep Metadata
- **Date:** 2026-05-06T14:21Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Snapshot Counts by Source

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| bmorphism | user | 300 | 509 | 2026-05-06 |
| plurigrid | org | 300 | 148 | 2026-05-06 |
| kubeflow | org | 141 | 101,728 | 2026-05-06 |
| TeglonLabs | org | 110 | 14 | 2026-01-16 |
| zubyul | user | 97 | 40 | 2026-04-24 |
| AustinCStone | user (social graph) | 92 | 322 | 2026-04-01 |
| migalkin | user (social graph) | 69 | 832 | 2026-04-16 |
| wasita | user (social graph) | 60 | 6 | 2026-04-13 |
| kristinezheng | user (social graph) | 36 | 0 | 2026-04-09 |
| M1shaaa | user (social graph) | 32 | 0 | 2026-04-13 |
| DJedamski | user (social graph) | 22 | 14 | 2018-03-07 |
| **TOTAL** | | **1,259** | **103,613** | |

### GF(3) Trit Chain — world_increments

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 112 |
| +1 | PLUS | `#b8bb26` | 113 |
| -1 | MINUS | `#cc241d` | 113 |

**338 world_increments total** — near-perfectly balanced GF(3) distribution across the social graph sweep.

Chain rule: `id % 3 == 0 → ERGODIC · id % 3 == 1 → PLUS · id % 3 == 2 → MINUS`

### Notable Repos (This Sweep)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,623 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,133 | Python | ML Pipelines for Kubeflow (pushed 2026-05-05) |
| kubeflow/spark-operator | 3,123 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,096 | Go | Distributed AI Model Training & LLM Fine-Tuning |
| kubeflow/katib | 1,683 | Python | Automated Machine Learning on Kubernetes |
| migalkin/NodePiece | 143 | Python | Compositional KG representations (ICLR'22) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| plurigrid/ontology | 7 | JavaScript | autopoietic ergodicity and embodied gradualism |
| plurigrid/gorj | 0 | Clojure | **This repo** — forj + Rama + GF(3) trit coloring |
| plurigrid/nanoclj-zig | 1 | Zig | NaN-boxed Clojure in Zig 0.15, GF(3) trit conservation |
| plurigrid/zig-syrup | 2 | Zig | OCapN Syrup with CapTP optimizations |
| TeglonLabs/mathpix-gem | 2 | Ruby | Mathematical OCR Ruby gem |

### Data Collection Notes

- No `gh` CLI available; no valid `GITHUB_TOKEN` in environment
- Used GitHub MCP search API (authenticated) for all repo queries
- bmorphism and plurigrid cross-membership means org repos appear under both
- Public events for bmorphism/zubyul not accessible without authenticated user-scoped token

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances — 28 Addresses

All addresses probed: `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| Label | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…35e | 0.0 |
| D | 0xf776…dd1 | 0.0 |
| E | 0xdc1d…d36 | 0.0 |
| F | 0x18a1…f71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…00f | 0.0 |
| I | 0x070f…c9 | 0.0 |
| J | 0x4d96…f54 | 0.0 |
| K | 0xa732…dc4 | 0.0 |
| L | 0x7c2e…ba9 | 0.0 |
| M | 0x6fed…2e9 | 0.0 |
| N | 0xe7dd…b2c | 0.0 |
| O | 0x7325…89d | 0.0 |
| P | 0x6218…948 | 0.0 |
| Q | 0xac40…89a9 | 0.0 |
| R | 0x7ce6…e10 | 0.0 |
| S | 0xb875…386 | 0.0 |
| T | 0x3578…588 | 0.0 |
| U | 0x7586…956 | 0.0 |
| V | 0xb59d…2c3 | 0.0 |
| W | 0x5f32…b0 | 0.0 |
| X | 0xa95c…47d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…97c | 0.0 |

**All 28 Hamming swarm addresses hold 0 APT on Aptos mainnet** (unfunded test addresses).

### Multisig Contract Health — 5 Pairs

All probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`

| Pair | Multisig Address | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c…0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c…7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa…eb6d | 2 | ✓ HEALTHY |

**All 5 multisig contracts healthy — 2-of-N signature threshold.**

### MNX Markets (`testnet.mnx.fi`)

**Status: SPA only — no public REST API discovered.**

`https://testnet.mnx.fi/` returns a Next.js client-side rendered application. Probing `/api/markets` and the root path returned no structured market data without JavaScript execution. `mnx_snapshots` table: 0 rows.

---

## DuckDB Schema Summary

```sql
-- world_increments: GF(3)-colored event log
SELECT COUNT(*) FROM world_increments;  -- 338

-- repo_snapshots: per-repo metadata snapshots
SELECT COUNT(*) FROM repo_snapshots;    -- 1,259

-- aptos_snapshots: Hamming swarm wallet balances  
SELECT COUNT(*) FROM aptos_snapshots;   -- 28

-- multisig_probes: Aptos multisig health
SELECT COUNT(*) FROM multisig_probes;   -- 5

-- mnx_snapshots: MNX market data (unavailable)
SELECT COUNT(*) FROM mnx_snapshots;     -- 0
```

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-05-06*
