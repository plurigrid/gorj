# World-Increment Sweep + Hamming Snapshot

**Generated:** 2026-08-07  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 143 | 102,213 |
| migalkin | user (social) | 65 | 829 |
| bmorphism | user | 300 | 509 |
| AustinCStone | user (social) | 89 | 322 |
| plurigrid | org | 300 | 193 |
| zubyul | user | 97 | 40 |
| TeglonLabs | org | 111 | 14 |
| DJedamski | user (social) | 22 | 14 |
| wasita | user (social) | 60 | 6 |
| M1shaaa | user (social) | 32 | 0 |
| kristinezheng | user (social) | 36 | 0 |

**Total repos snapshotted:** 1,255  
**Total world-increment events:** 334

### GF(3) Color Chain Distribution

| Color | Hex | GF3 Name | Count |
|-------|-----|----------|-------|
| Pink | `#d3869b` | ERGODIC (trit=0) | 110 |
| Yellow-Green | `#b8bb26` | PLUS (trit=+1) | 112 |
| Red | `#cc241d` | MINUS (trit=-1) | 112 |

### Notable Repos

**Most Active (recent push):**
- `plurigrid/gorj` — Clojure, 1 star, pushed 2026-08-07 (today)
- `plurigrid/eirobri` — Clojure, pushed 2026-08-04
- `bmorphism/Gay.jl` — Julia, 188 open issues, pushed 2026-08-07
- `kubeflow/pipelines` — Python, 4,181 stars, pushed 2026-08-07

**Highest Stars:**
- `kubeflow/kubeflow` — 15,805 ⭐
- `kubeflow/pipelines` — 4,181 ⭐
- `kubeflow/spark-operator` — 3,145 ⭐
- `kubeflow/trainer` — 2,173 ⭐
- `kubeflow/katib` — 1,694 ⭐
- `migalkin/NodePiece` — 144 ⭐ (knowledge graph KG)
- `AustinCStone/TextGAN` — 92 ⭐ (TF text generation)
- `migalkin/StarE` — 89 ⭐ (hyper-relational KGs)
- `plurigrid/asi` — 59 ⭐ (topological chemputer)
- `bmorphism/ocaml-mcp-sdk` — 61 ⭐ (OCaml MCP SDK)

**Plurigrid Ecosystem Themes:**
- Gay.jl GF(3) deterministic color system (plurigrid, bmorphism, zubyul)
- MCP server proliferation (bmorphism, TeglonLabs, kubeflow)
- Categorical / topos theory repos (bmorphism, plurigrid)
- Aptos / Move chain work (zubyul/vibesnipe, bmorphism/boxxy, bmorphism/vibesnipe-market)
- jank C++ Clojure IR (TeglonLabs/jank-crane, plurigrid/shrimp)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Snapshot timestamp:** 2026-08-07  
**Total APT across 28 addresses:** 20.34 APT  
**Method:** `0x1::coin::balance<0x1::aptos_coin::AptosCoin>` view function (fungible asset module)

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob | 12.657007 | 0x0a3c00c5... |
| F | 1.960516 | 0x18a14b5b... |
| L | 1.927269 | 0x7c2eaeaf... |
| J | 1.895093 | 0x4d964db8... |
| K | 0.161961 | 0xa732040a... |
| alice | 0.436434 | 0xc793acde... |
| O | 0.210136 | 0x73252b60... |
| P | 0.140136 | 0x62187920... |
| M | 0.112285 | 0x6fed37a7... |
| N | 0.106121 | 0xe7dde6da... |
| Q | 0.103240 | 0xac40fa50... |
| S | 0.091788 | 0xb8753014... |
| R | 0.090217 | 0x7ce605cc... |
| T | 0.073713 | 0x35781dc0... |
| U | 0.055773 | 0x75860da4... |
| A | 0.051767 | 0x8699edc0... |
| X | 0.042577 | 0xa95cbbd1... |
| W | 0.040705 | 0x5f32aef7... |
| B | 0.036256 | 0x3f892ebe... |
| V | 0.048833 | 0xb59dd817... |
| Y | 0.044449 | 0xd8e32848... |
| Z | 0.024268 | 0x7af0ef6e... |
| C | 0.010185 | 0x38b99e63... |
| D | 0.011629 | 0xf7765624... |
| E | 0.009372 | 0xdc1d9d53... |
| H | 0.001681 | 0xce67c327... |
| G | 0.000681 | 0x69a394c0... |
| I | 0.000681 | 0x070fe5d7... |

**Note:** alice (0xc793) is a smart contract account (PackageRegistry, ACSetMeta2, lending pool). Most wallets hold small gas balances; bob has the largest single holding at 12.66 APT.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required` view:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✅ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✅ HEALTHY |

All 5 multisig contracts require **2-of-n** threshold. All healthy.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — API endpoints return HTML (no JSON market data accessible via static fetch). Market data unavailable without browser execution. `mnx_snapshots` table: 0 rows.

---

## DuckDB Schema Summary

```sql
world_increments  — 334 rows  (GF3 color-chained events)
repo_snapshots    — 1,255 rows (full GitHub repo metadata)
aptos_snapshots   — 28 rows   (wallet balances, timestamp: 2026-08-07)
multisig_probes   — 5 rows    (2-of-n threshold, all healthy)
mnx_snapshots     — 0 rows    (SPA, no API data)
```
