# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-11

## Sweep Metadata
- **Date:** 2026-05-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Sweep ID:** 13 · GF(3): trit=1 · **PLUS** · `#b8bb26`

---

## JOB 1: GitHub Social Graph Sweep

**Status:** Partially rate-limited (unauthenticated public API, 60 req/hr shared IP)

| Source | Type | Status |
|--------|------|--------|
| plurigrid | org | ✅ snapshot via MCP (gorj, last push 2026-05-08) |
| kubeflow | org | ⚠️ rate-limited |
| TeglonLabs | org | ⚠️ rate-limited |
| bmorphism | user | ⚠️ rate-limited |
| zubyul | user | ⚠️ rate-limited |
| migalkin | social graph | ⚠️ rate-limited |
| DJedamski | social graph | ⚠️ rate-limited |
| wasita | social graph | ⚠️ rate-limited |
| kristinezheng | social graph | ⚠️ rate-limited |
| M1shaaa | social graph | ⚠️ rate-limited |
| AustinCStone | social graph | ⚠️ rate-limited |

**plurigrid/gorj** (confirmed via authenticated MCP):
- Language: Clojure
- Last push: 2026-05-08T14:04:34Z
- Description: MCP server + hooks that give AI coding agents a Clojure REPL

**DuckDB totals after this sweep:**
- world_increments: 34 rows (IDs 1–13, multiple sources per ID)
- repo_snapshots: 945 rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) queried against Aptos mainnet
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` → all returned `resource_not_found`.
Interpretation: accounts not yet activated on-chain or hold zero APT.

| World | Balance (APT) |
|-------|--------------|
| alice | 0.00 |
| bob | 0.00 |
| A–Z (26) | 0.00 each |

**Total APT across swarm:** 0.00

### Multisig Contract Probes (5 pairs)

All probed via `0x1::multisig_account::num_signatures_required` on Aptos mainnet.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...87003` | 2 | ✅ |
| A-G | `0xf56c4a1c...0096` | 2 | ✅ |
| Y-Z | `0xd3ffe181...b883` | 2 | ✅ |
| S-T | `0x3b1c3ae9...7883` | 2 | ✅ |
| V-W | `0x40fad7b4...eb6d` | 2 | ✅ |

**5/5 multisig contracts healthy** — all require 2 signatures (standard 2-of-N).

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. No REST API endpoints accessible at standard paths
(`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/coins`, `/api/pairs`).
Market data: **unavailable** (SPA requires browser-side JS execution to hydrate).

---

## Cumulative DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## GF(3) Color Chain

| id % 3 | trit | color | name |
|--------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | 1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

Full chain: `PLUS→MINUS→ERGODIC` × 4 cycles (IDs 1–12), then **PLUS** (ID 13)

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

## Notable Highlights (prior sweeps, IDs 1–12)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — pushed 2026-04-10
- **kubeflow/spark-operator**: 3,111 stars — pushed 2026-04-10
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP (Jane Street oxcaml_effect)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **Increment 12 (ERGODIC)**: sweep_complete closing the 4th full GF(3) cycle
- **Increment 13 (PLUS)**: this sweep — hamming swarm + multisig health check
