# World-Increment Sweep + Hamming Swarm Snapshot
**Run date:** 2026-07-26  
**Increment ID:** 13  
**GF(3):** trit=1 · PLUS · #b8bb26  
**Snapshot hash:** 3f1a8c2b4e7d9f06

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted | Notable |
|--------|------|-------------------|---------|
| plurigrid | org | 44 | gorj (1408 open issues), asi (31 ★) |
| kubeflow | org | 26 | kubeflow/kubeflow (15,794 ★), pipelines (4,170 ★) |
| TeglonLabs | org | 5 | jank-crane (C++), mathpix-gem (Ruby) |
| bmorphism | user | 20 | Gay.jl (188 open issues), ocaml-mcp-sdk (61 ★) |
| zubyul | user | 18 | from-possible-worlds (TeX, pushed 2026-07-18) |
| migalkin | social | 6 | NodePiece (144 ★), StarE (89 ★) |
| kristinezheng | social | 3 | kristinezheng.github.io active |
| AustinCStone | social | 5 | TextGAN (92 ★), byteruckus (2026-07-15) |
| DJedamski | social | 3 | kaggle_ncaa18, School |
| wasita | social | 6 | wasita.github.io active (2026-07-21) |
| M1shaaa | social | 3 | profile config, lab-bookshelf- |

**Total repos this sweep:** 139 (cumulative in DB: 1,083)

### Most Active Repos (recent pushes)
- `kubeflow/pipelines` — 2026-07-26 (Python, 4,170 ★)
- `plurigrid/gorj` — 2026-07-26 (Clojure, 1,408 open issues)
- `kubeflow/dashboard` — 2026-07-26 (TypeScript)
- `bmorphism/Gay.jl` — 2026-07-26 (Julia, 188 open issues)
- `zubyul/from-possible-worlds` — 2026-07-18 (TeX)
- `wasita/wasita.github.io` — 2026-07-21 (Svelte)

### Top Stars This Sweep
- `kubeflow/kubeflow` — 15,794 ★
- `kubeflow/pipelines` — 4,170 ★
- `kubeflow/spark-operator` — 3,143 ★
- `kubeflow/trainer` — 2,153 ★
- `kubeflow/katib` — 1,692 ★
- `kubeflow/examples` — 1,461 ★

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming swarm wallets queried against Aptos mainnet fullnode.  
**Result:** All wallets return 0.0 APT (CoinStore resource absent — accounts may be uninitiated or hold non-APT assets).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | 0x8699...→ 0x7af0... | 0.0 each |

> Note: Zero balance likely means CoinStore<AptosCoin> not registered on these addresses, not that they are empty — they may hold other tokens or Move objects.

### Multisig Contract Probes (5 pairs)

| Pair | Contract Address (prefix) | Sigs Required | Status |
|------|--------------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

All 5 multisig contracts operational, all require **2-of-N signatures**.

### MNX Markets (testnet.mnx.fi)

- `/api/markets` → HTTP 404 (endpoint not found)
- Main page → SPA shell, renders only "MNX" text
- **Status: UNAVAILABLE** — no public API accessible without JS execution

---

## DuckDB State

```
DB: packages/world-increment/ducklake/world-increments.duckdb
world_increments:  24 rows (IDs 1–13 + historical)
repo_snapshots:  1,083 rows total
aptos_snapshots:    28 rows (this sweep)
multisig_probes:     5 rows (this sweep)
mnx_snapshots:       0 rows (unavailable)
```

## GF(3) Color Chain

| id mod 3 | trit | color | name |
|----------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | 1 | #b8bb26 | **PLUS** ← id=13 |
| 2 | -1 | #cc241d | MINUS |
