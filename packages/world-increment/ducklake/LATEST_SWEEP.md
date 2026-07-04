# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-04

## Sweep Metadata
- **Date:** 2026-07-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger:** 6,105,972,185 | epoch 16,417 | block 876,601,138

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 140 |
| Total Repo Snapshots (DB total) | 1084 |
| Sources Covered | 3 orgs + 8 users |
| Aptos addresses probed | 28 (alice, bob, A–Z) |
| Multisig contracts probed | 5 |
| MNX markets | unavailable (Vercel auth) |

---

## JOB 1: GitHub Social Graph — Top Repos by Source

### plurigrid (100 repos, sorted by push)
| Repo | Language | Stars | Issues | Pushed At |
|------|----------|-------|--------|-----------|
| gorj | Clojure | 0 | 973 | 2026-07-04 (today!) |
| shrimp | — | 0 | 0 | 2026-07-03 |
| asi | HTML | 28 | 4 | 2026-06-29 |
| eirobri | Clojure | 0 | 30 | 2026-06-30 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |
| asi-skills | Julia | 3 | 0 | 2026-04-26 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,761 | 2026-07-04 |
| pipelines | Python | 4,169 | 2026-07-03 |
| spark-operator | Python | 3,132 | 2026-07-03 |
| trainer | Go | 2,129 | 2026-07-03 |
| katib | Python | 1,689 | 2026-07-03 |
| arena | Go | 815 | 2026-07-04 |
| sdk | Python | 123 | 2026-07-02 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (105 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 61 |
| TextGAN (via AustinCStone) | Python | 92 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |
| Gay.jl | Julia | 2 (187 open issues!) |
| risc0-cosmwasm-example | Rust | 23 |

### migalkin (19 repos — knowledge graph researcher)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| NBFNet_mlx | Python | 10 |
| kgcourse2021 | HTML | 25 |

### Social graph
| User | Notable repo | Stars |
|------|-------------|-------|
| wasita | wasita.github.io (Svelte/personal) | 1 |
| AustinCStone | TextGAN (TF text generation) | 92 |
| zubyul | tilelang-kernels (GPU/GF3/Sinkhorn) | 0 |

---

## GF(3) Color Chain Distribution (this run, 140 increments)

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | ~47 |
| PLUS | #b8bb26 | +1 | ~47 |
| MINUS | #cc241d | -1 | ~46 |

Rule: `id%3==0→ERGODIC, id%3==1→PLUS, id%3==2→MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z — 28 addresses)

All 28 addresses returned `resource_not_found` on mainnet for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These addresses may hold APT via the newer `0x1::fungible_asset` module, or may be unfunded.

| Worlds | Status |
|--------|--------|
| alice, bob | no CoinStore resource |
| A through Z (26) | no CoinStore resource |

### Multisig Contract Probes — ALL HEALTHY ✓

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | **2** | ✓ |
| A-G | 0xf56c...0096 | **2** | ✓ |
| Y-Z | 0xd3ff...b883 | **2** | ✓ |
| S-T | 0x3b1c...7883 | **2** | ✓ |
| V-W | 0x40fa...eb6d | **2** | ✓ |

All 5 multisig accounts require exactly **2-of-N** signatures. All live and responsive on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — Vercel deployment protection (password-required, HTTP 401).  
No API paths accessible (`/api/markets`, `/api/v1/markets`). Requires visitor password or bypass token.

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

## Notable Highlights
- **plurigrid/gorj**: 973 open issues, pushed TODAY — most active plurigrid repo
- **kubeflow/kubeflow**: 15,761 stars — grown 196 stars since April sweep
- **bmorphism/Gay.jl**: 187 open issues — GF(3) color identity core, heavy development
- **zubyul/tilelang-kernels**: GPU kernels targeting NVIDIA GB10 Blackwell (CUDA 13, compute 12.1)
- **kubeflow/trainer**: 2,129 stars, LLM fine-tuning on Kubernetes
- **All 5 multisigs**: healthy, 2-of-N on Aptos mainnet
- **Hamming swarm wallets**: no APT CoinStore resources found — possible fungible_asset migration
