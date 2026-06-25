# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-25

## Sweep Metadata
- **Date:** 2026-06-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 403 |
| Sources Covered | 3 orgs + 8 users |

### Repos by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user (social graph) | 40 |
| migalkin | user (social graph) | 19 |
| M1shaaa | user (social graph) | 8 |
| DJedamski | user (social graph) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social graph) | 5 |
| wasita | user (social graph) | 2+ |
| **TOTAL** | | **382+** |

### GF(3) Color Chain Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

Chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...` (repeating over 403 increments)

### Notable Updates Since Last Sweep (2026-04-12)

| Repo | Source | Pushed | Notes |
|------|--------|--------|-------|
| M1shaaa/M1shaaa | M1shaaa | 2026-06-25 | Profile config updated **today** |
| wasita/wasita.github.io | wasita | 2026-06-25 | Personal site updated **today** |
| TeglonLabs/jank-crane | TeglonLabs | 2026-06-08 | **NEW** C++ crane-jank GF3 converged-IR hub |
| kristinezheng/kristinezheng.github.io | kristinezheng | 2026-06-07 | Personal site updated |

### Top Repos by Stars

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow/kubeflow | — | 15565 | 2026-01-05 |
| kubeflow/pipelines | Python | 4119 | 2026-04-10 |
| kubeflow/spark-operator | Python | 3111 | 2026-04-10 |
| kubeflow/trainer | Go | 2080 | 2026-04-10 |
| kubeflow/katib | Python | 1676 | 2026-04-02 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | — |
| AustinCStone/TextGAN | Python | 92 | — |
| migalkin/NodePiece | Python | 143 | — |
| migalkin/StarE | Python | 88 | — |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming-swarm wallets (alice, bob, A–Z) show **0.0 APT** on mainnet.
The CoinStore resource returned HTTP 404 for every address — these wallets are
unfunded on Aptos mainnet or have never received APT.

| Wallet | Address (prefix) | Balance (APT) |
|--------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts are **structurally healthy** — each deployed and requiring 2-of-N threshold.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | healthy |
| A-G | 0xf56c...096 | 2 | healthy |
| Y-Z | 0xd3ff...883 | 2 | healthy |
| S-T | 0x3b1c...883 | 2 | healthy |
| V-W | 0x40fa...b6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — endpoints `/api/markets`, `/api/tickers`, `/api/v1/markets` all return HTTP 401 Unauthorized.
The testnet requires authentication. No market data captured this sweep.

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb

Tables:
  world_increments   — 403 rows (GitHub repo events, GF3-tagged)
  repo_snapshots     — 403 rows (repo metadata: lang, stars, forks, issues)
  aptos_snapshots    —  28 rows (Hamming swarm wallet balances)
  multisig_probes    —   5 rows (contract health probes, all healthy)
  mnx_snapshots      —   0 rows (unavailable this sweep)
```

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

## Key Findings

1. **Graph active today (2026-06-25):** wasita.github.io and M1shaaa/M1shaaa both pushed this morning.
2. **TeglonLabs jank-crane is new since last sweep** — C++ GF3 converged-IR hub, most active new org repo.
3. **All 28 Hamming swarm Aptos wallets hold 0 APT** — swarm not yet funded on mainnet.
4. **All 5 multisig pairs are deployed and healthy** — 2-of-N threshold on all; infrastructure live without funded wallets.
5. **MNX testnet auth-gated** — market data unavailable without credentials.
6. **Delta from 2026-04-12:** +403 increments this run (up from 12 sweep-level increments in prior run); wasita gained a live push today.
