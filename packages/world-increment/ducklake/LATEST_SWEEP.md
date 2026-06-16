# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-16

## Sweep Metadata
- **Date:** 2026-06-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source (2026-06-16)

### plurigrid (100 repos — most recently pushed: gorj 2026-06-16)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | — | — | 2026-06-16 |
| place | — | — | 2026-06-15 |

### kubeflow (48 repos — updated 2026-06-15)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,726 | 2026-06-11 |
| pipelines | Python | 4,154 | 2026-06-15 |
| spark-operator | Python | 3,127 | 2026-06-15 |
| trainer | Go | 2,115 | 2026-06-15 |
| katib | Python | 1,683 | 2026-06-15 |
| community-distribution | YAML | 1,023 | 2026-06-15 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 (2 forks) | 2025-09-21 |

### bmorphism (100 repos — active 2026-06-16)
| Repo | Language | Pushed At |
|------|----------|-----------|
| Gay.jl | Julia | 2026-06-16 |
| satreadout | — | 2026-06-15 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |

### AustinCStone (40 repos)
Active historical repos in Python/ML domain.

### wasita (11 repos — active 2026-06-15)
Personal site `wasita.github.io` (Svelte) pushed 2026-06-15T20:15Z.

### kristinezheng (5 repos — active 2026-06-07)
Portfolio `kristinezheng.github.io` (HTML) pushed 2026-06-07T22:52Z.

### M1shaaa (8 repos — profile updated 2026-06-15)
Profile README (M1shaaa/M1shaaa) pushed 2026-06-15T17:09Z.

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-16)

All 28 wallets queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Result: 0.0 APT across all addresses.** The CoinStore resource was absent or zero — accounts are on-chain but unfunded at sweep time.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...12d5d | 0.0 |
| A–Z | (see `aptos_snapshots` table) | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy with sigs_required=2.**

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Protected by Vercel deployment authentication. All paths (`/`, `/api/markets`, `/api/v1/markets`) return auth-gate HTML. No market data this sweep. `mnx_snapshots` = 0 rows.

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

## Notable Highlights (2026-06-16)
- **kubeflow/kubeflow**: 15,726 stars (+161 since April sweep) — ML platform for Kubernetes
- **kubeflow/pipelines**: 4,154 stars (+35) — pushed today (2026-06-15)
- **kubeflow/mcp-apache-spark-history-server**: 177 stars — new MCP server for Spark (added since last sweep)
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings
- **TeglonLabs/jank-crane**: New C++ repo — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps" (pushed 2026-06-08)
- **bmorphism/Gay.jl**: Julia repo pushed today (2026-06-16T00:49Z) — most recent activity
- **plurigrid/gorj**: This repo — pushed 2026-06-16T02:12Z (most recently pushed of all 391)
- **Hamming swarm**: All 28 wallets at 0.0 APT; all 5 multisigs healthy (sigs_required=2)
- **MNX testnet**: Vercel-gated, no market data available this run
