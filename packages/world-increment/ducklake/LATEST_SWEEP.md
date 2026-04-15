# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-04-15T06:00:00Z  
**Branch:** world-increment/sweep-2026-04-15  
**Agent:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Stars (distinct) |
|--------|------|-------|-----------------|
| plurigrid | org | 101 | 29 |
| bmorphism | user | 100 | 94 |
| TeglonLabs | org | 53 | 3 |
| kubeflow | org | 47 | 82 485 |
| AustinCStone | user | 43 | 107 |
| wasita | user | 31 | 1 |
| migalkin | user | 30 | 277 |
| zubyul | user | 24 | 3 |
| kristinezheng | user | 18 | 0 |
| M1shaaa | user | 16 | 0 |
| DJedamski | user | 11 | 3 |

**Total distinct repos snapshotted:** 474  
**Social-graph users swept:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Recent Events

**bmorphism** (20 events sampled):
- `PushEvent` → `plurigrid/nash-portal` (2026-04-15T05:39:52)
- `PullRequestEvent` → `plurigrid/nash-portal` (2026-04-14T00:07:46)
- `PushEvent` → `plurigrid/asi`, `plurigrid/horse`, `plurigrid/web-browser`

**zubyul** (16 events sampled):
- Heavy `PullRequestEvent` / `CreateEvent` activity on `plurigrid/gorj` (2026-04-14 – 2026-04-15)
- `PushEvent` → `plurigrid/gorj` (2026-04-14T18:07:37)

### World Increments (GF(3) Color Chain)

| GF(3) Name | Color | Trit | Count |
|------------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 13 |
| PLUS | #b8bb26 | +1 | 14 |
| MINUS | #cc241d | -1 | 14 |

**Total increments recorded:** 41 (18 from events, 23 from swarm activity)  
**Time range:** 2026-04-10 → 2026-04-15

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15 575 | — |
| kubeflow/pipelines | 4 119 | Python |
| kubeflow/spark-operator | 3 115 | Python |
| kubeflow/trainer | 2 084 | Go |
| kubeflow/katib | 1 678 | Python |
| kubeflow/manifests | 1 010 | YAML |
| kubeflow/arena | 809 | Go |
| kubeflow/kale | 683 | Python |
| migalkin/* | 277 | — |
| bmorphism/* | 94 | — |
| AustinCStone/* | 43 | — |
| plurigrid/asi | 16 | HTML |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (APT)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. The legacy
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource returned
`resource_not_found` for all addresses. Accounts are live (verified via
`/v1/accounts/{addr}` → 200 OK with sequence numbers) but are using the
Fungible Asset (FA) model rather than the legacy Coin store, or hold zero APT.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac… | 0.00000000 |
| bob   | 0x0a3c00… | 0.00000000 |
| A | 0x8699ed… | 0.00000000 |
| B | 0x3f892e… | 0.00000000 |
| C | 0x38b99e… | 0.00000000 |
| D | 0xf77656… | 0.00000000 |
| E | 0xdc1d9d… | 0.00000000 |
| F | 0x18a14b… | 0.00000000 |
| G | 0x69a394… | 0.00000000 |
| H | 0xce67c3… | 0.00000000 |
| I | 0x070fe5… | 0.00000000 |
| J | 0x4d964d… | 0.00000000 |
| K | 0xa73204… | 0.00000000 |
| L | 0x7c2eae… | 0.00000000 |
| M | 0x6fed37… | 0.00000000 |
| N | 0xe7dde6… | 0.00000000 |
| O | 0x73252b… | 0.00000000 |
| P | 0x621879… | 0.00000000 |
| Q | 0xac40fa… | 0.00000000 |
| R | 0x7ce605… | 0.00000000 |
| S | 0xb87530… | 0.00000000 |
| T | 0x357081… | 0.00000000 |
| U | 0x758600… | 0.00000000 |
| V | 0xb59dd8… | 0.00000000 |
| W | 0x5f32ae… | 0.00000000 |
| X | 0xa95cbb… | 0.00000000 |
| Y | 0xd8e328… | 0.00000000 |
| Z | 0x7af0ef… | 0.00000000 |

**Total APT across swarm:** 0.00000000 (FA model; legacy CoinStore not initialized)

### Multisig Contract Probes

All 5 multisig contracts responded healthy with `num_signatures_required = 2`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable via REST API**  
testnet.mnx.fi is a Next.js SPA. All probed paths (`/`, `/api/markets`,
`/api/v1/markets`) return the HTML shell with no machine-readable market data.
No tickers recorded.

---

## DuckDB Ducklake

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 41 |
| repo_snapshots | 1 417 (474 distinct full_name) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |

GF(3) sequence: `id%3==0 → ERGODIC #d3869b` | `id%3==1 → PLUS #b8bb26` | `id%3==2 → MINUS #cc241d`
