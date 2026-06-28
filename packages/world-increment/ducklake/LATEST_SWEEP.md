# World-Increment Sweep — 2026-06-28

## Sweep Metadata
- **Date:** 2026-06-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger version:** 5975508784

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 347 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel protection) |

---

## GF(3) Color Chain — 11 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | 48 | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 7 | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | 11 | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | 8 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (100 repos, pushed today: gorj + asi + place)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-28 |
| gorj | Clojure | 0 | 2026-06-28 |
| place | TeX | 1 | 2026-06-27 |
| eirobri | Clojure | 0 | 2026-06-23 |
| nash-portal | Rust | 2 | 2026-05-19 |
| ontology | JavaScript | 8 | 2025-05-27 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| asi-skills | Julia | 3 | 2026-04-26 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,749 | 2026-06-18 |
| pipelines | Python | 4,158 | 2026-06-27 |
| spark-operator | Python | 3,129 | 2026-06-26 |
| trainer | Go | 2,125 | 2026-06-26 |
| katib | Python | 1,687 | 2026-06-23 |
| examples | Jsonnet | 1,460 | 2025-04-14 |
| arena | Go | 814 | 2026-06-26 |
| kale | Python | 694 | 2026-06-25 |
| mpi-operator | Go | 528 | 2026-06-25 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| Gay.jl | Julia | 2 | 2026-06-28 |
| world | Python | 0 | 2026-06-02 |
| satreadout | HTML | 0 | 2026-06-20 |
| bci-preview | HTML | 0 | 2026-06-20 |

### migalkin (7 repos, knowledge graph researcher)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

### wasita (11 repos, network science / Svelte dev)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| wasita.github.io | Svelte | 1 | 2026-06-25 |
| magic-garden | Python | 2 | 2026-04-22 |
| proj-template | — | 0 | 2026-06-19 |

### AustinCStone (8 repos, ML engineer)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Hamming Swarm: Aptos Wallets

**Ledger:** mainnet v5975508784 (block 861594885, epoch 16337)

All 28 addresses (alice, bob, A–Z) queried for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
All returned `resource_not_found` — accounts active on chain but no registered APT CoinStore.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…fdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…f71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…fc9 | 0.0 |
| J | 0x4d96…f54 | 0.0 |
| K | 0xa732…dc4 | 0.0 |
| L | 0x7c2e…ba9 | 0.0 |
| M | 0x6fed…f2e9 | 0.0 |
| N | 0xe7dd…1b2c | 0.0 |
| O | 0x7325…a89d | 0.0 |
| P | 0x6218…c948 | 0.0 |
| Q | 0xac40…c89a9 | 0.0 |
| R | 0x7ce6…e10 | 0.0 |
| S | 0xb875…0386 | 0.0 |
| T | 0x3578…f588 | 0.0 |
| U | 0x7586…f956 | 0.0 |
| V | 0xb59d…f2c3 | 0.0 |
| W | 0x5f32…c7b0 | 0.0 |
| X | 0xa95c…047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…97c | 0.0 |

---

## Hamming Swarm: Multisig Contracts

All 5 probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — each requires 2-of-N signatures.**

---

## MNX Markets
Status: **Unavailable** — `testnet.mnx.fi` is behind Vercel deployment protection; no market data accessible without bypass token.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC

## Notable Highlights
- **kubeflow/kubeflow**: 15,749 stars — flagship ML platform for Kubernetes (15K+!)
- **kubeflow/pipelines**: 4,158 stars — pushed 2026-06-27 (active!)
- **kubeflow/spark-operator**: 3,129 stars — Kubernetes Spark operator
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (TensorFlow)
- **plurigrid/asi**: 26 stars — topological chemputer (pushed TODAY 2026-06-28)
- **bmorphism/Gay.jl**: active today — wide-gamut color sampling with splittable determinism
- **All multisig 2-of-N**: A-B, A-G, Y-Z, S-T, V-W all healthy
