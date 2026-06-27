# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-27 19:10 UTC  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Source Summary

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 77 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 48 | 34271 |
| wasita | social | 11 | 5 |
| migalkin | social | 9 | 279 |
| M1shaaa | social | 8 | 0 |
| AustinCStone | social | 6 | 106 |
| DJedamski | social | 6 | 3 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | social | 5 | 0 |

**Total:** 347 repos, 35004 aggregate stars

### Top 15 Repos by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|----------|
| kubeflow/kubeflow | - | 15749 | 2680 | 2026-06-18 |
| kubeflow/pipelines | Python | 4158 | 2012 | 2026-06-27 |
| kubeflow/spark-operator | Python | 3129 | 1492 | 2026-06-26 |
| kubeflow/trainer | Go | 2125 | 972 | 2026-06-26 |
| kubeflow/katib | Python | 1687 | 527 | 2026-06-23 |
| kubeflow/examples | Jsonnet | 1460 | 756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1028 | 1065 | 2026-06-25 |
| kubeflow/arena | Go | 814 | 192 | 2026-06-26 |
| kubeflow/kale | Python | 694 | 156 | 2026-06-25 |
| kubeflow/mpi-operator | Go | 528 | 236 | 2026-06-25 |
| kubeflow/fairing | Jsonnet | 337 | 143 | 2022-04-11 |
| kubeflow/pytorch-operator | Jsonnet | 310 | 143 | 2021-12-01 |
| kubeflow/community | Jupyter Notebook | 194 | 264 | 2026-06-22 |
| kubeflow/website | HTML | 184 | 923 | 2026-06-19 |
| kubeflow/kfp-tekton | TypeScript | 183 | 123 | 2024-11-19 |

### GF(3) Color Chain Distribution

| Name | Color | Trit | Source Slots |
|------|-------|------|--------------|
| #d3869b | `ERGODIC` | 0 | 3 |
| #b8bb26 | `PLUS` | 1 | 4 |
| #cc241d | `MINUS` | 2 | 4 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

- **Addresses probed:** 28 (alice, bob, A–Z = 28 total)
- **Funded addresses:** 0
- **Total APT on-chain:** 0.0000 APT
- **Status:** All addresses returned `resource_not_found` — no `CoinStore<AptosCoin>` registered at mainnet ledger v5,966,557,264

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | `...` | 2 | YES |
| A-G | `...` | 2 | YES |
| S-T | `...` | 2 | YES |
| V-W | `...` | 2 | YES |
| Y-Z | `...` | 2 | YES |

**All 5 multisig contracts report sigs_required=2 — healthy.**

### MNX Markets (`testnet.mnx.fi`)

Endpoint returns Vercel authentication challenge — market data not accessible without a bypass token. No rows written to `mnx_snapshots`.

---

## DuckDB Ducklake Schema

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments   11 rows  (one per GitHub source, GF3-colored)
├── repo_snapshots    347 rows  (full repo metadata, all sources)
├── aptos_snapshots    28 rows  (hamming swarm wallet probes)
├── multisig_probes     5 rows  (A-B, A-G, Y-Z, S-T, V-W)
└── mnx_snapshots       0 rows  (auth-gated)
```

## GF(3) Legend

| Trit | Name | Hex | Meaning |
|------|------|-----|---------|
| 0 | ERGODIC | `#d3869b` | Neutral / entropic |
| 1 | PLUS | `#b8bb26` | Constructive / additive |
| -1 / 2 | MINUS | `#cc241d` | Destructive / subtractive |
