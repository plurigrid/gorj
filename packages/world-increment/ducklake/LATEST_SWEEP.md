# World-Increment Sweep + Hamming Snapshot — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this sweep) | 203 |
| Total Repo Snapshots (cumulative) | 1124 |
| Aptos Wallets Queried | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |
| Sources Covered | 3 orgs + 9 users |

---

## GF(3) Color Chain

Rotation: `id%3==0` → trit=0 ERGODIC `#d3869b` | `id%3==1` → trit=+1 PLUS `#b8bb26` | `id%3==2` → trit=-1 MINUS `#cc241d`

Sample of this sweep's increment sequence (203 total):

| ID | Source | Full Name | GF3 | Color |
|----|--------|-----------|-----|-------|
| 1 | plurigrid | plurigrid/asi | PLUS | #b8bb26 |
| 2 | plurigrid | plurigrid/gorj | MINUS | #cc241d |
| 3 | plurigrid | plurigrid/shrimp | ERGODIC | #d3869b |
| … | … | … | … | … |
| 101 | kubeflow | kubeflow/pipelines | PLUS | #b8bb26 |
| 150 | bmorphism | bmorphism/gay-chat | ERGODIC | #d3869b |
| 203 | AustinCStone | AustinCStone/TextGAN | MINUS | #cc241d |

---

## Top Repos by Source (This Sweep — 2026-07-16)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| place | TeX | 1 | 2026-07-14 |
| gorj | Clojure | 1 | 2026-07-16 |
| eirobri | Clojure | 0 | 2026-07-14 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15779 | 2026-07-16 |
| pipelines | Python | 4167 | 2026-07-16 |
| spark-operator | Python | 3137 | 2026-07-16 |
| trainer | Go | 2150 | 2026-07-16 |
| mcp-apache-spark-history-server | Python | 183 | 2026-07-16 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (106 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| penrose-mcp | JavaScript | 9 | 2026-06-24 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| Gay.jl | Julia | 2 | 2026-07-14 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (41 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| byteruckus | HTML | 0 | 2026-07-15 |

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos Snapshotted |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| TeglonLabs | org | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| **TOTAL** | | **400** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-07-16)
Queried: `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on fullnode.mainnet.aptoslabs.com

All 28 wallets (alice, bob, A–Z) returned **0.0 APT** — zero-balance or uninitialised CoinStore accounts on mainnet.

### Multisig Contract Probes
View function: `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

All 5 contracts live, each requiring **2-of-N signatures**.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — site protected by Vercel deployment authentication. `mnx_snapshots` table has 0 rows.

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

## Notable Highlights (2026-07-16 sweep delta)
- **kubeflow/kubeflow**: now 15,779 stars (+207 since last sweep) — still the flagship ML platform for K8s
- **kubeflow/mcp-apache-spark-history-server**: new entry at 183 stars — Apache Spark history server via MCP
- **plurigrid/asi**: now 30 stars (+14) — rapid growth, pushed 2026-07-10
- **plurigrid/gorj**: this very repo, Clojure, pushed 2026-07-16 (today)
- **bmorphism/gay-chat**: newest bmorphism repo (2026-07-14, Scheme) — gay://chat over Spritely Brassica
- **bmorphism/Gay.jl**: 2 stars, 187 open issues, Julia — extremely active
- **wasita/wasita.github.io**: pushed TODAY (2026-07-16) — active development
- **migalkin/NodePiece**: 144 stars — ICLR'22, scalable KG embeddings
- **AustinCStone/byteruckus**: pushed 2026-07-15 — latest AustinCStone activity
- All 5 Hamming multisig contracts healthy (2-of-N each)
