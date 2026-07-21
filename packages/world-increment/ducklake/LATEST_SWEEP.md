# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 99 |
| Total Repo Snapshots | 1020 |
| Sources Covered | 3 orgs + 5 users + 6 social graph |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph

### GF(3) Color Chain Distribution

World increments colored by `id % 3`:
- **ERGODIC** (#d3869b, trit=0): ids 3,6,9,…  
- **PLUS** (#b8bb26, trit=1): ids 1,4,7,…  
- **MINUS** (#cc241d, trit=-1): ids 2,5,8,…  

### Top Repos by Source

#### kubeflow/plurigrid (49 repos, active 2026-07-21)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4169 | 2026-07-21 |
| spark-operator | Python | 3141 | 2026-07-17 |
| trainer | Go | 2152 | 2026-07-20 |
| katib | Python | 1692 | 2026-07-20 |
| community-distribution | YAML | 1029 | 2026-07-21 |
| mcp-apache-spark-history-server | Python | 183 | 2026-07-16 |
| mcp-server | Python | 28 | 2026-07-20 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |

#### bmorphism (106 repos, top 10 indexed)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 22 |
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |
| manifold-mcp-server | JavaScript | 14 |
| penrose-mcp | JavaScript | 9 |
| Gay.jl | Julia | 2 (updated 2026-07-20) |

#### zubyul (49 repos, top 5 indexed)
| Repo | Language | Stars |
|------|----------|-------|
| voice-observatory | Python | 0 |
| gay-world | Python | 1 |
| tilelang-kernels | Python | 0 |

#### Social Graph (migalkin, wasita, AustinCStone, M1shaaa, DJedamski, kristinezheng)
| Repo | Language | Stars |
|------|----------|-------|
| migalkin/NodePiece | Python | 144 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |
| wasita/wasita.github.io | Svelte | 1 (updated 2026-07-20) |
| wasita/send2kobo | TypeScript | 1 |

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid/kubeflow | org | 49 |
| bmorphism | user | 106 total, 10 indexed |
| zubyul | user | 49 total, 5 indexed |
| TeglonLabs | org | 5 |
| social graph (6 users) | users | ~30 indexed |
| **TOTAL INDEXED** | | **~99 world increments** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-21)

All 28 hamming-swarm wallets queried via `fullnode.mainnet.aptoslabs.com`.  
**All wallets report 0 APT.** Accounts exist on-chain (CoinStore initialized) but are unfunded.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded to `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f4… | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a… | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe1… | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3a… | 2 | ✅ HEALTHY |
| V-W | 0x40fad7… | 2 | ✅ HEALTHY |

All multisigs require 2-of-N signatures. All contracts on-chain and healthy.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` and `/api/markets` return **HTTP 401 Unauthorized**.  
Testnet requires authentication. Market data unavailable — recorded as `UNAVAILABLE` in `mnx_snapshots`.

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
- **kubeflow/pipelines**: 4,169 stars — active 2026-07-21 (up from 4,119 in April)
- **kubeflow/spark-operator**: 3,141 stars — Kubernetes/Spark operator
- **migalkin/NodePiece**: 144 stars — KG embeddings (ICLR'22), recently active
- **bmorphism/Gay.jl**: Julia repo updated 2026-07-20 — most recent bmorphism activity
- **wasita/wasita.github.io**: updated 2026-07-20 — Svelte personal site
- **All 28 Aptos wallets**: 0 APT — swarm wallets initialized but unfunded
- **All 5 multisigs**: 2-sig healthy — operational on mainnet
