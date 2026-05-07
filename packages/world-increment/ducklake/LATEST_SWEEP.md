# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-07T19:15:32Z
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
**Total world-increments:** 390

---

## JOB 1: GitHub Social Graph Sweep

Sources swept: plurigrid (org), kubeflow (org), TeglonLabs (org), bmorphism (user), zubyul (user),
plus zubyul social graph: migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone.

### Org/User Summary

| Source | Repos | Total Stars |
|--------|-------|-------------|
| kubeflow | 47 | 34014 |
| migalkin | 19 | 279 |
| bmorphism | 100 | 247 |
| AustinCStone | 40 | 108 |
| plurigrid | 100 | 70 |
| zubyul | 49 | 14 |
| wasita | 11 | 4 |
| DJedamski | 6 | 3 |
| TeglonLabs | 4 | 2 |
| kristinezheng | 6 | 0 |
| M1shaaa | 8 | 0 |

### Top Repos by Stars

| Org/User | Full Name | Stars | Language | Last Pushed |
|----------|-----------|-------|----------|-------------|
| kubeflow | kubeflow/kubeflow | 15625 |  | 2026-05-07 |
| kubeflow | kubeflow/pipelines | 4136 | Python | 2026-05-07 |
| kubeflow | kubeflow/spark-operator | 3124 | Python | 2026-05-05 |
| kubeflow | kubeflow/trainer | 2095 | Go | 2026-05-07 |
| kubeflow | kubeflow/katib | 1683 | Python | 2026-05-07 |
| kubeflow | kubeflow/examples | 1461 | Jsonnet | 2025-04-14 |
| kubeflow | kubeflow/manifests | 1015 | YAML | 2026-05-07 |
| kubeflow | kubeflow/arena | 810 | Go | 2026-05-07 |
| kubeflow | kubeflow/kale | 684 | Python | 2026-05-07 |
| kubeflow | kubeflow/mpi-operator | 524 | Go | 2026-05-05 |
| kubeflow | kubeflow/fairing | 337 | Jsonnet | 2022-04-11 |
| kubeflow | kubeflow/pytorch-operator | 310 | Jsonnet | 2021-12-01 |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| MINUS | #cc241d | -1 | 130 |
| ERGODIC | #d3869b | 0 | 130 |
| PLUS | #b8bb26 | 1 | 130 |

Rule: `id%3==0` → trit=0 ERGODIC #d3869b · `id%3==1` → trit=+1 PLUS #b8bb26 · `id%3==2` → trit=-1 MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) queried via Aptos fullnode mainnet API
at ledger version ~5.17B (2026-05-07).

**Result:** All addresses return `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — wallets not yet initialized on mainnet.
Balance = 0.0 APT for all 28 addresses.

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | yes |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | yes |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | yes |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | yes |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | yes |

All 5 multisig contracts require **2-of-N signatures** and are healthy.

### MNX Markets

- URL: `https://testnet.mnx.fi`
- Status: **Unavailable** — Next.js SPA, no accessible JSON API at common paths (/api/markets, /api/v1/markets).

---

## DuckDB Schema

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 390 | GF(3) color-chain event log |
| repo_snapshots | 390 | GitHub repo metadata snapshot |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Aptos multisig health checks |
| mnx_snapshots | 1 | MNX market data (unavailable) |
