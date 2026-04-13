# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-13

## Sweep Metadata
- **Date:** 2026-04-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 78 |
| Total Repo Snapshots | 537 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 (all healthy, 2-of-N) |
| MNX Markets | unavailable (SPA, no JSON API) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — Source Sequence

| Increment | Source | GF3 Trit | Color | Name |
|---|---|---|---|---|
| 1 | plurigrid/nash-portal | +1 | `#b8bb26` | **PLUS** |
| 2 | plurigrid/gorj | -1 | `#cc241d` | **MINUS** |
| 3 | plurigrid/asi | 0 | `#d3869b` | **ERGODIC** |
| 4 | plurigrid/horse | +1 | `#b8bb26` | **PLUS** |
| 5 | plurigrid/web-browser | -1 | `#cc241d` | **MINUS** |
| 6 | plurigrid/nanoclj-zig | 0 | `#d3869b` | **ERGODIC** |
| … | … (66 total) | … | … | … |
| 66 | AustinCStone/EpsteinSearch | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC` repeating across all 66 repo increments.

### Top Repos by Source

#### plurigrid (16 repos sampled, pushed today 2026-04-13)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-04-13 |
| nash-portal | Rust | 0 | 2026-04-13 |
| asi | HTML | 16 | 2026-04-13 |
| nanoclj-zig | Zig | 0 | 2026-04-09 |
| asi-skills | Julia | 3 | 2026-04-09 |
| ontology | JavaScript | 7 | 2025-05-27 |

#### kubeflow (11 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,570 | 2026-01-05 |
| pipelines | Python | 4,119 | 2026-04-12 |
| spark-operator | Python | 3,114 | 2026-04-11 |
| trainer | Go | 2,082 | 2026-04-10 |
| katib | Python | 1,678 | 2026-04-12 |
| mpi-operator | Go | 523 | 2026-04-13 |
| model-registry | Go | 172 | 2026-04-13 |

#### TeglonLabs (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| topoi | Python | 0 |
| monad-mcp-server | — | 0 |

#### bmorphism (12 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| hypernym-mcp-server | JavaScript | 6 |
| GeoACSets.jl | Julia | 0 |

#### zubyul social graph
| Repo | Language | Stars |
|------|----------|-------|
| migalkin/NodePiece | Python | 143 |
| migalkin/StarE | Python | 88 |
| AustinCStone/TextGAN | Python | 92 |
| AustinCStone/StereoVisionMRF | Python | 11 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Probed:** 2026-04-13  
**Node:** `fullnode.mainnet.aptoslabs.com`

### Wallet Balances — alice, bob, A–Z (28 addresses)

All 28 addresses returned **0.00 APT** via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
Accounts are either unregistered or unfunded on Aptos mainnet.

| World | Address | Balance |
|---|---|---|
| alice | 0xc793acdec12b4a63… | 0.00 APT |
| bob | 0x0a3c00c58fdf9020… | 0.00 APT |
| A–Z (26) | 0x8699…–0x7af0… | 0.00 APT each |

### Multisig Contract Probes — All Healthy ✅

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f428a0c007da… | **2** | ✅ healthy |
| A-G | 0xf56c4a1c0906214f… | **2** | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df406… | **2** | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a… | **2** | ✅ healthy |
| V-W | 0x40fad7b423a84365… | **2** | ✅ healthy |

All 5 multisig accounts require 2-of-N signatures and responded successfully.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — The SPA at testnet.mnx.fi exposes no accessible JSON API.  
Probed: `/api/markets`, `/api/v1/markets`, `/api/tickers` — all returned empty responses.  
`mnx_snapshots` table remains empty for this sweep.

---

## DuckDB Schema

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
- **kubeflow/kubeflow**: 15,570 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — ML pipelines (pushed 2026-04-12)
- **kubeflow/spark-operator**: 3,114 stars — Kubernetes Spark operator (pushed 2026-04-11)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP via Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-13)
- **plurigrid/gorj**: This very repo — forj + Rama nREPL routing + GF(3) gay trit coloring (172 open issues, pushed 2026-04-13)
- **Multisigs A-B, A-G, Y-Z, S-T, V-W**: All live on Aptos mainnet, 2-of-N threshold, 100% healthy
