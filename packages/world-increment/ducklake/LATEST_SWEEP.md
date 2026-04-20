# World-Increment Sweep — 2026-04-20

## Sweep Metadata
- **Date:** 2026-04-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 50 | 44 |
| kubeflow | org | 47 | 33,914 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 50 | 119 |
| zubyul | user | 47 | 14 |
| migalkin | user | 19 | 278 |
| AustinCStone | user | 40 | 108 |
| DJedamski | user | 6 | 3 |
| wasita | user | 10 | 3 |
| kristinezheng | user | 6 | 0 |
| M1shaaa | user | 8 | 0 |
| **TOTAL** | | **287** | **34,485** |

> Note: GitHub REST API rate limit exhausted (60 req/hr unauthenticated). Data collected via GitHub MCP search API.

### Top Repos by Stars

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,587 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,125 | 2026-04-10 |
| kubeflow/spark-operator | Python | 3,116 | 2026-04-10 |
| kubeflow/trainer | Go | 2,085 | 2026-04-10 |
| kubeflow/katib | Go | 1,680 | 2026-04-02 |
| migalkin/kgcourse2021 | HTML | 25 | recently |
| plurigrid/asi | HTML | 17 | 2026-04-20 |
| bmorphism/shitcoin | Python | 5 | recently |

### plurigrid Activity (top recent pushes)
- `gorj` (Clojure) — 2026-04-20 (this repo)
- `asi` (HTML) — 2026-04-20
- `bci-blue-share` (HTML) — 2026-04-19
- `horse` (TeX) — 2026-04-19
- `nanoclj-zig` (Zig) — 2026-04-18
- `reafference` (HTML) — 2026-04-16
- `nash-portal` (Rust) — 2026-04-15

### GF(3) Color Chain Distribution (287 world increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 95 |
| +1 | `#b8bb26` | PLUS | 96 |
| -1 | `#cc241d` | MINUS | 96 |

GF(3) rule: `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) queried via Aptos mainnet fullnode.

**Result:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

Accounts **exist** on-chain (alice: `sequence_number=72`), but hold assets in custom store formats rather than the legacy CoinStore (e.g., `store_v2::ACSetMeta2` on alice). Stored as `-1.0` APT (sentinel: account exists, no CoinStore).

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | no CoinStore (seq=72) |
| bob | 0x0a3c00... | no CoinStore |
| A–Z | 0x8699ed...–0x7af0ef... | no CoinStore (×26) |

### Multisig Contract Probes — ALL HEALTHY ✓

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f4... | **2** | ✓ HEALTHY |
| A-G | 0xf56c4a... | **2** | ✓ HEALTHY |
| Y-Z | 0xd3ffe1... | **2** | ✓ HEALTHY |
| S-T | 0x3b1c3a... | **2** | ✓ HEALTHY |
| V-W | 0x40fad7... | **2** | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE via REST API** — Next.js SPA, no public REST endpoints (all paths return HTTP 404). Market data requires JS execution.

---

## DuckDB Schema

```sql
world_increments  — 287 rows  (GF3-annotated event log)
repo_snapshots    — 287 rows  (GitHub repo metadata)
aptos_snapshots   —  28 rows  (Hamming swarm wallets, sentinel -1.0)
multisig_probes   —   5 rows  (all healthy, 2-of-N)
mnx_snapshots     —   1 row   (unavailable marker)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`

## Notable Highlights
- **kubeflow/kubeflow**: 15,587 stars — flagship ML platform for Kubernetes
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) trit coloring
- **plurigrid/asi**: 17 stars — topological chemputer, pushed today
- **All 5 Aptos multisigs**: healthy, requiring 2-of-N sigs on mainnet
- **Hamming swarm**: 28 accounts confirmed on-chain, assets in custom stores (not legacy CoinStore)
