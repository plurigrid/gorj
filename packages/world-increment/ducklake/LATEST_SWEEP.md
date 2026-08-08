# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-08T00:00:00Z  
**Branch:** world-increment sweep + hamming snapshot [GF3 color chain]

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| kubeflow | org | 49 | 102,216 |
| bmorphism | user | 100 | 509 |
| plurigrid | org | 100 | 194 |
| migalkin | user (social) | 19 | 821 |
| AustinCStone | user (social) | 41 | 308 |
| zubyul | user | 49 | 40 |
| wasita | user (social) | 14 | 9 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | user (social) | 6 | 3 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |

**Total repos snapshotted: 323**

### Top Repositories by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,805 | 2,691 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,181 | 2,083 | 2026-08-07 |
| kubeflow/spark-operator | Python | 3,145 | 1,512 | 2026-08-06 |
| kubeflow/trainer | Go | 2,175 | 1,017 | 2026-08-08 |
| kubeflow/katib | Python | 1,694 | 535 | 2026-08-06 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 21 | 2021-06-14 |
| migalkin/StarE | Python | 89 | 16 | 2020-09-17 |
| migalkin/kgcourse2021 | HTML | 24 | 8 | 2026-07-10 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 114 |
| 1 | `#b8bb26` | PLUS | 116 |
| -1 | `#cc241d` | MINUS | 116 |

### Notable Recent Activity

- **wasita/wm-cv** (Svelte) — pushed 2026-08-07 (yesterday)
- **wasita/xoxowasita-analysis** (Python) — pushed 2026-08-06
- **kubeflow/pipelines** — pushed 2026-08-07 (active ML pipeline dev)
- **kubeflow/trainer** — pushed 2026-08-08 (today!)
- **TeglonLabs/jank-crane** (C++) — GF3 convergence maps, pushed 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) queried against Aptos mainnet.

**Result:** All wallets return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
This indicates the accounts are not activated/funded on Aptos mainnet — zero APT across the entire swarm.

| Wallet | APT Balance |
|--------|-------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26 wallets) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ Healthy |
| A-G | 0xf56c4a1c... | 2 | ✅ Healthy |
| Y-Z | 0xd3ffe181... | 2 | ✅ Healthy |
| S-T | 0x3b1c3ae9... | 2 | ✅ Healthy |
| V-W | 0x40fad7b4... | 2 | ✅ Healthy |

All multisig contracts are **2-of-N** and responding normally.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is live but serves a Next.js SPA. No public REST/JSON API endpoints found at `/api/markets` or `/api/v1/markets` — all paths return the HTML shell. **Market data unavailable** via direct API probe.

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Description |
|-------|-------------|
| `world_increments` | GF(3)-tagged events for every repo snapshot |
| `repo_snapshots` | Full repo metadata per org/user source |
| `aptos_snapshots` | Hamming swarm wallet balances (APT) |
| `multisig_probes` | Multisig contract signature requirements |
| `mnx_snapshots` | MNX market data (empty — SPA unavailable) |
