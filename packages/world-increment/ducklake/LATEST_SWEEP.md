# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-08

## Sweep Metadata
- **Date:** 2026-07-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 346 |
| Total Repo Snapshots | 1,267 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain

GF(3) trit = `id % 3`:
- `id % 3 == 0` → trit=0, color=#d3869b, **ERGODIC** (~115 increments)
- `id % 3 == 1` → trit=1, color=#b8bb26, **PLUS** (~116 increments)
- `id % 3 == 2` → trit=-1, color=#cc241d, **MINUS** (~115 increments)

### Top Repos by Source

#### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| gorj | Clojure | — | (this repo) |

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,769 | 2026-07-xx |
| pipelines | Python | 4,169 | 2026-07-xx |
| spark-operator | Python | 3,134 | 2026-07-xx |
| trainer | Go | 2,132 | 2026-07-xx |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

#### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |

#### Social Graph (zubyul + 6 nodes)
| User | Top Repo | Stars |
|------|----------|-------|
| migalkin | NodePiece (ICLR'22 KG embeddings) | 144 |
| AustinCStone | TextGAN | 92 |
| migalkin | StarE (EMNLP 2020) | 89 |
| wasita | wasita.github.io (Svelte, pushed 2026-07-06) | 1 |
| kristinezheng | kristinezheng.github.io (pushed 2026-07-01) | 0 |

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | social | 40 |
| migalkin | social | 19 |
| wasita | social | 11 |
| M1shaaa | social | 8 |
| kristinezheng | social | 5 |
| TeglonLabs | org | 5 |
| DJedamski | social | 6 |
| **TOTAL** | | **~392** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, Ledger ~617,656,xxx)

**All 28 wallets queried — all have 0 APT (CoinStore uninitialized)**

| World | Address (truncated) | APT | Status |
|-------|---------------------|-----|--------|
| alice | 0xc793…cc7b | 0.0 | no_coinstore |
| bob | 0x0a3c…2d5d | 0.0 | no_coinstore |
| A | 0x8699…9d7a | 0.0 | no_coinstore |
| B–Z | (24 addresses) | 0.0 each | no_coinstore |

All wallets exist on-chain but `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` is absent for every address.

### Multisig Contract Probes (Mainnet)

**All 5 pairs healthy — each requires 2-of-N signatures**

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — Vercel deployment protection requires visitor password. No market data extracted.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,769 stars (+204 since 2026-04-12 sweep)
- **TeglonLabs/jank-crane**: new since last sweep — C++ crane-jank GF3 convergence hub
- **wasita/wasita.github.io**: most recently pushed node in social graph (2026-07-06)
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR'22)
- **All 5 multisig pairs**: healthy 2-of-N on Aptos mainnet
- **28 Hamming wallets**: all uninitialized — 0 APT across entire swarm
