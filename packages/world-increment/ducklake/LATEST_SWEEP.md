# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 79 (cumulative, +56 this run) |
| Total Repo Snapshots | 529 (cumulative) |
| Sources Covered | 3 orgs + 8 users + social graph |
| Aptos Wallets Queried | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy) |
| MNX Markets | unavailable (Next.js SPA) |

---

## GF(3) Color Chain — All 12 Increments

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

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle

---

## JOB 2: Hamming Swarm Snapshot (2026-07-22)

### Aptos Wallet Balances

Method: `0x1::primary_fungible_store::balance` view function (Fungible Asset standard, Aptos 1.16+).  
Note: Legacy `CoinStore` resource returns 404 on all accounts — FA standard confirmed.

| World | APT Balance | Address |
|-------|-------------|---------|
| bob | 12.65700700 | 0x0a3c...b5d |
| F | 1.96051600 | 0x18a1...f71 |
| L | 1.92726900 | 0x7c2e...ba9 |
| J | 1.89509300 | 0x4d96...f54 |
| alice | 0.43643352 | 0xc793...c7b |
| K | 0.16197700 | 0xa732...dc4 |
| O | 0.21013400 | 0x7325...89d |
| P | 0.14011000 | 0x6218...948 |
| M | 0.11233200 | 0x6fed...e9 |
| N | 0.10611300 | 0xe7dd...b2c |
| A | 0.05176700 | 0x8699...7a |
| B | 0.03625600 | 0x3f89...b13 |
| C | 0.01018500 | 0x38b9...35e |
| D | 0.01161700 | 0xf776...dd1 |
| E | 0.00937600 | 0xdc1d...d36 |
| G | 0.00073300 | 0x69a3...f32 |
| H | 0.00170100 | 0xce67...30f |
| I | 0.00073200 | 0x070f...fc9 |
| Q | 0.10320400 | 0xac40...a9 |
| R | 0.09022200 | 0x7ce6...e10 |
| S | 0.09182700 | 0xb875...386 |
| T | 0.07374800 | 0x3578...588 |
| U | 0.05584000 | 0x7586...956 |
| V | 0.04879800 | 0xb59d...2c3 |
| W | 0.04073400 | 0x5f32...7b0 |
| X | 0.04256000 | 0xa95c...47d |
| Y | 0.04443000 | 0xd8e3...4c4 |
| Z | 0.02431400 | 0x7af0...97c |

**Total swarm balance: ~20.29 APT** across 28 addresses  
**Richest address:** `bob` at 12.657 APT  
**Richest letter:** `F` at 1.961 APT

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable — Next.js SPA, no accessible REST API.**  
Endpoints tried: `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/instruments` (all 404).  
`/markets` returns HTTP 200 but serves HTML shell — no embedded market data extractable via curl.

---

## Notable Highlights This Run

- **plurigrid/gorj** — pushed TODAY (2026-07-22), 1325 open issues
- **kubeflow/trainer** — Go, 2,153★, LLM fine-tuning on Kubernetes (pushed today)
- **bmorphism/Gay.jl** — Julia, 187 open issues (active development)
- **migalkin/NodePiece** — 144★ KG embeddings (ICLR'22)
- **bob wallet** — holds 12.657 APT (dominant in swarm)
- **All 5 multisig contracts** → 2-of-N, all healthy
