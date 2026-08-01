# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-01

## Sweep Metadata
- **Date:** 2026-08-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.0+
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 12 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 41 |
| **TOTAL (this run)** | | **~294** |

**Cumulative repo_snapshots in DB:** 1161

### Notable Repos (Recent Activity)

**TeglonLabs:**
- `jank-crane` (C++) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow — pushed 2026-06-08
- `mathpix-gem` (Ruby, 2★, 11 open issues) — Mathematical OCR gem — pushed 2026-01-01

**migalkin (social graph):**
- `NodePiece` (Python, 144★, 21 forks) — Compositional KG representations (ICLR'22) — last updated 2026-05-07
- `StarE` (Python, 89★) — Hyper-Relational KG message passing (EMNLP 2020) — updated 2026-04-16
- `NBFNet_mlx` (Python, 10★) — Neural Bellman-Ford on Apple Silicon — updated 2026-03-11

**wasita (social graph):**
- `wasita.github.io` (Svelte, 8 open issues) — personal website, active as of 2026-07-21
- `magic-garden` (Python, 2★) — Discord game bot — updated 2026-04-22

**AustinCStone (social graph):**
- `byteruckus` (HTML) — most recent repo, created 2026-07-15
- `TextGAN` (Python, 92★, 30 forks) — GAN for text generation in TensorFlow
- `EpsteinSearch` (Python) — updated 2026-02-11

**kristinezheng (social graph):**
- `kristinezheng.github.io` (HTML) — active as of 2026-07-01

### GF(3) Color Chain — This Run (11 new increments)

| Source | GF3 Trit | Color | Name |
|--------|----------|-------|------|
| plurigrid | +1 | `#b8bb26` | **PLUS** |
| kubeflow | -1 | `#cc241d` | **MINUS** |
| bmorphism | 0 | `#d3869b` | **ERGODIC** |
| zubyul | +1 | `#b8bb26` | **PLUS** |
| TeglonLabs | -1 | `#cc241d` | **MINUS** |
| wasita | 0 | `#d3869b` | **ERGODIC** |
| DJedamski | +1 | `#b8bb26` | **PLUS** |
| kristinezheng | -1 | `#cc241d` | **MINUS** |
| M1shaaa | 0 | `#d3869b` | **ERGODIC** |
| AustinCStone | +1 | `#b8bb26` | **PLUS** |
| migalkin | -1 | `#cc241d` | **MINUS** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-08-01)

All 28 Hamming swarm addresses queried against `fullnode.mainnet.aptoslabs.com`.

| World | Balance (APT) | Status |
|-------|---------------|--------|
| alice | 0.0 | resource not found |
| bob | 0.0 | resource not found |
| A–Z (26 addresses) | 0.0 each | resource not found |

**Result:** All 28 addresses returned "Resource not found" — no `CoinStore<AptosCoin>` resource
registered on any address. These accounts have never held APT on mainnet or have not been initialized on-chain.

### Multisig Contract Probes (Aptos Mainnet)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✅ HEALTHY |

**All 5 multisigs require 2-of-2 signatures and are on-chain and reachable.**

### MNX Markets (testnet.mnx.fi)

The MNX testnet is a Next.js SPA deployed on Vercel (HTTP 200). REST paths
`/markets` and `/v1/markets` on `api.testnet.mnx.fi` return 404. The Content-Security-Policy
header reveals the live data API uses WebSocket: `wss://api.testnet.mnx.fi` — not queryable
via REST/curl. **Market data: unavailable (WebSocket-only API).**

---

## DuckDB State (Cumulative)

```
Table               Rows
world_increments    34
repo_snapshots      1161
aptos_snapshots     28   (this run)
multisig_probes     5    (this run)
mnx_snapshots       0    (WebSocket API — no REST access)
```

DB: `packages/world-increment/ducklake/world-increments.duckdb`

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
