# World-Increment Sweep — 2026-06-12

## Sweep Metadata
- **Date:** 2026-06-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-06-12-2106`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this sweep) | 11 |
| Total World Increments (all time) | 34 |
| New Repo Snapshots (this sweep) | 253 |
| Total Repo Snapshots (all time) | 1,197 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Testnet | unavailable (Vercel auth gate) |

---

## GF(3) Color Chain — This Sweep (Increments 13–23)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|----------|-------|------|
| 13 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | 48 | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | 30 | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | 21 | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 9 | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | 11 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | 10 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

(Continues from sweep 2026-04-12 which closed at increment 12 ERGODIC)

---

## Top Repos by Source (This Sweep)

### plurigrid (100 repos, top stars: 26)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ontology | JavaScript | 26 | recent |
| asi | HTML | 16 | recent |
| zig-syrup | Zig | 2 | 2026-03-28 |
| vivarium | Clojure | 1 | recent |
| gorj | Clojure | — | active |

### kubeflow (48 repos, top stars: 15,719)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,719 | recent |
| pipelines | Python | 4,119+ | active |
| spark-operator | Python | 3,111+ | active |
| trainer | Go | 2,080+ | active |
| katib | Python | 1,676+ | active |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| jank-crane | C++ | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (30 repos sampled, top stars: 61)
| Repo | Language | Stars |
|------|----------|-------|
| anti-bullshit-mcp-server | JavaScript | 23 |
| risc0-cosmwasm-example | Rust | 23 |
| babashka-mcp-server | JavaScript | 19 |
| say-mcp-server | JavaScript | 20 |
| ocaml-mcp-sdk | OCaml | 61 |
| satreadout | Lean | 0 (newest, 2026-06-10) |

### migalkin (9 repos, top stars: 144)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| RWL | Python | 8 |
| NBFNet_mlx | Python | 10 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (10 repos, top stars: 92)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (This Sweep)

| Source | Type | Repos | Top Stars |
|--------|------|-------|-----------|
| plurigrid | org | 100 | 26 |
| kubeflow | org | 48 | 15,719 |
| bmorphism | user | 30 | 61 |
| zubyul | user | 21 | 2 |
| wasita | user | 11 | 2 |
| AustinCStone | user | 10 | 92 |
| migalkin | user | 9 | 144 |
| M1shaaa | user | 8 | 0 |
| DJedamski | user | 6 | 1 |
| TeglonLabs | org | 5 | 2 |
| kristinezheng | user | 5 | 0 |
| **SWEEP TOTAL** | | **253** | |
| **ALL-TIME TOTAL** | | **1,197** | |

---

## JOB 2: Hamming Swarm Snapshot (Aptos)

### Wallet Balances — 28 Addresses
All 28 Hamming-swarm wallets probed against Aptos mainnet (ledger ~v5705263303).

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793ac... | 0.000000 | no CoinStore |
| bob | 0x0a3c00... | 0.000000 | no CoinStore |
| A | 0x8699ed... | 0.000000 | no CoinStore |
| B | 0x3f892e... | 0.000000 | no CoinStore |
| C | 0x38b99e... | 0.000000 | no CoinStore |
| D | 0xf77656... | 0.000000 | no CoinStore |
| E | 0xdc1d9d... | 0.000000 | no CoinStore |
| F | 0x18a14b... | 0.000000 | no CoinStore |
| G | 0x69a394... | 0.000000 | no CoinStore |
| H | 0xce67c3... | 0.000000 | no CoinStore |
| I | 0x070fe5... | 0.000000 | no CoinStore |
| J | 0x4d964d... | 0.000000 | no CoinStore |
| K | 0xa73204... | 0.000000 | no CoinStore |
| L | 0x7c2eae... | 0.000000 | no CoinStore |
| M | 0x6fed37... | 0.000000 | no CoinStore |
| N | 0xe7dde6... | 0.000000 | no CoinStore |
| O | 0x73252b... | 0.000000 | no CoinStore |
| P | 0x621879... | 0.000000 | no CoinStore |
| Q | 0xac40fa... | 0.000000 | no CoinStore |
| R | 0x7ce605... | 0.000000 | no CoinStore |
| S | 0xb87530... | 0.000000 | no CoinStore |
| T | 0x35781d... | 0.000000 | no CoinStore |
| U | 0x758600... | 0.000000 | no CoinStore |
| V | 0xb59dd8... | 0.000000 | no CoinStore |
| W | 0x5f32ae... | 0.000000 | no CoinStore |
| X | 0xa95cbb... | 0.000000 | no CoinStore |
| Y | 0xd8e328... | 0.000000 | no CoinStore |
| Z | 0x7af0ef... | 0.000000 | no CoinStore |

> **Note:** All 28 addresses lack a `CoinStore<AptosCoin>` resource — wallets exist on-chain but have never received APT on mainnet, or have not been initialized.

**Total APT held by swarm: 0.000000 APT**

---

### Multisig Contract Probes (5 contracts)

All 5 multisig accounts are **healthy** — 2-of-N threshold each.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

All pairs use 2-of-N multisig signing — threshold satisfied, no degraded contracts detected.

---

### MNX Testnet Markets

**Status: UNAVAILABLE**
- `https://testnet.mnx.fi/api/markets` — Vercel auth gate (HTML, not JSON)
- `https://testnet.mnx.fi/api/v1/markets` — Same
- The frontend is a SPA behind authentication; no market data extractable without credentials.

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

---

## Notable Highlights

- **kubeflow/kubeflow**: 15,719 stars — flagship ML platform remains most-starred in sweep
- **migalkin/NodePiece**: 144 stars — ICLR'22 knowledge graph embeddings, still growing
- **migalkin/StarE**: 89 stars — EMNLP 2020 hyper-relational KG
- **AustinCStone/TextGAN**: 92 stars — TensorFlow GAN for text generation
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **bmorphism/satreadout**: newest repo (2026-06-10) — Lean 4.28 + mathlib machine-checked saturating perceptual readout
- **zubyul/tilelang-kernels**: TileLang GPU kernels for GF(3) trit classification on NVIDIA Blackwell
- **TeglonLabs/jank-crane**: newest TeglonLabs repo (2026-06-08) — crane-jank converged-IR hub with GF3 maps
- **Hamming swarm**: All 28 wallet addresses probed — 0 APT on mainnet, 5/5 multisigs healthy at threshold=2
- **GF(3) cycle**: Increments 13–23 complete 3 full PLUS→MINUS→ERGODIC cycles + 2 more
