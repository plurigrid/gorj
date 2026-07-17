# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-07-17T00:00:00Z  
**GF(3) Color Chain:** ERGODIC `#d3869b` | PLUS `#b8bb26` | MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 5 |
| DJedamski | social graph | 2 |
| wasita | social graph | 5 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 4 |
| **TOTAL** | | **323** |

### Top Repos by Stars
| Repo | Stars | Language | Source |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15779 | N/A | kubeflow |
| kubeflow/pipelines | 4167 | Python | kubeflow |
| kubeflow/spark-operator | 3137 | Python | kubeflow |
| kubeflow/trainer | 2150 | Go | kubeflow |
| kubeflow/katib | 1690 | Python | kubeflow |
| kubeflow/examples | 1460 | Jsonnet | kubeflow |
| kubeflow/community-distribution | 1029 | YAML | kubeflow |
| kubeflow/arena | 815 | Go | kubeflow |
| kubeflow/kale | 696 | Python | kubeflow |
| kubeflow/mpi-operator | 530 | Go | kubeflow |
| kubeflow/fairing | 337 | Jsonnet | kubeflow |
| kubeflow/pytorch-operator | 310 | Jsonnet | kubeflow |
| kubeflow/community | 195 | Jupyter Notebook | kubeflow |
| kubeflow/website | 184 | HTML | kubeflow |
| kubeflow/mcp-apache-spark-history-server | 183 | Python | kubeflow |

### Notable Activity
- **plurigrid/gorj** (1 match): pushed 2026-07-17 (today) — Clojure, 1209 open issues
- **wasita/wasita.github.io**: pushed 2026-07-16 (yesterday) — Svelte personal site
- **wasita/pnas-typst-template**: pushed 2026-07-16 (yesterday) — new repo
- **AustinCStone/byteruckus**: pushed 2026-07-15 — new HTML repo
- **migalkin/kgcourse2021**: pushed 2026-07-10 — KG course materials (HTML, 24★)

### DuckDB ducklake
- **world-increments.duckdb**: 346 total world_increments, 1267 total repo_snapshots
- GF(3) trit distribution: ERGODIC=114, PLUS=116, MINUS=116 (this sweep: 323 new records)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All accounts returned `resource_not_found` — either inactive/new accounts or accounts using the newer Aptos Fungible Asset module (which supersedes the legacy CoinStore interface).

| World | Address (prefix) | Balance (APT) | Status |
|-------|-----------------|---------------|--------|
| alice | 0xc793acde... | 0.0000 | resource_not_found |
| bob | 0x0a3c00c5... | 0.0000 | resource_not_found |
| A | 0x8699edc0... | 0.0000 | resource_not_found |
| B | 0x3f892ebe... | 0.0000 | resource_not_found |
| C | 0x38b99e63... | 0.0000 | resource_not_found |
| D | 0xf7765624... | 0.0000 | resource_not_found |
| E | 0xdc1d9d53... | 0.0000 | resource_not_found |
| F | 0x18a14b5b... | 0.0000 | resource_not_found |
| G | 0x69a394c0... | 0.0000 | resource_not_found |
| H | 0xce67c327... | 0.0000 | resource_not_found |
| I | 0x070fe5d7... | 0.0000 | resource_not_found |
| J | 0x4d964db8... | 0.0000 | resource_not_found |
| K | 0xa732040a... | 0.0000 | resource_not_found |
| L | 0x7c2eaeaf... | 0.0000 | resource_not_found |
| M | 0x6fed37a7... | 0.0000 | resource_not_found |
| N | 0xe7dde6da... | 0.0000 | resource_not_found |
| O | 0x73252b60... | 0.0000 | resource_not_found |
| P | 0x6218792d... | 0.0000 | resource_not_found |
| Q | 0xac40fa50... | 0.0000 | resource_not_found |
| R | 0x7ce605cc... | 0.0000 | resource_not_found |
| S | 0xb8753014... | 0.0000 | resource_not_found |
| T | 0x35781dc0... | 0.0000 | resource_not_found |
| U | 0x75860da4... | 0.0000 | resource_not_found |
| V | 0xb59dd817... | 0.0000 | resource_not_found |
| W | 0x5f32aef7... | 0.0000 | resource_not_found |
| X | 0xa95cbbd1... | 0.0000 | resource_not_found |
| Y | 0xd8e32848... | 0.0000 | resource_not_found |
| Z | 0x7af0ef6e... | 0.0000 | resource_not_found |

**Total APT across swarm:** 0.0000 APT

### Multisig Contract Probes
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**Status:** 5/5 multisig contracts healthy, all require 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)
All probed endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`) returned HTML SPA responses with no extractable market data. MNX testnet market data is **unavailable** via direct API — the frontend is a JavaScript SPA that loads data client-side.

---

## Summary
- **GitHub:** 323 repos snapshotted across 11 org/user/social-graph sources
- **Aptos wallets:** 28 addresses queried, all `resource_not_found` (legacy CoinStore interface; may need Fungible Asset endpoint)
- **Multisigs:** 5/5 healthy (2-of-2 each): A-B, A-G, Y-Z, S-T, V-W
- **MNX:** Unavailable (SPA, no REST API)
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` updated
