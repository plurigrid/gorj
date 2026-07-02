# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-02

## Sweep Metadata
- **Date:** 2026-07-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 324 |
| Total Repo Snapshots | 324 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 5 |
| wasita | social | 5 |
| DJedamski | social | 3 |
| kristinezheng | social | 3 |
| M1shaaa | social | 3 |
| AustinCStone | social | 3 |
| **Total** | | **324** |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 108 |
| 1 | PLUS | `#b8bb26` | 108 |
| -1 | MINUS | `#cc241d` | 108 |

Assignment rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

### Top Starred Repos

| Repo | Stars | Language | Pushed At |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,757 | — | 2026-04-11 |
| kubeflow/pipelines | 4,167 | Python | 2026-04-10 |
| kubeflow/spark-operator | 3,130 | Python | 2026-04-10 |
| kubeflow/trainer | 2,128 | Go | 2026-04-10 |
| kubeflow/katib | 1,688 | Python | 2026-04-02 |
| kubeflow/examples | 1,460 | Jupyter | 2025-11-05 |
| kubeflow/community-distribution | 1,028 | Shell | 2026-04-10 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Notable Recent Activity (2026-07)

- **wasita/wasita.github.io** (Svelte): pushed 2026-07-02 — most recently active in social graph
- **kristinezheng/kristinezheng.github.io** (HTML): pushed 2026-07-01
- **TeglonLabs/jank-crane** (C++): pushed 2026-06-08 — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow"
- **migalkin/RWL** (Python): pushed 2026-05-28 — "Weisfeiler and Leman Go Relational (LOG 2022)"
- **migalkin/NodePiece** (Python): pushed 2026-05-07 — 144 stars, KG embeddings ICLR'22

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned **0.0 APT** — accounts hold no APT in their `CoinStore<AptosCoin>` resource (may hold other tokens or be unfunded).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I–Z (18 wallets) | … | 0.0 each |

### Multisig Contract Probes

All 5 multisig pairs are **healthy** (2-of-2 signatures required):

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — `testnet.mnx.fi` is behind Vercel deployment protection (visitor password required). No market data extracted. `mnx_snapshots` table has 0 rows.

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
