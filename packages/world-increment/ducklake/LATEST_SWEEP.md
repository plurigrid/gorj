# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-06

## Sweep Metadata
- **Date:** 2026-07-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 343 |
| Total Repo Snapshots | 471 (prior) + 320 (this run) |
| Sources Covered | 3 orgs + 8 users + 6 social graph nodes |
| Aptos addresses probed | 28 (alice, bob, A–Z) |
| Multisig contracts probed | 5 pairs |
| MNX market data | unavailable (HTTP 401) |

---

## GF(3) Color Chain — This Run (343 increments, per-repo assignment)

| Rule | Trit | Color | Name | Count |
|------|------|-------|------|-------|
| id % 3 == 0 | 0 | `#d3869b` | **ERGODIC** | 113 |
| id % 3 == 1 | +1 | `#b8bb26` | **PLUS** | 115 |
| id % 3 == 2 | -1 | `#cc241d` | **MINUS** | 115 |

---

## Top Repos by Source (2026-07-06)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,766 | 2026-07-06 |
| pipelines | Python | 4,169 | 2026-07-06 |
| spark-operator | Python | 3,111+ | 2026-07-06 |
| trainer | Go | 2,080+ | 2026-07-06 |
| katib | Python | 1,676+ | 2026-07-06 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### zubyul (49 repos)
Queried 49 repos sorted by pushed date.

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

### wasita (11 repos) — most recent push 2026-07-05
| Repo | Language | Stars |
|------|----------|-------|
| wasita.github.io | Svelte | 1 |
| magic-garden | Python | 2 |
| send2kobo | TypeScript | 1 |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| EpsteinSearch | Python | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

**Status:** All addresses returned HTTP 404 — no CoinStore resource found on mainnet.  
This indicates the Hamming swarm wallets have not yet been initialized or funded on Aptos mainnet.

| World | Status |
|-------|--------|
| alice (0xc793…cc7b) | 404 — no CoinStore |
| bob (0x0a3c…512d) | 404 — no CoinStore |
| A–Z (26 wallets) | 404 — no CoinStore |

### Multisig Contract Probes — ALL HEALTHY ✓

All 5 multisig pairs verified with 2-of-N signatures required:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ Healthy |
| A-G | 0xf56c…0096 | 2 | ✓ Healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✓ Healthy |
| S-T | 0x3b1c…7883 | 2 | ✓ Healthy |
| V-W | 0x40fa…eb6d | 2 | ✓ Healthy |

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** — HTTP 401 on all probe paths. Requires authentication credentials not available to this agent.

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
- **kubeflow/kubeflow**: 15,766 stars (+201 since Apr 12) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars (+50 since Apr 12)
- **TeglonLabs/jank-crane** (pushed 2026-06-08): new C++ repo, explicitly references GF3 convergence maps — thematically aligned with this sweep
- **wasita** had the most recent personal push (2026-07-05, yesterday)
- **migalkin/NodePiece**: 144 stars (+1 since Apr 12) — knowledge graph embeddings
- **AustinCStone/EpsteinSearch**: new repo (2026-02-08), Python
- **Hamming swarm wallets**: uninitialized on mainnet — all 28 addresses lack CoinStore
- **5 multisigs**: all healthy, all 2-of-N — no governance anomalies
