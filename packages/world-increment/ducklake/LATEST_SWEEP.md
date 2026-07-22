# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 197 |
| Total Repo Snapshots | 1118 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain (first 12 of 197 increments)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | plurigrid (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | plurigrid (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | plurigrid (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | plurigrid (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | plurigrid (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: cycles `PLUS → MINUS → ERGODIC` continuously across all 197 increments.

---

## Top Repos by Source

### plurigrid (100 repos — most recently active)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-22 |
| eirobri | Clojure | 0 | 2026-07-21 |
| place | TeX | 1 | 2026-07-14 |
| shrimp | — | 0 | 2026-07-03 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15788 | 2026-07-10 |
| pipelines | Python | 4169 | 2026-07-22 |
| spark-operator | Python | 3142 | 2026-07-17 |
| trainer | Go | 2153 | 2026-07-22 |
| katib | Python | 1692 | 2026-07-22 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (106 repos — top by stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 19 | 2026-06-05 |
| manifold-mcp-server | JavaScript | 14 | 2026-04-15 |

### migalkin (19 repos — KG researcher)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

### AustinCStone (41 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 worlds: alice, bob, A–Z)
All queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` with 1s sleep between calls.

**Result: All 28 wallets returned 0.0 APT** — accounts either unfunded or `CoinStore` resource not registered on mainnet.

### Multisig Contract Probes
Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

**All 5 contracts HEALTHY — 2 signatures required.**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)
`testnet.mnx.fi` is a Next.js SPA. API endpoints `/api/markets` and `/api/v1/markets` return HTML shell — no JSON data extractable without JS execution. **Status: unavailable via curl.**

---

## Schema
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

## Notable Highlights (2026-07-22)
- **kubeflow/trainer** and **kubeflow/pipelines** and **kubeflow/katib** all pushed today (2026-07-22)
- **plurigrid/gorj**: pushed today — this is the sweep repo itself
- **bmorphism/Gay.jl**: 187 open issues, active Julia color sampling project
- **bmorphism/gay-chat**: new (2026-07-14) Scheme/Spritely Brassica chat operationalization
- **TeglonLabs/jank-crane**: new C++ repo (2026-06-08) — GF3 convergence maps + crane-jank IR
- **wasita/wasita.github.io**: updated yesterday (2026-07-21) — active personal site
- **All 5 Aptos multisig contracts**: healthy, all require 2-of-N signatures
- **Hamming swarm**: all 28 wallets at 0.0 APT (likely testnet/unfunded state)
