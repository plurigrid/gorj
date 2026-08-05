# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-05  
**Timestamp:** 2026-08-05T23:17 UTC  
**GF(3) color chain:** PLUS #b8bb26 → MINUS #cc241d → ERGODIC #d3869b

---

## JOB 1: GitHub Social Graph Sweep

### Sources swept
| Source | Type | Repos captured |
|--------|------|---------------|
| plurigrid | org | 13 |
| kubeflow | org | 10 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 6 |
| migalkin | user (social) | 3 |
| wasita | user (social) | 3 |
| AustinCStone | user (social) | 2 |
| kristinezheng | user (social) | 1 |
| M1shaaa | user (social) | 1 |

**54 new world_increment rows** added to DuckDB this run (998 repo_snapshots cumulative across all runs).

### Notable activity (pushed today or recently)
- **kubeflow/trainer** (Go, ⭐2171) — pushed 2026-08-05; Distributed AI Model Training
- **kubeflow/pipelines** (Python, ⭐4178) — pushed 2026-08-05; ML Pipelines
- **kubeflow/sdk** (Python, ⭐133) — pushed 2026-08-05; Universal Python SDK
- **kubeflow/spark-operator** (Python, ⭐3144) — pushed 2026-08-05
- **kubeflow/mcp-apache-spark-history-server** (Python, ⭐186) — new MCP server for Spark debug
- **plurigrid/gorj** (Clojure, ⭐1) — pushed 2026-08-05 (this repo, active today)
- **plurigrid/eirobri** (Clojure) — pushed 2026-08-04; EiRoBri replay world (31 open issues)
- **wasita/xoxowasita-analysis** (Python) — pushed 2026-08-05, brand new repo

### GF(3) distribution (this run)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 18 |
| 1 | PLUS | #b8bb26 | 18 |
| -1 | MINUS | #cc241d | 18 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
Queried 28 addresses (alice, bob, A–Z) via Aptos mainnet fullnode.  
**All 28 wallets returned 0.0 APT** — accounts may be uninitialized or have zero CoinStore balance on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A–Z | 0x8699... – 0x7af0... | 0.0 each |

### Multisig Contract Probes
All 5 multisig contracts responded healthy with `sigs_required = 2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
`https://testnet.mnx.fi/api/markets` — **unavailable** (SPA returns Next.js HTML, no accessible REST API endpoint). MNX testnet is a client-side rendered app; no market data extractable via HTTP without browser execution.

---

## DuckDB Ducklake Schema
Location: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (cumulative) |
|-------|------------------|
| world_increments | 77 |
| repo_snapshots | 998 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, unavailable) |
