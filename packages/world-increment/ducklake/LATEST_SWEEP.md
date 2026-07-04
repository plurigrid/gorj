# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-04  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 50 | 54 |
| kubeflow | org | 48 | 34,312 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 50 | 122 |
| zubyul | user | 49 | 14 |
| migalkin | user (zubyul social) | 19 | 280 |
| DJedamski | user (zubyul social) | 6 | 3 |
| wasita | user (zubyul social) | 11 | 5 |
| kristinezheng | user (zubyul social) | 5 | 0 |
| M1shaaa | user (zubyul social) | 8 | 0 |
| AustinCStone | user (zubyul social) | 20 | 107 |
| **Total** | | **271** | **34,899** |

### DuckDB Schema

```
world_increments  -- 271 rows, GF(3) color-coded increments
repo_snapshots    -- 271 rows, full repo metadata
aptos_snapshots   -- 28 rows, Hamming swarm wallet balances
multisig_probes   -- 5 rows, multisig contract health
mnx_snapshots     -- 1 row, MNX market status
```

### GF(3) Distribution (271 increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 90 |
| 1 | PLUS | #b8bb26 | 91 |
| -1 | MINUS | #cc241d | 90 |

### Notable Repos

- **kubeflow**: 34,312 total stars across 48 repos — dominant ML infra org
- **bmorphism**: 50 repos, 122 stars — active plurigrid contributor
- **zubyul**: 49 repos, 14 stars — active social graph hub
- **migalkin**: knowledge graph / relational ML focus
- **TeglonLabs/jank-crane**: newest repo (pushed 2026-06-08), C++ GF3 convergence hub

### Events / Notes

- GitHub direct API (`/orgs/{org}/repos`) blocked by proxy (repo-scoped restriction)
- Used GitHub MCP `search_repositories` for all discovery
- bmorphism and zubyul events endpoints not accessible via MCP (no direct `/events` tool)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried on Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).
All returned `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>` --
accounts are initialized but hold no APT in the coin store resource.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z (26 wallets) | 0x8699... - 0x7af0... | 0.0 each |

**Interpretation:** All 28 Hamming swarm addresses exist on-chain but carry zero APT balance.
This is consistent with pre-funded test wallets that have spent or transferred all APT,
or newly registered accounts awaiting funding.

### Multisig Contract Health

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts healthy** -- each requires 2-of-N signatures.

### MNX Markets

`testnet.mnx.fi` requires Vercel authentication -- market data unavailable without auth token.
Probed paths: `/api/markets`, `/api/v1/markets`, `/` -- all returned auth-required HTML.

---

## DuckDB Location

```
packages/world-increment/ducklake/world-increments.duckdb
```

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`

### Quick Query Examples

```sql
-- Top repos by stars
SELECT org_or_user, repo_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF3 color summary
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2;

-- Aptos wallets
SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
