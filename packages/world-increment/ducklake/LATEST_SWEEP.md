# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-21

## Sweep Metadata
- **Date:** 2026-06-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (GF3 chain) | 97 |
| Total Repo Snapshots | 1018 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Snapshots | 0 (auth-gated) |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Distribution (97 increments)

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 31 |
| PLUS | +1 | `#b8bb26` | 33 |
| MINUS | -1 | `#cc241d` | 33 |

GF(3) chain rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

---

## Top Repos by Source

### plurigrid (org — active today)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | **2026-06-21** (today, 721 open issues) |
| asi | HTML | 26 | 2026-06-10 |
| place | TeX | 1 | 2026-06-20 |
| eirobri | Clojure | 0 | 2026-06-03 |
| nash-portal | Rust | 2 | 2026-05-19 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |

### kubeflow (org — very active)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15738 | 2026-06-18 |
| pipelines | Python | 4155 | **2026-06-20** |
| spark-operator | Python | 3127 | 2026-06-18 |
| trainer | Go | 2118 | 2026-06-19 |
| katib | Python | 1683 | **2026-06-20** |
| dashboard | TypeScript | 16 | **2026-06-21** |

### TeglonLabs (org)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (user — active today)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | **2026-06-21** (187 open issues!) |
| satreadout | HTML | 0 | 2026-06-20 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |

### zubyul (user)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |
| Gay.jl | Julia | 0 | 2026-03-28 |
| gay-world | Python | 1 | 2026-03-26 |

### migalkin (user — knowledge graphs)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| RWL | Python | 8 | 2026-05-28 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### AustinCStone (user)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| EpsteinSearch | Python | 0 | 2026-02-11 |

### wasita / kristinezheng / M1shaaa / DJedamski
Smaller social graph nodes: academic/research repos, web/Svelte personal sites, lab analysis notebooks.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)
All 28 Hamming swarm wallets (alice, bob, A–Z) queried via Aptos mainnet fullnode at `fullnode.mainnet.aptoslabs.com`.

**Result: All 28 wallets return 0.00 APT.** CoinStore resources not found — accounts unfunded or not initialized on mainnet.

### Multisig Contract Probes
All 5 contracts respond healthy:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)
**Unavailable** — Vercel deployment protection (auth required). `mnx_snapshots` table left empty.

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

## Key Signals — 2026-06-21
- **plurigrid/gorj** pushed today (721 open issues) — this sweep is being committed inside the very repo it sweeps
- **bmorphism/Gay.jl** pushed today (187 open issues) — active GF(3) SPI color development  
- **kubeflow/dashboard, katib, pipelines** all pushed 2026-06-20/21 — very active ML platform
- **TeglonLabs/jank-crane** (C++ crane-jank IR) pushed 2026-06-08
- **All 28 Hamming swarm wallets at 0 APT** — swarm unfunded on mainnet
- **All 5 multisig contracts healthy** with 2-of-N policy
