# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-16

## Sweep Metadata
- **Date:** 2026-04-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) Increment #25:** trit=1 PLUS `#b8bb26`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 25 |
| Total Repo Snapshots | 1,183 |
| Sources Covered | 3 orgs + 8 users + social graph |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### This Run — Repos Snapshotted

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| bmorphism | user | 99 | 248 | 2026-04-09 |
| plurigrid | org | 50 | 43 | 2026-04-16 |
| kubeflow | org | 47 | 33,887 | 2026-04-16 |
| zubyul | user | 11 | 5 | 2026-04-13 |
| AustinCStone | social-graph | 6 | 107 | 2026-04-01 |
| migalkin | social-graph | 6 | 276 | 2026-03-11 |
| wasita | social-graph | 5 | 2 | 2026-04-13 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |
| DJedamski | social-graph | 4 | 2 | 2023-04-21 |
| M1shaaa | social-graph | 4 | 0 | 2026-02-04 |
| kristinezheng | social-graph | 3 | 0 | 2026-04-09 |
| **TOTAL** | | **239** | **34,572** | |

### Notable Repos (Most Recent Activity)

- `plurigrid/reafference` — latest push 2026-04-16 (HTML)
- `kubeflow/pipelines` — 4,120 stars, Python, pushed 2026-04-16
- `kubeflow/spark-operator` — 3,111 stars, pushed 2026-04-16
- `zubyul/nash-web` — NASH token browser TUI (Rust), pushed 2026-04-13
- `zubyul/nash-tui` — NASH TUI real-time candles (Rust), pushed 2026-04-13
- `wasita/wasita.github.io` — personal website (Svelte), pushed 2026-04-13
- `migalkin/NodePiece` — 143 stars, KG representations (Python)
- `AustinCStone/TextGAN` — 92 stars, TF text generation (Python)
- `bmorphism/shitcoin` — 5 stars (Python), pushed 2026-04-09

### Zubyul Social Graph

- **migalkin**: KG researcher — NodePiece (143⭐), StarE (88⭐), NBFNet MLX (10⭐)
- **wasita**: Svelte/TypeScript dev — active site + ch3-lib (Typst)
- **AustinCStone**: ML/CV — TextGAN (92⭐), StereoVisionMRF (11⭐)
- **DJedamski**: Data science/Kaggle competitions
- **kristinezheng**: Neuroscience + HCI (MIT Lookit studies, HackMIT)
- **M1shaaa**: Lab research tools (Yale/MIT)

### GF(3) Color Chain — Increment Table

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| … | *(prior sweeps)* | … | … | … | … |
| 25 | world-increment-sweep | github-snapshot | +1 | `#b8bb26` | **PLUS** |

GF(3) assignment: `id%3==0` → ERGODIC `#d3869b` · `id%3==1` → PLUS `#b8bb26` · `id%3==2` → MINUS `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger ~v4,888,436,901)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned
`resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Accounts have no initialized APT coin store on mainnet at this ledger version.
All balances recorded as `NULL` in `aptos_snapshots`.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...4cc7b | — |
| bob   | 0x0a3c...512d5d | — |
| A–Z   | *(26 addresses)* | — |

### Multisig Contract Probes — ALL HEALTHY ✓

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|--------------------:|:-------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisig contracts healthy. All require 2-of-N signatures.**

### MNX Markets (`testnet.mnx.fi`)

Returns a Next.js SPA — no JSON API exposed at `/api/markets` or `/api/v1/markets`.
Market data is rendered client-side only. `mnx_snapshots` table: **0 rows** this run.

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

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*
*DuckDB: `packages/world-increment/ducklake/world-increments.duckdb`*
