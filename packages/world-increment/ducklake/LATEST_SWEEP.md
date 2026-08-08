# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-08T01:10 UTC  
**Branch:** world-increment/sweep-2026-08-08-0108  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### GF(3) Increment Chain

| Increment | GF3 | Color | Source | Repos |
|-----------|-----|-------|--------|-------|
| #12 | ERGODIC (0) | #d3869b | org:plurigrid | 50 |
| #13 | PLUS (+1) | #b8bb26 | org:kubeflow | 49 |
| #14 | MINUS (-1) | #cc241d | org:TeglonLabs | 5 |
| #15 | ERGODIC (0) | #d3869b | user:bmorphism | 15 |
| #16 | PLUS (+1) | #b8bb26 | user:zubyul | 8 |
| #17 | MINUS (-1) | #cc241d | social_graph | 13 |

**Total repos this sweep:** 140 (cumulative in DB: 1,084)  
**Total world-increments in DB:** 29

### Notable Repos by Source

**plurigrid (org) — 50 repos**  
Session-bound GITHUB_TOKEN; listing retrieved via `search_repositories`. Existing DB entries from prior sweeps plus this run cover the full org portfolio.

**kubeflow (org) — 49 repos**  
MLOps/Kubernetes ML platform ecosystem (Katib, Pipelines, Training, Notebooks, etc.).

**TeglonLabs (org) — 5 repos**  
- `jank-crane` (C++, 2026-06-08) — crane-jank converged-IR hub, GF3 convergence maps  
- `mathpix-gem` (Ruby) — math OCR gem, 2 stars, 11 open issues  
- `coin-flip-mcp` (JS) — MCP server for random.org coin flips  
- `monad-mcp-server` — Monad MCP Server  
- `topoi` (Python) — 1 open issue  

**bmorphism — 15 repos (top recent)**  
- `anti-bullshit-mcp-server` — 23⭐, 7 forks, updated 2026-08-02  
- `ocaml-mcp-sdk` — 61⭐, OCaml SDK for MCP using oxcaml_effect  
- `Gay.jl` — 2⭐, wide-gamut color sampling (188 open issues)  
- `gay-chat` (Scheme) — gay://chat operationalization over Spritely Brassica  
- `satreadout` (HTML) — machine-checked saturating non-Riemannian perceptual readout  
- `world` (Python) — local worlds launcher for SA3, jank, world proofs  
- `oxgame` (OCaml) — stellar resolution + open-game composition  

**zubyul — 8 repos (top recent)**  
- `voice-observatory` (Python) — passive macOS TUI for voice-download pathways  
- `ghostel-emacs-worlds` (GLSL) — Ghostty config + alice/bob emacs-mods  
- `tilelang-kernels` (Python) — TileLang GPU kernels for GF(3) trit classification, targeting NVIDIA GB10 Blackwell  
- `gay-world` (Python) — 1⭐/1fork, goblin world builder  

**Social Graph (migalkin, wasita, kristinezheng, M1shaaa, AustinCStone, DJedamski)**  
- `migalkin/NodePiece` — 144⭐, 21 forks — compositional KG representations (ICLR'22)  
- `migalkin/StarE` — 89⭐, 16 forks — EMNLP 2020 hyper-relational KGs  
- `migalkin/kgcourse2021` — 24⭐, 8 forks — KG course, updated 2026-07-10  
- `wasita/wm-cv` — updated 2026-08-07 (most recent push in social graph)  
- `wasita/xoxowasita-analysis` — created 2026-08-04  

> **Note:** Direct GitHub org/user listing endpoints blocked (session scoped to `plurigrid/gorj`). All repo data retrieved via `search_repositories` public search API. DJedamski returned no public repos in search results.

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances

**Ledger at time of query:** block 956,496,058 | epoch 16,827 | timestamp ~2026-08-08T01:10 UTC

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

This means **no address in the swarm holds initialized APT** — either the accounts  
have never received APT, or the CoinStore resource was never registered.

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | resource_not_found |
| bob | 0.0 | resource_not_found |
| A–Z (26) | 0.0 each | resource_not_found |

### Multisig Contract Probes

All 5 multisig contracts are **live and responsive** on Aptos mainnet:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...987003` | **2** | ✓ |
| A-G | `0xf56c4a1c...0096` | **2** | ✓ |
| Y-Z | `0xd3ffe181...b883` | **2** | ✓ |
| S-T | `0x3b1c3ae9...7883` | **2** | ✓ |
| V-W | `0x40fad7b4...eb6d` | **2** | ✓ |

All pairs configured as **2-of-N multisig** (2 signatures required). All contracts respond to `0x1::multisig_account::num_signatures_required`. **Status: HEALTHY.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no public JSON API found at  
`/api/markets`, `/api/v1/markets`, or root. Market data not extractable  
without browser execution. **Status: UNAVAILABLE (SPA, no public API).**

---

## DuckDB State Summary

```
world_increments : 29 rows   (6 new this sweep)
repo_snapshots   : 1,084 rows (140 new this sweep)
aptos_snapshots  : 28 rows   (28 new this sweep)
multisig_probes  : 5 rows    (5 new this sweep)
mnx_snapshots    : 0 rows    (SPA, no data available)
```

## Key Signals

1. **bmorphism active:** `anti-bullshit-mcp-server` updated 2026-08-02 (6 days ago); `Gay.jl` branch `gay` has 188 open issues — high activity.  
2. **wasita most recent:** `wm-cv` pushed 2026-08-07 (yesterday) — latest commit in the entire social graph.  
3. **All Hamming swarm multisigs healthy** at 2-of-N threshold — no degradation detected.  
4. **Hamming swarm wallets:** No APT balance found anywhere in alice/bob/A-Z — wallets appear uninitialized on Aptos mainnet.  
5. **TeglonLabs jank-crane** (GF3 convergence maps, C++) — newest TeglonLabs repo, June 2026.
