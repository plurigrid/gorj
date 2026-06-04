# World-Increment Sweep — 2026-05-03

## Sweep Metadata
- **Date:** 2026-05-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-05-03-2227`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 12 (IDs 13–24) |
| New Repo Snapshots (this run) | 350 |
| Total World Increments (cumulative) | 24+ |
| Total Repo Snapshots (cumulative) | 1,294 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Market Data | Unavailable (SPA, no API) |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — This Run (IDs 13–24)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|----------|-------|------|
| 13 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | bmorphism (closing) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source (This Sweep)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 17 | 2026-04-26 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| StochFlow | Python | 4 | 2024-03-20 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 1 | 2026-04-26 |
| gorj | Clojure | 0 | 2026-05-03 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,619 | 2026-04-29 |
| pipelines | Python | 4,131 | 2026-05-01 |
| spark-operator | Python | 3,123 | 2026-04-28 |
| trainer | Go | 2,096 | 2026-05-01 |
| katib | Python | 1,681 | 2026-04-14 |
| manifests | YAML | 1,014 | 2026-04-30 |
| arena | Go | 810 | 2026-04-28 |
| kale | Python | 684 | 2026-04-30 |
| mpi-operator | Go | 524 | 2026-04-14 |

### TeglonLabs (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (101 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |
| Gay.jl | Julia | 1 |

### zubyul (49 repos)
| Repo | Language | Stars |
|------|----------|-------|
| gay-world | Python | 1 |
| zubyul.github.io | CSS | 1 |
| cascade-world | Python | 1 |
| defcon | JavaScript | 1 |
| ghostty-modifications | JavaScript | 1 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 7 |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (This Run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 101 |
| zubyul | user | 49 |
| kubeflow | org | 47 |
| AustinCStone | user | 10 |
| wasita | user | 10 |
| migalkin | user | 10 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 6 |
| TeglonLabs | org | 4 |
| **TOTAL (this run)** | | **351** |

---

## Hamming Swarm Snapshot — Aptos Mainnet

Queried 28 addresses on Aptos mainnet (`fullnode.mainnet.aptoslabs.com/v1`).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...12d5 | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...35e | 0.00000000 |
| D | 0xf776...dd1 | 0.00000000 |
| E | 0xdc1d...d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...00f | 0.00000000 |
| I | 0x070f...c9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...e9 | 0.00000000 |
| N | 0xe7dd...b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...a9 | 0.00000000 |
| R | 0x7ce6...e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...2c3 | 0.00000000 |
| W | 0x5f32...7b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...4c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

All 28 addresses returned **0.00000000 APT** — accounts either unregistered on-chain or empty CoinStore.

---

## Multisig Contract Probes

All 5 contracts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | **2** | ✓ |
| A-G | 0xf56c...096 | **2** | ✓ |
| Y-Z | 0xd3ff...883 | **2** | ✓ |
| S-T | 0x3b1c...883 | **2** | ✓ |
| V-W | 0x40fa...b6d | **2** | ✓ |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures.

---

## MNX Market Data

`https://testnet.mnx.fi` is a **Next.js SPA** with client-side rendering only. No REST API endpoints available at `/api/markets` or `/api/v1/markets` — both return the HTML shell. Market data is **unavailable** from server-side probing; would require a headless browser to execute JavaScript.

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

### GitHub Social Graph
- **kubeflow/kubeflow**: 15,619 stars — flagship ML platform for Kubernetes (up from 15,565 on 2026-04-12)
- **kubeflow/pipelines**: 4,131 stars — most active, pushed 2026-05-01
- **kubeflow/spark-operator**: 3,123 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 143 stars — scalable KG embeddings (ICLR'22)
- **migalkin/StarE**: 89 stars — EMNLP 2020 hyper-relational KG
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK using oxcaml_effect
- **bmorphism/Gay.jl**: actively maintained — GF(3) deterministic color engine with 187 open issues
- **bmorphism/anti-bullshit-mcp-server**: 23 stars — MCP for claim validation
- **plurigrid/gorj**: 0 stars, 53 open issues — this very repo, pushed 2026-05-03

### Aptos Hamming Swarm
- All 28 wallets (alice, bob, A–Z) report **0 APT** balance — consistent with test/unregistered state
- All 5 multisig contracts respond correctly with **sigs_required=2**
- Swarm topology: symmetric 2-of-N multisig pairing across the alphabet

### Increment 24: ERGODIC — sweep_complete closing the 4th GF(3) cycle of this run
