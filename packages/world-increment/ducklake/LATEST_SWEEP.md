# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-05-02 01:19 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 65 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 47 | 33,985 |
| AustinCStone | user (zubyul social) | 40 | 108 |
| migalkin | user (zubyul social) | 19 | 278 |
| wasita | user (zubyul social) | 10 | 4 |
| M1shaaa | user (zubyul social) | 8 | 0 |
| kristinezheng | user (zubyul social) | 6 | 0 |
| DJedamski | user (zubyul social) | 6 | 3 |
| TeglonLabs | org | 4 | 2 |

**Total repos snapshotted: 389**

### GF(3) Color Chain
- `id % 3 == 0` → trit=0, color `#d3869b` (ERGODIC)
- `id % 3 == 1` → trit=1, color `#b8bb26` (PLUS)
- `id % 3 == 2` → trit=-1, color `#cc241d` (MINUS)

### Notable Highlights
- **kubeflow/kubeflow**: 13,900+ stars, Python ML platform
- **migalkin** (ULTRA graph researcher): 19 repos, highest star density per repo
- **TeglonLabs/mathpix-gem**: Ruby gem for mathematical OCR (newest: Jan 2026)
- **M1shaaa/M1shaaa**: last pushed 2026-05-01 (1 day ago)
- **wasita/wasita.github.io**: active Svelte personal site (pushed 2026-04-28)

### Data Notes
- External network (curl/GitHub API) blocked; data fetched via MCP GitHub search tool
- Events for bmorphism/zubyul: not available (events API not exposed via MCP search)
- kubeflow search returned 47 repos (100-repo cap hit plurigrid/bmorphism first)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Status: UNAVAILABLE** — outbound connections to `fullnode.mainnet.aptoslabs.com` 
are blocked in this sandboxed environment (curl exits with code 5, no proxy/route).

All 28 addresses (alice, bob, A–Z) recorded in `aptos_snapshots` with `NULL` balance.

| World | Address (truncated) |
|-------|---------------------|
| alice | 0xc793acd... |
| bob | 0x0a3c00c... |
| A–Z | 26 addresses |

### Multisig Contract Probes

**Status: UNAVAILABLE** — same network constraint.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f42... | NULL | FALSE |
| A-G | 0xf56c4a1... | NULL | FALSE |
| Y-Z | 0xd3ffe18... | NULL | FALSE |
| S-T | 0x3b1c3ae... | NULL | FALSE |
| V-W | 0x40fad7b... | NULL | FALSE |

### MNX Markets (`testnet.mnx.fi`)

**Status: UNAVAILABLE** — network blocked, no data fetched.

---

## DuckDB Schema Summary

```
world_increments (389 rows) — GF(3)-colored increment chain
repo_snapshots   (389 rows) — full repo metadata per increment
aptos_snapshots  (28 rows)  — Hamming swarm wallet states
multisig_probes  (5 rows)   — A-B, A-G, Y-Z, S-T, V-W contracts
mnx_snapshots    (0 rows)   — MNX market data (unavailable)
```

## Query Examples

```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF(3) color distribution
SELECT gf3_name, gf3_color, count(*) FROM world_increments GROUP BY gf3_name, gf3_color;

-- Aptos wallets (when network available)
SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world;
```
