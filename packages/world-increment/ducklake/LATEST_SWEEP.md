# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-11  
**Run type:** Automated background sweep  
**GF(3) color chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 300 |
| bmorphism | user | 209 |
| TeglonLabs | org | 109 |
| kubeflow | org | 100 |
| AustinCStone | user (social) | 88 |
| migalkin | user (social) | 64 |
| wasita | user (social) | 63 |
| zubyul | user | 53 |
| kristinezheng | user (social) | 38 |
| M1shaaa | user (social) | 33 |
| DJedamski | user (social) | 24 |

**Total repo snapshots:** 1,081  
**World increments logged:** 160

### GF(3) Trit Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 52 |
| 1 | #b8bb26 | PLUS | 54 |
| -1 | #cc241d | MINUS | 54 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,772 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,136 | Python |
| kubeflow/trainer | 2,134 | Go |
| kubeflow/katib | 1,689 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| plurigrid/asi | 30 | HTML |

### Notable Activity (most recently pushed)

- **plurigrid/gorj** — pushed 2026-07-10 (1,109 open issues — GF3+nREPL routing)
- **plurigrid/asi** — pushed 2026-07-10 (30 stars, "everything is topological chemputer!")
- **plurigrid/place** — pushed 2026-07-07
- **kubeflow/pipelines** — pushed 2026-07-10 (417 open issues)
- **kubeflow/trainer** — pushed 2026-07-10
- **migalkin/kgcourse2021** — pushed 2026-07-10

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `https://fullnode.mainnet.aptoslabs.com/v1` at 1s intervals.

**All 28 wallets (alice, bob, A-Z) show 0.0 APT.**
Wallets appear unfunded on mainnet for the CoinStore<AptosCoin> resource.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A-Z | 0x8699ed...–0x7af0ef... | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts on Aptos mainnet are HEALTHY (2-of-N threshold each).

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f4... | 2 | healthy |
| A-G | 0xf56c4a... | 2 | healthy |
| Y-Z | 0xd3ffe1... | 2 | healthy |
| S-T | 0x3b1c3a... | 2 | healthy |
| V-W | 0x40fad7... | 2 | healthy |

### MNX Markets

`https://testnet.mnx.fi` is behind Vercel deployment protection (auth required).
No market data available this sweep. Requires Vercel CLI auth or Trusted Sources OIDC token.

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 160 |
| repo_snapshots | 1,081 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

## Key Findings

1. **plurigrid/gorj has 1,109 open issues** — highest issue count in sweep, active GF3+nREPL work
2. **Kubeflow dominates by stars** (15k+) — active ML-on-Kubernetes ecosystem
3. **All 28 Hamming swarm wallets show 0 APT** — wallets exist on-chain but hold no native APT
4. **All 5 multisig contracts healthy** — all require 2-of-N signatures, all responding
5. **bmorphism active in OCaml/ZK/Zig space** — ocaml-mcp-sdk (61 stars), recently active
6. **MNX testnet gated** — Vercel auth wall, market data unavailable this sweep
