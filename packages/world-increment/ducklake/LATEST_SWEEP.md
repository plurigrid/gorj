# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-12  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain

| trit | name | color |
|------|------|-------|
| 0 | ERGODIC | `#d3869b` |
| +1 | PLUS | `#b8bb26` |
| -1 | MINUS | `#cc241d` |

Assignment: `id % 3 == 0` → ERGODIC, `id % 3 == 1` → PLUS, `id % 3 == 2` → MINUS

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 259 |
| Total Repo Snapshot Rows | 1,180 |
| Unique Repos Captured | 543 |
| Sources | 11 (3 orgs + 8 users) |
| Repos with Stars | 158 |
| Total Stars (starred repos) | 103,498 |
| Languages Observed | 26+ |

### Repos by Source

| Source | Type | Unique Repos | Total Stars |
|--------|------|-------------|-------------|
| kubeflow | org | 49 | ~101,764 |
| migalkin | user (social/zubyul) | 30 | 833 |
| bmorphism | user | 115 | 383 |
| AustinCStone | user (social/zubyul) | 43 | 308 |
| plurigrid | org | 117 | 131 |
| zubyul | user | 59 | 40 |
| DJedamski | user (social/zubyul) | 11 | 16 |
| TeglonLabs | org | 53 | 14 |
| wasita | user (social/zubyul) | 32 | 9 |
| kristinezheng | user (social/zubyul) | 18 | 0 |
| M1shaaa | user (social/zubyul) | 16 | 0 |
| **TOTAL** | | **543** | **~103,498** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | ~15,600 | — |
| kubeflow/pipelines | ~4,130 | Python |
| kubeflow/spark-operator | ~3,120 | Python |
| kubeflow/trainer | ~2,097 | Go |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/NodePiece | ~143 | Python |
| migalkin/StarE | ~88 | Python |

### plurigrid Recent Activity (today: 2026-05-12)

| Repo | Language | Stars | Open Issues | Description |
|------|----------|-------|-------------|-------------|
| gorj | Clojure | 0 | 166 | forj + Rama topology nREPL routing + GF(3) gay trit coloring |
| horse | TeX | 1 | 9 | — |
| zig-syrup | Zig | 2 | 0 | High-performance Zig OCapN Syrup |
| asi | HTML | 21 | 4 | topological chemputer |
| nash-portal | Rust | 2 | 0 | NASH token TUI in the browser |

### GitHub API Notes

- Unauthenticated GitHub REST API: rate-limited (60 req/hr exceeded for this IP)
- Data collected via MCP `search_repositories` tool with automatic pagination
- Events endpoint (bmorphism/zubyul): not queried due to rate limit; repo push timestamps used instead

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Endpoint: `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|--------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B | 0x3f892e... | 0.0 |
| C | 0x38b99e... | 0.0 |
| D | 0xf77656... | 0.0 |
| E | 0xdc1d9d... | 0.0 |
| F | 0x18a14b... | 0.0 |
| G | 0x69a394... | 0.0 |
| H | 0xce67c3... | 0.0 |
| I | 0x070fe5... | 0.0 |
| J | 0x4d964d... | 0.0 |
| K | 0xa73204... | 0.0 |
| L | 0x7c2eae... | 0.0 |
| M | 0x6fed37... | 0.0 |
| N | 0xe7dde6... | 0.0 |
| O | 0x73252b... | 0.0 |
| P | 0x621879... | 0.0 |
| Q | 0xac40fa... | 0.0 |
| R | 0x7ce605... | 0.0 |
| S | 0xb87530... | 0.0 |
| T | 0x35781d... | 0.0 |
| U | 0x75860d... | 0.0 |
| V | 0xb59dd8... | 0.0 |
| W | 0x5f32ae... | 0.0 |
| X | 0xa95cbb... | 0.0 |
| Y | 0xd8e328... | 0.0 |
| Z | 0x7af0ef... | 0.0 |

**Total APT across 28-node swarm:** 0.0 APT  
(Addresses resolve on mainnet but CoinStore shows 0 balance — accounts unfunded or coin resource not initialized)

### Multisig Contract Probes

Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f4... | 2-of-2 | ✓ |
| A-G | 0xf56c4a... | 2-of-2 | ✓ |
| Y-Z | 0xd3ffe1... | 2-of-2 | ✓ |
| S-T | 0x3b1c3a... | 2-of-2 | ✓ |
| V-W | 0x40fad7... | 2-of-2 | ✓ |

**All 5 multisig contracts healthy** — 2-of-2 quorum confirmed on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — testnet.mnx.fi serves a Next.js SPA only.  
API paths probed: `/api/markets`, `/api/v1/markets` — both return HTML (client-side rendering).  
`mnx_snapshots` table: 0 rows recorded.

---

## DuckDB Schema

```sql
packages/world-increment/ducklake/world-increments.duckdb

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

*Sweep completed autonomously. GF(3) trit 259 % 3 = 2 → MINUS `#cc241d`*
