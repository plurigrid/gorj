# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-02

## Sweep Metadata
- **Date:** 2026-05-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Previous sweep:** 2026-04-12 (471 snapshots, 12 increments)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 317 |
| Total Repo Snapshots | 317 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 (all healthy) |
| Total APT in Swarm | ~20.28 APT |

---

## JOB 1: GitHub Social Graph Sweep

### Sources & Repo Counts

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 47 | 33,986 | 2026-05-01 |
| migalkin | user (zubyul graph) | 5 | 267 | 2026-04-16 |
| bmorphism | user | 100 | 247 | 2026-05-02 |
| AustinCStone | user (zubyul graph) | 3 | 103 | 2026-04-01 |
| plurigrid | org | 100 | 65 | 2026-05-02 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| wasita | user (zubyul graph) | 3 | 3 | 2026-04-28 |
| TeglonLabs | org | 4 | 2 | 2026-01-01 |
| DJedamski | user (zubyul graph) | 2 | 1 | 2023-04-21 |
| kristinezheng | user (zubyul graph) | 2 | 0 | 2026-04-09 |
| M1shaaa | user (zubyul graph) | 2 | 0 | 2026-02-04 |
| **TOTAL** | | **317** | **34,688** | |

### GF(3) Color Chain Distribution
- `id mod 3 == 0` → trit=0, `#d3869b` ERGODIC: **105 increments**
- `id mod 3 == 1` → trit=+1, `#b8bb26` PLUS: **106 increments**
- `id mod 3 == 2` → trit=-1, `#cc241d` MINUS: **106 increments**

### Notable Repos

**kubeflow** (47 repos, 33,986 total stars)
- `kubeflow/kubeflow` — 15,565★ ML platform for Kubernetes
- `kubeflow/pipelines` — 4,119★ Python, pushed 2026-05-01
- `kubeflow/spark-operator` — 3,111★ Python, pushed 2026-05-01
- `kubeflow/trainer` — 2,080★ Go

**migalkin** (knowledge graphs)
- `migalkin/NodePiece` — 143★ Python, ICLR'22, pushed 2026-03-02
- `migalkin/StarE` — 89★ Python, EMNLP 2020, pushed 2026-04-16
- `migalkin/kgcourse2021` — 25★ HTML, pushed 2026-02-16

**bmorphism** (100 repos, most recently pushed 2026-05-02)
- Active plurigrid contributor, most recent push today

**AustinCStone**
- `AustinCStone/TextGAN` — 92★ Python, TF text generation
- `AustinCStone/StereoVisionMRF` — 11★ Python

**TeglonLabs**
- `TeglonLabs/mathpix-gem` — Ruby, math→LaTeX OCR gem
- `TeglonLabs/coin-flip-mcp` — JS, random.org MCP server (2 forks)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 2026-05-02

Queried via `0x1::coin::balance` view function on `fullnode.mainnet.aptoslabs.com`.

| World | Balance (APT) | Address (truncated) |
|-------|---------------|---------------------|
| bob | **12.657007** | 0x0a3c00...12d5d |
| F | **1.960516** | 0x18a14b...3cf71 |
| L | **1.927269** | 0x7c2eae...eba9 |
| J | **1.895093** | 0x4d964d...7f54 |
| alice | 0.436434 | 0xc793ac...cc7b |
| O | 0.210136 | 0x73252b...a89d |
| K | 0.161961 | 0xa73204...dc4 |
| P | 0.140136 | 0x621879...948 |
| M | 0.112285 | 0x6fed37...f2e9 |
| N | 0.106121 | 0xe7dde6...b2c |
| Q | 0.103240 | 0xac40fa...89a9 |
| S | 0.091788 | 0xb87530...386 |
| R | 0.090217 | 0x7ce605...6e10 |
| T | 0.073713 | 0x357810...588 |
| U | 0.055773 | 0x758600...956 |
| A | 0.051767 | 0x8699ed...c7a |
| V | 0.048833 | 0xb59dd8...2c3 |
| Y | 0.044449 | 0xd8e328...4c4 |
| X | 0.042577 | 0xa95cbb...47d |
| W | 0.040705 | 0x5f32ae...7b0 |
| B | 0.036256 | 0x3f892e...b13 |
| Z | 0.024268 | 0x7af0ef...97c |
| D | 0.011629 | 0xf77656...dd1 |
| C | 0.010185 | 0x38b99e...35e |
| E | 0.009372 | 0xdc1d9d...d36 |
| H | 0.001681 | 0xce67c3...00f |
| G | 0.000681 | 0x69a394...f32 |
| I | 0.000681 | 0x070fe5...c9 |

**Total APT in swarm:** ~20.28 APT
**Top holders:** bob (12.66), F (1.96), L (1.93), J (1.90)

### Multisig Contract Probes

All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7...b6d | 2 | ✓ HEALTHY |

All 5 multisig accounts require 2-of-N signatures and are responsive on mainnet.

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable — site returns a Next.js SPA with no accessible JSON API at `/api/markets`. Market data requires browser JS execution. `mnx_snapshots` table has 0 rows.

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
