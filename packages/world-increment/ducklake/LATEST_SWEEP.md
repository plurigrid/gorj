# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 (101 total) |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (105 total) |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 11 |
| AustinCStone | user (social graph) | 40 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |

### Top Repos by Stars (2026-06-26 snapshot)

#### kubeflow (flagship ML platform)
| Repo | Language | Stars | Forks | Open Issues | Pushed |
|------|----------|-------|-------|-------------|--------|
| kubeflow/kubeflow | — | 15,744 | 2,680 | 0 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,156 | 2,009 | 457 | 2026-06-25 |
| kubeflow/spark-operator | Python | 3,128 | 1,492 | 100 | 2026-06-26 |
| kubeflow/trainer | Go | 2,122 | 972 | 127 | 2026-06-25 |
| kubeflow/community-distribution | YAML | 1,028 | 1,065 | 22 | 2026-06-25 |
| kubeflow/katib | Python | 1,685 | 527 | 111 | 2026-06-23 |
| kubeflow/sdk | Python | 121 | 181 | 136 | 2026-06-26 |

#### plurigrid
| Repo | Language | Stars | Open Issues | Pushed | Notes |
|------|----------|-------|-------------|--------|-------|
| plurigrid/asi | HTML | 26 | 4 | 2026-06-26 | "everything is topological chemputer!" |
| plurigrid/ontology | JavaScript | 8 | 16 | 2025-05-27 | "autopoietic ergodicity" |
| plurigrid/vcg-auction | Rust | 7 | 1 | 2023-03-16 | VCG auction contract |
| plurigrid/agent | Python | 5 | 6 | 2023-03-31 | Agency amplification framework |
| plurigrid/gorj | Clojure | 0 | **827** | 2026-06-26 | This repo — forj + Rama + GF(3) |
| plurigrid/eirobri | Clojure | 0 | 30 | 2026-06-23 | EiRoBri replay world |
| plurigrid/nanoclj-zig | Zig | 1 | 20 | 2026-04-25 | NaN-boxed Clojure in Zig 0.15 |

#### bmorphism
| Repo | Language | Stars | Open Issues | Pushed |
|------|----------|-------|-------------|--------|
| bmorphism/Gay.jl | Julia | 2 | **187** | 2026-06-26 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 0 | 2026-03-16 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 1 | 2022-10-20 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 1 | 2026-01-16 |
| bmorphism/say-mcp-server | JavaScript | 20 | 3 | 2025-01-07 |
| bmorphism/babashka-mcp-server | JavaScript | 19 | 3 | 2025-01-05 |

#### TeglonLabs
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| TeglonLabs/topoi | Python | 0 | 2025-01-24 |
| TeglonLabs/coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

#### Social Graph Highlights
| Repo | Language | Stars | Pushed | Notes |
|------|----------|-------|--------|-------|
| migalkin/NodePiece | Python | 144 | 2026-05-07 | KG embedding ICLR'22 |
| migalkin/StarE | Python | 89 | 2026-04-16 | Hyper-relational KG EMNLP'20 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 | TF text generation GAN |
| AustinCStone/StereoVisionMRF | Python | 11 | 2026-04-01 | MRF stereo depth |
| wasita/magic-garden | Python | 2 | 2026-04-22 | Discord magic garden bot |
| zubyul/WGCNA | HTML | 2 | 2023-07-05 | Gene correlation network analysis |
| zubyul/gay-world | Python | 1 | 2026-03-26 | Goblin world builder w/ MLX |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 Hamming swarm addresses)

Queried: `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on mainnet Aptos fullnode.  
**Result:** All 28 addresses returned no APT CoinStore — balance 0.0 APT for all.

These addresses likely hold Move resources other than native APT, or are contract/multisig accounts without initialized coin stores.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5 pairs)

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.  
**All 5 multisig contracts are live and healthy, requiring exactly 2 signatures.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Protected by Vercel deployment authentication (password-required SPA). No market data accessible without bypass token. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Schema Summary

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

## GF(3) Color Chain Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

GF(3) chain for 12-unit cycle: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`
