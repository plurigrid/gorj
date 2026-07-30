# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 341 |
| Total Repo Snapshots (cumulative) | 1,262 |
| New records this run | 318 repos + 28 Aptos + 5 multisig |
| Sources Covered | 3 orgs + 8 users (social graph) |

---

## GF(3) Color Chain Distribution (cumulative)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 113 |
| +1 | `#b8bb26` | PLUS | 114 |
| −1 | `#cc241d` | MINUS | 114 |

GF(3) cycling rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

---

## Top Repos by Source (this run)

### plurigrid (100 repos, 188 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 56 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-30 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| place | TeX | 1 | 2026-07-14 |

### kubeflow (49 repos, 102,161 total stars)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4171 | 2026-07-29 |
| spark-operator | Python | 3142 | 2026-07-29 |
| trainer | Go | 2163 | 2026-07-30 |
| hub | — | 179 | 2026-07-29 |
| mcp-server | Python | 31 | 2026-07-30 |

### TeglonLabs (5 repos, 14 total stars)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (100 repos, 508 total stars)
| Repo | Language | Pushed At |
|------|----------|-----------|
| Gay.jl | Julia | 2026-07-30 |
| gay-chat | Scheme | 2026-07-14 |

### Social Graph — migalkin (19 repos)
| Repo | Stars | Description |
|------|-------|-------------|
| NodePiece | 144 | KG param-efficient reps (ICLR'22) |
| StarE | 89 | Hyper-relational KG (EMNLP'20) |
| kgcourse2021 | 24 | Knowledge Graphs course |

### Social Graph — AustinCStone (41 repos)
| Repo | Stars |
|------|-------|
| TextGAN | 92 |
| StereoVisionMRF | 11 |

---

## Repo Counts by Source (this run)

| Source | Type | Repos This Run | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 188 |
| bmorphism | user | 100 | 508 |
| kubeflow | org | 49 | 102,161 |
| zubyul | user | 49 | 40 |
| AustinCStone | social-graph | 41 | 319 |
| TeglonLabs | org | 5 | 14 |
| migalkin | social-graph | 19 | 821 |
| wasita | social-graph | 12 | 7 |
| M1shaaa | social-graph | 8 | 0 |
| kristinezheng | social-graph | 5 | 0 |
| DJedamski | social-graph | 6 | 15 |
| **TOTAL** | | **318** | **103,873** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z + alice/bob)

**Result:** All 28 addresses returned NULL for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
CoinStore resource not initialized — accounts may exist on-chain but APT coin stores have not been registered.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | not initialized |
| bob | 0x0a3c00... | not initialized |
| A–Z (all 26) | … | not initialized |

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** (all require 2-of-2 signatures):

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f4... | 2 | HEALTHY |
| A-G | 0xf56c4a... | 2 | HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | HEALTHY |
| S-T | 0x3b1c3a... | 2 | HEALTHY |
| V-W | 0x40fad7... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

The SPA at `testnet.mnx.fi` loaded (HTTP 200, Next.js). CSP reveals API at `api.testnet.mnx.fi` (WebSocket + REST).
Standard REST paths (`/markets`, `/v1/markets`, `/api/markets`) returned 404 — API uses custom protocol.
**Market data unavailable via REST; WebSocket protocol required.**

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
- **kubeflow/pipelines**: 4,171 stars — pushed today (2026-07-30), highly active ML platform
- **kubeflow/trainer**: 2,163 stars — pushed today, distributed training for Kubernetes
- **kubeflow/mcp-server**: 31 stars — Kubeflow now has MCP integration (new since last sweep)
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings still getting traction
- **AustinCStone/TextGAN**: 92 stars — text generation GAN
- **plurigrid/asi**: 56 stars (up from 16) — significant growth since April sweep
- **plurigrid/gorj**: This very repo, pushed today — scheduled task working correctly
- **bmorphism/Gay.jl**: Julia repo, pushed today
- **Aptos Swarm**: All 28 addresses have uninitialized CoinStores — no APT balances
- **Multisig Health**: All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) require 2 sigs and are HEALTHY
