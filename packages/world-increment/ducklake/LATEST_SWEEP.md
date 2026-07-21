# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 50 |
| kubeflow | org | 30 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social-graph | 5 |
| wasita | social-graph | 3 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| AustinCStone | social-graph | 4 |
| DJedamski | social-graph | 3 |

**Total this run:** 205 repo snapshots. **Cumulative in DB:** 1149 repo_snapshots, 228 world_increments.

### GF(3) Color Chain (this sweep, increments by ID mod 3)

- `id%3==0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id%3==1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id%3==2` → trit=-1, color=`#cc241d`, name=**MINUS**

Chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → …`

### Top Repos by Stars (this sweep)

| Org/User | Repo | Stars | Language | Pushed |
|----------|------|-------|----------|--------|
| kubeflow | kubeflow | 15,788 | — | 2026 |
| kubeflow | pipelines | 4,169 | Python | 2026 |
| kubeflow | spark-operator | 3,142 | Go | 2026 |
| migalkin | NodePiece | 144 | Python | 2026-05 |
| AustinCStone | TextGAN | 92 | Python | 2025 |
| migalkin | StarE | 89 | Python | 2026-04 |
| AustinCStone | StereoVisionMRF | 11 | Python | 2026 |
| migalkin | kgcourse2021 | 24 | HTML | 2026-07 |
| plurigrid | asi | 31 | HTML | 2026-07 |

### Recent Activity Highlights

- `plurigrid/gorj` — pushed **2026-07-21 today**; 1297 open issues; Clojure GF(3) REPL orchestration
- `wasita/wasita.github.io` — pushed **2026-07-20**; Svelte personal site
- `migalkin/kgcourse2021` — pushed **2026-07-10**; knowledge graphs course
- `AustinCStone/byteruckus` — pushed **2026-07-15** (new repo, HTML)
- `wasita/pnas-typst-template` — pushed **2026-07-16** (new fork)
- `TeglonLabs/jank-crane` — pushed **2026-06-08**; C++; "crane-jank converged-IR hub: GF3 convergence maps"
- `plurigrid/asi` — pushed **2026-07-10**; 31 ⭐; "everything is topological chemputer!"
- `zubyul/voice-observatory` — pushed **2026-04-24**; "Passive macOS TUI observing voice-download pathways — companion to bmorphism/say-mcp-server"

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

**Status:** All 28 wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These wallets exist on-chain but have **no initialized APT CoinStore** — they are new or unfunded accounts.

| World | Address | APT Balance |
|-------|---------|------------|
| alice | 0xc793acdec1...4cc7b | — (no CoinStore) |
| bob | 0x0a3c00c58f...512d5d | — (no CoinStore) |
| A–Z (26 addresses) | various | — (no CoinStore) |

All 28 recorded as NULL in `aptos_snapshots`.

### Multisig Contract Probes (Aptos mainnet)

All 5 multisig pairs are **HEALTHY** at 2-of-2 threshold:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — All probed API paths (`/api/markets`, `/api/v1/markets`, `/api/v2/markets`, `/markets`) return the HTML SPA shell with no embedded JSON market data. No REST endpoint surfaced without browser JS execution. Recorded as `SPA_NO_API` in `mnx_snapshots`.

---

## DuckDB Table State

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Cumulative Rows |
|-------|----------------|
| world_increments | 228 |
| repo_snapshots | 1149 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

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
