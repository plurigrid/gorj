# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-05

## Sweep Metadata
- **Date:** 2026-06-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 225 |
| Total Repo Snapshots | 225 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — Distribution (225 increments)

| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | `#d3869b` (trit=0) | 75 |
| PLUS | `#b8bb26` (trit=1) | 75 |
| MINUS | `#cc241d` (trit=2) | 75 |

Rule: `id mod 3 == 0` → ERGODIC | `id mod 3 == 1` → PLUS | `id mod 3 == 2` → MINUS

---

## Top Repos by Source

### plurigrid (50 repos — most recently pushed)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-06-05 |
| place | TeX | 1 | 2026-06-04 |
| eirobri | Clojure | 0 | 2026-06-03 |
| nash-portal | Rust | 2 | 2026-05-19 |
| asi | HTML | 25 | 2026-04-26 |
| asi-skills | Julia | 3 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-30 |

### kubeflow (48 repos — top by stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,706 | 2026-05-24 |
| pipelines | Python | 4,152 | 2026-06-05 |
| spark-operator | Python | 3,125 | 2026-06-04 |
| trainer | Go | 2,111 | 2026-06-05 |
| katib | Python | 1,684 | 2026-06-04 |

### TeglonLabs (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (50 repos — top by stars)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| hypernym-mcp-server | — | 6 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

### AustinCStone (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |
| EpsteinSearch | Python | 0 |

---

## Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 48 | 34,174 |
| plurigrid | org | 50 | 51 |
| bmorphism | user | 50 | 121 |
| zubyul | user | 49 | 14 |
| migalkin | user | 5 | 276 |
| wasita | user | 5 | 4 |
| TeglonLabs | org | 4 | 2 |
| DJedamski | user | 4 | 3 |
| AustinCStone | user | 4 | 106 |
| kristinezheng | user | 3 | 0 |
| M1shaaa | user | 3 | 0 |
| **TOTAL** | | **225** | **34,751** |

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice/bob)

All 28 addresses queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All returned **0.0 APT** — no liquid APT in the coin store at time of snapshot.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793…cc7b | 0.0 APT |
| bob | 0x0a3c…512d | 0.0 APT |
| A–Z | (26 addresses) | 0.0 APT each |

### Multisig Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…003 | 2 | HEALTHY |
| A-G | 0xf56c…096 | 2 | HEALTHY |
| Y-Z | 0xd3ff…883 | 2 | HEALTHY |
| S-T | 0x3b1c…883 | 2 | HEALTHY |
| V-W | 0x40fa…b6d | 2 | HEALTHY |

All multisigs require 2 signatures. All 5 are healthy.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — All paths behind Vercel auth gate. No market data extracted.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,706 stars — flagship ML platform for Kubernetes (active 2026-05-24)
- **kubeflow/pipelines**: 4,152 stars — pushed 2026-06-05 (today!)
- **migalkin/NodePiece**: 144 stars — compositional KG representations (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — GAN text generation
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **All 5 multisigs**: 2-of-N, all healthy — Hamming swarm pairs A-B, A-G, Y-Z, S-T, V-W
