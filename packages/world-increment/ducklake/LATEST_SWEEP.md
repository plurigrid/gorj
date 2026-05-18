# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-18

## Sweep Metadata
- **Date:** 2026-05-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 13 · GF(3) trit=1 · PLUS · `#b8bb26`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 (ID 1–13 this session) |
| Total Repo Snapshots | 1158 (+214 this sweep) |
| Sources Covered (this sweep) | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, sigs=2) |
| MNX Markets | unavailable (SPA) |

---

## GF(3) Color Chain — All 13 Increments (this session)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |
| **13** | **social_graph** | **github_sweep + hamming_snapshot** | **+1** | **`#b8bb26`** | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Hamming Swarm Snapshot (Job 2)

### Aptos Wallet Balances — Mainnet

All 28 addresses probed at ledger version ~5,323,877,476.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | `0xc793...cc7b` | 0.0 |
| bob | `0x0a3c...512d` | 0.0 |
| A | `0x8699...9d7a` | 0.0 |
| B | `0x3f89...b13` | 0.0 |
| C | `0x38b9...35e` | 0.0 |
| D | `0xf776...dd1` | 0.0 |
| E | `0xdc1d...d36` | 0.0 |
| F | `0x18a1...f71` | 0.0 |
| G | `0x69a3...f32` | 0.0 |
| H | `0xce67...00f` | 0.0 |
| I | `0x070f...fc9` | 0.0 |
| J | `0x4d96...f54` | 0.0 |
| K | `0xa732...dc4` | 0.0 |
| L | `0x7c2e...ba9` | 0.0 |
| M | `0x6fed...2e9` | 0.0 |
| N | `0xe7dd...b2c` | 0.0 |
| O | `0x7325...89d` | 0.0 |
| P | `0x6218...948` | 0.0 |
| Q | `0xac40...a9` | 0.0 |
| R | `0x7ce6...e10` | 0.0 |
| S | `0xb875...386` | 0.0 |
| T | `0x3578...588` | 0.0 |
| U | `0x7586...956` | 0.0 |
| V | `0xb59d...b3` | 0.0 |
| W | `0x5f32...7b0` | 0.0 |
| X | `0xa95c...47d` | 0.0 |
| Y | `0xd8e3...4c4` | 0.0 |
| Z | `0x7af0...97c` | 0.0 |

All accounts: `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — CoinStore not initialized.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4...003` | 2 | ✅ |
| A-G | `0xf56c...096` | 2 | ✅ |
| Y-Z | `0xd3ff...883` | 2 | ✅ |
| S-T | `0x3b1c...883` | 2 | ✅ |
| V-W | `0x40fa...b6d` | 2 | ✅ |

All 5 multisig contracts healthy — each requires **2-of-N signatures**.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returns HTTP 200 but serves a Next.js SPA. API endpoints `/api/markets`, `/api/v1/markets`, `/api/tickers` all return the same SPA HTML. Market data is not available via server-side REST API.

**Status: UNAVAILABLE**

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

## Repo Counts by Source (this sweep, increment 13)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 50 |
| kubeflow | org | 30 |
| bmorphism | user | 30 |
| zubyul | user | 30 |
| AustinCStone | user | 20 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 6 |
| TeglonLabs | org | 4 |
| **TOTAL (this sweep)** | | **214** |
| **TOTAL (cumulative)** | | **1158** |

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
- **kubeflow/kubeflow**: 15,647 stars — flagship ML platform for Kubernetes (+82 since last sweep)
- **kubeflow/pipelines**: 4,140 stars — most popular ML pipeline for Kubernetes (+21)
- **kubeflow/spark-operator**: 3,126 stars — Kubernetes operator for Apache Spark (+15)
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (+1)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK using Jane Street's oxcaml_effect (+1)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 23 stars — topological chemputer (+7 since last sweep!)
- **plurigrid/gorj**: 243 open issues — active forj + Rama topology nREPL routing + GF(3)
- **bmorphism/oxgame**: NEW — Stellar resolution + open-game composition for OxCaml
- **kubeflow/mcp-server**: NEW — MCP Server for AI-Assisted Development with Kubeflow Tools
- **Increment 13**: PLUS (`#b8bb26`) — github_sweep + hamming_snapshot, opening the 5th GF(3) cycle
