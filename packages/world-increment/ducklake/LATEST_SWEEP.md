# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-06  
**GF(3) color chain active:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## Job 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 33 |
| kubeflow | org | 17 |
| TeglonLabs | org | 5 |
| bmorphism | user | 18 |
| zubyul | user | 12 |
| migalkin | social | 5 |
| DJedamski | social | 2 |
| wasita | social | 6 |
| kristinezheng | social | 2 |
| M1shaaa | social | 2 |
| AustinCStone | social | 4 |
| **Total this run** | | **106** |

### Top Repos by Stars (this sweep)
| Repo | Language | ⭐ | Last Push |
|------|----------|----|-----------|
| kubeflow/kubeflow | — | 15,805 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,178 | 2026-08-05 |
| kubeflow/spark-operator | Python | 3,144 | 2026-08-05 |
| kubeflow/trainer | Go | 2,171 | 2026-08-05 |
| kubeflow/katib | Python | 1,694 | 2026-08-05 |
| kubeflow/examples | Jsonnet | 1,461 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-08-04 |
| kubeflow/arena | Go | 816 | 2026-07-29 |
| kubeflow/kale | Python | 699 | 2026-08-05 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| plurigrid/asi | HTML | 59 | 2026-07-10 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |

### Notable Activity (48h window)
- **plurigrid/gorj** pushed 2026-08-06 (today) — 1,662 open issues
- **bmorphism/Gay.jl** pushed 2026-08-06 (today) — 188 open issues
- **kubeflow/sdk** pushed 2026-08-06 (today)
- **wasita/xoxowasita-analysis** pushed 2026-08-05 (new repo, yesterday)
- **wasita/joint-planning-lit** pushed 2026-08-04 (new repo)

### DuckDB State
- `world_increments`: 127 total rows (104 new this run)
- `repo_snapshots`: 1,048 total rows (104 new this run)
- GF(3) distribution: ERGODIC 41 · PLUS 43 · MINUS 43

---

## Job 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
All 28 Hamming-swarm wallets queried at ledger version ~6,633,624,727.

**Result: All wallets return `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`.**  
Balances recorded as 0.0 APT — accounts exist on-chain but have no APT coin store initialized (never received APT). Total swarm APT: **0.00**.

| World | Balance (APT) | World | Balance (APT) |
|-------|---------------|-------|---------------|
| alice | 0.0 | N | 0.0 |
| bob   | 0.0 | O | 0.0 |
| A–M   | 0.0 each | P–Z | 0.0 each |

### Multisig Contract Probes
All 5 probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f...7003 | 2 | ✅ |
| A-G | 0xf56c4...0096 | 2 | ✅ |
| Y-Z | 0xd3ffe...b883 | 2 | ✅ |
| S-T | 0x3b1c3...7883 | 2 | ✅ |
| V-W | 0x40fad...eb6d | 2 | ✅ |

All 5 multisigs healthy — each requires 2/2 signatures.

### MNX Markets (testnet.mnx.fi)
- `/api/markets` → HTTP 404
- Root page → SPA shell, no market data accessible without JS execution
- Status: **unavailable** (no data inserted into `mnx_snapshots`)

---

## DuckDB Path
`packages/world-increment/ducklake/world-increments.duckdb`

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
