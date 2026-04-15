# World-Increment Sweep + Hamming Snapshot

**Date/Time:** 2026-04-15T00:00:00Z
**Agent:** world-increment-sweep
**DuckDB version:** v1.5.2 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos Collected |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 53 |
| bmorphism | user | 100 |
| zubyul | user | 24 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| wasita | user | 31 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| **TOTAL** | | **473** |

**Public events also collected:** 60 (30 each for bmorphism and zubyul)

### Top 10 Repos by Stars

| Rank | Full Name | Stars | Language |
|------|-----------|------:|----------|
| 1 | kubeflow/kubeflow | 15575 | — |
| 2 | kubeflow/pipelines | 4119 | Python |
| 3 | kubeflow/spark-operator | 3114 | Python |
| 4 | kubeflow/trainer | 2083 | Go |
| 5 | kubeflow/katib | 1678 | Python |
| 6 | kubeflow/examples | 1460 | Jsonnet |
| 7 | kubeflow/manifests | 1010 | YAML |
| 8 | kubeflow/arena | 809 | Go |
| 9 | kubeflow/kale | 683 | Python |
| 10 | kubeflow/mpi-operator | 523 | Go |

---

## Aptos Hamming Swarm Snapshot

### Wallet Balances

All 28 wallets queried against Aptos mainnet fullnode (ledger version ~4876511516).
All returned `resource_not_found` — CoinStore not initialized (no APT holdings).

| Label | Address (truncated) | APT Balance |
|-------|--------------------:|------------:|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

---

## Multisig Contract Probes

All 5 multisig contracts successfully probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|--------------------:|:-------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts are healthy with 2-of-N signature threshold.

---

## MNX Markets Status

**Status:** UNAVAILABLE (structured data)

- `https://testnet.mnx.fi/api/markets` returns a Next.js HTML page, not JSON
- No machine-readable market data accessible via public API
- `mnx_snapshots` table: 0 rows this sweep

---

## GF(3) Color Chain Statistics

World increment rows assigned GF(3) trits by `row_id % 3`:

| Trit | Name | Color | Rule | Count |
|-----:|------|-------|------|------:|
| 0 | ERGODIC | #d3869b | id % 3 == 0 | 11 |
| +1 | PLUS | #b8bb26 | id % 3 == 1 | 13 |
| -1 | MINUS | #cc241d | id % 3 == 2 | 12 |

**Total world_increments rows (cumulative):** 36

### GF(3) Chain — Current Sweep Sources (13 entries)
```
plurigrid(1)=PLUS → kubeflow(2)=MINUS → TeglonLabs(3)=ERGODIC →
bmorphism(4)=PLUS → zubyul(5)=MINUS → migalkin(6)=ERGODIC →
DJedamski(7)=PLUS → wasita(8)=MINUS → kristinezheng(9)=ERGODIC →
M1shaaa(10)=PLUS → AustinCStone(11)=MINUS → events_bmorphism(12)=ERGODIC →
events_zubyul(13)=PLUS
```

---

## DuckDB Storage Summary

**Database path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|-----:|-------------|
| world_increments | 36 | GF(3)-colored source sweep events |
| repo_snapshots | 1417 | All GitHub repos collected (cumulative) |
| aptos_snapshots | 28 | Aptos wallet balances (all 0.0 APT) |
| multisig_probes | 5 | Multisig threshold probes (all healthy, sigs=2) |
| mnx_snapshots | 0 | MNX Markets (unavailable) |

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

## Notable Highlights

- **kubeflow/kubeflow**: 15,575 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,114 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: topological chemputer project
- All 5 Aptos multisig contracts operational (2-of-N threshold)
- All 28 Aptos wallets: 0.0 APT (CoinStore not initialized on mainnet)
