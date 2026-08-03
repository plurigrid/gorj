# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger version:** 6591319306 (epoch 16773, block 945663336)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 90 |
| Total Repo Snapshots | 90 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets Available | 0 (SPA) |

---

## GF(3) Color Chain Distribution

GF(3) assignment: `id%3==0` → ERGODIC #d3869b, `id%3==1` → PLUS #b8bb26, `id%3==2` → MINUS #cc241d

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 30 |
| 1 | `#b8bb26` | PLUS | 30 |
| -1 | `#cc241d` | MINUS | 30 |

---

## Top Repos by Stars (2026-08-03)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15805 | — | 2026-08-03 |
| kubeflow/pipelines | 4173 | Python | 2026-08-03 |
| kubeflow/spark-operator | 3142 | Python | 2026-08-01 |
| kubeflow/trainer | 2165 | Go | 2026-07-31 |
| kubeflow/katib | 1694 | Python | 2026-08-01 |
| kubeflow/examples | 1461 | Jsonnet | 2026-07-22 |
| kubeflow/community-distribution | 1029 | YAML | 2026-07-29 |
| kubeflow/arena | 816 | Go | 2026-07-30 |
| kubeflow/kale | 699 | Python | 2026-08-01 |
| kubeflow/mcp-apache-spark | 185 | Python | 2026-08-01 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 58 | HTML | 2026-08-01 |

## Most Recently Active Repos

| Repo | Pushed |
|------|--------|
| kubeflow/kubeflow | 2026-08-03 |
| kubeflow/pipelines | 2026-08-03 |
| kubeflow/mcp-server | 2026-08-03 |
| plurigrid/microworlds | 2026-08-02 |
| bmorphism/anti-bullshit-mcp-server | 2026-08-02 |
| plurigrid/asi | 2026-08-01 |

## Repo Counts by Source

| Source | Type | Repos Indexed |
|--------|------|---------------|
| plurigrid | org | 25 |
| kubeflow | org | 15 |
| bmorphism | user | 16 |
| zubyul | user | 10 |
| migalkin | user | 5 |
| wasita | user | 5 |
| TeglonLabs | org | 5 |
| AustinCStone | user | 5 |
| kristinezheng | user | 3 |
| DJedamski | user | 2 |
| M1shaaa | user | 2 |
| **TOTAL** | | **90** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger v6591319306)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. The CoinStore resource is not initialized on any of these accounts — **0 APT** across the entire Hamming swarm.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B–Z | (25 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig pairs are responsive and healthy, each requiring 2-of-N signatures:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

Site returns Next.js SPA HTML — no REST API endpoints expose market data directly. **Status: unavailable** (browser-rendered SPA).

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
- **kubeflow/kubeflow**: 15,805 stars (+240 since Apr sweep) — active daily pushes
- **plurigrid/gorj**: 1599 open issues — gorj this very repo, GF(3) trit-colored nREPL routing
- **plurigrid/asi**: 58★ topological chemputer, pushed 2026-08-01
- **bmorphism/Gay.jl**: 188 open issues, actively developed GF(3) color library
- **bmorphism/anti-bullshit-mcp-server**: 23★ MCP epistemology server, pushed 2026-08-02
- **migalkin/NodePiece**: 144★ ICLR'22 KG embeddings — recent push 2026-05-07
- **All 5 Hamming multisigs**: ✅ 2-of-N, healthy (A-B, A-G, Y-Z, S-T, V-W)
- **Hamming swarm balances**: All 28 addresses at 0 APT (CoinStore not initialized)
