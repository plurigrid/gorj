# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-16  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted | GF(3) | Color |
|--------|------|-------------------|-------|-------|
| plurigrid | org | 100 | PLUS (1) | `#b8bb26` |
| kubeflow | org | 48 | MINUS (-1) | `#cc241d` |
| TeglonLabs | org | 4 | ERGODIC (0) | `#d3869b` |
| bmorphism | user | 100 | PLUS (1) | `#b8bb26` |
| zubyul | user | 49 | MINUS (-1) | `#cc241d` |
| migalkin | user (social) | 7 | ERGODIC (0) | `#d3869b` |
| DJedamski | user (social) | 6 | PLUS (1) | `#b8bb26` |
| wasita | user (social) | 6 | MINUS (-1) | `#cc241d` |
| kristinezheng | user (social) | 6 | ERGODIC (0) | `#d3869b` |
| M1shaaa | user (social) | 6 | PLUS (1) | `#b8bb26` |
| AustinCStone | user (social) | 7 | MINUS (-1) | `#cc241d` |

**Total repo snapshots:** 339

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,632 | — | 2026-05-07 |
| kubeflow/pipelines | 4,140 | Python | 2026-05-15 |
| kubeflow/spark-operator | 3,125 | Python | 2026-05-15 |
| kubeflow/trainer | 2,098 | Go | 2026-05-15 |
| kubeflow/katib | 1,682 | Python | 2026-05-09 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### TeglonLabs Repos

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| mathpix-gem | Ruby | 2 | LaTeX/SMILES/markdown OCR gem |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | — |
| coin-flip-mcp | JavaScript | 0 | Coin flip MCP with random.org |

### World Increments (GF(3) chain)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1 | plurigrid | 1 | `#b8bb26` | PLUS |
| 2 | kubeflow | -1 | `#cc241d` | MINUS |
| 3 | TeglonLabs | 0 | `#d3869b` | ERGODIC |
| 4 | bmorphism | 1 | `#b8bb26` | PLUS |
| 5 | zubyul | -1 | `#cc241d` | MINUS |
| 6 | migalkin | 0 | `#d3869b` | ERGODIC |
| 7 | DJedamski | 1 | `#b8bb26` | PLUS |
| 8 | wasita | -1 | `#cc241d` | MINUS |
| 9 | kristinezheng | 0 | `#d3869b` | ERGODIC |
| 10 | M1shaaa | 1 | `#b8bb26` | PLUS |
| 11 | AustinCStone | -1 | `#cc241d` | MINUS |
| 12 | aptos_hamming | 0 | `#d3869b` | ERGODIC |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned 0 APT — addresses exist on the Hamming-alphabet swarm but hold no APT coin store on mainnet at time of snapshot.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (see aptos_snapshots table) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded healthy with **2-of-N signatures required**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

The MNX testnet is a **Next.js SPA** — all paths (`/`, `/api/markets`, `/api/v1/markets`, `/markets`) return the HTML shell with no JSON API data. Market data unavailable at time of sweep; `mnx_snapshots` table is empty.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| `world_increments` | 12 |
| `repo_snapshots` | 339 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (SPA, no API) |

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent on 2026-05-16.*
