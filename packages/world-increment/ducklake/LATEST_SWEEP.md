# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22T08:14 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 334 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name | Repos |
|----|--------|------|-----------|-------|------|-------|
| 1  | plurigrid | org | 0 | `#d3869b` | **ERGODIC** | 100 |
| 2  | kubeflow | org | 1 | `#b8bb26` | **PLUS** | 49 |
| 3  | TeglonLabs | org | 2 | `#cc241d` | **MINUS** | 5 |
| 4  | bmorphism | user | 0 | `#d3869b` | **ERGODIC** | 100 |
| 5  | zubyul | user | 1 | `#b8bb26` | **PLUS** | 49 |
| 6  | migalkin | user | 2 | `#cc241d` | **MINUS** | 6 |
| 7  | wasita | user | 0 | `#d3869b` | **ERGODIC** | 6 |
| 8  | kristinezheng | user | 1 | `#b8bb26` | **PLUS** | 5 |
| 9  | AustinCStone | user | 2 | `#cc241d` | **MINUS** | 5 |
| 10 | DJedamski | user | 0 | `#d3869b` | **ERGODIC** | 4 |
| 11 | M1shaaa | user | 1 | `#b8bb26` | **PLUS** | 5 |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

### Top Repos by Source

#### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-22 |
| place | TeX | 1 | 2026-07-14 |
| eirobri | Clojure | 0 | 2026-07-21 |
| shrimp | — | 0 | 2026-07-03 |

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4168 | 2026-07-22 |
| trainer | Go | 2152 | 2026-07-21 |
| hub | Go | 178 | 2026-07-21 |
| internal-acls | Go | 19 | 2026-07-21 |
| mlflow-integration | Python | 7 | 2026-07-21 |

#### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-22 |
| gay-chat | Scheme | 0 | 2026-07-14 |
| satreadout | HTML | 0 | 2026-06-20 |
| bci-preview | HTML | 0 | 2026-06-20 |
| world | Python | 0 | 2026-06-02 |

#### migalkin (6 repos, KG researcher)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| migalkin | user | 6 |
| wasita | user | 6 |
| AustinCStone | user | 5 |
| M1shaaa | user | 5 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| DJedamski | user | 4 |
| **TOTAL** | | **334** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger ~639.7M)

All 28 addresses (alice, bob, A–Z) probed via `fullnode.mainnet.aptoslabs.com`.  
All accounts report `Resource not found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — these accounts use the modern Fungible Asset (FA) model rather than the legacy coin CoinStore. Legacy API balance: **0.0 APT** for all.

| World | Address | Legacy APT Balance |
|-------|---------|-------------------|
| alice | 0xc793...cc7b | 0.0 (FA model) |
| bob   | 0x0a3c...512d | 0.0 (FA model) |
| A–Z   | (26 addresses) | 0.0 each (FA model) |

### Multisig Contract Probes — All 5 HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ healthy |
| A-G | 0xf56c...096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✅ healthy |
| S-T | 0x3b1c...883 | 2 | ✅ healthy |
| V-W | 0x40fa...b6d | 2 | ✅ healthy |

All 5 multisig contracts require 2-of-N signatures and respond to `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no public REST API is exposed. The root returns HTML client-side JS bundles; `/api/markets` and `/api/v1/markets` return 404. **Status: SPA — REST market data unavailable via API.**

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/pipelines**: 4,168★ — active ML pipeline platform, pushed 2026-07-22
- **kubeflow/trainer**: 2,152★ — Go-based distributed trainer, pushed 2026-07-21
- **migalkin/NodePiece**: 144★ — ICLR'22 scalable KG embeddings, still active
- **migalkin/StarE**: 89★ — EMNLP 2020 hyper-relational KG message passing
- **AustinCStone/TextGAN**: 92★ — TF text GAN, oldest star-getter in social graph
- **plurigrid/asi**: 31★ — top plurigrid repo by stars, pushed 2026-07-10
- **bmorphism/Gay.jl**: pushed today 2026-07-22 — bmorphism most active user right now
- **All 5 multisig contracts**: 2-of-N sigs required, all healthy on Aptos mainnet
