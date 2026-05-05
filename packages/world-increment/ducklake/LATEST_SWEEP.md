# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-05T17:30 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
**DuckDB version:** v1.5.2 (Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 20 |
| kubeflow | org | 17 |
| TeglonLabs | org | 4 |
| bmorphism | user | 11 |
| zubyul | user | 12 |
| migalkin | user (zubyul social graph) | 5 |
| DJedamski | user (zubyul social graph) | 3 |
| wasita | user (zubyul social graph) | 3 |
| kristinezheng | user (zubyul social graph) | 2 |
| M1shaaa | user (zubyul social graph) | 2 |
| AustinCStone | user (zubyul social graph) | 4 |
| **Total** | | **82 repos** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,623 | — | 2026-04-29 |
| kubeflow/pipelines | 4,133 | Python | 2026-05-05 |
| kubeflow/spark-operator | 3,123 | Python | 2026-05-05 |
| kubeflow/trainer | 2,096 | Go | 2026-05-05 |
| kubeflow/katib | 1,683 | Python | 2026-04-14 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,015 | YAML | 2026-04-30 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Most Active (recently pushed)

| Repo | Last Push | Notes |
|------|-----------|-------|
| plurigrid/gorj | 2026-05-05 | This repo — forj + Rama topology |
| kubeflow/pipelines | 2026-05-05 | Active ML platform |
| kubeflow/kale | 2026-05-05 | Data scientist tooling |
| bmorphism/Gay.jl | 2026-05-05 | GF(3) color system, 187 open issues |
| kubeflow/spark-operator | 2026-05-05 | Spark on K8s |

### GF(3) Color Chain Distribution (82 world_increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 27 |
| 1 | #b8bb26 | PLUS | 28 |
| -1 | #cc241d | MINUS | 27 |

GF(3) chain rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z + alice/bob)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (prefix) | Balance (APT) | Status |
|-------|-----------------|---------------|--------|
| alice | 0xc793acd... | 0.0 | Uninitialized CoinStore |
| bob | 0x0a3c00c... | 0.0 | Uninitialized CoinStore |
| A | 0x8699edc... | 0.0 | Uninitialized CoinStore |
| B | 0x3f892eb... | 0.0 | Uninitialized CoinStore |
| C | 0x38b99e6... | 0.0 | Uninitialized CoinStore |
| D | 0xf776562... | 0.0 | Uninitialized CoinStore |
| E | 0xdc1d9d5... | 0.0 | Uninitialized CoinStore |
| F | 0x18a14b5... | 0.0 | Uninitialized CoinStore |
| G | 0x69a394c... | 0.0 | Uninitialized CoinStore |
| H | 0xce67c32... | 0.0 | Uninitialized CoinStore |
| I | 0x070fe5d... | 0.0 | Uninitialized CoinStore |
| J | 0x4d964db... | 0.0 | Uninitialized CoinStore |
| K | 0xa732040... | 0.0 | Uninitialized CoinStore |
| L | 0x7c2eaea... | 0.0 | Uninitialized CoinStore |
| M | 0x6fed37a... | 0.0 | Uninitialized CoinStore |
| N | 0xe7dde6d... | 0.0 | Uninitialized CoinStore |
| O | 0x73252b6... | 0.0 | Uninitialized CoinStore |
| P | 0x6218792... | 0.0 | Uninitialized CoinStore |
| Q | 0xac40fa5... | 0.0 | Uninitialized CoinStore |
| R | 0x7ce605c... | 0.0 | Uninitialized CoinStore |
| S | 0xb875301... | 0.0 | Uninitialized CoinStore |
| T | 0x35781dc... | 0.0 | Uninitialized CoinStore |
| U | 0x75860da... | 0.0 | Uninitialized CoinStore |
| V | 0xb59dd81... | 0.0 | Uninitialized CoinStore |
| W | 0x5f32aef... | 0.0 | Uninitialized CoinStore |
| X | 0xa95cbbd... | 0.0 | Uninitialized CoinStore |
| Y | 0xd8e3284... | 0.0 | Uninitialized CoinStore |
| Z | 0x7af0ef6... | 0.0 | Uninitialized CoinStore |

> All 28 Aptos addresses return `Resource not found` for the legacy `CoinStore`. These wallets may use the Aptos Fungible Asset (FA) standard or are simply unfunded on mainnet.

### Multisig Contract Health

All 5 contracts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Contract Address | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✅ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✅ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no JSON API data available.**
The site serves a Next.js single-page application for all `/api/*` paths. No structured market data was extractable.

---

## DuckDB Schema

```
world-increments.duckdb
├── world_increments    (82 rows)  — GF3-colored sweep events (repo snapshots)
├── repo_snapshots      (82 rows)  — GitHub repo metadata with stars/forks/issues
├── aptos_snapshots     (28 rows)  — Wallet balance probes (A-Z + alice/bob)
├── multisig_probes     (5 rows)   — Aptos multisig contract health checks
└── mnx_snapshots       (1 row)    — MNX testnet (SPA/unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,623 stars — flagship ML platform for Kubernetes (updated from 15,565)
- **kubeflow/pipelines**: 4,133 stars — most active, pushed 2026-05-05
- **plurigrid/gorj**: This very repo — actively pushing today (2026-05-05)
- **bmorphism/Gay.jl**: 187 open issues — most active issue tracker in the swarm
- **migalkin/NodePiece**: 143 stars — ICLR'22 KG embeddings paper
- **AustinCStone/TextGAN**: 92 stars — TensorFlow text GAN
- **All multisigs**: 2-of-N threshold, all 5 healthy on Aptos mainnet
- **Hamming swarm**: 28 wallets probed, all show uninitialized APT CoinStore

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-05-05*
