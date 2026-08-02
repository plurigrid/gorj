# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-02  
**Branch:** world-increment/sweep  
**GF3 Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| wasita | social | 12 |
| AustinCStone | social | 30 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| **Total** | | **383** |

### Top Repos by Stars

| Repo | Stars | Language | Org/User |
|------|-------|----------|----------|
| kubeflow/kubeflow | 15,803 | — | kubeflow |
| kubeflow/pipelines | 4,173 | Python | kubeflow |
| kubeflow/spark-operator | 3,142 | Python | kubeflow |
| kubeflow/trainer | 2,165 | Go | kubeflow |
| kubeflow/katib | 1,694 | Python | kubeflow |
| kubeflow/examples | 1,461 | Jsonnet | kubeflow |
| kubeflow/community-distribution | 1,029 | YAML | kubeflow |
| migalkin/NodePiece | 144 | Python | migalkin |

### TeglonLabs Highlights

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### Recent Activity (Social Graph)

- **M1shaaa/M1shaaa** — pushed 2026-08-02T02:26:27Z (most recent of all sources)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-07-01 (active portfolio)
- **wasita/wasita.github.io** — pushed 2026-07-21 (Svelte, active)

### GF3 Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 127 |
| PLUS | #b8bb26 | +1 | 128 |
| MINUS | #cc241d | -1 | 128 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**API:** `https://fullnode.mainnet.aptoslabs.com/v1`  
**Status:** API reachable. All 28 addresses (alice, bob, A–Z) returned "Resource not found" on `coin::CoinStore<aptos_coin::AptosCoin>` — coin stores not initialized, balance = **0.0 APT** each.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793acd… | 0.0 |
| bob | 0x0a3c00c… | 0.0 |
| A–Z (26 wallets) | various | 0.0 |

> "Resource not found" from `/coin::CoinStore` indicates the APT coin store has not been registered on-chain. Accounts may hold non-APT assets or may be unfunded.

### Multisig Contract Probes

**Endpoint:** `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428… | 2 | ✅ |
| A-G | 0xf56c4a1c… | 2 | ✅ |
| Y-Z | 0xd3ffe181… | 2 | ✅ |
| S-T | 0x3b1c3ae9… | 2 | ✅ |
| V-W | 0x40fad7b4… | 2 | ✅ |

All 5 multisig contracts are **healthy** (2-of-2 signatures required).

### MNX Markets (testnet.mnx.fi)

- `/api/markets` → HTTP 404 Not Found
- Testnet endpoint unavailable at sweep time
- Status: **UNAVAILABLE**

---

## DuckDB Ducklake

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

### Rows Inserted This Run

| Table | New Rows |
|-------|---------|
| world_increments | 383 |
| repo_snapshots | 383 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |

### Schema

```sql
world_increments  -- GF3-tagged event log
repo_snapshots    -- GitHub repo metadata
aptos_snapshots   -- Hamming swarm wallet balances
multisig_probes   -- Multisig health checks
mnx_snapshots     -- MNX market data
```
