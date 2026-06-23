# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-23

## Sweep Metadata
- **Date:** 2026-06-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 49 |
| Total Repo Snapshots | 49 (representative selection) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Market Data | Unavailable (Vercel auth gate) |

---

## GF(3) Color Chain — 49 Increments (2026-06-23)

GF(3) assignment: `id%3==0` → ERGODIC #d3869b · `id%3==1` → PLUS #b8bb26 · `id%3==2` → MINUS #cc241d

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 16 |
| +1 | PLUS | `#b8bb26` | 17 |
| -1 | MINUS | `#cc241d` | 16 |

Chain runs from id=1 (plurigrid/asi, PLUS) through id=49 (M1shaaa/lab-bookshelf-, PLUS), covering 16 complete GF(3) triples + 1 leading PLUS.

---

## Top Repos by Source (2026-06-23 Snapshot)

### plurigrid (100 repos)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| gorj | Clojure | 0 | **752** | 2026-06-22 |
| place | TeX | 1 | 9 | 2026-06-20 |
| asi | HTML | 26 | 4 | 2026-06-10 |
| eirobri | Clojure | 0 | 29 | 2026-06-03 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,740 | 2026-06-18 |
| pipelines | Python | 4,157 | 2026-06-22 |
| spark-operator | Python | 3,128 | 2026-06-22 |
| trainer | Go | 2,118 | 2026-06-22 |
| katib | Python | 1,685 | 2026-06-22 |
| mcp-apache-spark-history-server | Python | 178 | 2026-06-22 (**NEW**) |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 (newest) |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (100 repos)
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| Gay.jl | Julia | 2 | **187** | 2026-06-22 |
| satreadout | HTML | 0 | 0 | 2026-06-20 |
| ocaml-mcp-sdk | OCaml | 61 | 0 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 1 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 3 | 2025-01-07 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| NBFNet_mlx | Python | 10 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StructureFromMotion | Python | 1 |
| EpsteinSearch | Python | 0 | (pushed 2026-02-11) |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| AustinCStone | user | 30 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **381** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 2026-06-23
Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result: All 28 wallets show 0.0 APT** — CoinStore resource not found on mainnet for any address. Accounts are likely testnet-only or unfunded.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | 26 addresses | 0.0 each |

### Multisig Contract Probes — 2026-06-23
All probed via `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 contracts healthy** — all configured as 2-of-N multisig.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — all endpoints return Vercel authentication gate (401). No market data could be retrieved. `mnx_snapshots` table remains empty.

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

## Notable Highlights — 2026-06-23
- **plurigrid/gorj**: 752 open issues — this very repo, very active, pushed yesterday
- **bmorphism/Gay.jl**: 187 open issues needs attention — wide-gamut GF(3) color engine
- **kubeflow/kubeflow**: 15,740 stars — flagship ML platform, pushed 2026-06-18
- **kubeflow/pipelines**: 4,157 stars, 448 open issues — pushed 2026-06-22
- **kubeflow/mcp-apache-spark-history-server**: new (178★) MCP server for Spark debugging
- **TeglonLabs/jank-crane**: new C++ repo (June 2026) — GF3 convergence maps
- **migalkin/NodePiece**: 144 stars — compositional KG embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation GAN (2016, still referenced)
- All 5 Aptos multisig contracts (A-B, A-G, Y-Z, S-T, V-W) are healthy, requiring 2 signatures
