# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-10  
**Run:** world-increment sweep #13–23 (GF3 color chain)  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Sampled | Top Stars |
|--------|------|--------------|-----------|
| plurigrid | org | 15 | asi (60★), gorj (1★, 1770 issues) |
| kubeflow | org | 15 | kubeflow (15810★), pipelines (4180★), spark-operator (3146★) |
| TeglonLabs | org | 5 | mathpix-gem (2★), jank-crane (C++) |
| bmorphism | user | 13 | Gay.jl (2★, 188 issues), ocaml-mcp-sdk (61★), anti-bullshit-mcp-server (23★) |
| zubyul | user | 10 | gay-world (1★), plurigrid-site |
| migalkin | social | 5 | NodePiece (144★), StarE (89★), kgcourse2021 (24★) |
| DJedamski | social | 4 | — |
| wasita | social | 5 | wasita.github.io (1★), magic-garden (2★) |
| kristinezheng | social | 2 | — |
| M1shaaa | social | 2 | — |
| AustinCStone | social | 4 | TextGAN (92★), StereoVisionMRF (11★) |

**Total new increments:** 11 (ids 13–23)  
**Total repo snapshots inserted:** 80  
**Cumulative DB state:** 34 increments, 1024 repo snapshots

### GF(3) Color Chain (this run)

| id | trit | color | name | source |
|----|------|-------|------|--------|
| 13 | +1 | #b8bb26 PLUS | plurigrid | 2026-08-10 |
| 14 | -1 | #cc241d MINUS | kubeflow | 2026-08-10 |
| 15 | 0 | #d3869b ERGODIC | TeglonLabs | 2026-08-10 |
| 16 | +1 | #b8bb26 PLUS | bmorphism | 2026-08-10 |
| 17 | -1 | #cc241d MINUS | zubyul | 2026-08-10 |
| 18 | 0 | #d3869b ERGODIC | migalkin | 2026-08-10 |
| 19 | +1 | #b8bb26 PLUS | DJedamski | 2026-08-10 |
| 20 | -1 | #cc241d MINUS | wasita | 2026-08-10 |
| 21 | 0 | #d3869b ERGODIC | kristinezheng | 2026-08-10 |
| 22 | +1 | #b8bb26 PLUS | M1shaaa | 2026-08-10 |
| 23 | -1 | #cc241d MINUS | AustinCStone | 2026-08-10 |

### Notable Activity

- **plurigrid/gorj**: Clojure, 1770 open issues — active forj development
- **plurigrid/eirobri**: 31 open issues — EiRoBri replay world active
- **kubeflow/pipelines**: 4180★, 525 open issues — top ML pipeline project
- **kubeflow/trainer**: 2177★ — LLM fine-tuning on Kubernetes
- **bmorphism/Gay.jl**: 188 open issues — wide-gamut GF(3) color library active
- **bmorphism**: 3 repos pushed today (nashator-h1, attention-heat-capacity, oldies-clearing, paraoptic, keywire, oldies-kernel) — extremely active
- **wasita**: xoxowasita-analysis pushed 2026-08-10 — new analysis repo
- **migalkin**: kgcourse2021 updated 2026-07-10 — KG course materials still maintained

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 wallets in the Hamming swarm (alice, bob, A–Z) returned **0 APT** at time of sweep. The Aptos fullnode API returned no CoinStore resource, indicating accounts either have zero balance or the AptosCoin store has not been initialized for these addresses on mainnet.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A | 0x8699ed… | 0.0 |
| B | 0x3f892e… | 0.0 |
| C | 0x38b99e… | 0.0 |
| D | 0xf77656… | 0.0 |
| E | 0xdc1d9d… | 0.0 |
| F | 0x18a14b… | 0.0 |
| G | 0x69a394… | 0.0 |
| H | 0xce67c3… | 0.0 |
| I | 0x070fe5… | 0.0 |
| J | 0x4d964d… | 0.0 |
| K | 0xa73204… | 0.0 |
| L | 0x7c2eae… | 0.0 |
| M | 0x6fed37… | 0.0 |
| N | 0xe7dde6… | 0.0 |
| O | 0x73252b… | 0.0 |
| P | 0x621879… | 0.0 |
| Q | 0xac40fa… | 0.0 |
| R | 0x7ce605… | 0.0 |
| S | 0xb87530… | 0.0 |
| T | 0x357810… | 0.0 |
| U | 0x758600… | 0.0 |
| V | 0xb59dd8… | 0.0 |
| W | 0x5f32ae… | 0.0 |
| X | 0xa95cbb… | 0.0 |
| Y | 0xd8e328… | 0.0 |
| Z | 0x7af0ef… | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires **2 signatures**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4… | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a… | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1… | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a… | 2 | ✓ HEALTHY |
| V-W | 0x40fad7… | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` returned a Next.js SPA shell — no static `/api/markets` endpoint responds with JSON. Market data requires JavaScript execution; no records inserted into `mnx_snapshots`.

---

## DB Stats After Run

```
world_increments:  34 rows (23 new this session)
repo_snapshots:  1024 rows (80 new this session)
aptos_snapshots:    28 rows (new this run)
multisig_probes:     5 rows (new this run)
mnx_snapshots:       0 rows (SPA, no API)
```
