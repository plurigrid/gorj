# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-27

## Sweep Metadata
- **Date:** 2026-04-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 200 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts | 5 (all healthy, 2-of-N) |
| MNX Markets | SPA — data unavailable server-side |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | bmorphism (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | zubyul (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | migalkin (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | AustinCStone (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | DJedamski (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

## Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~5019627342.
No address in the swarm has registered an APT CoinStore on mainnet.

| Range | Balance APT | Status |
|-------|-------------|--------|
| alice (0xc793...) | 0.0 | not_found |
| bob (0x0a3c...) | 0.0 | not_found |
| A–Z (26 addrs) | 0.0 each | not_found |

### Multisig Contract Health

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | **2** | ✓ |
| A-G | 0xf56c4a1c... | **2** | ✓ |
| Y-Z | 0xd3ffe181... | **2** | ✓ |
| S-T | 0x3b1c3ae9... | **2** | ✓ |
| V-W | 0x40fad7b4... | **2** | ✓ |

**5/5 contracts healthy — 2-of-N threshold uniformly enforced.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA (dpl=`dpl_BMQ5avRxvijtT1PNSd4ap9eLZkfS`).
All API probe paths return the SPA HTML shell — no JSON market data exposed server-side.
Market data requires browser JS execution. Recorded as unavailable.

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (2026-04-27 sweep)

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 50 | 44 |
| bmorphism | user | 50 | 119 |
| zubyul | user | 49 | 14 |
| kubeflow | org | 15 | 31,928 |
| AustinCStone | social | 7 | 107 |
| migalkin | social | 7 | 278 |
| wasita | social | 6 | 4 |
| DJedamski | social | 5 | 3 |
| TeglonLabs | org | 4 | 2 |
| kristinezheng | social | 4 | 0 |
| M1shaaa | social | 3 | 0 |
| **TOTAL** | | **200** | **32,499** |

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
- **kubeflow/kubeflow**: 15,606 stars — flagship ML platform for Kubernetes (pushed 2026-04-27)
- **kubeflow/pipelines**: 4,126 stars — most popular ML pipeline (pushed 2026-04-26)
- **kubeflow/spark-operator**: 3,120 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs in TensorFlow
- **plurigrid/asi**: 17 stars — everything is topological chemputer! (pushed 2026-04-26)
- **plurigrid/gorj**: 0 stars (this very repo) — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed 2026-04-27)
- **bmorphism/Gay.jl**: active 2026-04-27 — deterministic gay color system in Julia
