# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-15

**Sweep timestamp:** 2026-06-15T17:30:00Z
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB version:** v1.5.3 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`
**GF(3) color chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos (sample) | Notable |
|--------|------|----------------|---------|
| plurigrid | org | 100 | gorj (598 open issues), asi (⭐26) |
| kubeflow | org | 48 | kubeflow/kubeflow (⭐15,726), pipelines (⭐4,153) |
| TeglonLabs | org | 5 | mathpix-gem (⭐2), jank-crane (C++) |
| bmorphism | user | 104 | ocaml-mcp-sdk (⭐61), anti-bullshit-mcp-server (⭐23) |
| zubyul | user | 49 | gay-world (⭐1), jonikas_lab_data (⭐2) |
| migalkin | social | 19 | NodePiece (⭐144), StarE (⭐89) |
| wasita | social | 11 | magic-garden (⭐2) |
| DJedamski | social | 6 | Kaggle (⭐1) |
| kristinezheng | social | 5 | Green-Machine (HackMIT 2021) |
| AustinCStone | social | 40 | TextGAN (⭐92), StereoVisionMRF (⭐11) |
| M1shaaa | social | 8 | lab-bookshelf- (TypeScript) |

### Notable Activity (pushed 2026-06-15)

- **kubeflow/community-distribution** — YAML, ⭐1,023 — pushed 16:47Z
- **kubeflow/spark-operator** — Python, ⭐3,127 — pushed 16:37Z
- **bmorphism/Gay.jl** — Julia, ⭐1, 189 open issues — pushed 16:43Z (GF(3) coloring work)
- **kubeflow/hub** — Go, ⭐173 — pushed 16:42Z (Model Registry)
- **plurigrid/gorj** — Clojure, 598 open issues — pushed 16:14Z (this repo!)
- **kubeflow/trainer** — Go, ⭐2,115 — pushed 14:58Z (Distributed AI training on k8s)

### DuckDB Ducklake State

```
world_increments : 82 rows  (this sweep added 59 new GF(3)-colored increments)
repo_snapshots   : 1003 rows cumulative (prior sweep: 471 + 532 historical)
aptos_snapshots  : 28 rows
multisig_probes  : 5 rows
mnx_snapshots    : 1 row (unavailable)
```

### GF(3) Color Chain — This Sweep (sample)

| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | asi | +1 | `#b8bb26` | PLUS |
| 2  | plurigrid | place | -1 | `#cc241d` | MINUS |
| 3  | plurigrid | eirobri | 0 | `#d3869b` | ERGODIC |
| 4  | plurigrid | gorj | +1 | `#b8bb26` | PLUS |
| 5  | plurigrid | nash-portal | -1 | `#cc241d` | MINUS |
| … | … | … | … | … | … |
| 59 | M1shaaa | Python-Lookit-Uploads | -1 | `#cc241d` | MINUS |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

**Status:** All 28 addresses returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~5.75B.

Wallets exist on Aptos mainnet but hold no native APT CoinStore resource —
either uninitialized accounts or APT held via different mechanisms.
All recorded as NULL in `aptos_snapshots`.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acdec12b… | NULL |
| bob | 0x0a3c00c58fdf… | NULL |
| A–Z | (26 addresses) | NULL (all) |

### Multisig Contract Probes — ALL HEALTHY ✓

All 5 probed multisig accounts respond correctly and require **2-of-2** signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c0… | 2 | ✓ |
| A-G | 0xf56c4a1c0906… | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2d… | 2 | ✓ |
| S-T | 0x3b1c3ae905d4… | 2 | ✓ |
| V-W | 0x40fad7b423a8… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — Vercel authentication challenge returned.
No API data accessible without bypass token or Vercel CLI credentials.
Recorded as NULL placeholder in `mnx_snapshots`.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

*Generated 2026-06-15 by world-increment-sweep + hamming-swarm-snapshot agent*
