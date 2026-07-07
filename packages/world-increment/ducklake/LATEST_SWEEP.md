# LATEST_SWEEP — 2026-07-07

## JOB 1: GitHub Social Graph Sweep

**Timestamp:** 2026-07-07 (UTC)  
**Total repos snapshotted this run:** 368  
**GF(3) color chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d (repeating by id%3)

### Sources

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 49 | 102,049 |
| migalkin | user (zubyul social) | 19 | 834 |
| bmorphism | user | 100 | 509 |
| AustinCStone | user (zubyul social) | 40 | 324 |
| plurigrid | org | 100 | 159 |
| zubyul | user | 49 | 40 |
| DJedamski | user (zubyul social) | 6 | 14 |
| TeglonLabs | org | 5 | 12 |
| wasita | user (zubyul social) | 11 | 11 |
| kristinezheng | user (zubyul social) | 5 | 0 |
| M1shaaa | user (zubyul social) | 8 | 0 |

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,769 | — | 2026-07-06 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-07 |
| kubeflow/spark-operator | 3,132 | Python | 2026-07-02 |
| kubeflow/trainer | 2,129 | Go | 2026-07-06 |

### Notable Recent Activity

- **wasita/wasita.github.io** — pushed 2026-07-06 (Svelte personal site, actively updated)
- **M1shaaa/M1shaaa** — pushed 2026-07-07 (profile config repo)
- **kubeflow/pipelines** — pushed 2026-07-07 (active ML infra)
- **TeglonLabs/jank-crane** — pushed 2026-06-08 (crane-jank converged-IR hub, GF3 convergence maps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Timestamp:** 2026-07-07 (UTC)  
**Wallets probed:** 28 (alice, bob, A–Z)  
**Method:** `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 addresses returned 0 APT. The Aptos CoinStore resource is not initialized — wallets may be freshly generated or hold no native APT.

| World | Balance (APT) | Note |
|-------|---------------|------|
| alice | 0.0 | No CoinStore |
| bob | 0.0 | No CoinStore |
| A–Z (26 wallets) | 0.0 each | No CoinStore |

### Multisig Contract Probes

**Method:** `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

All 5 multisig contracts are healthy, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — Vercel deployment protection active (visitor password required). No market data could be extracted.

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments    (GF3 color-tagged event log)
├── repo_snapshots      (GitHub repo metadata)
├── aptos_snapshots     (Hamming swarm wallet balances)
├── multisig_probes     (Aptos multisig contract health)
└── mnx_snapshots       (MNX market data — empty, auth-gated)
```

## GF(3) Color Chain Legend

| id % 3 | Trit | Color | Name |
|--------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | 1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |
