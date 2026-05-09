# World-Increment Sweep + Hamming Snapshot — 2026-05-09

## Sweep Metadata
- **Date:** 2026-05-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 359 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain — 11 Increments

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1  | AustinCStone (user) | +1 | `#b8bb26` | **PLUS** |
| 2  | DJedamski (user) | -1 | `#cc241d` | **MINUS** |
| 3  | M1shaaa (user) | 0 | `#d3869b` | **ERGODIC** |
| 4  | TeglonLabs (org) | +1 | `#b8bb26` | **PLUS** |
| 5  | bmorphism (user) | -1 | `#cc241d` | **MINUS** |
| 6  | kristinezheng (user) | 0 | `#d3869b` | **ERGODIC** |
| 7  | kubeflow (org) | +1 | `#b8bb26` | **PLUS** |
| 8  | migalkin (user) | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid (org) | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita (user) | +1 | `#b8bb26` | **PLUS** |
| 11 | zubyul (user) | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Repo Counts by Source

| Source | Type | Repos | Stars | Latest Push |
|--------|------|------:|------:|-------------|
| plurigrid | org | 100 | 71 | 2026-05-09 |
| bmorphism | user | 100 | 248 | 2026-05-09 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| kubeflow | org | 48 | 34,030 | 2026-05-09 |
| migalkin | user (zubyul graph) | 19 | 279 | 2025-08-04 |
| wasita | user (zubyul graph) | 11 | 4 | 2026-05-06 |
| AustinCStone | user (zubyul graph) | 8 | 107 | 2026-04-01 |
| M1shaaa | user (zubyul graph) | 8 | 0 | 2026-02-04 |
| kristinezheng | user (zubyul graph) | 6 | 0 | 2026-04-09 |
| DJedamski | user (zubyul graph) | 6 | 3 | 2018-03-07 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |
| **TOTAL** | | **359** | **34,758** | |

### Notable Repos

- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — ML pipeline orchestration
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Spark
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **AustinCStone/TextGAN**: 92 stars — GAN-based text generation
- **bmorphism**: 100 repos, latest push 2026-05-09 (extremely active)
- **plurigrid/gorj**: Clojure, latest push 2026-05-09 (this very repo)
- **TeglonLabs/mathpix-gem**: Ruby gem for mathematical OCR
- **wasita/vocoder**: JS vocoder, pushed 2026-05-06

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1`.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...cc7b | 0.0 | No CoinStore (acct seq=72) |
| bob | 0x0a3c...2d5d | 0.0 | No CoinStore |
| A–Z (26 addrs) | various | 0.0 each | No CoinStore |

**Note:** All accounts exist on-chain but lack `0x1::coin::CoinStore<AptosCoin>` resources.
Addresses may use the Fungible Assets (FA) standard or hold zero balance.

**Total APT across swarm:** 0.0 APT

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...3003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts operational** — uniform 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

- Site responds (293 KB SPA)
- `/api/markets`, `/api/v1/markets`, `/api/tickers` → HTTP 404
- `/markets` → SPA HTML (no JSON)
- **Status: Unavailable** — SPA requires JS execution; no public REST endpoint found

---

## DuckDB Schema

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
