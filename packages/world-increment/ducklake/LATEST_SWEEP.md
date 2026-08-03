# World-Increment Sweep — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID (this run):** id=1 @ 2026-08-03 (GF3 cycle continues from prior id=12)
- **GF3:** PLUS · trit=+1 · #b8bb26

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all runs) | 25 |
| Total Repo Snapshots (all runs) | 1,045 |
| Sources Covered (this run) | 3 orgs + 8 users |
| New Repos Stored (this run) | 101 |

---

### GF(3) Color Chain — This Sweep (id=13 in sequence, stored as id=1)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 13 | multi-org sweep | +1 | `#b8bb26` | **PLUS** |

GF(3) chain continues: `… ERGODIC(12) → **PLUS(13)**`

---

### Sources Snapshotted

| Source | Type | Total Found | Stored |
|--------|------|-------------|--------|
| plurigrid | org | 100 | 20 |
| kubeflow | org | 49 | 20 |
| bmorphism | user | 100 | 20 |
| zubyul | user | 49 | 20 |
| TeglonLabs | org | 5 | 5 |
| migalkin (social) | user | 19 | 4 |
| DJedamski (social) | user | 6 | 2 |
| wasita (social) | user | 12 | 3 |
| kristinezheng (social) | user | 5 | 2 |
| M1shaaa (social) | user | 8 | 2 |
| AustinCStone (social) | user | 41 | 3 |
| **TOTAL** | | | **101** |

---

### Top Repos by Stars (this sweep)

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | ~15,565 | recent |
| kubeflow/pipelines | Python | ~4,119 | recent |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |

### Notable Recent Activity (pushed since 2026-06-01)

- **TeglonLabs/jank-crane** (C++) — `crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow` pushed 2026-06-08
- **migalkin/kgcourse2021** (HTML) — Knowledge Graphs course materials pushed 2026-07-10
- **wasita/wasita.github.io** (Svelte) — personal website pushed 2026-07-21
- **wasita/wm-cv** (Svelte) — Academic CV pushed 2026-07-14
- **AustinCStone/byteruckus** (HTML) — pushed 2026-07-15
- **kristinezheng/kristinezheng.github.io** (HTML) — pushed 2026-07-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

**28 wallets queried** (alice, bob, A–Z) via Aptos fullnode mainnet API.
All wallets returned **0 APT** — CoinStore resources not registered or balances are zero. No non-zero balances detected.

| World | Address (prefix) | Balance APT |
|-------|-----------------|------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A | 0x8699ed… | 0.0 |
| B | 0x3f892e… | 0.0 |
| C | 0x38b99e… | 0.0 |
| D | 0xf77656… | 0.0 |
| E | 0xdc1d9d… | 0.0 |
| F | 0x18a14b… | 0.0 |
| G | 0x69a394… | 0.0 |
| H | 0xce67c3… | 0.0 |
| I | 0x070fe5… | 0.0 |
| J | 0x4d964d… | 0.0 |
| K | 0xa73204… | 0.0 |
| L | 0x7c2eae… | 0.0 |
| M | 0x6fed37… | 0.0 |
| N | 0xe7dde6… | 0.0 |
| O | 0x73252b… | 0.0 |
| P | 0x621879… | 0.0 |
| Q | 0xac40fa… | 0.0 |
| R | 0x7ce605… | 0.0 |
| S | 0xb87530… | 0.0 |
| T | 0x357810… | 0.0 |
| U | 0x758600… | 0.0 |
| V | 0xb59dd8… | 0.0 |
| W | 0x5f32ae… | 0.0 |
| X | 0xa95cbb… | 0.0 |
| Y | 0xd8e328… | 0.0 |
| Z | 0x7af0ef… | 0.0 |

---

### Multisig Contract Probes

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f4… | 2 | ✓ healthy |
| A-G | 0xf56c4a… | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1… | 2 | ✓ healthy |
| S-T | 0x3b1c3a… | 2 | ✓ healthy |
| V-W | 0x40fad7… | 2 | ✓ healthy |

All 5 pairs require **2-of-N signatures** and are reachable on mainnet.

---

### MNX Markets (testnet.mnx.fi)

Site is a **Next.js SPA** — no public JSON API endpoints accessible.
Both `/api/markets` and `/api/v1/markets` return the SPA HTML shell.
Market data unavailable; recorded as unavailable in `mnx_snapshots` table.

---

## DuckDB Table State (post-insert)

```
world_increments : 25 records  (1 new @ 2026-08-03)
repo_snapshots   : 1,045 records (101 new @ 2026-08-03)
aptos_snapshots  :  28 records  (28 new @ 2026-08-03)
multisig_probes  :   5 records  ( 5 new @ 2026-08-03)
mnx_snapshots    :   1 record   ( 1 new @ 2026-08-03)
```

---

## Schema Reference
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
- `id mod 3 == 2` → trit=−1, color=#cc241d, name=MINUS
