# World-Increment Sweep + Hamming Snapshot — 2026-07-23

## Sweep Metadata
- **Date:** 2026-07-23 11:08 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-07-23-1108`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 180 |
| New Repo Snapshots (this run) | 180 |
| Sources Covered | 3 orgs + 8 users |
| Aptos wallets probed | 28 (all null — mainnet unreachable) |
| Multisig pairs probed | 5/5 healthy (2-of-2 each) |
| MNX markets | unavailable (SPA, no REST API) |

---

## GF(3) Color Chain — 180 Increments This Run

Each repo snapshot is assigned a trit based on its sequential ID:

| Trit | Color | Name | Count |
|------|-------|------|------:|
| 0 | `#d3869b` | ERGODIC | 67 |
| +1 | `#b8bb26` | PLUS | 68 |
| -1 | `#cc241d` | MINUS | 68 |

Cyclic pattern: `ERGODIC → PLUS → MINUS → ERGODIC → ...` (60 full GF(3) cycles this run)

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 wallets)

**Status: ALL NULL — `fullnode.mainnet.aptoslabs.com` unreachable from this environment**

Network policy blocks outbound connections to the Aptos mainnet fullnode.
All 28 balance queries returned errors. Records stored with `balance_apt = NULL`.

### Multisig Contract Probes

**All 5 healthy ✓ — 2-of-2 signatures required**

| Pair | Short Address | Sigs Required | Healthy |
|------|---------------|:-------------:|:-------:|
| A-B | 0x0da4f428...87003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

> Multisig view-function POSTs succeeded while wallet GET resource queries failed — proxy permits `/v1/view` but blocks `/v1/accounts/{addr}/resource/...`.

### MNX Markets

**Unavailable** — `https://testnet.mnx.fi` is a Next.js SPA with no public REST endpoints. Client-side data only. Stored sentinel record.

---

---

## Top Repos by Source (this run)

### kubeflow (20 snapshotted, 49 total in org)
| Repo | Language | Stars | Pushed |
|------|----------|------:|--------|
| kubeflow/kubeflow | — | 15,789 | 2026-07-23 |
| kubeflow/pipelines | Python | 4,169 | 2026-07-23 |
| kubeflow/spark-operator | Python | 3,143 | 2026-07-23 |
| kubeflow/trainer | Go | 2,153 | 2026-07-23 |
| kubeflow/katib | Python | 1,692 | 2026-07-20 |
| kubeflow/examples | Jsonnet | 1,461 | 2026-07-22 |
| kubeflow/arena | Go | 815 | 2026-07-21 |
| kubeflow/mpi-operator | Go | 530 | 2026-07-22 |

### plurigrid (100 snapshotted)
Top pushed recently: **gorj** (2026-07-23), **asi** (2026-07-10, ★31), **place** (2026-07-14), **eirobri** (2026-07-21)

### bmorphism (20 snapshotted)
| Repo | Stars | Pushed |
|------|------:|--------|
| ocaml-mcp-sdk | 61 | 2026-05-08 |
| risc0-cosmwasm-example | 23 | 2025-05-21 |
| anti-bullshit-mcp-server | 22 | 2026-07-12 |
| say-mcp-server | 20 | 2026-03-19 |
| babashka-mcp-server | 19 | 2026-06-05 |
| manifold-mcp-server | 14 | 2026-04-15 |
| penrose-mcp | 9 | 2026-06-24 |
| marginalia-mcp-server | 8 | 2026-03-27 |

### migalkin (5 snapshotted)
NodePiece ★144, StarE ★89, NBFNet_mlx ★10, RWL ★8

### AustinCStone (4 snapshotted)
TextGAN ★92, StereoVisionMRF ★11

---

## Repo Counts by Source (this sweep)

| Source | Type | Snapshotted |
|--------|------|:-----------:|
| plurigrid | org | 100 |
| kubeflow | org | 20 |
| bmorphism | user | 20 |
| zubyul | user | 11 |
| wasita | user | 6 |
| TeglonLabs | org | 5 |
| migalkin | user | 5 |
| AustinCStone | user | 4 |
| kristinezheng | user | 3 |
| M1shaaa | user | 3 |
| DJedamski | user | 3 |
| **TOTAL** | | **180** |

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

## Notable Highlights (2026-07-23)
- **kubeflow/kubeflow**: 15,789 stars (+224 since Apr) — pushed today
- **kubeflow/pipelines**: 4,169 stars (+50 since Apr) — pushed today
- **kubeflow/spark-operator**: 3,143 stars (+32 since Apr) — pushed today
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut color sampling, very active
- **bmorphism/gay-chat**: new repo (Jul 14) — gay://chat over Spritely Brassica
- **bmorphism/ocaml-mcp-sdk**: 61 stars — Jane Street oxcaml_effect MCP integration
- **migalkin/NodePiece**: 144 stars — ICLR'22 KG embeddings still active
- **AustinCStone/TextGAN**: 92 stars — GAN text generation (2016, still referenced)
- **plurigrid/gorj**: pushed today — this sweep's own repo
- **plurigrid/asi**: ★31 (was 16 in Apr) — significant growth
- **wasita/wasita.github.io**: pushed 2026-07-21 — recently updated Svelte personal site
- **Multisig**: All 5 Hamming pairs (A-B, A-G, Y-Z, S-T, V-W) healthy with 2-of-2 threshold
- **Aptos fullnode**: balance GETs blocked by env network policy; view-function POSTs work
