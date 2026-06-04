# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-07  
**DuckDB:** v1.5.2 (Variegata)  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Orgs Swept
| Org/User | Repos Captured | Total Stars |
|---|---|---|
| kubeflow | 20 | 32,455 |
| migalkin (social) | 4 | 127 |
| bmorphism | 15 | 95 |
| plurigrid | 20 | 31 |
| TeglonLabs | 15 | 5 |
| zubyul | 15 | 5 |
| DJedamski (social) | 3 | 4 |
| wasita (social) | 4 | 3 |
| kristinezheng (social) | 3 | 0 |
| AustinCStone (social) | 3 | 0 |
| M1shaaa (social) | 3 | 0 |

**Total repos:** 105 | **Total world_increments:** 16

### GF(3) Color Chain (id % 3)
- `0` → trit=0 **ERGODIC** `#d3869b` (pink)
- `1` → trit=1 **PLUS** `#b8bb26` (yellow-green)
- `2` → trit=-1 **MINUS** `#cc241d` (red)

### Top Repos by Stars
| Repo | Stars | Language | Pushed |
|---|---|---|---|
| kubeflow/kubeflow | 15,625 | — | 2026-04-29 |
| kubeflow/pipelines | 4,136 | Python | 2026-05-07 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-05 |
| kubeflow/trainer | 2,095 | Go | 2026-05-07 |
| kubeflow/katib | 1,683 | Python | 2026-05-06 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,015 | YAML | 2026-04-30 |
| kubeflow/arena | 810 | Go | 2026-05-07 |
| kubeflow/kale | 684 | Python | 2026-05-06 |
| kubeflow/mpi-operator | 524 | Go | 2026-05-05 |
| kubeflow/sdk | 112 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/asi | 20 | HTML | 2026-04-26 |
| bmorphism/Gay.jl | 1 | Julia | 2026-05-07 (187 issues!) |

### Recent Events (bmorphism)
| Event | Repo | Date |
|---|---|---|
| CreateEvent | bmorphism/nanoclj-zig | 2026-05-07 |
| WatchEvent | scicloj/janqua | 2026-05-06 |
| ForkEvent | DavidJaz/DynamicalSystemsBook | 2026-05-03 |
| PushEvent | plurigrid/zig-syrup | 2026-04-30 |
| PushEvent | bmorphism/boxxy | 2026-04-30 |
| PullRequestEvent | plurigrid/horse | 2026-04-26 |

### Recent Events (zubyul)
| Event | Repo | Date |
|---|---|---|
| PullRequestEvent | plurigrid/gorj | 2026-05-07 (×multiple) |
| CreateEvent | plurigrid/gorj | 2026-05-07 |
| PullRequestEvent | plurigrid/horse | 2026-05-07 |

### Zubyul Social Graph Snapshot
| User | Most Recent Repo | Lang | Stars |
|---|---|---|---|
| migalkin | kgcourse2021 | HTML | 25 |
| DJedamski | awesome-ruby | — | 2 |
| wasita | vocoder | JavaScript | 0 |
| kristinezheng | kristinezheng.github.io | HTML | 0 |
| M1shaaa | M1shaaa (profile) | — | 0 |
| AustinCStone | EpsteinSearch | Python | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**Endpoint:** `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 addresses (alice, bob, A–Z) returned `resource_not_found`. These accounts have no APT `CoinStore` resource on mainnet — either unfunded or resource not initialized.

| World | Address (prefix) | Balance APT |
|---|---|---|
| alice | 0xc793… | unfunded |
| bob | 0x0a3c… | unfunded |
| A–Z | 0x8699…–0x7af0… | unfunded (26 addrs) |

> Note: `resource_not_found` on `CoinStore<AptosCoin>` means the account has never received APT or the resource was never registered. This is distinct from zero balance.

### Multisig Contract Probes
**Endpoint:** `POST /v1/view → 0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4f428… | **2** | HEALTHY |
| A-G | 0xf56c4a1c… | **2** | HEALTHY |
| Y-Z | 0xd3ffe181… | **2** | HEALTHY |
| S-T | 0x3b1c3ae9… | **2** | HEALTHY |
| V-W | 0x40fad7b4… | **2** | HEALTHY |

All 5 multisig contracts healthy: **2-of-N threshold** uniformly across all pairs.

### MNX Markets (testnet.mnx.fi)
Status: **SPA — data unavailable**  
`https://testnet.mnx.fi` serves a Next.js SPA. No `/api/markets` or `/api/v1/markets` endpoints returned structured data (HTML-only response). Market data requires client-side JS execution. `mnx_snapshots` table is empty pending a headless browser probe.

---

## DuckDB Schema Summary

| Table | Rows |
|---|---|
| world_increments | 16 |
| repo_snapshots | 105 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, unavailable) |

---

## GF(3) Increment Log

| id | trit | color | name | source | event |
|---|---|---|---|---|---|
| 1 | 1 | PLUS #b8bb26 | plurigrid | org | repo_sweep |
| 2 | 2 | MINUS #cc241d | kubeflow | org | repo_sweep |
| 3 | 0 | ERGODIC #d3869b | TeglonLabs | org | repo_sweep |
| 4 | 1 | PLUS #b8bb26 | bmorphism | user | repo_sweep |
| 5 | 2 | MINUS #cc241d | zubyul | user | repo_sweep |
| 6 | 0 | ERGODIC #d3869b | social_graph | user | repo_sweep |
| 7 | 1 | PLUS #b8bb26 | bmorphism | event | CreateEvent |
| 8 | 2 | MINUS #cc241d | bmorphism | event | WatchEvent |
| 9 | 0 | ERGODIC #d3869b | bmorphism | event | ForkEvent |
| 10 | 1 | PLUS #b8bb26 | bmorphism | event | PushEvent |
| 11 | 2 | MINUS #cc241d | bmorphism | event | PushEvent |
| 12 | 0 | ERGODIC #d3869b | bmorphism | event | PullRequestEvent |
| 13 | 1 | PLUS #b8bb26 | zubyul | event | PullRequestEvent |
| 14 | 2 | MINUS #cc241d | zubyul | event | CreateEvent |
| 15 | 0 | ERGODIC #d3869b | zubyul | event | PullRequestEvent |
| 16 | 1 | PLUS #b8bb26 | zubyul | event | CreateEvent |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,625 stars — flagship ML platform for Kubernetes (delta +60 since last sweep)
- **kubeflow/pipelines**: 4,136 stars — most active push 2026-05-07
- **kubeflow/sdk**: new MCP-adjacent Universal Python SDK entry
- **bmorphism/Gay.jl**: 187 open issues — highly active GF(3) color library
- **plurigrid/gorj**: 96 open issues — this very repo, world-increment home
- **zubyul**: 15+ PRs to plurigrid/gorj today — active contributor
- **All 5 Aptos multisigs**: 2-of-N, all healthy on mainnet
- **28 Hamming swarm wallets**: all show resource_not_found (unfunded CoinStore)
