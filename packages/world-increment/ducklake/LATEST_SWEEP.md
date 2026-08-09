# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-09  
**Run:** world-increment-sweep + hamming-swarm-snapshot  
**GF(3) color chain:** id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Snapshot Summary

| Source | Type | Repos Captured | Notable |
|--------|------|----------------|---------|
| plurigrid | org | 100 | gorj (1750 issues!), asi (60★), place, eirobri, nash-portal |
| kubeflow | org | 17 | kubeflow/kubeflow (15808★), pipelines (4180★), spark-operator (3146★), katib (1694★) |
| TeglonLabs | org | 5 | jank-crane (C++, GF3 convergence maps), mathpix-gem (Ruby) |
| bmorphism | user | 9 | ocaml-mcp-sdk (61★), anti-bullshit-mcp-server (23★), Gay.jl (188 issues) |
| zubyul | user | 4 | voice-observatory, gay-world, tilelang-kernels, kinesis-kb360pro |
| migalkin | social | 3 | NodePiece (144★), StarE (89★) — KG research |
| wasita | social | 2 | wm-cv (active 2026-08-07), magic-garden |
| AustinCStone | social | 2 | TextGAN (92★), byteruckus (active 2026-07-15) |
| kristinezheng | social | 1 | GitHub pages |
| M1shaaa | social | 1 | GitHub profile |
| DJedamski | social | 1 | NCAA Kaggle project |
| **TOTAL** | | **145** | |

### Hot Repos (pushed within 48h of sweep)

- `plurigrid/gorj` — pushed 2026-08-09 (this repo, 1750 open issues)
- `plurigrid/place` — pushed 2026-08-09 (TeX, 3★/5 forks)
- `kubeflow/mpi-operator` — pushed 2026-08-09 (Go, 531★)
- `kubeflow/hub` — pushed 2026-08-09 (Go, 181★)
- `kubeflow/pipelines` — pushed 2026-08-09 (Python, 4180★)
- `wasita/wm-cv` — pushed 2026-08-07 (Svelte academic CV)
- `wasita/xoxowasita-analysis` — pushed 2026-08-06

### DuckDB Tables

- `world_increments`: 145 rows — GF(3) colored repo increment chain
- `repo_snapshots`: 145 rows — full metadata per repo

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for `CoinStore<AptosCoin>` — indicating zero or no APT coin store initialized. All recorded as 0.0 APT.

| Status | Count |
|--------|-------|
| resource_not_found (0 APT) | 28 |
| balance > 0 | 0 |

**Ledger version at probe time:** ~6,683,736,676

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ healthy |

All multisigs require 2-of-N signatures and responded successfully. No anomalies.

### MNX Markets (testnet.mnx.fi)

Site is a Next.js SPA. No public REST API path (`/api/markets`, `/api/v1/markets`) returned JSON market data. The frontend loads data client-side via internal routes not reachable without browser execution. Status: **unavailable via curl probe**.

---

## DuckDB Ducklake

**Location:** `packages/world-increment/ducklake/world-increments.duckdb`

```
world_increments  145 rows  (GF3 color chain, one per repo snapshot)
repo_snapshots    145 rows  (org, name, language, stars, forks, issues, pushed_at)
aptos_snapshots    28 rows  (all 0.0 APT — no CoinStore initialized)
multisig_probes     5 rows  (all healthy, 2 sigs required)
mnx_snapshots       0 rows  (SPA, no API data)
```

GF(3) distribution: 49 ERGODIC (#d3869b) | 48 PLUS (#b8bb26) | 48 MINUS (#cc241d)
