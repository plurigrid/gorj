# World-Increment Sweep + Hamming Snapshot — 2026-06-12

## Sweep Metadata
- **Date:** 2026-06-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| migalkin | user (zubyul graph) | 49 |
| kubeflow | org | 48 |
| zubyul | user | 19 |
| AustinCStone | user (zubyul graph) | 10 |
| M1shaaa | user (zubyul graph) | 8 |
| wasita | user (zubyul graph) | 11 |
| DJedamski | user (zubyul graph) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (zubyul graph) | 5 |
| **TOTAL** | | **361** |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 120 |
| PLUS | 1 | `#b8bb26` | 121 |
| MINUS | -1 | `#cc241d` | 120 |

GF(3) assignment: `id % 3 == 0` → ERGODIC, `id % 3 == 1` → PLUS, `id % 3 == 2` → MINUS

### Notable Highlights

- **kubeflow/kubeflow**: flagship ML platform for Kubernetes (leading stars in sweep)
- **bmorphism**: 100 repos, 247 total stars — active MCP/OCaml ecosystem builder
- **zubyul**: 19 repos, 280 total stars — active contributor
- **AustinCStone/TextGAN**: 92 stars — GAN for text generation in TensorFlow
- **AustinCStone/StereoVisionMRF**: 11 stars — depth from stereo using MRF
- **TeglonLabs/jank-crane**: C++ converged-IR hub with GF3 convergence maps (pushed 2026-06-08)
- **migalkin**: 49 repos, 14 total stars — knowledge graph / GNN researcher
- **wasita/magic-garden**: 2 stars — Discord bot for the magic garden game

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (`alice`, `bob`, `A`–`Z`) via `fullnode.mainnet.aptoslabs.com`.  
**All 28 wallets returned 0.0 APT** — accounts are either unfunded or uninitialized on mainnet.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | 0x8699...–0x7af0... | 0.0 each |

### Multisig Contract Probes

All 5 contracts are live and healthy, each requiring exactly 2 signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — all endpoints (`/`, `/api/markets`, `/api/v1/markets`) are gated behind Vercel deployment protection authentication. The `mnx_snapshots` table is empty this sweep.

---

## DuckDB Schema & Row Counts

```
world_increments   361 rows  — one per repo, GF3 trit/color/name, md5 snapshot_hash
repo_snapshots     361 rows  — org_or_user, full_name, language, stars, forks, open_issues, pushed_at
aptos_snapshots     28 rows  — world, address, balance_apt (all 0.0)
multisig_probes      5 rows  — pair, address, sigs_required=2, healthy=true
mnx_snapshots        0 rows  — unavailable (Vercel auth gate)
```

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
