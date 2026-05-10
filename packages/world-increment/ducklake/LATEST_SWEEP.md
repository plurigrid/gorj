# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-10  
**Session:** world-increment-sweep + hamming-swarm-snapshot agent  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.2 Variegata)

---

## JOB 1 — GitHub Social Graph Sweep

### Sources

| Source | Type | Status |
|--------|------|--------|
| plurigrid | org | ✓ live via MCP (gorj repo) |
| kubeflow | org | rate-limited (unauthenticated) |
| TeglonLabs | org | rate-limited (unauthenticated) |
| bmorphism | user | rate-limited (unauthenticated) |
| zubyul | user | rate-limited (unauthenticated) |
| migalkin | user (zubyul graph) | rate-limited (unauthenticated) |
| DJedamski | user (zubyul graph) | rate-limited (unauthenticated) |
| wasita | user (zubyul graph) | rate-limited (unauthenticated) |
| kristinezheng | user (zubyul graph) | rate-limited (unauthenticated) |
| M1shaaa | user (zubyul graph) | rate-limited (unauthenticated) |
| AustinCStone | user (zubyul graph) | rate-limited (unauthenticated) |

**Note:** `gh` CLI unavailable; unauthenticated GitHub REST API rate-limited (60 req/hr per IP). `plurigrid/gorj` queried live via MCP GitHub tools; historical data for other sources preserved in cumulative `repo_snapshots` (945 rows).

### plurigrid/gorj (Live MCP Snapshot)

- Latest commit: `5b28fe016e0e3d0b0f22e35e01f7db0722d988e1` (2026-05-08T14:04:34Z)
- Message: `chore: ignore duckdb binary in repo root`
- Branches: 107 (latest world-increment: `world-increment/sweep-2026-05-07-0816`)
- Open PRs: 427+ sweep branches targeting master
- Description: forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional open game REPL orchestration

### GF(3) Color Chain — This Sweep (ids 27–37)

```
id mod 3 == 0 → trit=0  ERGODIC  #d3869b
id mod 3 == 1 → trit=1  PLUS     #b8bb26
id mod 3 == 2 → trit=-1 MINUS    #cc241d
```

| id | trit | color | name | source |
|----|------|-------|------|--------|
| 27 | 0 | #d3869b | ERGODIC | plurigrid |
| 28 | 1 | #b8bb26 | PLUS | kubeflow |
| 29 | -1 | #cc241d | MINUS | TeglonLabs |
| 30 | 0 | #d3869b | ERGODIC | bmorphism |
| 31 | 1 | #b8bb26 | PLUS | zubyul |
| 32 | -1 | #cc241d | MINUS | migalkin |
| 33 | 0 | #d3869b | ERGODIC | DJedamski |
| 34 | 1 | #b8bb26 | PLUS | wasita |
| 35 | -1 | #cc241d | MINUS | kristinezheng |
| 36 | 0 | #d3869b | ERGODIC | M1shaaa |
| 37 | 1 | #b8bb26 | PLUS | AustinCStone |

GF(3) chain continuing: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

### DuckDB Cumulative State

| Table | Rows |
|-------|------|
| `world_increments` | 34 |
| `repo_snapshots` | 945 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 1 |

### Top Repos (from cumulative DB, last sweep 2026-04-12)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,565 | — | 2026-01-05 |
| kubeflow/pipelines | 4,119 | Python | 2026-04-10 |
| kubeflow/spark-operator | 3,111 | Python | 2026-04-10 |
| migalkin/NodePiece | 143 | Python | — |
| AustinCStone/TextGAN | 92 | Python | — |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | — |
| plurigrid/gorj | — | Clojure | 2026-05-08 |

---

## JOB 2 — Hamming Swarm Snapshot

Queried via `0x1::coin::balance` view function on `fullnode.mainnet.aptoslabs.com`.  
**All 28 wallets have positive APT balances (live data 2026-05-10).**

### Wallet Balances

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | 0x0a3c…2d5d | **12.6570** |
| F | 0x18a1…cf71 | 1.9605 |
| L | 0x7c2e…eba9 | 1.9273 |
| J | 0x4d96…f54 | 1.8951 |
| alice | 0xc793…cc7b | 0.4364 |
| O | 0x7325…89d | 0.2101 |
| K | 0xa732…dc4 | 0.1620 |
| P | 0x6218…948 | 0.1401 |
| M | 0x6fed…2e9 | 0.1123 |
| N | 0xe7dd…b2c | 0.1061 |
| Q | 0xac40…a9 | 0.1032 |
| S | 0xb875…386 | 0.0918 |
| R | 0x7ce6…e10 | 0.0902 |
| T | 0x3578…588 | 0.0737 |
| U | 0x7586…956 | 0.0558 |
| A | 0x8699…9d7a | 0.0518 |
| V | 0xb59d…2c3 | 0.0488 |
| Y | 0xd8e3…4c4 | 0.0444 |
| X | 0xa95c…47d | 0.0426 |
| W | 0x5f32…7b0 | 0.0407 |
| Z | 0x7af0…97c | 0.0243 |
| B | 0x3f89…b13 | 0.0363 |
| D | 0xf776…dd1 | 0.0116 |
| E | 0xdc1d…d36 | 0.0094 |
| C | 0x38b9…35e | 0.0102 |
| H | 0xce67…00f | 0.0017 |
| G | 0x69a3…f32 | 0.0007 |
| I | 0x070f…fc9 | 0.0007 |

**Total swarm: ~20.34 APT**  
**Top holder:** bob (62.2% of swarm)  
**Funded wallets:** 28/28

### Multisig Contract Probes

`0x1::multisig_account::num_signatures_required` — all 5 contracts healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…003 | 2 | ✓ |
| A-G | 0xf56c…096 | 2 | ✓ |
| Y-Z | 0xd3ff…883 | 2 | ✓ |
| S-T | 0x3b1c…883 | 2 | ✓ |
| V-W | 0x40fa…b6d | 2 | ✓ |

### MNX Markets

`testnet.mnx.fi` is a Next.js SPA — all API paths (`/api/markets`, `/api/v1/markets`) return HTML. No structured market data accessible. Sentinel row recorded in `mnx_snapshots`.

---

## Verification Queries

```sql
-- duckdb packages/world-increment/ducklake/world-increments.duckdb

-- Table row counts
SELECT 'world_increments' as tbl, count(*) FROM world_increments
UNION ALL SELECT 'repo_snapshots', count(*) FROM repo_snapshots
UNION ALL SELECT 'aptos_snapshots', count(*) FROM aptos_snapshots
UNION ALL SELECT 'multisig_probes', count(*) FROM multisig_probes
UNION ALL SELECT 'mnx_snapshots', count(*) FROM mnx_snapshots;

-- GF(3) distribution this sweep (ids 27-37)
SELECT gf3_name, count(*) FROM world_increments WHERE id BETWEEN 27 AND 37 GROUP BY gf3_name;

-- Swarm top 5
SELECT world, balance_apt FROM aptos_snapshots ORDER BY balance_apt DESC LIMIT 5;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```

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

*Generated by Claude Code (claude-sonnet-4-6) — 2026-05-10*
