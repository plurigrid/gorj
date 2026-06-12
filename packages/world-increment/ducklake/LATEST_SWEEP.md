# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-12  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100+ |
| kubeflow | org | 48+ |
| TeglonLabs | org | 5 |
| bmorphism | user | 100+ |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |

**Total deduplicated repo_snapshots in DB: 874**

### Top Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,714 | 2,671 |
| kubeflow/pipelines | Python | 4,152 | 2,005 |
| kubeflow/spark-operator | Python | 3,127 | 1,489 |
| kubeflow/trainer | Go | 2,111 | 965 |
| kubeflow/katib | Python | 1,683 | 525 |
| kubeflow/examples | Jsonnet | 1,461 | 756 |
| kubeflow/manifests | YAML | 1,022 | 1,065 |
| kubeflow/arena | Go | 812 | 190 |
| migalkin/NodePiece | Python | 144 | 21 |
| migalkin/StarE | Python | 89 | 16 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2 |
| bmorphism/say-mcp-server | JavaScript | 20 | 9 |
| bmorphism/babashka-mcp-server | JavaScript | 19 | 6 |
| plurigrid/asi | HTML | 25 | 7 |
| plurigrid/ontology | JavaScript | 8 | 9 |

### Language Distribution (Top 15)

| Language | Repos |
|----------|-------|
| Python | 134 |
| Go | 33 |
| HTML | 31 |
| Rust | 29 |
| JavaScript | 26 |
| Jupyter Notebook | 23 |
| TypeScript | 22 |
| Jsonnet | 16 |
| Clojure | 16 |
| R | 11 |
| Java | 10 |
| TeX | 10 |
| C | 10 |
| Julia | 10 |
| Scheme | 8 |

### GF(3) Color Chain (world_increments)

| ID | Trit | Color | Name | Source |
|----|------|-------|------|--------|
| 12 | 0 | #d3869b | ERGODIC | github_sweep/multi-source |
| 13 | 1 | #b8bb26 | PLUS | org/plurigrid |
| 14 | -1 | #cc241d | MINUS | org/kubeflow |
| 15 | 0 | #d3869b | ERGODIC | org/TeglonLabs |
| 16 | 1 | #b8bb26 | PLUS | user/bmorphism |
| 17 | -1 | #cc241d | MINUS | user/zubyul |
| 18 | 0 | #d3869b | ERGODIC | hamming_swarm/aptos_mainnet |
| 19 | 1 | #b8bb26 | PLUS | hamming_swarm/multisig_probe |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (truncated) | Balance (APT) |
|-------|--------------------|--------------:|
| alice | 0xc793ac…4cc7b | 0.0 |
| bob | 0x0a3c00…512d5d | 0.0 |
| A | 0x8699ed…be9d7a | 0.0 |
| B | 0x3f892e…cb13 | 0.0 |
| C | 0x38b99e…535e | 0.0 |
| D | 0xf77656…cfdd1 | 0.0 |
| E | 0xdc1d9d…8d36 | 0.0 |
| F | 0x18a14b…3cf71 | 0.0 |
| G | 0x69a394…7f32 | 0.0 |
| H | 0xce67c3…5300f | 0.0 |
| I | 0x070fe5…1fc9 | 0.0 |
| J | 0x4d964d…7f54 | 0.0 |
| K | 0xa73204…5dc4 | 0.0 |
| L | 0x7c2eae…eba9 | 0.0 |
| M | 0x6fed37…7f2e9 | 0.0 |
| N | 0xe7dde6…51b2c | 0.0 |
| O | 0x73252b…a89d | 0.0 |
| P | 0x621879…c948 | 0.0 |
| Q | 0xac40fa…c89a9 | 0.0 |
| R | 0x7ce605…76e10 | 0.0 |
| S | 0xb87530…d0386 | 0.0 |
| T | 0x35781d…f4588 | 0.0 |
| U | 0x75860d…f9956 | 0.0 |
| V | 0xb59dd8…af2c3 | 0.0 |
| W | 0x5f32ae…c7b0 | 0.0 |
| X | 0xa95cbb…3047d | 0.0 |
| Y | 0xd8e328…444c4 | 0.0 |
| Z | 0x7af0ef…e197c | 0.0 |

**All 28 hamming-swarm wallets: 0.0 APT** (accounts have zero APT coin balance on mainnet)

### Multisig Contract Probes

All 5 contracts probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`

| Pair | Address (truncated) | Sigs Required | Status |
|------|--------------------|--------------:|--------|
| A-B | 0x0da4f4…87003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a…0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe1…b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3a…7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fad7…eb6d | 2 | ✅ HEALTHY |

**All 5 multisigs: 2-of-2 threshold, healthy.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — Vercel deployment protection active. The SPA at `testnet.mnx.fi` and all API paths (`/api/markets`, `/api/v1/markets`) return HTTP 401 Authentication Required. No market data could be extracted.

---

## Database Summary

```
Table              Rows
-----------------  ----
world_increments     31  (GF3 color chain, today + prior sweeps)
repo_snapshots      874  (deduplicated across all orgs/users/social-graph)
aptos_snapshots      28  (hamming swarm: alice, bob, A-Z)
multisig_probes       5  (A-B, A-G, Y-Z, S-T, V-W — all 2-of-2)
mnx_snapshots         1  (unavailable — Vercel auth required)
```

## Notable Findings

- **plurigrid/gorj** (this repo) has 516 open issues — most issue-active repo in the sweep
- **bmorphism/Gay.jl** has 189 open issues, pushed 2026-06-12 (active today)
- **bmorphism/ocaml-mcp-sdk** is the highest-starred bmorphism repo (61⭐) — OCaml MCP SDK using Jane Street's `oxcaml_effect` library
- **plurigrid/eirobri** has 29 open issues; **plurigrid/nanoclj-zig** has 20 (NaN-boxed Clojure in Zig 0.15)
- **TeglonLabs/jank-crane** pushed 2026-06-08 — C++ crane-jank converged-IR hub with GF3 convergence maps
- **kubeflow/trainer** (2,111⭐) provides distributed AI/LLM fine-tuning on Kubernetes
- **zubyul** social graph spans bio/neuro research (WGCNA, connectome) + cryptographic art (Gay.jl, GayMove, chromatic-VRF)
- All hamming swarm wallets: 0 APT on mainnet (zero-balance or uninitialized CoinStore)
- All 5 multisigs healthy at 2-of-2 threshold — symmetric hamming pairs verified
