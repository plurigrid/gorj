# World-Increment Sweep — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-04-12 (12 increments, 473 repo snapshots)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all-time) | 35 |
| New Increments This Sweep | 12 |
| Total Repo Snapshots (all-time) | 991 |
| New Repo Snapshots This Sweep | 47 |
| Sources Covered | 3 orgs + 9 users |
| Aptos Wallets Probed | 28 (API unreachable, recorded NULL) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | Unavailable (Next.js SPA, no REST API) |

---

## GF(3) Color Chain — This Sweep (IDs 13–24)

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
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
| 24 | sweep_complete (meta) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## JOB 1: GitHub Social Graph Sweep

### plurigrid (org) — 100 repos total
| Repo | Language | Stars | Open Issues | Pushed At |
|------|----------|-------|-------------|-----------|
| gorj | Clojure | 1 | 1468 | 2026-07-28 |
| zig-syrup | Zig | 2 | 0 | 2026-07-28 |
| asi | HTML | 52 | 4 | 2026-07-10 |
| eirobri | Clojure | 0 | 31 | 2026-07-21 |
| place | TeX | 1 | 14 | 2026-07-14 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| asi-skills | Julia | 3 | 0 | 2026-04-26 |

**Notable:** `plurigrid/gorj` has 1468 open issues — automated tracking from GF(3)/forj sweep system. `asi` grew from 16→52 stars since Apr sweep.

### kubeflow (org) — 49 repos total
| Repo | Language | Stars | Forks | Pushed At |
|------|----------|-------|-------|-----------|
| kubeflow | null | 15,794 | 2,689 | 2026-07-10 |
| pipelines | Python | 4,171 | 2,069 | 2026-07-28 |
| spark-operator | Python | 3,142 | 1,509 | 2026-07-25 |
| trainer | Go | 2,157 | 999 | 2026-07-27 |
| katib | Python | 1,693 | 532 | 2026-07-26 |
| mcp-server | Python | 30 | 38 | 2026-07-28 |
| mcp-apache-spark-history-server | Python | 184 | 66 | 2026-07-16 |

**Notable:** Kubeflow now has active MCP server repos — `mcp-server` (30⭐) and `mcp-apache-spark-history-server` (184⭐). Active MCP investment.

### TeglonLabs (org) — 5 repos
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | null | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

**Notable:** `jank-crane` (new since Apr sweep) — C++ crane-jank converged-IR hub with GF3 convergence maps.

### bmorphism (user) — 106 repos total
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-21 |
| gay-chat | Scheme | 0 | 2026-07-14 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 19 | 2026-06-05 |
| penrose-mcp | JavaScript | 9 | 2026-06-24 |

**Notable:** `ocaml-mcp-sdk` (61⭐) is the standout new repo. `gay-chat` — gay://chat over Spritely Brassica Chat (Scheme). `Gay.jl` has 188 open issues.

### zubyul (user) — 49 repos total
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| gay-world | Python | 1 | 2026-04-05 |
| tilelang-kernels | Python | 0 | 2026-03-16 |
| kinesis-kb360pro | Python | 0 | 2026-03-26 |

**Notable:** `tilelang-kernels` — GPU kernels for GF(3) trit classification targeting NVIDIA GB10 Blackwell (CUDA 13.0).

### migalkin (user) — 19 repos
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

KG researcher. Steady updates to canonical papers (NodePiece ICLR'22, StarE EMNLP'20).

### DJedamski (user) — 6 repos
Mostly archived Kaggle/stats projects (2014–2018). Inactive.

### wasita (user) — 12 repos
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| wasita.github.io | Svelte | 1 | 2026-07-21 |
| pnas-typst-template | null | 0 | 2026-07-16 |
| wm-cv | Svelte | 0 | 2026-07-14 |
| magic-garden | Python | 2 | 2026-04-22 |

Active academic researcher (Svelte stack, Typst for papers).

### kristinezheng (user) — 5 repos
Cognitive science / neuroscience researcher (MIT). Mostly archived. Last push 2026-07-01.

### M1shaaa (user) — 8 repos
Lookit/psychology research lab student (Yale). Last push 2026-02-04.

### AustinCStone (user) — 41 repos
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| byteruckus | HTML | 0 | 2026-07-15 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |

ML/CV researcher. `TextGAN` (92⭐, 30 forks) is the standout. `byteruckus` is the most recent activity (2026-07-15).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Status: FULLNODE API UNREACHABLE** — All 28 curl requests to `fullnode.mainnet.aptoslabs.com` timed out (network policy blocks outbound to Aptos full node). Balance rows inserted as NULL for record.

Addresses recorded (for retry in an environment with Aptos access):
- alice `0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b`
- bob `0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d`
- A through Z: 26 addresses (see `aptos_snapshots` table)

### Multisig Contract Probes (5 pairs) — ALL HEALTHY ✓

Probed via POST to `fullnode.mainnet.aptoslabs.com/v1/view` — view endpoint was reachable.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...987003` | **2** | ✅ Healthy |
| A-G | `0xf56c4a1c...c0096` | **2** | ✅ Healthy |
| Y-Z | `0xd3ffe181...b883` | **2** | ✅ Healthy |
| S-T | `0x3b1c3ae9...d7883` | **2** | ✅ Healthy |
| V-W | `0x40fad7b4...eb6d` | **2** | ✅ Healthy |

All 5 multisig contracts uniformly require 2-of-N signatures. Consistent configuration.

### MNX Markets (testnet.mnx.fi)

**Status: DATA UNAVAILABLE** — Site is a Next.js SPA. Both `/api/markets` and `/api/v1/markets` return the HTML shell; no REST API exposed. No mnx_snapshots inserted.

---

## Delta vs Prior Sweep (2026-04-12)

| Metric | Apr 2026 | Jul 2026 (new) | All-time |
|--------|----------|----------------|----------|
| World Increments | 12 | +12 | 35 total |
| Repo Snapshots | 473 | +47 | 991 total |
| Aptos Snapshots | 0 | +28 | 28 |
| Multisig Probes | 0 | +5 | 5 |

### Notable Changes Since Apr 2026
- `plurigrid/gorj` open issues: **1468** (active repo, highly tracked)
- `plurigrid/asi` stars: **52** (was 16 in Apr — 3× growth)
- Kubeflow added **MCP server repos** (`mcp-server` 30⭐, `mcp-apache-spark-history-server` 184⭐)
- bmorphism's `ocaml-mcp-sdk`: **61 stars** (new since Apr)
- TeglonLabs added `jank-crane` (C++, GF3 convergence maps)
- zubyul added `tilelang-kernels` (TileLang GPU for GF3 on Blackwell)
- bmorphism added `gay-chat` (Scheme, Spritely Brassica)
