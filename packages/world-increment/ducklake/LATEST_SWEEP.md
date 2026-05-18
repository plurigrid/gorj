# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-18  
**Branch:** world-increment/sweep  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 47 |
| kubeflow | org | 32 |
| TeglonLabs | org | 4 |
| bmorphism | user | 20 |
| zubyul | user | 13 |
| migalkin | social graph | 7 |
| wasita | social graph | 6 |
| AustinCStone | social graph | 5 |
| kristinezheng | social graph | 4 |
| M1shaaa | social graph | 4 |
| DJedamski | social graph | 4 |
| **TOTAL** | | **146** |

### Top Repositories by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,647 | — |
| kubeflow/pipelines | 4,139 | Python |
| kubeflow/spark-operator | 3,126 | Python |
| kubeflow/trainer | 2,100 | Go |
| kubeflow/katib | 1,682 | Python |
| kubeflow/examples | 1,463 | Jsonnet |
| kubeflow/manifests | 1,017 | YAML |
| kubeflow/arena | 810 | Go |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| plurigrid/asi | 23 | HTML |
| plurigrid/ontology | 8 | JavaScript |

### Active Recently (pushed 2026)

- **plurigrid/gorj** — pushed 2026-05-18 (240 open issues) — forj + Rama topology nREPL routing + GF(3)
- **plurigrid/asi** — pushed 2026-04-26 — everything is topological chemputer!
- **plurigrid/nanoclj-zig** — pushed 2026-04-25 — NaN-boxed Clojure interpreter in Zig 0.15
- **bmorphism/Gay.jl** — pushed 2026-05-18 (189 issues) — Wide-gamut color sampling
- **bmorphism/oxgame** — pushed 2026-05-15 — Stellar resolution and open-game composition
- **kubeflow/hub** — pushed 2026-05-18 — Model Registry for ML model developers
- **wasita/wasita.github.io** — pushed 2026-05-18 — personal website (Svelte)
- **zubyul/ghostel-emacs-worlds** — pushed 2026-04-24 — Ghostty + alice/bob emacs stack

### GF(3) Color Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 48 |
| 1 | #b8bb26 | PLUS | 49 |
| -1 | #cc241d | MINUS | 49 |

### DuckDB Schema

```sql
world_increments  -- 146 rows: GF3 trit-colored event log
repo_snapshots    -- 146 rows: full repo metadata
aptos_snapshots   -- 28 rows: Hamming swarm wallet balances
multisig_probes   -- 5 rows: multisig contract health
mnx_snapshots     -- 0 rows: SPA, no public JSON API
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 accounts: alice, bob, A-Z)

All 28 addresses queried against Aptos mainnet
(fullnode.mainnet.aptoslabs.com v1 CoinStore resource endpoint)

**Result:** All accounts returned 0 APT — addresses do not hold CoinStore resources
on-chain (uninitialised or empty accounts on mainnet).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z | 0x8699... to 0x7af0... | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 probed via 0x1::multisig_account::num_signatures_required

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

Status: **SPA / unavailable via public JSON API**
testnet.mnx.fi is a Next.js SPA (MegaETH testnet DEX).
API backend at api.testnet.mnx.fi returned Cannot GET /markets and Cannot GET /v1/markets.
No structured market data could be extracted. mnx_snapshots table is empty.

---

## Summary

- **146 GitHub repos** snapshotted across 11 sources (3 orgs + 8 users incl. zubyul social graph)
- **28 Aptos wallets** probed — all 0 APT (uninitialised mainnet accounts)
- **5 multisig contracts** healthy, all requiring 2 signatures
- **MNX markets** unavailable via public API (SPA, no REST endpoints exposed)
- DuckDB: packages/world-increment/ducklake/world-increments.duckdb
