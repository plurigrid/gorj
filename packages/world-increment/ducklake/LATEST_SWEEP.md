# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-20  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 30 |
| kubeflow | org | 30 |
| TeglonLabs | org | 5 |
| bmorphism | user | 30 |
| zubyul | user | 30 |
| migalkin | social graph | 5 |
| DJedamski | social graph | 4 |
| wasita | social graph | 4 |
| kristinezheng | social graph | 3 |
| M1shaaa | social graph | 3 |
| AustinCStone | social graph | 4 |
| **Total** | | **148** |

### Most Recently Pushed (top 10)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kale | Python | 694 | 2026-06-20T11:20:36Z |
| plurigrid/gorj | Clojure | 0 | 2026-06-20T11:12:18Z |
| kubeflow/dashboard | TypeScript | 16 | 2026-06-20T10:18:56Z |
| kubeflow/pipelines | Python | 4155 | 2026-06-20T07:29:44Z |
| kubeflow/pipelines-components | Python | 11 | 2026-06-20T03:06:51Z |
| kubeflow/sdk | Python | 120 | 2026-06-20T03:05:26Z |
| bmorphism/satreadout | HTML | 0 | 2026-06-20T01:12:01Z |
| bmorphism/Gay.jl | Julia | 1 | 2026-06-20T00:40:04Z |
| plurigrid/place | TeX | 1 | 2026-06-20T00:28:26Z |
| bmorphism/bci-preview | HTML | 0 | 2026-06-20T00:20:44Z |

### Notable Repos (by stars)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/pipelines | 4155 | Python | Machine Learning Pipelines for Kubeflow |
| migalkin/NodePiece | 144 | Python | Compositional Knowledge Graph Representations (ICLR'22) |
| migalkin/StarE | 89 | Python | EMNLP 2020: Hyper-Relational Knowledge Graphs |
| AustinCStone/TextGAN | 92 | Python | Generative adversarial network for text generation |
| kubeflow/kale | 694 | Python | Kubeflow automation toolkit |

### TeglonLabs Highlight
- **jank-crane** (C++, 2026-06-08): crane-jank converged-IR hub with GF3 convergence maps  
- **mathpix-gem** (Ruby, 2 stars): LaTeX OCR + SMILES structure extraction  
- **coin-flip-mcp** (JS, 2 forks): MCP server for randomness via random.org

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 wallets probed via `/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 addresses returned `resource_not_found` — CoinStore not initialized on mainnet for these accounts. Balance recorded as NULL (no APT deposited yet).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...12d5 | NULL |
| A–Z (26) | 0x86…–0x7af0… | NULL |

> Note: `resource_not_found` means the account exists but the CoinStore resource has not been initialized. Accounts may have been created but never funded.

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold configured.**

### MNX Markets

`testnet.mnx.fi` returned **HTTP 401 — Vercel authentication required**. Market data unavailable without a visitor password or bypass token. `mnx_snapshots` table inserted zero rows.

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 171 (148 new) |
| repo_snapshots | 1092 (148 new) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

**DB:** `packages/world-increment/ducklake/world-increments.duckdb`
