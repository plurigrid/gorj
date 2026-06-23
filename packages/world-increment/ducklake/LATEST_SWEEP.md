# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-23

## Sweep Metadata
- **Date:** 2026-06-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 317 |
| Total Repo Snapshots | 317 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| migalkin (social) | user | 5 |
| TeglonLabs | org | 5 |
| AustinCStone (social) | user | 3 |
| wasita (social) | user | 3 |
| M1shaaa (social) | user | 2 |
| DJedamski (social) | user | 1 |
| kristinezheng (social) | user | 1 |
| **TOTAL** | | **317** |

### Top Repos by Stars
| full_name | language | ★ | forks |
|-----------|----------|---|-------|
| kubeflow/kubeflow | — | 15741 | — |
| kubeflow/pipelines | Python | 4157 | 2009 |
| kubeflow/spark-operator | Python | 3128 | — |
| kubeflow/trainer | Go | 2119 | 971 |
| kubeflow/katib | Python | 1685 | — |
| migalkin/NodePiece | Python | 144 | 21 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| migalkin/StarE | Python | 89 | 16 |
| plurigrid/asi | HTML | 26 | 8 |
| migalkin/kgcourse2021 | HTML | 25 | 9 |

### Recently Active (as of 2026-06-23)
- `plurigrid/gorj` (Clojure) — pushed 2026-06-23 — 769 open issues
- `plurigrid/eirobri` (Clojure) — pushed 2026-06-23
- `plurigrid/place` (TeX) — pushed 2026-06-20
- `wasita/proj-template` — pushed 2026-06-19
- `bmorphism/satreadout` (HTML) — pushed 2026-06-20

### TeglonLabs Snapshot
| repo | language | ★ | notes |
|------|----------|---|-------|
| jank-crane | C++ | 0 | crane-jank converged-IR hub, GF3 convergence maps |
| mathpix-gem | Ruby | 2 | LaTeX OCR via Mathpix API |
| coin-flip-mcp | JavaScript | 0 | random.org MCP coin flipper |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | |

### GF(3) Color Chain Distribution (317 increments)
| trit | color | name | count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | ~106 |
| 1 | #b8bb26 | PLUS | ~106 |
| -1 | #cc241d | MINUS | ~105 |

GF(3) rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-23)
All 28 wallets queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 wallets returned 0.00 APT** — accounts either unfunded or CoinStore resource not initialized on mainnet.

| world | address | balance APT |
|-------|---------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A–Z (26) | 0x8699…–0x7af0… | 0.0 each |

### Multisig Contract Probes (Aptos mainnet)
All 5 pairs probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| pair | address (prefix…suffix) | sigs_required | healthy |
|------|------------------------|---------------|---------|
| A-B | 0x0da4…7003 | **2** | ✓ |
| A-G | 0xf56c…0096 | **2** | ✓ |
| Y-Z | 0xd3ff…b883 | **2** | ✓ |
| S-T | 0x3b1c…7883 | **2** | ✓ |
| V-W | 0x40fa…eb6d | **2** | ✓ |

All 5 multisig contracts live, responding correctly with `sigs_required=2`.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment protection active on all API paths (`/`, `/api/markets`, `/api/v1/markets`). Requires Vercel auth token or trusted source OIDC configuration.

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
