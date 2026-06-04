# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-04T14:51 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 19 |
| zubyul | user | 49 |
| migalkin | user | 40 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **Total** | | **330** |

### Top Repositories by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,152 | Go |
| kubeflow/spark-operator | 3,124 | Go |
| kubeflow/trainer | 2,111 | Python |
| AustinCStone/TextGAN | 92 | Python |
| AustinCStone/StereoVisionMRF | 11 | Python |
| AustinCStone/SpectralClustering | 3 | Python |

### Top Languages (across social graph)

| Language | Count |
|----------|-------|
| Python | 241+ |
| Go | 50 |
| Rust | 47 |
| JavaScript | 44 |
| TypeScript | 42 |
| Jupyter Notebook | 39 |
| HTML | 51 |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 117 |
| +1 | PLUS | #b8bb26 | 118 |
| -1 | MINUS | #cc241d | 118 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming-swarm wallets (alice, bob, A-Z) were queried against the Aptos mainnet `CoinStore<AptosCoin>` resource.

**Result:** All wallets returned 0.0 APT — no `CoinStore` resource initialized on-chain for any address.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A-Z | 0x8699...197c | 0.0 each |

Total APT across swarm: **0.0**

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig pairs responded successfully. All require **2 signatures** — healthy 2-of-N configuration.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (authentication required). Both `/api/markets` and `/api/v1/markets` endpoints return an auth gate. No market data could be extracted. Recorded as `MNX_UNAVAILABLE` in `mnx_snapshots` table.

---

## DuckDB Schema Summary

```
world_increments  -- GF(3) tagged sweep events (353 rows)
repo_snapshots    -- GitHub repo metadata (1274 rows incl. duplicates from merge)
aptos_snapshots   -- Hamming wallet balances (28 rows)
multisig_probes   -- Multisig contract health (5 rows)
mnx_snapshots     -- MNX market data (1 row: unavailable marker)
```

---

## Notes

- Aptos: CoinStore absence means accounts are uninitialized on mainnet (expected for test/placeholder addresses).
- MNX: Protected behind Vercel auth; a bypass token or OIDC config is needed for programmatic access.
- GF(3) trit chain: Each world-increment event is colored by `id % 3` -> ERGODIC (0, rose #d3869b), PLUS (+1, yellow-green #b8bb26), MINUS (-1, red #cc241d).
