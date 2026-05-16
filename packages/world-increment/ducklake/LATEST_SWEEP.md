# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-05-16  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

| id%3 | trit | color name | hex |
|------|------|-----------|-----|
| 0 | 0 | ERGODIC | #d3869b |
| 1 | +1 | PLUS | #b8bb26 |
| 2 | -1 | MINUS | #cc241d |

### Sources Swept

| Source | Type | Repos | GF(3) |
|--------|------|-------|-------|
| AustinCStone | user | 40 | ERGODIC #d3869b |
| DJedamski | user | 6 | PLUS #b8bb26 |
| kristinezheng | user | 6 | MINUS #cc241d |
| kubeflow | org | 48 | ERGODIC #d3869b |
| M1shaaa | user | 8 | PLUS #b8bb26 |
| migalkin | user | 19 | MINUS #cc241d |
| plurigrid | org | 100 | ERGODIC #d3869b |
| bmorphism | user | 100 | PLUS #b8bb26 |
| TeglonLabs | org | 4 | MINUS #cc241d |
| wasita | user | 11 | ERGODIC #d3869b |
| zubyul | user | 49 | PLUS #b8bb26 |

**Total repos snapshotted: 391**

### Notable Repos (recently active)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kristinezheng/kristinezheng.github.io | 0 | HTML | 2026-05-14 |
| M1shaaa/M1shaaa | 0 | — | 2026-05-16 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |
| wasita/wasita.github.io | 1 | Svelte | 2026-05-14 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 addresses in the A-Z + alice + bob Hamming swarm returned
`resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These wallets hold **0.0000 APT** each. Account S (0xb8753...) has
sequence_number=11 confirming on-chain activity with non-APT resources.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793acdec12b4a63... | 0.0000 |
| bob | 0x0a3c00c58fdf9020... | 0.0000 |
| A-Z | (26 addresses) | 0.0000 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | YES |
| A-G | 0xf56c4a1c09062...   | 2 | YES |
| Y-Z | 0xd3ffe1812b2df4...  | 2 | YES |
| S-T | 0x3b1c3ae905d44c...  | 2 | YES |
| V-W | 0x40fad7b423a843...  | 2 | YES |

All pairs require 2-of-2 signatures and are responding on mainnet.

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — all API paths return the SPA HTML shell.
The testnet frontend is a client-side React app with no accessible
machine-readable API endpoints.

---

## DuckDB Schema Summary

```
world_increments   — GF(3) tagged sweep events     (11 rows)
repo_snapshots     — repo metadata                 (391 rows)
aptos_snapshots    — Hamming swarm wallet balances (28 rows)
multisig_probes    — multisig health checks         (5 rows)
mnx_snapshots      — market data (N/A)              (1 row)
```
