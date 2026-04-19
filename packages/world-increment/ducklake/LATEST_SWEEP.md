# World Increment + Hamming Swarm Snapshot — 2026-04-19

## Sweep Metadata
- **Date:** 2026-04-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Increment ID:** 13 — GF(3) **PLUS** `#b8bb26` (trit=1, id%3=1)
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 13 |
| Total Repo Snapshots | 949 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts | 5 (all healthy) |
| MNX Markets | 25 |

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Repos | Notes |
|--------|------|-------|-------|
| plurigrid/gorj | repo (MCP) | 1 | ✓ snapshotted |
| kubeflow | org | — | ✗ rate-limited (unauthenticated API) |
| TeglonLabs | org | — | ✗ rate-limited (unauthenticated API) |
| bmorphism | user | — | ✗ rate-limited (unauthenticated API) |
| zubyul | user | — | ✗ rate-limited (unauthenticated API) |
| zubyul social graph | 6 users | — | ✗ rate-limited (unauthenticated API) |

> `gh` CLI unavailable; GITHUB_TOKEN absent; MCP scoped to plurigrid/gorj only. Previous sweeps (increments 1–12) captured 471 repos across all sources.

### plurigrid/gorj Snapshot
| Field | Value |
|-------|-------|
| Language | Clojure |
| Description | MCP server + hooks giving AI coding agents a Clojure REPL |
| Last push | 2026-04-14T18:07:32Z |
| Active sweep branches | 50+ (world-increment/sweep-2026-03-26 → present) |
| Head commit | `ebf263f` |

### GF(3) Color Chain — All 13 Increments

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1  | plurigrid (org) | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (sweep_complete) | 0 | `#d3869b` | **ERGODIC** |
| 13 | gorj (this sweep) | +1 | `#b8bb26` | **PLUS** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Epoch:** 15492 | **Block:** 721,782,328 | **Probed:** 2026-04-19T05:11:45Z

All 28 wallets returned `resource_not_found` for `CoinStore<AptosCoin>` — addresses hold 0 APT (no coin store initialized).

| World | Address (prefix) | APT |
|-------|-----------------|-----|
| alice | 0xc793… | 0.0 |
| bob   | 0x0a3c… | 0.0 |
| A–Z   | (26 addresses) | 0.0 each |

**Total swarm APT: 0.0**

### Multisig Contract Probes — All HEALTHY

All 5 contracts confirmed live with 2-of-N threshold via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B  | 0x0da4… | 2 | ✓ healthy |
| A-G  | 0xf56c… | 2 | ✓ healthy |
| Y-Z  | 0xd3ff… | 2 | ✓ healthy |
| S-T  | 0x3b1c… | 2 | ✓ healthy |
| V-W  | 0x40fa… | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi) — 25 Markets

| Ticker | Name | Category | Price |
|--------|------|----------|-------|
| NVDA | NVIDIA | stock | $201.11 |
| AAPL | Apple | stock | $270.26 |
| MSFT | Microsoft | stock | $422.86 |
| TSLA | Tesla | stock | $401.35 |
| GOOGL | Alphabet | stock | $340.98 |
| AMZN | Amazon | stock | $250.90 |
| META | Meta | stock | $686.53 |
| INTC | Intel | stock | $68.29 |
| TSM | TSMC | stock | $369.80 |
| MU | Micron | stock | $452.75 |
| ASML | ASML | stock | $1,500.00 |
| GOLD | Gold | commodity | $4,800.00 |
| SILVER | Silver | commodity | $80.93 |
| USO | US Oil Fund | commodity | $116.19 |
| CPER | Copper ETF | commodity | $37.34 |
| TLT | Treasury 20yr | bond | $86.90 |
| IEF | Treasury 7-10yr | bond | $95.91 |
| SPX | S&P 500 | index | $7,116.00 |
| VIX | Volatility Index | index | $17.51 |
| H100 | H100 GPU Rental | specialty | $2.76 |
| CRWV | CoreWeave | stock | $117.15 |
| OAI26 | OpenAI 2026 Val | prediction | $519B |
| ANT26 | Anthropic 2026 Val | prediction | $427B |
| DPREZ | Dem Pres 2028 | prediction | 50% |
| INVADE27 | China/Taiwan 2027 | prediction | 17% |

> Volume: ~$289.4M (standardized across assets)

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
