# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-27 UTC
**Branch:** world-increment/sweep-2026-06-27
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
**DuckDB version:** v1.5.4 (Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Repos Snapshotted | Max Stars |
|--------|------|-------------------|-----------|
| plurigrid | org | 30 | 26 (asi) |
| kubeflow | org | 20 | 15,746 (kubeflow/kubeflow) |
| bmorphism | user | 18 | 61 (ocaml-mcp-sdk) |
| zubyul | user | 15 | 1 |
| wasita | social-graph | 11 | 2 |
| migalkin | social-graph | 9 | 144 (NodePiece) |
| M1shaaa | social-graph | 8 | 0 |
| DJedamski | social-graph | 6 | 1 |
| AustinCStone | social-graph | 6 | 92 (TextGAN) |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | social-graph | 5 | 0 |
| **TOTAL** | | **133** | |

### GF(3) Color Chain Distribution

| GF3 Trit | Color | Name | Count |
|----------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 44 |
| +1 | #b8bb26 | PLUS | 45 |
| -1 | #cc241d | MINUS | 44 |

**GF(3) Rule:** id%3==0 -> ERGODIC, id%3==1 -> PLUS, id%3==2 -> MINUS

### Notable Repos

**plurigrid/asi** (star:26) - "everything is topological chemputer!" - pushed 2026-06-26
**plurigrid/gorj** (846 open issues) - forj + Rama topology nREPL routing + GF(3) trit coloring - pushed 2026-06-26
**kubeflow/kubeflow** (star:15746) - Machine Learning Toolkit for Kubernetes - pushed 2026-06-18
**kubeflow/spark-operator** (star:3128) - Kubernetes operator for Apache Spark - pushed 2026-06-26
**kubeflow/pipelines** (star:4156) - Machine Learning Pipelines - pushed 2026-06-26
**kubeflow/mcp-server** (star:17) - MCP Server for AI-Assisted Kubeflow Development - pushed 2026-06-24
**bmorphism/ocaml-mcp-sdk** (star:61) - OCaml SDK for MCP using Jane Street oxcaml_effect - pushed 2026-03-16
**bmorphism/Gay.jl** (star:2, 187 issues) - Wide-gamut color sampling with splittable determinism - pushed 2026-06-26
**bmorphism/anti-bullshit-mcp-server** (star:23) - claims analysis and manipulation detection - pushed 2026-01-16
**migalkin/NodePiece** (star:144) - ICLR22 knowledge graph embeddings - pushed 2026-05-07
**AustinCStone/TextGAN** (star:92) - Text GAN in TensorFlow - pushed 2025-03-03
**TeglonLabs/jank-crane** (C++) - crane-jank converged-IR hub, GF3 convergence maps - pushed 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, Ledger v5952372392)

All 28 addresses (alice, bob, A-Z) queried against fullnode.mainnet.aptoslabs.com.

**Result:** All 28 addresses returned resource_not_found for 0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>.
All hamming swarm wallet addresses have **zero APT balance** at this ledger version.

**Total Swarm Balance: 0.0 APT across all 28 addresses**

### Multisig Contract Probes (5 pairs)

Probed via POST /v1/view -> 0x1::multisig_account::num_signatures_required

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | YES |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | YES |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | YES |

**All 5 multisig contracts healthy - 2-of-N signatures required for all pairs.**

### MNX Markets (testnet.mnx.fi)

testnet.mnx.fi returned HTTP 401 - Vercel deployment protection active.
**Status: UNAVAILABLE** - no market data accessible without bypass token.

---

## DuckDB Schema Summary

| Table | Rows | Purpose |
|-------|------|---------|
| world_increments | 133 | GF(3) trit-colored event log |
| repo_snapshots | 133 | GitHub repo metadata snapshots |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Multisig contract health checks |
| mnx_snapshots | 0 | MNX market data (unavailable) |

---

## Key Signals

1. plurigrid/gorj has 846 open issues - highest in plurigrid org, active triage
2. bmorphism/Gay.jl has 187 open issues - most active development in bmorphism repos
3. kubeflow org most active with 9+ repos pushed in last week
4. All 28 hamming swarm wallets unfunded - no APT at mainnet ledger v5952372392
5. 5/5 multisig contracts healthy - all report 2 sigs required (2-of-N topology)
6. TeglonLabs/jank-crane (C++, GF3 convergence maps) most recently pushed TeglonLabs repo (2026-06-08)
7. kubeflow/mcp-server active (pushed 2026-06-24) - Kubeflow entering MCP ecosystem
8. MNX testnet inaccessible - Vercel auth gate requires owner-provided bypass token
