# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-01  
**GF(3) chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (mod 3 on increment id)

---

## JOB 1: GitHub Social Graph Sweep

### Repo Snapshot Summary

| Source | Type | Repos Captured | Notable |
|--------|------|---------------|---------|
| plurigrid | org | 100 | gorj (Clojure, pushed 2026-08-01), zig-syrup (Zig), asi (HTML, 57★) |
| kubeflow | org | 30 | kubeflow/kubeflow (15802★), pipelines (4172★), trainer (2165★) |
| TeglonLabs | org | 5 | jank-crane (C++, GF3 convergence maps), mathpix-gem (Ruby) |
| bmorphism | user | 30 | Gay.jl (Julia, 188 issues), ocaml-mcp-sdk (61★), anti-bullshit-mcp-server (22★) |
| zubyul | user | 30 | voice-observatory, ghostel-emacs-worlds, gay-world |
| migalkin | social | 10 | NodePiece (144★, ICLR'22), StarE (89★, EMNLP'20) |
| wasita | social | 10 | wasita.github.io (Svelte), send2kobo (TypeScript) |
| kristinezheng | social | 5 | kristinezheng.github.io, lookit-jenga |
| AustinCStone | social | 10 | byteruckus, EpsteinSearch |
| M1shaaa | social | 8 | lab-bookshelf- (TypeScript) |
| DJedamski | social | 6 | kaggle_ncaa18, Kaggle |

**Total:** 143 new repo snapshots inserted  
**Cumulative DB:** 1087 repo_snapshots, 166 world_increments

### Highlights
- **plurigrid/gorj** pushed 2026-08-01 (this repo) — most recent activity
- **kubeflow/mcp-apache-spark-history-server** pushed 2026-08-01 — 185★
- **bmorphism/Gay.jl** has 188 open issues, recently most active bmorphism repo
- **TeglonLabs/jank-crane** describes "GF3 convergence maps" — thematically linked to this sweep's color chain
- **migalkin** focus: knowledge graph reasoning (NodePiece, StarE, NBFNet_mlx)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 hamming-swarm addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 addresses) | 0x8699...–0x7af0... | 0.0 each |

**Finding:** All 28 addresses return 0 APT. Accounts exist on-chain (API responds, not 404) but hold no native APT. This is consistent with unfunded Hamming swarm addresses or addresses holding only non-APT assets (tokens, NFTs, objects).

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

All 5 multisig contracts report `num_signatures_required = 2`. All healthy.

### MNX Markets (testnet.mnx.fi)

Status: **SPA only — no JSON API accessible.** `https://testnet.mnx.fi/api/markets` and `/api/v1/markets` return 404. The site is a Next.js SPA; market data is loaded client-side. No `mnx_snapshots` rows inserted this run.

---

## DuckDB Summary

```
Table               Rows (cumulative)
world_increments    166
repo_snapshots      1087
aptos_snapshots     28  (this run)
multisig_probes     5   (this run)
mnx_snapshots       0
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`
