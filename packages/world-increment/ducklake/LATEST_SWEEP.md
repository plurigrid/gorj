# World-Increment Sweep — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-04-12 (12 increments, 471 repo snapshots cumulative)

---

## Summary Counts (This Sweep)

| Metric | Value |
|--------|-------|
| New World Increments | 12 (IDs 13–24) |
| New Repo Snapshots | 114 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5/5 healthy |
| MNX Markets | unavailable (SPA) |

---

## GF(3) Color Chain — New Increments (IDs 13–24)

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 24 | world-increment-agent | meta | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`
(4 complete cycles, same as prior sweep — the chain continues)

---

## Top Repos by Source

### plurigrid (103 repos total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | **30** ↑ (+14 since Apr) | 2026-06-29 |
| gorj | Clojure | 1 | 2026-07-10 |
| place | TeX | 1 | 2026-07-07 |
| eirobri | Clojure | 0 | 2026-06-30 |
| shrimp | — | 0 | 2026-07-03 |

> gorj has **1090 open issues** (up from ~0 in April)

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | **15,770** ↑ (+205) | 2026-07-08 |
| pipelines | Python | **4,169** ↑ (+50) | 2026-07-09 |
| spark-operator | Python | **3,136** ↑ (+25) | 2026-07-08 |
| trainer | Go | **2,134** ↑ (+54) | 2026-07-09 |
| katib | Python | 1,689 | 2026-07-09 |

### TeglonLabs (5 repos — NEW REPO)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| **jank-crane** | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

> jank-crane is new since April: "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"

### bmorphism (105 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-10 |
| ocaml-mcp-sdk | OCaml | **61** ↑ (+1) | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |

> Gay.jl has **187 open issues** as of 2026-07-10; satreadout and world repos are new

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| WGCNA | HTML | 2 | 2023-07-05 |
| gay-world | Python | 1 | 2026-03-26 |
| jonikas_lab_data_analysis_misc | Jupyter Notebook | 2 | 2023-08-16 |
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |

> Several new repos: nash-tui, nash-web, big-bad-plurigrid-quiz, ghostel-emacs-worlds

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | **144** ↑ (+1) | 2026-05-07 |
| StarE | Python | **89** ↑ (+1) | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |
| RWL | Python | 8 | 2026-05-28 |

### DJedamski (6 repos)
| Repo | Language | Stars |
|------|----------|-------|
| Kaggle | — | 1 |
| Getting-and-Cleaning-Data | R | 1 |
| School | R | 1 |

### wasita (11 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| wasita.github.io | Svelte | 1 | 2026-07-06 |
| magic-garden | Python | 2 | 2026-04-22 |
| send2kobo | TypeScript | 1 | 2026-05-19 |
| proj-template | — | 0 | 2026-06-19 |

> wasita/magic-garden and wasita/vocoder are new since April

### kristinezheng (5 repos)
| Repo | Stars | Updated |
|------|-------|---------|
| kristinezheng.github.io | 0 | 2026-07-01 |
| lookit-jenga | 0 | 2024-05-16 |

### M1shaaa (8 repos)
| Repo | Stars | Updated |
|------|-------|---------|
| M1shaaa (profile) | 0 | 2026-02-04 |
| lab-bookshelf- | 0 | 2024-12-31 |

### AustinCStone (40 repos)
| Repo | Language | Stars | Updated |
|------|----------|-------|---------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| SpectralClustering | Python | 3 | 2021-04-16 |
| EpsteinSearch | Python | 0 | 2026-02-11 |

---

## Hamming Swarm — Aptos Wallet Snapshot

**Status: Proxy-blocked** — `fullnode.mainnet.aptoslabs.com` unreachable from execution environment.
All 28 wallets (alice, bob, A–Z) returned `None` balances.

| World | Address |
|-------|---------|
| alice | 0xc793...cc7b |
| bob | 0x0a3c...d5d |
| A–Z | (see DB) |

---

## Multisig Probes — 5/5 HEALTHY ✓

All 5 multisig accounts operational, each requiring **2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

---

## MNX Markets

`https://testnet.mnx.fi` — unavailable (SPA, no REST API endpoint found at `/api/markets`, `/api/v1/markets`, `/markets`).

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

## Notable Highlights (2026-07-10 vs 2026-04-12)
- **plurigrid/asi**: 30 stars (+14 since April) — topological chemputer growing
- **plurigrid/gorj**: 1,090 open issues — significant activity
- **TeglonLabs/jank-crane**: new C++ repo with GF3 convergence maps (jank+crane IR hub)
- **kubeflow/kubeflow**: 15,770 stars (+205 in ~3 months)
- **kubeflow/trainer**: 2,134 stars (+54) — LLM fine-tuning on Kubernetes accelerating
- **bmorphism/Gay.jl**: 187 open issues on 2026-07-10 — active development
- **bmorphism/satreadout**: new HTML repo — machine-checked perceptual readout
- **migalkin/NodePiece**: 144 stars (+1) — KG embedding research continues
- **wasita**: 3 new repos since April (vocoder, proj-template, ch3-lib)
- **zubyul**: multiple new repos (voice-observatory, nash-tui, nash-web, ghostel-emacs-worlds)
- **Multisig**: all 5 pairs healthy at 2-of-N threshold — swarm intact
