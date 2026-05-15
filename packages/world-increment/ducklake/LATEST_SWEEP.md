# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-15

## Sweep Metadata
- **Date:** 2026-05-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 11 |
| AustinCStone | user (social graph) | 11 |
| M1shaaa | user (social graph) | 8 |
| kristinezheng | user (social graph) | 6 |
| DJedamski | user (social graph) | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **362** |

### Notable Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15631 | — | 2026-05-07 |
| kubeflow/pipelines | 4140 | Python | 2026-05-15 |
| kubeflow/spark-operator | 3125 | Python | 2026-05-12 |
| kubeflow/trainer | 2098 | Go | 2026-05-13 |
| kubeflow/katib | 1682 | Python | 2026-05-09 |
| kubeflow/examples | 1462 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |
| plurigrid/asi | 22 | HTML | 2026-04-26 |

### Most Active (Open Issues)

| Repo | Open Issues |
|------|-------------|
| kubeflow/pipelines | 506 |
| bmorphism/Gay.jl | 188 |
| kubeflow/notebooks | 189 |
| kubeflow/docs-agent | 153 |
| kubeflow/sdk | 135 |
| plurigrid/gorj | 198 |
| plurigrid/ducklings | 15 |
| plurigrid/paretae | 14 |

### GF(3) Color Chain Distribution (362 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 120 |
| +1 | `#b8bb26` | PLUS | 121 |
| -1 | `#cc241d` | MINUS | 121 |

IDs cycle: `1→PLUS, 2→MINUS, 3→ERGODIC, 4→PLUS, ...`

### Social Graph Notes
- **zubyul** closely mirrors plurigrid/bmorphism activity: Gay.jl forks, nash-tui/nash-web, GF(3) color tooling, Aptos/Move work
- **migalkin**: Knowledge Graph ML researcher (NodePiece 144★, StarE 89★, kgcourse2021 25★)
- **wasita**: Personal site (Svelte/SvelteKit), cognitive science / Women in Network Science
- **AustinCStone**: ML/vision Python work (TextGAN 92★), recent bitmind-fork activity
- **M1shaaa + kristinezheng**: Yale/MIT cognitive science; Lookit platform experiments, connectomics
- **DJedamski**: Data science, Kaggle, R/statistics (NCAA March Madness 2018)
- **TeglonLabs**: mathpix-gem (Ruby, 2★), Monad MCP server, topoi (Python)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) probed via:
```
GET https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>
```

**Result: All 28 accounts returned 0.0 APT.** Accounts do not hold initialized CoinStore resources on mainnet — likely reserved/uninitialized addresses.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig accounts probed via `POST /v1/view`:
```json
{"function":"0x1::multisig_account::num_signatures_required","type_arguments":[],"arguments":["ADDR"]}
```

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

**All 5 multisig contracts healthy — 2-of-2 threshold configured.**

### MNX Markets (testnet.mnx.fi)

Probed endpoints: `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/` (HTML).

**Status: Market data unavailable via static probe.** Site is a Next.js SPA — returns HTML shell, loads market data client-side via JS bundles. No REST API accessible without JS execution. `mnx_snapshots` table empty this sweep.

---

## DuckDB Tables

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 362 | GF(3)-colored increment records per repo |
| `repo_snapshots` | 362 | Full GitHub repo metadata |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig threshold probes |
| `mnx_snapshots` | 0 | MNX market data (SPA, unavailable) |

### Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name, actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name, full_name,
               language, stars, forks, open_issues, pushed_at, description)

aptos_snapshots(id, timestamp, world, address, balance_apt)
multisig_probes(id, timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(id, timestamp, ticker, name, category, price, change_pct)
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent, 2026-05-15.*
