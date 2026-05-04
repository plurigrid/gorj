# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-04

## Sweep Metadata
- **Date:** 2026-05-04T15:08:22Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.2
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 402 |
| Total Repo Snapshots | 1323 |
| Sources Covered | 3 orgs + 8 users (11 sources) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain

GF(3) chain cycling: **ERGODIC (#d3869b) → PLUS (#b8bb26) → MINUS (#cc241d)** per `id mod 3`

| GF3 Name | Trit | Color | Count (this sweep) |
|----------|------|-------|-------------------|
| ERGODIC | 0 | `#d3869b` | 133 |
| PLUS | +1 | `#b8bb26` | 135 |
| MINUS | -1 | `#cc241d` | 134 |

---

## GitHub Social Graph Sweep

### Sources + Repo Counts

| Source | Type | Repos This Sweep |
|--------|------|-----------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 47 |
| zubyul | user | 49 |
| AustinCStone | social-graph | 30 |
| migalkin | social-graph | 19 |
| M1shaaa | social-graph | 8 |
| wasita | social-graph | 10 |
| kristinezheng | social-graph | 6 |
| DJedamski | social-graph | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **379** |

### Most Recently Pushed

| Org/User | Repo | Pushed At |
|----------|------|-----------|
| plurigrid | gorj | 2026-05-04T14:27:37Z |
| kubeflow | hub | 2026-05-04T14:21:21Z |
| M1shaaa | M1shaaa | 2026-05-04T13:51:23Z |
| kubeflow | kale | 2026-05-04T12:38:49Z |
| bmorphism | Gay.jl | 2026-05-04T00:31:32Z |
| kubeflow | pipelines | 2026-05-01T19:55:52Z |

### Top Languages

| Language | Count |
|----------|-------|
| Python | 232 |
| Rust | 57 |
| JavaScript | 53 |
| Go | 51 |
| HTML | 51 |
| TypeScript | 47 |
| Jupyter Notebook | 40 |
| Clojure | 29 |
| Jsonnet | 24 |
| R | 22 |

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-05-04)

All 28 wallets queried via Aptos fullnode REST API. All show **0.0 APT** balance — accounts exist on-chain but hold no native coin. Consistent with pure multisig / resource-account usage.

| World | Address (prefix) | APT |
|-------|-----------------|-----|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A–Z (26) | (see DB) | 0.0 each |

### Multisig Contract Probes

All 5 multisig accounts **healthy** · **2-of-2 signatures required**

| Pair | Address (prefix) | Sigs | Healthy |
|------|-----------------|------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — Next.js SPA; no REST API accessible. `mnx_snapshots` table is empty this sweep.

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

## Notable Highlights
- **kubeflow/kubeflow**: flagship ML platform for Kubernetes (most-starred in sweep)
- **plurigrid/gorj**: this repo — last pushed 2026-05-04T14:27:37Z
- **bmorphism/Gay.jl**: active Julia work, pushed today (2026-05-04)
- **migalkin/NodePiece**: scalable KG embeddings — top ML stars in social graph
- **AustinCStone**: 30 repos, research ML/vision focus
- **All 5 multisig pairs**: 2-of-2 healthy — Hamming swarm topology intact
- **28 Aptos wallets**: 0 APT balances — pure resource/multisig usage confirmed
