# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-30
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|----------|-------|------|
| 1 | AustinCStone | social | 40 | +1 | `#b8bb26` | **PLUS** |
| 2 | DJedamski | social | 6 | -1 | `#cc241d` | **MINUS** |
| 3 | M1shaaa | social | 8 | 0 | `#d3869b` | **ERGODIC** |
| 4 | TeglonLabs | org | 4 | +1 | `#b8bb26` | **PLUS** |
| 5 | bmorphism | user | 100 | -1 | `#cc241d` | **MINUS** |
| 6 | kristinezheng | social | 6 | 0 | `#d3869b` | **ERGODIC** |
| 7 | kubeflow | org | 48 | +1 | `#b8bb26` | **PLUS** |
| 8 | migalkin | social | 19 | -1 | `#cc241d` | **MINUS** |
| 9 | plurigrid | org | 100 | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita | social | 11 | +1 | `#b8bb26` | **PLUS** |
| 11 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

**Total:** 391 repos snapped · 644 unique full_names in DB (pagination overlaps captured multiple star-count snapshots)

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,690 | — |
| kubeflow/pipelines | 4,150 | Python |
| kubeflow/spark-operator | 3,124 | Python |
| kubeflow/trainer | 2,107 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,463 | Jsonnet |
| kubeflow/manifests | 1,019 | YAML |
| kubeflow/arena | 811 | Go |

### Language Distribution (top 10)

| Language | Count |
|----------|-------|
| Python | 235 |
| Rust | 57 |
| JavaScript | 53 |
| HTML | 51 |
| Go | 51 |
| TypeScript | 47 |
| Jupyter Notebook | 40 |
| Clojure | 30 |
| Jsonnet | 23 |
| R | 22 |

### Notable Recent Activity

- **M1shaaa/M1shaaa** — pushed 2026-05-30 (today)
- **wasita/wasita.github.io** — pushed 2026-05-20 (Svelte personal site)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-05-14
- **TeglonLabs/mathpix-gem** — pushed 2026-01-01 (Ruby, 11 open issues)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) against Aptos mainnet fullnode.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac… | 0.00 |
| bob | 0x0a3c00… | 0.00 |
| A | 0x8699ed… | 0.00 |
| B | 0x3f892e… | 0.00 |
| C | 0x38b99e… | 0.00 |
| D | 0xf77656… | 0.00 |
| E | 0xdc1d9d… | 0.00 |
| F | 0x18a14b… | 0.00 |
| G | 0x69a394… | 0.00 |
| H | 0xce67c3… | 0.00 |
| I | 0x070fe5… | 0.00 |
| J | 0x4d964d… | 0.00 |
| K | 0xa73204… | 0.00 |
| L | 0x7c2eae… | 0.00 |
| M | 0x6fed37… | 0.00 |
| N | 0xe7dde6… | 0.00 |
| O | 0x73252b… | 0.00 |
| P | 0x621879… | 0.00 |
| Q | 0xac40fa… | 0.00 |
| R | 0x7ce605… | 0.00 |
| S | 0xb87530… | 0.00 |
| T | 0x35781d… | 0.00 |
| U | 0x75860d… | 0.00 |
| V | 0xb59dd8… | 0.00 |
| W | 0x5f32ae… | 0.00 |
| X | 0xa95cbb… | 0.00 |
| Y | 0xd8e328… | 0.00 |
| Z | 0x7af0ef… | 0.00 |

**Status:** All wallets show 0 APT. Accounts either unfunded or CoinStore not registered on mainnet.

### Multisig Contract Probes (Aptos Mainnet)

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

**Status:** All 5 multisig contracts live on mainnet with `num_signatures_required = 2`. All healthy (2-of-2 threshold).

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable for API scraping. `https://testnet.mnx.fi` serves a Next.js SPA; `/api/markets` and `/api/v1/markets` return the same HTML shell — no JSON market data embedded. No `mnx_snapshots` rows inserted.

---

## DuckDB Ducklake Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 34 (cumulative, 11 new sources this sweep) |
| repo_snapshots | 1,335 (644 unique repos) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (API unavailable) |

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
- **kubeflow/kubeflow**: 15,690 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,150 stars — ML pipelines (pushed since last sweep)
- **kubeflow/spark-operator**: 3,124 stars — Kubernetes operator for Apache Spark
- **Hamming swarm**: 5 multisig contracts all live 2-of-2, wallets uniformly empty
- **M1shaaa** most recently active — pushed today (2026-05-30)
- **MNX testnet**: SPA-only, no machine-readable market feed detected

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*
