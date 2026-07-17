# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-17

## Sweep Metadata
- **Date:** 2026-07-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 82 |
| kubeflow | org | 49 | 34,375 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 252 |
| zubyul | user | 10 | 7 |
| migalkin | social-graph | 5 | 275 |
| AustinCStone | social-graph | 5 | 106 |
| wasita | social-graph | 6 | 5 |
| DJedamski | social-graph | 4 | 3 |
| M1shaaa | social-graph | 3 | 0 |
| kristinezheng | social-graph | 3 | 0 |
| **TOTAL** | | **290** | **35,107** |

### GF(3) Color Chain
290 world increments assigned with rotating GF(3) trit chain:
- `id % 3 == 0` → trit=0, **ERGODIC** `#d3869b`
- `id % 3 == 1` → trit=1, **PLUS** `#b8bb26`
- `id % 3 == 2` → trit=-1, **MINUS** `#cc241d`

### Notable Repos

**plurigrid** — pushed most recently 2026-07-17:
- `gorj` (Clojure, 1★) — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `asi` (HTML, 30★) — everything is topological chemputer!
- `place` (TeX, 1★) — pushed 2026-07-14

**kubeflow** — most active org:
- `pipelines` (Python, 4167★) — pushed 2026-07-16 — Machine Learning Pipelines
- `trainer` (Go, 2150★) — pushed 2026-07-16 — Distributed AI Model Training + LLM Fine-Tuning
- `spark-operator` (Python, 3137★) — pushed 2026-07-16

**bmorphism**:
- `ocaml-mcp-sdk` (OCaml, 61★) — OCaml SDK for MCP using Jane Street's oxcaml_effect
- `anti-bullshit-mcp-server` (JS, 22★) — Claims analysis via epistemological frameworks
- `Gay.jl` (Julia, 2★) — Wide-gamut color sampling with splittable determinism, pushed 2026-07-14

**migalkin** (social graph):
- `NodePiece` (Python, 144★) — Compositional KG Representations, ICLR'22
- `StarE` (Python, 89★) — Hyper-Relational KG message passing, EMNLP 2020

**AustinCStone** (social graph):
- `TextGAN` (Python, 92★) — GAN-based text generation in TensorFlow
- `byteruckus` (HTML) — pushed 2026-07-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned **0.0 APT**.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B | 0x3f892e... | 0.0 |
| C | 0x38b99e... | 0.0 |
| D | 0xf77656... | 0.0 |
| E | 0xdc1d9d... | 0.0 |
| F | 0x18a14b... | 0.0 |
| G | 0x69a394... | 0.0 |
| H | 0xce67c3... | 0.0 |
| I | 0x070fe5... | 0.0 |
| J | 0x4d964d... | 0.0 |
| K | 0xa73204... | 0.0 |
| L | 0x7c2eae... | 0.0 |
| M | 0x6fed37... | 0.0 |
| N | 0xe7dde6... | 0.0 |
| O | 0x73252b... | 0.0 |
| P | 0x621879... | 0.0 |
| Q | 0xac40fa... | 0.0 |
| R | 0x7ce605... | 0.0 |
| S | 0xb87530... | 0.0 |
| T | 0x35781d... | 0.0 |
| U | 0x75860d... | 0.0 |
| V | 0xb59dd8... | 0.0 |
| W | 0x5f32ae... | 0.0 |
| X | 0xa95cbb... | 0.0 |
| Y | 0xd8e328... | 0.0 |
| Z | 0x7af0ef... | 0.0 |

All 28 accounts hold 0 APT in their `CoinStore<AptosCoin>`. Accounts exist on-chain but may be funded via other token types or have not yet received APT.

### Multisig Contract Probes

All 5 multisigs live and responding — all require **2 signatures**:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✅ healthy |
| A-G | 0xf56c4a... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1... | 2 | ✅ healthy |
| S-T | 0x3b1c3a... | 2 | ✅ healthy |
| V-W | 0x40fad7... | 2 | ✅ healthy |

### MNX Markets

`https://testnet.mnx.fi/api/markets` → **401 Unauthorized**
`https://testnet.mnx.fi/api/v1/markets` → **unavailable**

MNX testnet API requires authentication. No market data extracted. `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments    (290 rows) — GF(3) chain indexed repo events
├── repo_snapshots      (290 rows) — full repo metadata
├── aptos_snapshots     (28 rows)  — Hamming swarm wallet balances
├── multisig_probes     (5 rows)   — multisig signature requirements
└── mnx_snapshots       (0 rows)   — MNX unavailable (401)
```

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
