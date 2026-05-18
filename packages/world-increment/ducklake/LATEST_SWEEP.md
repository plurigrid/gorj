# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-05-18 13:15:37 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 1 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 30 |

**Total repositories snapshotted:** 371

### GF(3) Color Chain

| id%3 | Trit | Color | Name |
|------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | 1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

### Notable Repos

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| plurigrid/gorj | 0 | Clojure | 2026-05-18 |
| plurigrid/nanoclj-zig | 1 | Zig | 2026-04-25 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |
| plurigrid/ontology | 8 | JavaScript | 2025-05-27 |
| kubeflow/pipelines | 4139 | Python | 2026-05-17 |
| kubeflow/kubeflow | 15646 | — | 2026-05-07 |
| kubeflow/trainer | 2100 | Go | 2026-05-15 |
| kubeflow/katib | 1682 | Python | 2026-05-09 |
| bmorphism/Gay.jl | 1 | Julia | 2026-05-18 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |

### DuckDB Tables Created

- `world_increments` — 394 rows (GF3-stamped event stream)
- `repo_snapshots` — 371 rows (normalized repo metadata)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | `0xc793...cc7b` | 0.00000000 |
| bob | `0x0a3c...512d` | 0.00000000 |
| A | `0x8699...b9d7a` | 0.00000000 |
| B | `0x3f89...cb13` | 0.00000000 |
| C | `0x38b9...535e` | 0.00000000 |
| D | `0xf776...fdd1` | 0.00000000 |
| E | `0xdc1d...8d36` | 0.00000000 |
| F | `0x18a1...3cf71` | 0.00000000 |
| G | `0x69a3...7f32` | 0.00000000 |
| H | `0xce67...300f` | 0.00000000 |
| I | `0x070f...1fc9` | 0.00000000 |
| J | `0x4d96...7f54` | 0.00000000 |
| K | `0xa732...25dc4` | 0.00000000 |
| L | `0x7c2e...eba9` | 0.00000000 |
| M | `0x6fed...7f2e9` | 0.00000000 |
| N | `0xe7dd...51b2c` | 0.00000000 |
| O | `0x7325...a89d` | 0.00000000 |
| P | `0x6218...c948` | 0.00000000 |
| Q | `0xac40...89a9` | 0.00000000 |
| R | `0x7ce6...6e10` | 0.00000000 |
| S | `0xb875...0386` | 0.00000000 |
| T | `0x3578...4588` | 0.00000000 |
| U | `0x7586...f9956` | 0.00000000 |
| V | `0xb59d...af2c3` | 0.00000000 |
| W | `0x5f32...c7b0` | 0.00000000 |
| X | `0xa95c...047d` | 0.00000000 |
| Y | `0xd8e3...444c4` | 0.00000000 |
| Z | `0x7af0...197c` | 0.00000000 |

> **Note:** All addresses returned 0 APT — these are likely unregistered/unfunded accounts on Aptos mainnet. The `CoinStore` resource was not found for any address, indicating these wallets have not been initialized with an APT CoinStore.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4...7003` | 2 | ✓ |
| A-G | `0xf56c...0096` | 2 | ✓ |
| Y-Z | `0xd3ff...b883` | 2 | ✓ |
| S-T | `0x3b1c...7883` | 2 | ✓ |
| V-W | `0x40fa...eb6d` | 2 | ✓ |

All 5 multisig contracts **healthy** — 2-of-N threshold active.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable as JSON API** — testnet.mnx.fi serves a Next.js SPA. No `/api/markets` or `/api/v1/markets` endpoint responded with machine-readable data. The site is live but market data is client-side rendered.

---

## DuckDB Ducklake

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 394 | GF(3) color-chained event stream |
| `repo_snapshots` | 371 | GitHub repo metadata |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig contract health |
| `mnx_snapshots` | 1 | MNX market status (SPA only) |

---

*Sweep completed: {ts}*
