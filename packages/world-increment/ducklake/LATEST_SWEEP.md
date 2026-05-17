# World-Increment Sweep + Hamming Snapshot — 2026-05-17

## Sweep Metadata
- **Date:** 2026-05-17
- **Agent:** world-increment-sweep + hamming-swarm
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Social Graph Sweep

### Repos Found Per Org/User

| org/user | repos in DB | total on GitHub |
|---|---|---|
| plurigrid | 50 | 100 |
| bmorphism | 50 | 102 |
| kubeflow | 48 | 48 |
| AustinCStone | 40 | 40 |
| zubyul | 49 | 49 |
| migalkin | 19 | 19 |
| wasita | 11 | 11 |
| TeglonLabs | 4 | 4 |
| kristinezheng | 6 | 6 |
| M1shaaa | 8 | 8 |
| DJedamski | 6 | 6 |
| **TOTAL** | **291** | **393+** |

Note: GitHub search API caps results at 50 per query. Orgs with >50 repos (plurigrid 100, bmorphism 102) have partial coverage.

### Notable Repos
- `kubeflow/kubeflow` — 15,640 stars, ML Toolkit for Kubernetes
- `kubeflow/pipelines` — 4,139 stars, ML Pipelines (pushed 2026-05-17)
- `kubeflow/spark-operator` — 3,125 stars
- `migalkin/NodePiece` — 144 stars, knowledge graph representations
- `AustinCStone/TextGAN` — 92 stars, GAN for text generation
- `bmorphism/ocaml-mcp-sdk` — 61 stars, OCaml SDK for MCP
- `plurigrid/asi` — 23 stars, topological chemputer (pushed 2026-04-26)

---

## Aptos Hamming Snapshot

All 28 addresses queried against Aptos mainnet `fullnode.mainnet.aptoslabs.com`.

| World | Address (snippet) | Balance (APT) |
|---|---|---|
| alice | 0xc793acde... | 0.0 |
| bob | 0x0a3c00c5... | 0.0 |
| A | 0x8699edc0... | 0.0 |
| B | 0x3f892ebe... | 0.0 |
| C | 0x38b99e63... | 0.0 |
| D | 0xf7765624... | 0.0 |
| E | 0xdc1d9d53... | 0.0 |
| F | 0x18a14b5b... | 0.0 |
| G | 0x69a394c0... | 0.0 |
| H | 0xce67c327... | 0.0 |
| I | 0x070fe5d7... | 0.0 |
| J | 0x4d964db8... | 0.0 |
| K | 0xa732040a... | 0.0 |
| L | 0x7c2eaeaf... | 0.0 |
| M | 0x6fed37a7... | 0.0 |
| N | 0xe7dde6da... | 0.0 |
| O | 0x73252b60... | 0.0 |
| P | 0x6218792d... | 0.0 |
| Q | 0xac40fa50... | 0.0 |
| R | 0x7ce605cc... | 0.0 |
| S | 0xb8753014... | 0.0 |
| T | 0x35781dc0... | 0.0 |
| U | 0x75860da4... | 0.0 |
| V | 0xb59dd817... | 0.0 |
| W | 0x5f32aef7... | 0.0 |
| X | 0xa95cbbd1... | 0.0 |
| Y | 0xd8e32848... | 0.0 |
| Z | 0x7af0ef6e... | 0.0 |

All balances 0.0 APT — accounts either not yet funded or no `CoinStore<AptosCoin>` resource registered on mainnet.

---

## Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required` on Aptos mainnet.

| Pair | Contract Address | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f428...4987003 | 2 | YES |
| A-G | 0xf56c4a1c...fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe181...75b883 | 2 | YES |
| S-T | 0x3b1c3ae9...ed7883 | 2 | YES |
| V-W | 0x40fad7b4...80eb6d | 2 | YES |

All 5 multisig contracts are live and healthy, each requiring 2-of-n signatures.

---

## MNX Market Status

`https://testnet.mnx.fi/api/markets` and `/api/tickers` return HTML (Next.js SSR), not JSON.
**Status: API unavailable** — no machine-readable market data at these endpoints as of 2026-05-17.

---

## GF(3) Color Chain Stats

The 291 world-increment rows are colored via GF(3) arithmetic (id mod 3):

| GF(3) Name | Trit | Color Hex | Count |
|---|---|---|---|
| ERGODIC | 0 | #d3869b | 97 |
| PLUS | 1 | #b8bb26 | 97 |
| MINUS | -1 | #cc241d | 97 |

Distribution is perfectly balanced (97 each) across the 291 repos.

Chain pattern: `ERGODIC(0) → PLUS(1) → MINUS(2) → ERGODIC(3) → ...` repeating every 3 increments.

---

## DuckDB Tables

| Table | Rows | Description |
|---|---|---|
| world_increments | 291 | One per repo snapshot, GF3-colored |
| repo_snapshots | 291 | Full repo metadata from GitHub |
| aptos_snapshots | 28 | Wallet balances for A-Z + alice/bob |
| multisig_probes | 5 | Multisig contract health checks |
| mnx_snapshots | 1 | Placeholder (API unavailable) |

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
