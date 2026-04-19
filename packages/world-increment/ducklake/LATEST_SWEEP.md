# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-19

## Sweep Metadata
- **Date:** 2026-04-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — Increments 13–17
| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | github-social-graph | rate_limited | +1 | `#b8bb26` | **PLUS** |
| 14 | hamming-swarm (aptos) | balance_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | hamming-swarm (aptos) | multisig_probe | 0 | `#d3869b` | **ERGODIC** |
| 16 | mnx_markets | unavailable_spa | +1 | `#b8bb26` | **PLUS** |
| 17 | world-increment | sweep_complete | -1 | `#cc241d` | **MINUS** |

GF(3) chain continues: `... ERGODIC(12) → PLUS(13) → MINUS(14) → ERGODIC(15) → PLUS(16) → MINUS(17)`

### Targets Queried
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Social graph (zubyul):** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Result: GitHub API Rate Limited (unauthenticated)
All parallel requests to `api.github.com` were rejected:
> `API rate limit exceeded for {IP}. Authenticated requests get a higher rate limit.`

**Confirmed repo (local git):**
| org/user | repo | language | pushed_at | description |
|----------|------|----------|-----------|-------------|
| plurigrid | gorj | Clojure | 2026-04-14 | MCP server + hooks for AI coding agents with Clojure REPL |

**Prior sweep (2026-04-12) had 471 repos across all 11 sources** — see historical data in `world_increments` ids 1–12.

**Action required:** Set `GITHUB_TOKEN` env var for authenticated API access (5,000 req/hr).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)
All 28 addresses probed via `fullnode.mainnet.aptoslabs.com`.  
All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address | Balance (APT) | Status |
|-------|---------|:-------------:|--------|
| alice | 0xc793...cc7b | 0.0 | resource_not_found |
| bob | 0x0a3c...2d5d | 0.0 | resource_not_found |
| A | 0x8699...9d7a | 0.0 | resource_not_found |
| B | 0x3f89...b13 | 0.0 | resource_not_found |
| C | 0x38b9...35e | 0.0 | resource_not_found |
| D | 0xf776...dd1 | 0.0 | resource_not_found |
| E | 0xdc1d...d36 | 0.0 | resource_not_found |
| F | 0x18a1...f71 | 0.0 | resource_not_found |
| G | 0x69a3...f32 | 0.0 | resource_not_found |
| H | 0xce67...00f | 0.0 | resource_not_found |
| I | 0x070f...fc9 | 0.0 | resource_not_found |
| J | 0x4d96...f54 | 0.0 | resource_not_found |
| K | 0xa732...dc4 | 0.0 | resource_not_found |
| L | 0x7c2e...ba9 | 0.0 | resource_not_found |
| M | 0x6fed...e9 | 0.0 | resource_not_found |
| N | 0xe7dd...b2c | 0.0 | resource_not_found |
| O | 0x7325...89d | 0.0 | resource_not_found |
| P | 0x6218...948 | 0.0 | resource_not_found |
| Q | 0xac40...a9 | 0.0 | resource_not_found |
| R | 0x7ce6...e10 | 0.0 | resource_not_found |
| S | 0xb875...386 | 0.0 | resource_not_found |
| T | 0x3578...588 | 0.0 | resource_not_found |
| U | 0x7586...956 | 0.0 | resource_not_found |
| V | 0xb59d...c3 | 0.0 | resource_not_found |
| W | 0x5f32...b0 | 0.0 | resource_not_found |
| X | 0xa95c...47d | 0.0 | resource_not_found |
| Y | 0xd8e3...4c4 | 0.0 | resource_not_found |
| Z | 0x7af0...97c | 0.0 | resource_not_found |

**Total APT across swarm:** 0.0  
**Note:** Accounts lack legacy `CoinStore` resource — may use FA (fungible asset) coin store or be unfunded.

### Multisig Contract Probes
All 5 probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on mainnet.**

### MNX Markets (testnet.mnx.fi)
- Status: **Unavailable** — all probed endpoints return SPA HTML (no REST API accessible)
- Paths tried: `/api/markets`, `/api/v1/markets`, `/api/v2/markets`, `/api/tickers`, `/api/orderbooks`, `/api/stats`, `/markets`
- `mnx_snapshots` table: 0 rows inserted this sweep

---

## DuckDB State After Sweep
| Table | Total Rows |
|-------|-----------|
| world_increments | 28 (ids 1–17) |
| repo_snapshots | 477 |
| aptos_snapshots | 28 (this sweep only) |
| multisig_probes | 5 (this sweep only) |
| mnx_snapshots | 0 |

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

## Historical Highlights (from 2026-04-12 sweep)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **plurigrid/asi**: 16 stars — topological chemputer
