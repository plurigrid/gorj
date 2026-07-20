# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 12 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 41 |

**Total this sweep:** 394 repos across 11 sources

### Top Starred Repos (this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,783 | — | 2026-07-10 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-19 |
| kubeflow/spark-operator | 3,140 | Python | 2026-07-17 |
| kubeflow/trainer | 2,152 | Go | 2026-07-19 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |
| migalkin/NBFNet_mlx | 10 | Python | 2026-03-11 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |

### Notable Activity (freshest pushes)

| Repo | Pushed | Note |
|------|--------|------|
| kubeflow/pipelines | 2026-07-19 | Very recent — active MLOps |
| kubeflow/trainer | 2026-07-19 | Very recent — distributed training |
| kubeflow/spark-operator | 2026-07-17 | Active Spark-on-K8s |
| wasita/wasita.github.io | 2026-07-16 | Personal site, 8 open issues |
| wasita/pnas-typst-template | 2026-07-16 | Brand-new repo (created same day) |
| AustinCStone/byteruckus | 2026-07-15 | Brand-new repo |
| migalkin/kgcourse2021 | 2026-07-10 | KG course still maintained |
| TeglonLabs/jank-crane | 2026-06-08 | GF3 convergence maps, C++ |

### GF(3) Color Chain — New Increments (this run)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1 | plurigrid (org) | +1 | `#b8bb26` | **PLUS** |
| 2 | kubeflow (org) | -1 | `#cc241d` | **MINUS** |
| 3 | TeglonLabs (org) | 0 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism (user) | +1 | `#b8bb26` | **PLUS** |
| 5 | zubyul (user) | -1 | `#cc241d` | **MINUS** |
| 6 | migalkin (social) | 0 | `#d3869b` | **ERGODIC** |
| 7 | wasita (social) | +1 | `#b8bb26` | **PLUS** |
| 8 | DJedamski (social) | -1 | `#cc241d` | **MINUS** |
| 9 | kristinezheng (social) | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (social) | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (social) | -1 | `#cc241d` | **MINUS** |

GF(3) assignment: `id mod 3 == 0 → ERGODIC (#d3869b)` · `id mod 3 == 1 → PLUS (#b8bb26)` · `id mod 3 == 2 → MINUS (#cc241d)`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses probed via Aptos fullnode REST API against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**All wallets: 0.0 APT.** Accounts are registered on-chain but the native APT coin store holds no balance at this timestamp.

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig contracts: 2-of-2, HEALTHY.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel authentication wall (password-protected deployment). No market data accessible without visitor credentials.

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,265 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

Database: `packages/world-increment/ducklake/world-increments.duckdb`

---

## Schema

```sql
CREATE TABLE world_increments (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
);
CREATE TABLE repo_snapshots (
  id INTEGER, timestamp TIMESTAMP DEFAULT now(), increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
);
CREATE TABLE aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR, address VARCHAR, balance_apt DOUBLE
);
CREATE TABLE multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR, address VARCHAR, sigs_required INTEGER, healthy BOOLEAN
);
CREATE TABLE mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
);
```
