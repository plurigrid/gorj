# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments | 6 |
| New Repo Snapshots | 52 |
| Sources Covered | 3 orgs + 3 users + 1 social-graph bundle |

### GF(3) Color Chain — New Increments (ids 7–12 in this run)

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1 | plurigrid (org) | org | -1 | `#cc241d` | **MINUS** |
| 2 | kubeflow (org) | org | 0 | `#d3869b` | **ERGODIC** |
| 3 | TeglonLabs (org) | org | +1 | `#b8bb26` | **PLUS** |
| 4 | bmorphism (user) | user | -1 | `#cc241d` | **MINUS** |
| 5 | zubyul (user) | user | 0 | `#d3869b` | **ERGODIC** |
| 6 | social_graph | user_network | +1 | `#b8bb26` | **PLUS** |

### Notable Activity (2026-08-03)

- **plurigrid/gorj** (this repo) — pushed 21:32 UTC — 1609 open issues, Clojure
- **kubeflow/pipelines** — pushed 21:39 UTC — 4,173★ Python
- **kubeflow/notebooks** — pushed 17:11 UTC
- **plurigrid/place** — pushed 20:00 UTC, TeX
- **bmorphism/anti-bullshit-mcp-server** — pushed 02:54 UTC — 23★
- **wasita/wasita.github.io** — pushed 15:55 UTC, Svelte
- **migalkin/kgcourse2021** — pushed 15:40 UTC (Knowledge Graphs course, 24★)

### Top Repos by Source

#### plurigrid (10 sampled)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| asi | HTML | 58 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-08-03 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| place | TeX | 1 | 2026-08-02 |
| nash-portal | Rust | 2 | 2026-05-19 |

#### kubeflow (10 sampled)
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow | — | 15,804 | 2026-07-10 |
| pipelines | Python | 4,173 | 2026-08-03 |
| spark-operator | Python | 3,142 | 2026-08-03 |
| trainer | Go | 2,165 | 2026-07-31 |
| katib | Python | 1,694 | 2026-08-03 |

#### TeglonLabs (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |
| topoi | Python | 0 |

#### bmorphism (9 sampled)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| risc0-cosmwasm-example | Rust | 23 |
| say-mcp-server | JavaScript | 20 |
| manifold-mcp-server | JavaScript | 14 |

#### zubyul (7 sampled)
| Repo | Language | Stars |
|------|----------|-------|
| gay-world | Python | 1 |
| jonikas_lab_data_analysis_misc | Jupyter Notebook | 2 |
| voice-observatory | Python | 0 |

#### Social Graph (migalkin/DJedamski/wasita/kristinezheng/M1shaaa/AustinCStone — 12 sampled)
| Repo | Language | Stars |
|------|----------|-------|
| AustinCStone/TextGAN | Python | 92 |
| migalkin/NodePiece | Python | 144 |
| migalkin/StarE | Python | 89 |
| migalkin/kgcourse2021 | HTML | 24 |
| wasita/magic-garden | Python | 2 |

### Repo Counts (this run)

| Source | Type | Repos Sampled |
|--------|------|--------------|
| kubeflow | org | 10 |
| social_graph | user_network | 12 |
| bmorphism | user | 9 |
| plurigrid | org | 10 |
| zubyul | user | 7 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **52** |

---

## JOB 2: Hamming Swarm Snapshot (Aptos)

### Wallet Balances — 28 Addresses (alice, bob, A–Z)

**Status:** All 28 addresses returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version **6,598,366,361**.

These wallets have not initialized the legacy APT CoinStore — they may use the  
Fungible Asset (FA) standard, or are uninitialized. All `balance_apt = NULL`.

### Multisig Contract Probes — 5 Pairs

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | `0x0da4f428...` | 2-of-2 | ✅ HEALTHY |
| A-G | `0xf56c4a1c...` | 2-of-2 | ✅ HEALTHY |
| Y-Z | `0xd3ffe181...` | 2-of-2 | ✅ HEALTHY |
| S-T | `0x3b1c3ae9...` | 2-of-2 | ✅ HEALTHY |
| V-W | `0x40fad7b4...` | 2-of-2 | ✅ HEALTHY |

All 5 multisig contracts are responsive on Aptos mainnet. All require 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA with no public REST API endpoint.  
Fetching the root returns JavaScript bundles, no market data. Recorded as `N/A`.

---

## DuckDB Table Summary (this run)

| Table | New Rows |
|-------|---------|
| world_increments | 6 |
| repo_snapshots | 52 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

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

## Previous Sweep (2026-04-12)
Total lifetime rows: world_increments=29, repo_snapshots=996, aptos_snapshots=28, multisig_probes=5
