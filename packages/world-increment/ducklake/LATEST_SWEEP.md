# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-01T21:16Z  
**Branch:** world-increment/sweep-2026-06-01  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 25 (of 101 total) |
| kubeflow | org | 15 (of 48 total) |
| TeglonLabs | org | 4 |
| bmorphism | user | 12 |
| zubyul | user | 10 |
| migalkin | social | 5 |
| DJedamski | social | 2 |
| wasita | social | 3 |
| kristinezheng | social | 2 |
| M1shaaa | social | 1 |
| AustinCStone | social | 3 |
| **Total** | | **82 new increments** |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,700 | — | 2026-05-24 |
| kubeflow/pipelines | 4,151 | Python | 2026-06-01 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-01 |
| kubeflow/trainer | 2,109 | Go | 2026-05-30 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 24 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### Most Active (open issues)

| Repo | Open Issues |
|------|-------------|
| kubeflow/pipelines | 485 |
| plurigrid/gorj | 293 |
| bmorphism/Gay.jl | 189 |
| kubeflow/notebooks | 193 |
| kubeflow/trainer | 130 |
| kubeflow/katib | 123 |

### GF(3) Distribution (today's 82 new increments)

- **ERGODIC** (trit=0, #d3869b): 28 increments
- **PLUS** (trit=1, #b8bb26): 27 increments
- **MINUS** (trit=-1, #cc241d): 27 increments

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → …` (82 steps, 27⅓ full cycles)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `0x1::coin::balance` view function at ledger ~5.52B.  
Note: APT migrated to FungibleAsset; `CoinStore` resource returns 404 — using view function instead.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| bob   | 0x0a3c… | 12.657007 |
| F     | 0x18a1… | 1.960516 |
| L     | 0x7c2e… | 1.927269 |
| J     | 0x4d96… | 1.895093 |
| alice | 0xc793… | 0.436434 |
| O     | 0x7325… | 0.210136 |
| K     | 0xa732… | 0.161961 |
| P     | 0x6218… | 0.140136 |
| M     | 0x6fed… | 0.112285 |
| N     | 0xe7dd… | 0.106121 |
| Q     | 0xac40… | 0.103240 |
| S     | 0xb875… | 0.091788 |
| R     | 0x7ce6… | 0.090217 |
| T     | 0x3578… | 0.073713 |
| U     | 0x7586… | 0.055773 |
| A     | 0x8699… | 0.051767 |
| V     | 0xb59d… | 0.048833 |
| Y     | 0xd8e3… | 0.044449 |
| X     | 0xa95c… | 0.042577 |
| W     | 0x5f32… | 0.040705 |
| B     | 0x3f89… | 0.036256 |
| Z     | 0x7af0… | 0.024268 |
| D     | 0xf776… | 0.011629 |
| C     | 0x38b9… | 0.010185 |
| E     | 0xdc1d… | 0.009372 |
| H     | 0xce67… | 0.001681 |
| G     | 0x69a3… | 0.000681 |
| I     | 0x070f… | 0.000681 |

**Total swarm APT:** ~21.58 APT across 28 addresses

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B  | 0x0da4… | 2 | ✅ |
| A-G  | 0xf56c… | 2 | ✅ |
| Y-Z  | 0xd3ff… | 2 | ✅ |
| S-T  | 0x3b1c… | 2 | ✅ |
| V-W  | 0x40fa… | 2 | ✅ |

All multisig contracts healthy — 2-of-N threshold confirmed on all 5 pairs.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — Next.js SPA with no public JSON API. `/api/markets`, `/api/v1/markets`, `/api/tickers` all return the HTML shell. No market data extractable without client-side JS execution.

---

## DuckDB Ducklake State

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Total Rows | New Today |
|-------|-----------|-----------|
| world_increments | 105 | 82 |
| repo_snapshots | ~1,026 | 82 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 0 | 0 |

Prior sweep (2026-04-10, 23 increments) preserved — append-only log.

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
