# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 319 |
| Total Repo Snapshots | 319 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution (319 increments)

| GF3 Name | GF3 Trit | Color | Count |
|----------|----------|-------|-------|
| ERGODIC | 0 | #d3869b | 106 |
| PLUS | +1 | #b8bb26 | 107 |
| MINUS | -1 | #cc241d | 106 |

GF(3) chain cycles perfectly across 319 repo snapshots (106+107+106).

---

## Top Repos by Stars (this sweep)

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,803 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,173 | 2026-08-01 |
| kubeflow/spark-operator | Python | 3,141 | 2026-07-31 |
| kubeflow/trainer | Go | 2,165 | 2026-07-31 |
| kubeflow/katib | Python | 1,695 | 2026-07-26 |
| kubeflow/examples | Jsonnet | 1,461 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-07-29 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| plurigrid/asi | HTML | 58 | 2026-07-10 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | user | 5 |
| wasita | user | 3 |
| AustinCStone | user | 3 |
| M1shaaa | user | 2 |
| kristinezheng | user | 2 |
| DJedamski | user | 1 |
| **TOTAL** | | **319** |

### Most Active (Recently Pushed)

- **plurigrid/gorj** (Clojure) — 2026-08-01 (this repo!)
- **kubeflow/docs-agent, kale, pipelines** — 2026-08-01
- **bmorphism/Gay.jl** (Julia) — 2026-08-01
- **wasita/wasita.github.io** (Svelte) — 2026-07-21
- **TeglonLabs/jank-crane** (C++, "GF3 convergence maps") — 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)

All 28 wallets (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`.
No APT CoinStore registered on mainnet for any probed address. **All balances = 0 APT.**

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793ac...4cc7b | 0.0 |
| bob | 0x0a3c00...512d5d | 0.0 |
| A | 0x8699ed...9d7a | 0.0 |
| B–Z | (25 more addresses) | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts responded on mainnet with consistent configuration:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f4...87003 | 2 | ✓ |
| A-G | 0xf56c4a...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ |
| S-T | 0x3b1c3a...d7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — uniform 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. Probed `/api/markets` and `/api/v1/markets` — both return the HTML shell.
**Status: UNAVAILABLE** — no public REST API; market data requires browser JS execution.

---

## DuckDB Storage Summary

| Table | Rows |
|-------|------|
| world_increments | 319 |
| repo_snapshots | 319 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,803 stars — ML platform for Kubernetes (up from 15,565 in Apr sweep)
- **kubeflow/pipelines**: 4,173 stars — pushed 2026-08-01 (active today)
- **TeglonLabs/jank-crane**: new C++ repo with "GF3 convergence maps" in description
- **migalkin/NodePiece**: 144 stars — ICLR'22 KG embeddings
- **bmorphism/Gay.jl**: most recently active bmorphism repo (Julia, pushed today)
- **plurigrid/gorj**: This repo — pushed 2026-08-01 (active sweep target)
- **All multisig contracts**: uniform 2-of-N, all healthy on mainnet
