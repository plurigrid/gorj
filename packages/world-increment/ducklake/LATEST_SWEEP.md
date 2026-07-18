# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-18

## Sweep Metadata
- **Date:** 2026-07-18T10:10 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (this run)

| Metric | Value |
|--------|-------|
| Repos inserted this run | 74 |
| Total world_increments in DB | 97 |
| Total repo_snapshots in DB | 1018 |
| Sources covered | 3 orgs + 8 users |

### GF(3) Distribution (this run, 74 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 31 |
| +1 | `#b8bb26` | PLUS | 33 |
| -1 | `#cc241d` | MINUS | 33 |

### Top Repos by Source

#### plurigrid (103 total, 15 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-17 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| asi-skills | Julia | 3 | 2026-04-26 |
| gorj | Clojure | 1 | 2026-07-07 |

#### kubeflow (49+ repos, 10 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,780 | 2026-07-10 |
| pipelines | Python | 4,168 | 2026-07-17 |
| spark-operator | Python | 3,138 | 2026-07-17 |
| trainer | Go | 2,151 | 2026-07-18 |
| katib | Python | 1,691 | 2026-07-16 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

#### bmorphism (103 total, 10 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| Gay.jl | Julia | 2 | 2026-07-14 |
| gay-chat | Scheme | 0 | 2026-07-14 |

#### Social Graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| wasita/wasita.github.io | Svelte | 1 | 2026-07-16 |
| wasita/pnas-typst-template | — | 0 | 2026-07-16 (created today) |
| zubyul/from-possible-worlds | TeX | 0 | 2026-07-18 (active today) |

### Active Today (pushed 2026-07-18)
- `kubeflow/sdk` — pushed 03:01 UTC
- `kubeflow/trainer` — pushed 02:23 UTC
- `zubyul/from-possible-worlds` — pushed 09:46 UTC
- `wasita/pnas-typst-template` — created today

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned **0.0 APT**.  
The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not present on any address,  
indicating these accounts are unfunded or not yet initialized on Aptos mainnet.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|--------------|
| alice | 0xc793… | 0.0 |
| bob | 0x0a3c… | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Probes (5 contracts)

All 5 multisig accounts are alive and require **2 signatures** — all healthy.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4… | 2 | ✅ |
| A-G | 0xf56c… | 2 | ✅ |
| Y-Z | 0xd3ff… | 2 | ✅ |
| S-T | 0x3b1c… | 2 | ✅ |
| V-W | 0x40fa… | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection (HTTP 401, visitor password required).  
No market data extracted. `mnx_snapshots` table has 0 rows.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 97 |
| repo_snapshots | 1018 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-07-18)
- **kubeflow/kubeflow**: 15,780 stars (+215 since Apr sweep) — still fastest growing ML Kubernetes platform
- **kubeflow/spark-operator**: 3,138 stars (+27) — active today
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1) — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **plurigrid/gorj**: 1,237 open issues — extremely active development
- **Hamming swarm**: 5/5 multisigs healthy at 2-of-N threshold
- **MNX markets**: blocked by Vercel auth, needs bypass token
