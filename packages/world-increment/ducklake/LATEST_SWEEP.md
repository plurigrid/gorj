# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-07

## Sweep Metadata
- **Date:** 2026-07-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger:** v6,166,066,056 (epoch 16453, block 883,169,558)

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 76 |
| Total Repo Snapshots | 76 |
| Sources Covered | 3 orgs + 8 users |

### Repo Counts by Source

| Source | Type | Repos Snapped |
|--------|------|--------------|
| plurigrid | org | 20 |
| kubeflow | org | 13 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 8 |
| migalkin | social graph | 5 |
| wasita | social graph | 3 |
| AustinCStone | social graph | 4 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 2 |
| DJedamski | social graph | 2 |
| **TOTAL** | | **76** |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 25 |
| +1 | PLUS | `#b8bb26` | 26 |
| -1 | MINUS | `#cc241d` | 25 |

Chain rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

### Top Repos by Source

#### plurigrid (20 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-07-07 |
| place | TeX | 1 | 2026-07-07 |
| asi | HTML | 30 | 2026-06-29 |
| eirobri | Clojure | 0 | 2026-06-30 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |

#### kubeflow (13 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,769 | 2026-07-07 |
| pipelines | Python | 4,169 | 2026-07-07 |
| spark-operator | Python | 3,133 | 2026-07-07 |
| trainer | Go | 2,130 | 2026-07-07 |
| katib | Python | 1,690 | 2026-07-06 |

#### bmorphism (10 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

#### migalkin (5 repos, KG researcher)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

#### AustinCStone (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Chain status:** Live — ledger v6,166,066,056 (epoch 16453)

All 28 wallets (alice, bob, A–Z) probed 2026-07-07. All return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — **no accounts are funded on mainnet** (0.0 APT each).

### Multisig Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — behind Vercel deployment authentication. No bypass token available. No market data this sweep. `mnx_snapshots` table is empty (0 rows).

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
- **kubeflow/kubeflow**: 15,769 stars (+204 since Apr sweep) — flagship ML platform
- **kubeflow/pipelines**: 4,169 stars (+50) — pushed 2026-07-07
- **kubeflow/spark-operator**: 3,133 stars (+22) — pushed 2026-07-07
- **migalkin/NodePiece**: 144 stars (+1) — scalable KG embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1) — OCaml SDK for MCP
- **AustinCStone/TextGAN**: 92 stars — text generation GANs
- **plurigrid/gorj**: 1 star, 1044 open issues — this repo; pushed 2026-07-07
- **plurigrid/asi**: 30 stars — topological chemputer
- **Hamming swarm**: All 28 addresses unfunded; all 5 multisigs healthy (2-of-N)
