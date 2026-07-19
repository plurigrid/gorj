# World-Increment Sweep — 2026-07-19

## Sweep Metadata
- **Date:** 2026-07-19
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments | 12 (IDs 13–24) |
| New Repo Snapshots | 394 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth wall) |
| All-Time Chain Length | 35 |

---

## GF(3) Color Chain — 2026-07-19 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | zubyul (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | migalkin (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | DJedamski (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | wasita (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | kristinezheng (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | M1shaaa (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | AustinCStone (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | bmorphism (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | bmorphism (user) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-19 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15782 | 2026-07-10 |
| pipelines | Python | 4169 | 2026-07-19 |
| spark-operator | Python | 3139 | 2026-07-17 |
| trainer | Go | 2152 | 2026-07-19 |
| katib | Python | 1691 | 2026-07-16 |

### TeglonLabs (5 repos) ⚠️ down from 53 in April sweep
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| risc0-cosmwasm-example | Rust | 23 |
| anti-bullshit-mcp-server | JavaScript | 22 |
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

### AustinCStone (41 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **394** |

---

## Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)
All 28 addresses (alice, bob, A–Z) returned **0.0 APT**.

| World | Address |
|-------|---------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d |
| A–Z | (26 addresses, all 0.0 APT) |

### Multisig Contract Probes (5 pairs)
All 5 contracts healthy — all require 2 signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

### MNX Markets
**Unavailable** — `https://testnet.mnx.fi` is behind a Vercel authentication wall (password-protected deployment). `mnx_snapshots` table is empty for this sweep.

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
- **kubeflow/kubeflow**: 15,782 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars — pushed 2026-07-19 (active)
- **kubeflow/spark-operator**: 3,139 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **plurigrid/asi**: 31 stars — topological chemputer (pushed 2026-07-10)
- **bmorphism/Gay.jl**: 2★, **187 open issues** — wide-gamut color sampling with splittable determinism
- **TeglonLabs**: repo count dropped **53 → 5** since April 2026 sweep (48 repos no longer visible)
- **Increment 24**: ERGODIC — sweep_complete closing the 8th full GF(3) cycle
- **All Aptos addresses**: 0.0 APT (swarm not yet funded)
- **All multisigs**: healthy, 2-of-N threshold across all 5 pairs
