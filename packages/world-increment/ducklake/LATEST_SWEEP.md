# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-11

## Sweep Metadata
- **Date:** 2026-07-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 44 |
| Total Repo Snapshots | 44 (curated highlights) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — Increments 1–44

GF(3) rule: `id%3==0` → trit=0 ERGODIC #d3869b | `id%3==1` → trit=1 PLUS #b8bb26 | `id%3==2` → trit=-1 MINUS #cc241d

The 44 increments cycle: `PLUS → MINUS → ERGODIC × 14…` completing 14 full GF(3) cycles + 2 residual.

---

## GitHub Social Graph — Top Repos by Source

### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| gorj | Clojure | 1 | 2026-07-11 |
| StochFlow | Python | 4 | 2024-03-20 |
| asi-skills | Julia | 3 | 2026-04-26 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15770 | 2026-07-11 |
| pipelines | Python | 4169 | 2026-07-11 |
| spark-operator | Python | 3137 | 2026-07-11 |
| trainer | Go | 2136 | 2026-07-11 |
| katib | Python | 1690 | 2026-07-11 |
| mcp-apache-spark-history-server | Python | 182 | 2026-07-07 |
| mcp-server | Python | 20 | 2026-07-10 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (105 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 19 | 2026-06-05 |
| Gay.jl | Julia | 2 | 2026-06-20 |
| satreadout | HTML | 0 | 2026-06-20 |

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-world | Python | 1 | 2026-04-05 |
| voice-observatory | Python | 0 | 2026-04-24 |
| kinesis-kb360pro | Python | 0 | 2026-03-26 |

### migalkin (19 repos — social)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (40 repos — social)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com`.

**Result:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Interpretation:** Accounts exist on-chain but have no APT coin store registered (unfunded or non-APT accounts).

| World | Balance (APT) |
|-------|---------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26 wallets) | 0.0 each |

### Multisig Contract Probes — 5/5 Healthy ✓

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f4...87003 | 2-of-2 | ✓ healthy |
| A-G | 0xf56c4a...0096 | 2-of-2 | ✓ healthy |
| Y-Z | 0xd3ffe1...b883 | 2-of-2 | ✓ healthy |
| S-T | 0x3b1c3a...7883 | 2-of-2 | ✓ healthy |
| V-W | 0x40fad7...eb6d | 2-of-2 | ✓ healthy |

All 5 multisig contracts confirm 2-of-2 signature threshold — **swarm fully operational**.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — Vercel authentication required (password-protected preview deployment). No market data extractable without bypass token.

---

## DuckDB Ducklake

**Location:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 44 |
| repo_snapshots | 44 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
- **kubeflow/kubeflow**: 15,770 stars — flagship ML platform for Kubernetes, pushed today 2026-07-11
- **kubeflow/trainer** grew to 2,136★; **kubeflow/mcp-server** now exists (MCP tooling adoption)
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **plurigrid/gorj** (this repo): 1124 open issues, pushed 2026-07-11 — highly active
- **plurigrid/asi** grew to 30★ (was 16★ in April sweep)
- **TeglonLabs/jank-crane**: new since April sweep (C++, GF3 convergence maps)
- All 5 Hamming swarm multisig contracts healthy at 2-of-2 threshold
- All 28 Aptos addresses show 0 APT (no coin stores registered — unfunded swarm)
