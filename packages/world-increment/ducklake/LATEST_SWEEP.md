# World-Increment Sweep — 2026-06-29

## Sweep Metadata
- **Date:** 2026-06-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-04-12 (471 snapshots, 12 world-increments)

---

## Summary Counts (This Sweep)

| Metric | Value |
|--------|-------|
| New World Increments | 13 |
| New Repo Snapshots | 329 |
| Sources Covered | 3 orgs + 10 users (social graph extended) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel auth required) |

---

## GF(3) Color Chain — This Sweep

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
| 12 | bmorphism-events | events | 0 | `#d3869b` | **ERGODIC** |
| 13 | zubyul-events | events | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## JOB 1: GitHub Social Graph Sweep

### Top Repos by Stars (Today's Snapshot)

| Repo | Stars | Pushed At | Description |
|------|-------|-----------|-------------|
| kubeflow/kubeflow | 15,752 | 2026-06-18 | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,159 | 2026-06-27 | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,129 | 2026-06-26 | Kubernetes operator for Apache Spark on Kubernetes |
| kubeflow/trainer | 2,126 | 2026-06-26 | Distributed AI Training and LLM Fine-Tuning on K8s |
| kubeflow/katib | 1,687 | 2026-06-23 | Automated Machine Learning on Kubernetes |
| migalkin/NodePiece | 144 | 2026-05-07 | Compositional & Parameter-Efficient KG Embeddings (ICLR'22) |
| migalkin/StarE | 89 | 2026-04-16 | Message Passing for Hyper-Relational Knowledge Graphs |
| AustinCStone/TextGAN | 92 | 2025-03-03 | Generative adversarial network for text generation |
| migalkin/kgcourse2021 | 25 | 2026-02-16 | Knowledge Graphs course materials |
| plurigrid/asi | 26 | 2026-06-28 | everything is topological chemputer! |

### Repo Counts by Source (This Sweep)

| Source | Type | Repos | Stars Total | Max Stars |
|--------|------|-------|-------------|-----------|
| plurigrid | org | 100 | 77 | 26 (asi) |
| bmorphism | user | 100 | 247 | 61 (ocaml-mcp-sdk) |
| kubeflow | org | 48 | 34,277 | 15,752 (kubeflow) |
| zubyul | user | 49 | 14 | 2 |
| TeglonLabs | org | 5 | 2 | 2 (mathpix-gem) |
| migalkin | user | 6 | 279 | 144 (NodePiece) |
| AustinCStone | user | 5 | 106 | 92 (TextGAN) |
| wasita | user | 6 | 4 | 2 |
| DJedamski | user | 4 | 3 | 1 |
| kristinezheng | user | 3 | 0 | 0 |
| M1shaaa | user | 3 | 0 | 0 |
| **TOTAL** | | **329** | **35,009** | |

### Most Recently Pushed (≥ 2026-06-25)

| Repo | Stars | Pushed At |
|------|-------|-----------|
| plurigrid/gorj | 0 | 2026-06-28T23:09 | 
| plurigrid/asi | 26 | 2026-06-28T00:42 |
| bmorphism/Gay.jl | 2 | 2026-06-28T00:39 |
| plurigrid/place | 1 | 2026-06-27T22:03 |
| kubeflow/hub | 174 | 2026-06-27T17:16 |
| kubeflow/pipelines | 4,159 | 2026-06-27T15:18 |
| kubeflow/spark-operator | 3,129 | 2026-06-26T23:02 |
| kubeflow/trainer | 2,126 | 2026-06-26T16:26 |

### Notable Changes Since April 2026 Sweep

- **kubeflow/kubeflow**: 15,565 → 15,752 stars (+187)
- **kubeflow/pipelines**: 4,119 → 4,159 stars (+40)
- **kubeflow/spark-operator**: 3,111 → 3,129 stars (+18)
- **kubeflow/trainer**: 2,080 → 2,126 stars (+46)
- **plurigrid/asi**: 16 → 26 stars (+10) — most active plurigrid repo
- **plurigrid/gorj**: 893 open issues (was much fewer April) — heavy active development
- **bmorphism/ocaml-mcp-sdk**: 60 → 61 stars
- **TeglonLabs**: jank-crane new repo (C++, GF3 convergence maps, pushed 2026-06-08)
- **kubeflow/mcp-server**: NEW — MCP Server for AI-Assisted Kubeflow Development
- **kubeflow/mcp-apache-spark-history-server**: NEW (178 stars!) — MCP for Spark History Server

### Social Graph (Zubyul circle)

| User | Repos | Notable |
|------|-------|---------|
| migalkin | 19 total | Knowledge graph researcher; NodePiece (144★), StarE (89★) |
| DJedamski | 6 total | Data science; NCAA bracket, Kaggle |
| wasita | 11 total | Personal site (Svelte), cognitive science tools |
| kristinezheng | 5 total | MIT neurosci; auditory illusion, Lookit |
| M1shaaa | 8 total | Yale work; lab bookshelf (TypeScript) |
| AustinCStone | 40 total | ML research; TextGAN (92★), StereoVisionMRF (11★) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 wallets (alice, bob, A–Z) probed on mainnet. All returned **0 APT** — accounts exist on-chain but CoinStore resources are uninitialized or empty.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | 0x8699...–0x7af0... | 0.0 each |

*All 28 wallets: zero APT balance. Likely pre-funded staging addresses awaiting deployment.*

### Multisig Contract Health (5 contracts)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...3003 | **2-of-N** | ✅ HEALTHY |
| A-G | 0xf56c...0096 | **2-of-N** | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | **2-of-N** | ✅ HEALTHY |
| S-T | 0x3b1c...883 | **2-of-N** | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | **2-of-N** | ✅ HEALTHY |

*All 5 multisig contracts require 2 signatures and are alive on mainnet.*

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active (authentication required).  
API endpoints `/api/markets` and `/api/v1/markets` both return HTTP 401.  
No market data could be extracted. Recorded as 0 rows in `mnx_snapshots`.

---

## Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
