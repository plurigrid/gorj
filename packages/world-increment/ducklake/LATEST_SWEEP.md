# World-Increment Sweep + Hamming Snapshot

**Run timestamp:** 2026-08-09  
**GF3 color chain:** ERGODIC=#d3869b · PLUS=#b8bb26 · MINUS=#cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos snapshotted | Total Stars |
|---|---|---|---|
| kubeflow | org | 49 | 102,221 |
| migalkin | user (social) | 19 | 821 |
| bmorphism | user | 100 | 509 |
| AustinCStone | user (social) | 41 | 308 |
| plurigrid | org | 100 | 195 |
| zubyul | user | 49 | 40 |
| TeglonLabs | org | 5 | 14 |
| DJedamski | user (social) | 6 | 14 |
| wasita | user (social) | 14 | 7 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 8 | 0 |

**Total repos this run: 315**

### Top repos by stars (this run)

| Repo | Stars | Language | Last pushed |
|---|---|---|---|
| kubeflow/kubeflow | 15,808 | Jupyter Notebook | 2026-07-10 |
| kubeflow/pipelines | 4,180 | Python | 2026-08-09 |
| kubeflow/spark-operator | 3,146 | Go | 2026-08-08 |
| kubeflow/trainer | 2,177 | Go | 2026-08-08 |
| kubeflow/katib | 1,694 | Go | 2026-08-06 |
| migalkin/NodePiece | 144 | Python | 2021-06-14 |
| AustinCStone/TextGAN | 92 | Python | 2016-09-19 |
| migalkin/StarE | 89 | Python | 2020-09-17 |

### Notable social graph repos

- **wasita/wm-cv** — Academic CV as Svelte SPA, pushed 2026-08-07 (very recent)
- **wasita/xoxowasita-analysis** — Python analysis, pushed 2026-08-06
- **TeglonLabs/jank-crane** — C++, crane-jank GF3 convergence maps, pushed 2026-06-08
- **migalkin/NBFNet_mlx** — Neural Bellman-Ford on Apple Silicon (MLX), 10 stars
- **AustinCStone/byteruckus** — HTML, pushed 2026-07-15

### DuckDB tables (cumulative)

| Table | Row count |
|---|---|
| world_increments | 338 |
| repo_snapshots | 1,259 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

GF3 distribution this run: ERGODIC=112 · PLUS=113 · MINUS=113

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses queried (alice, bob, A–Z) returned `resource_not_found` from the Aptos mainnet CoinStore resource. This indicates the accounts have zero APT balance (no CoinStore initialized) or are unfunded. All balance values recorded as 0.0 APT.

| World | Result |
|---|---|
| alice | 0.0 APT (resource_not_found) |
| bob | 0.0 APT (resource_not_found) |
| A–Z (26 wallets) | 0.0 APT each (resource_not_found) |

### Multisig Contract Probes

All 5 multisig pairs are **healthy** (2-of-N threshold on Aptos mainnet):

| Pair | Address (prefix) | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

**Observation:** All multisig accounts require exactly 2 signatures. Contracts are live on Aptos mainnet.

### MNX Markets

`https://testnet.mnx.fi` is a Next.js SPA (63KB HTML shell). No public REST API endpoints found at `/api/markets` or `/api/v1/markets` — data is loaded client-side via JavaScript bundles. Market data unavailable via direct HTTP probe. Recorded as `UNAVAILABLE` in mnx_snapshots.

---

## DuckDB Location

```
packages/world-increment/ducklake/world-increments.duckdb
```

Schema: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
