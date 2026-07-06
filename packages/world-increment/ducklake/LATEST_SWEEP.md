# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-06  
**Run type:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| wasita | user | 11 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |

**Total repos snapshotted:** 392

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,767 | — | 2026-07-06 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-06 |
| kubeflow/spark-operator | 3,132 | Python | 2026-07-02 |
| kubeflow/trainer | 2,129 | Go | 2026-07-06 |

### GF(3) Color Chain Applied

- `id % 3 == 0` → trit=0, color=`#d3869b` (ERGODIC)
- `id % 3 == 1` → trit=1, color=`#b8bb26` (PLUS)
- `id % 3 == 2` → trit=-1, color=`#cc241d` (MINUS)

### DuckDB Tables Written

- `world_increments`: 415 rows
- `repo_snapshots`: 392 rows

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets in the Hamming swarm (alice, bob, A–Z) queried against Aptos mainnet.

**Result:** All 28 addresses returned 0.0 APT — accounts do not exist on-chain or hold no AptosCoin balance.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**Status:** All 5 multisigs healthy, requiring 2-of-N signatures.

### MNX Markets

`https://testnet.mnx.fi` is behind **Vercel authentication** — the API is not publicly accessible without a bypass token. Market data unavailable; `mnx_snapshots` table is empty this run.

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

```sql
world_increments  -- GF3-colored increment events (392 repo push events)
repo_snapshots    -- Full repo metadata per source  
aptos_snapshots   -- Hamming swarm wallet balances (28 wallets, all 0.0 APT)
multisig_probes   -- 5 multisig contract health checks (all healthy, 2-sig)
mnx_snapshots     -- MNX market data (empty — Vercel auth required)
```
