# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 224 |
| Total World Increments (cumulative) | 247 |
| Total Repo Snapshots (cumulative) | 1,168 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Healthy Multisigs | 5/5 |

---

## GF(3) Color Chain — This Run (224 increments)

| GF3 Name | Trit | Color | Count |
|---|---|---|---|
| ERGODIC | 0 | `#d3869b` | 75 |
| PLUS | +1 | `#b8bb26` | 75 |
| MINUS | -1 | `#cc241d` | 74 |

GF(3) chain cycles every 3 increments: `ERGODIC → PLUS → MINUS → ERGODIC → ...`  
224 increments = 74 full cycles + 2 remainder (balanced)

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes (pushed 2026-07-28)
- **kubeflow/pipelines**: 4,119 stars — ML pipeline for Kubernetes (pushed 2026-07-28)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes Spark operator (pushed 2026-07-28)
- **migalkin/NodePiece**: 144 stars (+1) — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: top starred bmorphism repo — OCaml MCP SDK
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid** and **bmorphism**: both active today (2026-07-28)
- **wasita/wasita.github.io**: most recently pushed social-graph repo (2026-07-21)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) via Aptos fullnode REST API.  
Ledger version at query: ~6,500,869,954

**Result: 0/28 addresses have an APT CoinStore on mainnet.**

All addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These may be uninitialized accounts, addresses holding fungible assets under the newer FA standard, or testnet-only addresses.

| Wallet | Address | Balance (APT) |
|---|---|---|
| alice | 0xc793...4cc7b | NULL |
| bob | 0x0a3c...512d5d | NULL |
| A–Z | 0x8699...–0x7af0... | NULL (all 26) |

### Multisig Contract Probes (Mainnet)

POSTed `0x1::multisig_account::num_signatures_required` view function for 5 contracts.

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f428... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✅ healthy |
| V-W | 0x40fad7b4... | 2 | ✅ healthy |

**5/5 contracts respond correctly** — all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE as JSON API.**  
All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the SPA HTML shell. No JSON market data accessible without browser-side execution. `mnx_snapshots` table: 0 rows this run.

---

## DuckDB Table Totals After This Run

| Table | Rows |
|---|---|
| world_increments | 247 |
| repo_snapshots | 1,168 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-07-28*
