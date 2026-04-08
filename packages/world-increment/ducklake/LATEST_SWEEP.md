# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-08

## Sweep Metadata
- **Date:** 2026-04-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 465 |
| Total Repo Snapshots | 405 |
| Event Records | 60 (bmorphism×30, zubyul×30) |
| Sources Covered | 3 orgs + 8 users |

### Sources Scanned

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 46 |
| AustinCStone | user (social graph) | 43 |
| migalkin | user (social graph) | 30 |
| wasita | user (social graph) | 29 |
| zubyul | user | 23 |
| kristinezheng | user (social graph) | 18 |
| M1shaaa | user (social graph) | 16 |
| TeglonLabs | org | 2 |
| DJedamski | user (social graph) | 2 |
| **TOTAL** | | **409** |

### Recent Events (bmorphism + zubyul — 60 events)

| Event Type | Count |
|------------|-------|
| PushEvent | 33 |
| CreateEvent | 20 |
| PullRequestEvent | 7 |

### Top 10 Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,558 | 2,626 |
| kubeflow/pipelines | Python | 4,119 | 1,984 |
| kubeflow/spark-operator | Python | 3,111 | 1,481 |
| kubeflow/trainer | Go | 2,076 | 943 |
| kubeflow/katib | Python | 1,675 | 522 |
| kubeflow/examples | Jsonnet | 1,458 | 755 |
| kubeflow/manifests | YAML | 1,009 | 1,070 |
| kubeflow/arena | Go | 808 | 190 |
| kubeflow/kale | Python | 682 | 156 |
| kubeflow/mpi-operator | Go | 521 | 236 |

### Language Distribution (top 10)

| Language | Repos | Total Stars |
|----------|-------|-------------|
| Python | 71 | 10,398 |
| HTML | 18 | 232 |
| Go | 16 | 3,963 |
| TypeScript | 13 | 330 |
| JavaScript | 13 | 39 |
| Jupyter Notebook | 11 | 265 |
| Rust | 11 | 6 |
| Jsonnet | 8 | 2,408 |
| Clojure | 7 | 1 |
| C | 6 | 0 |

### GF(3) Color Chain Distribution

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 155 |
| PLUS | #b8bb26 | +1 | 155 |
| MINUS | #cc241d | -1 | 155 |

**Perfectly balanced:** 155 per trit (465 = 3 × 155).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

Queried via `0x1::coin::balance` view function. All accounts exist on-chain.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | 0x0a3c00c5...05512d5d | 12.65700700 |
| F | 0x18a14b5b...4c3cf71 | 1.96051600 |
| L | 0x7c2eaeaf...37eba9 | 1.92726900 |
| J | 0x4d964db8...b7f2e9... wait | 1.89509300 |
| alice | 0xc793acde...624cc7b | 0.43643352 |
| O | 0x73252b60...5a89d | 0.21013600 |
| K | 0xa732040a...425dc4 | 0.16196100 |
| P | 0x62187929...ec948 | 0.14013600 |
| M | 0x6fed37a7...7f2e9 | 0.11228500 |
| N | 0xe7dde6da...551b2c | 0.10612100 |
| Q | 0xac40fa50...c89a9 | 0.10324000 |
| S | 0xb8753014...d0386 | 0.09178800 |
| R | 0x7ce605cc...76e10 | 0.09021700 |
| T | 0x35781dc0...3f4588 | 0.07371300 |
| U | 0x75860da4...ef9956 | 0.05577300 |
| A | 0x8699edc0...be9d7a | 0.05176700 |
| V | 0xb59dd817...af2c3 | 0.04783299 |
| Y | 0xd8e32848...2444c4 | 0.04444900 |
| X | 0xa95cbbd1...e33047d | 0.04257700 |
| W | 0x5f32aef7...cc7b0 | 0.04070500 |
| B | 0x3f892ebe...577cb13 | 0.03625600 |
| Z | 0x7af0ef6e...e197c | 0.02326800 |
| E | 0xdc1d9d53...958d36 | 0.01256100 |
| D | 0xf7765624...cfdd1 | 0.01162900 |
| C | 0x38b99e63...91535e | 0.01018500 |
| G | 0x69a394c0...c7f32 | 0.00068100 |
| H | 0xce67c327...5300f | 0.00068100 |
| I | 0x070fe5d7...c1fc9 | 0.00068100 |

**Total APT across swarm:** ~20.27 APT  
**Richest:** bob (12.66 APT — 62.4% of total), F/L/J (~1.90 APT each)  
**Dust accounts (≤0.001 APT):** G, H, I

Note: `alice` account has `store_v2::ACSetMeta2`, `multiverse::MultiverseState`, and `lending_pool::UserPosition` resources — active on-chain contract account.

### Multisig Contract Probes (5/5 healthy)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

All 5 multisig accounts require **2-of-N** signatures. All healthy.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable via REST.**  
The site serves a Next.js SPA; market data API is WebSocket-only at `wss://api.testnet.mnx.fi`. REST endpoints `/markets`, `/api/markets`, `/v1/markets`, `/pairs` all returned 404. No market data extractable without WS client.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)              -- 465 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)              -- 405 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows

multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows

mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 1 row (unavailable marker)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
