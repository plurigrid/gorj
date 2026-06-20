# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-20  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
- **Orgs:** plurigrid (30 repos), kubeflow (46 repos), TeglonLabs (5 repos)
- **Users:** bmorphism (10 repos), zubyul (21 repos)
- **Zubyul social graph:** migalkin (7), DJedamski (5), wasita (7), kristinezheng (4), M1shaaa (4), AustinCStone (9)

**Total repo snapshots:** 148

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 49 |
| 1 | #b8bb26 | PLUS | 50 |
| -1 | #cc241d | MINUS | 49 |

### Stars by Source
| Source | Repos | Total Stars |
|--------|-------|-------------|
| kubeflow | 46 | 34,230 |
| migalkin | 7 | 280 |
| AustinCStone | 9 | 107 |
| plurigrid | 30 | 75 |
| zubyul | 21 | 9 |
| bmorphism | 10 | 7 |
| wasita | 7 | 5 |
| DJedamski | 5 | 3 |
| TeglonLabs | 5 | 2 |
| M1shaaa | 4 | 0 |
| kristinezheng | 4 | 0 |

### Most Active Repos (recently pushed)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| bmorphism/satreadout | HTML | 0 | 2026-06-20 |
| bmorphism/Gay.jl | Julia | 2 | 2026-06-20 |
| kubeflow/hub | Go | 173 | 2026-06-20 |
| kubeflow/dashboard | TypeScript | 16 | 2026-06-20 |
| kubeflow/pipelines | Python | 4155 | 2026-06-20 |
| plurigrid/gorj | Clojure | 0 | 2026-06-20 (698 open issues!) |
| plurigrid/place | TeX | 1 | 2026-06-20 |

### Notable Findings
- **plurigrid/gorj** 698 open issues — highest backlog in plurigrid graph
- **bmorphism/Gay.jl** 187 open issues, active today; Wide-gamut Julia color-sampling
- **kubeflow/kubeflow** flagship at 15,737 stars
- **kubeflow/mcp-apache-spark-history-server** (177 stars) — new MCP tool for Spark agents
- **migalkin/NodePiece** (144 stars) top-starred in social graph
- **TeglonLabs/jank-crane** freshest TeglonLabs repo (2026-06-08), GF3 IR hub in C++

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A-Z)
**Status: UNREACHABLE** — `fullnode.mainnet.aptoslabs.com` not accessible from this remote container (outbound blocked). All 28 addresses stored as NULL in `aptos_snapshots`.

### Multisig Contract Probes
All 5 probed contracts responded healthy — all require 2 signatures.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: VERCEL AUTH REQUIRED** — deployment protected, no market data captured. `mnx_snapshots` table empty.

---

## DuckDB Tables
```
world_increments  148 rows  GF(3) color-chained event log
repo_snapshots    148 rows  GitHub repo metadata
aptos_snapshots    28 rows  Hamming swarm balances (all NULL)
multisig_probes     5 rows  Aptos multisig health (all healthy)
mnx_snapshots       0 rows  MNX market data (auth blocked)
```

## Action Items
1. Aptos API blocked in container — needs endpoint allowlist or proxy
2. MNX Vercel bypass token needed for market data capture
3. plurigrid/gorj 698 issues spike warrants triage
4. bmorphism/Gay.jl 187 issues active development churn
