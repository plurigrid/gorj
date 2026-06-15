# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-06-15  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) → PLUS #b8bb26 (trit=1) → MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 100 | 77 |
| kubeflow | org | 48 | 34,213 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| migalkin | user (social) | 19 | 280 |
| DJedamski | user (social) | 6 | 3 |
| wasita | user (social) | 11 | 5 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |
| AustinCStone | user (social) | 40 | 108 |
| **TOTAL** | | **391** | **34,949** |

### GF(3) World-Increment Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 130 |
| 1 | #b8bb26 | PLUS | 131 |
| -1 | #cc241d | MINUS | 130 |

### Most Recently Active Repos (2026-06-15)
| Repo | Pushed At |
|------|-----------|
| kubeflow/website | 2026-06-15T11:38:22Z |
| plurigrid/gorj | 2026-06-15T11:15:02Z |
| kubeflow/community-distribution | 2026-06-15T09:56:57Z |
| kubeflow/pipelines | 2026-06-15T07:37:49Z |
| M1shaaa/M1shaaa | 2026-06-15T03:55:00Z |
| bmorphism/Gay.jl | 2026-06-15T00:44:40Z |

### Top Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,725 | — | 2026-06-11 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-15 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-14 |
| kubeflow/trainer | 2,115 | Go | 2026-06-13 |
| kubeflow/katib | 1,683 | Python | 2026-06-12 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 (newest TeglonLabs) |

### Notable Observations
- **plurigrid/gorj** pushed today at 11:15 UTC — this sweep is live
- **TeglonLabs/jank-crane** (C++, GF3 convergence maps) pushed 2026-06-08
- **bmorphism/Gay.jl** pushed today 2026-06-15
- **kubeflow** dominates by star count (34,213 of 34,949 total stars in graph)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**Queried:** 2026-06-15 via fullnode.mainnet.aptoslabs.com  
**Wallets probed:** 28 (alice, bob, A-Z)  
**Total APT across all wallets:** 0.0 APT

All 28 addresses returned zero APT balance via the CoinStore resource. Unfunded or pre-funded test addresses not yet receiving mainnet APT.

| Wallet | Address | Balance APT |
|--------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A-Z | (see DB) | 0.0 each |

### Multisig Contract Probes
**All 5 multisig contracts healthy — 2-of-2 signatures required.**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel deployment protection active. No bypass token available. No market data extracted.

---

## DuckDB Schema Summary

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 391 | GF(3)-colored increment chain, one per repo event |
| repo_snapshots | 391 | Full repo metadata (stars, forks, language, pushed_at) |
| aptos_snapshots | 28 | Hamming swarm wallet balances (all 0 APT) |
| multisig_probes | 5 | Multisig contract sigs_required probes (all 2-of-2) |
| mnx_snapshots | 0 | MNX markets unavailable this sweep |
