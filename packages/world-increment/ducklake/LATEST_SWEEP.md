# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (Cumulative DuckDB)

| Metric | Value |
|--------|-------|
| Total World Increments | 340 |
| Total Repo Snapshots | 1,261 |
| Aptos Snapshots (this run) | 28 |
| Multisig Probes (this run) | 5 |
| Sources Covered | 3 orgs + 8 users (this run: 317 new increments) |

---

## JOB 1: GitHub Social Graph Sweep

### Repos Queried This Run (317 total)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | social-graph | 5 (sampled) |
| migalkin | social-graph | 5 (sampled) |
| TeglonLabs | org | 5 (sampled) |
| wasita | social-graph | 3 (sampled) |
| DJedamski | social-graph | 1 (sampled) |
| kristinezheng | social-graph | 1 (sampled) |
| M1shaaa | social-graph | 1 (sampled) |
| **TOTAL** | | **317 new** |

### Top Repos by Stars (All-Time in DB)

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,793 |
| kubeflow/pipelines | Python | 4,170 |
| kubeflow/spark-operator | Python | 3,143 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/NodePiece | Python | 144 |
| migalkin/StarE | Python | 89 |
| plurigrid/asi | HTML | 31 |
| TeglonLabs/mathpix-gem | Ruby | 2 |

### Recently Active (plurigrid org, pushed 2026-07)

- **gorj** — `forj + Rama topology nREPL routing + GF(3) gay trit coloring` — pushed **2026-07-25**
- **eirobri** — `EiRoBri replay world` — pushed 2026-07-21
- **place** — pushed 2026-07-14
- **shrimp** — `Jank worked example` — pushed 2026-07-03

### TeglonLabs New (pushed 2026)

- **jank-crane** — `crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps` — C++ — pushed 2026-06-08

### GF(3) Color Chain (this run, first 6 increments)

| ID mod 3 | Trit | Color | Name |
|----------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | +1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

Chain cycles: PLUS → MINUS → ERGODIC (repeating across all 317 new increments)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 wallets (alice, bob, A–Z) queried against Aptos mainnet fullnode at `fullnode.mainnet.aptoslabs.com`.

**Result:** All 28 wallets return 0.0 APT — no `CoinStore<AptosCoin>` resource is initialized on any address. These are unfunded/uninitialized accounts on mainnet. This is consistent with the Hamming swarm representing theoretical world-addresses not yet funded.

| World | APT Balance |
|-------|------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 contracts queried via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f428... | **2** | ✓ healthy |
| A-G | 0xf56c4a1c... | **2** | ✓ healthy |
| Y-Z | 0xd3ffe181... | **2** | ✓ healthy |
| S-T | 0x3b1c3ae9... | **2** | ✓ healthy |
| V-W | 0x40fad7b4... | **2** | ✓ healthy |

All 5 multisig contracts are **healthy** (2-of-2 threshold). No anomalies detected.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/api/markets` — **SPA unavailable**: endpoint serves a Next.js client-side application (React hydration). No structured market data is accessible without browser JS execution. Recorded as unavailable in `mnx_snapshots` table.

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
