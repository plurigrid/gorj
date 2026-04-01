# World-Increment Sweep — 2026-04-01

## Sweep Metadata
- **Date:** 2026-04-01
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 529 |
| Total Repo Snapshots | 469 |
| Total Aptos Snapshots | 28 |
| Total Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users + events |

---

## GitHub Social Graph Sweep

### Sources Queried
| Type | Source | Repos |
|------|--------|-------|
| Org  | plurigrid | 100 |
| Org  | kubeflow | 46 |
| Org  | TeglonLabs | 53 |
| User | bmorphism | 100 |
| User | zubyul | 23 |
| User | migalkin | 30 |
| User | DJedamski | 11 |
| User | wasita | 29 |
| User | kristinezheng | 18 |
| User | M1shaaa | 16 |
| User | AustinCStone | 43 |
| Events | bmorphism | 30 events |
| Events | zubyul | 30 events |

**Total repos:** 469 | **Total events:** 60 | **Total world_increments:** 529

### Top 10 Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15549 | — |
| kubeflow/pipelines | 4118 | Python |
| kubeflow/spark-operator | 3110 | Python |
| kubeflow/trainer | 2070 | Go |
| kubeflow/katib | 1674 | Python |
| kubeflow/examples | 1459 | Jsonnet |
| kubeflow/manifests | 1006 | YAML |
| kubeflow/arena | 809 | Go |
| kubeflow/kale | 681 | Python |
| kubeflow/mpi-operator | 519 | Go |

---

## Aptos Hamming Swarm Snapshot

All 28 addresses queried against Aptos mainnet fullnode. All returned HTTP 404 — accounts have no APT CoinStore resource (unfunded / non-existent on mainnet).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acdec12b... | null (404) |
| bob | 0x0a3c00c58fdf... | null (404) |
| A–Z | (all 26 addresses) | null (404) |

All 28 wallets: **balance = null** (accounts not initialized on Aptos mainnet).

---

## Multisig Probe Results

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c0... | 2 | Yes |
| A-G | 0xf56c4a1c0906... | 2 | Yes |
| Y-Z | 0xd3ffe1812b2d... | 2 | Yes |
| S-T | 0x3b1c3ae905d4... | 2 | Yes |
| V-W | 0x40fad7b423a8... | 2 | Yes |

All 5 multisig contracts are **healthy** and require **2 signatures**.

---

## MNX Market Status

- `https://testnet.mnx.fi/api/markets` — **404 Not Found**
- `https://testnet.mnx.fi/api/v1/markets` — **404 Not Found**
- `https://testnet.mnx.fi` — Returns Next.js SPA (no JSON market data accessible via unauthenticated REST)

**Status: MNX testnet API endpoints unavailable.** Recorded as unavailable in mnx_snapshots table.

---

## GF(3) Color Chain Stats

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 176 |
| PLUS | +1 | #b8bb26 | 177 |
| MINUS | -1 | #cc241d | 176 |

**Total world_increments:** 529 (469 repo snapshots + 60 events)

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,549 stars — most starred ML infra org on GitHub
- **kubeflow/pipelines**: 4,118 stars — ML pipeline orchestration for Kubernetes
- **kubeflow/spark-operator**: 3,110 stars — Kubernetes operator for Apache Spark
- All 5 multisig contracts healthy with 2-of-N threshold
- Aptos mainnet wallets: all 28 addresses unfunded / not initialized
- MNX testnet markets API: unavailable (SPA only, no public REST)
