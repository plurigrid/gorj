# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-07

## Sweep Metadata
- **Date:** 2026-07-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 322 |
| Total Repo Snapshots (this run) | 322 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Snapshotted | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-n) |
| MNX Markets | unavailable (Vercel auth required) |

---

## GF(3) Color Chain — Sample (first 12 of 322)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | plurigrid/asi | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |

GF(3) distribution across 322 increments: ~108 ERGODIC · ~107 PLUS · ~107 MINUS

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 28 | 2026-06-29 |
| gorj | Clojure | 0 | 2026-07-07 |
| ontology | JavaScript | 8 | 2025-05-27 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15769 | 2026-07-06 |
| pipelines | Python | 4169 | 2026-07-07 |
| spark-operator | Python | 3132 | 2026-07-02 |
| trainer | Go | 2129 | 2026-07-06 |
| katib | Python | 1690 | 2026-07-07 |

### TeglonLabs (5 public repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| Gay.jl | Julia | 2 |
| shitcoin | Python | 5 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (2026-07-07)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 3 |
| migalkin | user | 6 |
| wasita | user | 4 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 2 |
| M1shaaa | user | 2 |
| DJedamski | user | 2 |
| **TOTAL** | | **322** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-07-07)

Queried via `0x1::coin::balance` view function.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| bob | 0x0a3c...5d | **12.6570** |
| F | 0x18a1...71 | **1.9605** |
| L | 0x7c2e...a9 | **1.9273** |
| J | 0x4d96...54 | **1.8951** |
| alice | 0xc793...7b | 0.4364 |
| K | 0xa732...c4 | 0.1620 |
| O | 0x7325...9d | 0.2101 |
| P | 0x6218...48 | 0.1401 |
| M | 0x6fed...e9 | 0.1123 |
| N | 0xe7dd...2c | 0.1061 |
| Q | 0xac40...a9 | 0.1032 |
| S | 0xb875...86 | 0.0918 |
| R | 0x7ce6...10 | 0.0902 |
| T | 0x3578...88 | 0.0737 |
| U | 0x7586...56 | 0.0558 |
| A | 0x8699...7a | 0.0518 |
| Y | 0xd8e3...c4 | 0.0444 |
| X | 0xa95c...7d | 0.0426 |
| V | 0xb59d...c3 | 0.0488 |
| W | 0x5f32...b0 | 0.0407 |
| B | 0x3f89...13 | 0.0363 |
| Z | 0x7af0...7c | 0.0243 |
| D | 0xf776...d1 | 0.0116 |
| C | 0x38b9...5e | 0.0102 |
| E | 0xdc1d...36 | 0.0094 |
| H | 0xce67...0f | 0.0017 |
| G | 0x69a3...32 | 0.0007 |
| I | 0x070f...c9 | 0.0007 |

**Total swarm:** ~20.00 APT  
**Concentration:** bob holds ~63.3% of swarm total

### Multisig Probes (5/5 healthy)

All contracts return `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — site is protected by Vercel deployment authentication (visitor password required). No market data could be retrieved without credentials.

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
- **kubeflow/kubeflow**: 15,769★ — flagship ML platform for Kubernetes (pushed 2026-07-06)
- **kubeflow/pipelines**: 4,169★ — most starred KF repo (pushed 2026-07-07)
- **migalkin/NodePiece**: 144★ — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92★ — text generation with GANs
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring (1032 open issues)
- **bmorphism/Gay.jl**: Wide-gamut color sampling (187 open issues, pushed 2026-07-07)
- **bob wallet**: 12.657 APT — largest holder in the Hamming swarm (~63% concentration)
- **All 5 multisigs**: healthy with 2-of-n threshold
