# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-08T14:30:00Z  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars | GF(3) Trit | Color |
|--------|------|-------|-------------|------------|-------|
| AustinCStone | user | 5 | 106 | 1 PLUS | #b8bb26 |
| DJedamski | user | 4 | 3 | 2 MINUS | #cc241d |
| M1shaaa | user | 3 | 0 | 0 ERGODIC | #d3869b |
| TeglonLabs | org | 4 | 2 | 1 PLUS | #b8bb26 |
| bmorphism | user | 100 | 247 | 2 MINUS | #cc241d |
| kristinezheng | user | 3 | 0 | 0 ERGODIC | #d3869b |
| kubeflow | org | 30 | 32809 | 1 PLUS | #b8bb26 |
| migalkin | user | 6 | 278 | 2 MINUS | #cc241d |
| plurigrid | org | 100 | 70 | 0 ERGODIC | #d3869b |
| wasita | user | 5 | 3 | 1 PLUS | #b8bb26 |
| zubyul | user | 49 | 14 | 2 MINUS | #cc241d |

**Total:** 309 repos across 11 sources

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15626 | 2026-05-07 |
| kubeflow/pipelines | Python | 4136 | 2026-05-08 |
| kubeflow/spark-operator | Python | 3124 | 2026-05-05 |
| kubeflow/trainer | Go | 2096 | 2026-05-08 |
| kubeflow/katib | Python | 1683 | 2026-05-08 |
| kubeflow/manifests | YAML | 1015 | 2026-05-08 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| plurigrid/gorj | Clojure | 0 | 2026-05-08 |

### Notable Observations
- **kubeflow** dominates by stars (32809 total); `kubeflow/manifests` pushed today
- **plurigrid/gorj** (this repo) pushed today with 111 open issues
- **bmorphism** has 100 repos with diverse language spread
- **zubyul** 49 repos, recently active
- **wasita** `vocoder` and `magic-garden` pushed within 2 days
- **zubyul social graph** (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) all snapshotted

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`.  
**Result:** All accounts returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — no APT CoinStore registered on any address. Balance = **0.0 APT** for all.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...cc7b | 0.0 | resource_not_found |
| bob | 0x0a3c...512d | 0.0 | resource_not_found |
| A–Z (26 addrs) | 0x8699...–0x7af0... | 0.0 each | resource_not_found |

Ledger version at query time: **5185879132**

### Multisig Contract Probes (Aptos Mainnet)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisigs healthy, all require **2-of-N** signatures.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a **Next.js SPA** — all API paths (`/api/markets`, `/api/v1/markets`) return the HTML shell. No public REST endpoint exposed. Market data **unavailable** via HTTP scrape.

---

## DuckDB Schema Summary

```
world_increments  — 11 rows  (one per source, GF3-colored)
repo_snapshots    — 309 rows (full GitHub snapshot)
aptos_snapshots   — 28 rows  (alice, bob, A–Z)
multisig_probes   — 5 rows   (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     — 1 row    (SPA_NO_API)
```

## GF(3) Color Chain

- **trit=0 ERGODIC** `#d3869b` — M1shaaa, kristinezheng, plurigrid
- **trit=1 PLUS** `#b8bb26` — AustinCStone, TeglonLabs, kubeflow, wasita
- **trit=2 MINUS** `#cc241d` — DJedamski, bmorphism, migalkin, zubyul
