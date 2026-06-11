# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-06-11
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 23 |
| kubeflow | org | 14 |
| TeglonLabs | org | 5 |
| bmorphism | user | 12 |
| zubyul | user | 10 |
| migalkin | social-graph | 6 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 6 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 8 |
| **Total** | | **103** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,714 | — | 2026-05-24 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-10 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-09 |
| kubeflow/trainer | 2,112 | Go | 2026-06-10 |
| kubeflow/katib | 1,684 | Python | 2026-06-05 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| plurigrid/asi | 25 | HTML | 2026-06-10 |
| migalkin/kgcourse2021 | 25 | HTML | 2025-08-04 |

### Most Active (Recent Push)

- `plurigrid/gorj` — 2026-06-11 (492 open issues, this repo)
- `bmorphism/Gay.jl` — 2026-06-11 (wide-gamut color sampling, SPI)
- `M1shaaa/M1shaaa` — 2026-06-11 (profile config)
- `bmorphism/satreadout` — 2026-06-10 (Lean 4, machine-checked perceptual readout)
- `kubeflow/pipelines` — 2026-06-10 (ML Pipelines for Kubeflow)

### GF(3) Color Chain

Increments assigned via `id % 3`:
- **trit=0 ERGODIC #d3869b:** id=3,6,9,...
- **trit=1 PLUS #b8bb26:** id=1,4,7,...
- **trit=-1 MINUS #cc241d:** id=2,5,8,...

103 total increments logged in `world_increments` table.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A-Z) queried against fullnode.mainnet.aptoslabs.com.

| World | APT Balance | Status |
|-------|-------------|--------|
| alice | 0.0 APT | no CoinStore resource |
| bob | 0.0 APT | no CoinStore resource |
| A-Z (26 wallets) | 0.0 APT each | no CoinStore resource |

All addresses return 0 - unfunded addresses with no `0x1::coin::CoinStore<AptosCoin>` resource initialized.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

All 5 multisig contracts are active 2-of-N configurations.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** - testnet.mnx.fi is behind Vercel deployment protection. No market data could be fetched without a bypass token or Vercel OIDC credential.

---

## DuckDB Schema

```
world_increments   -- 103 rows: GF3 trit-colored sweep events
repo_snapshots     -- 103 rows: GitHub repo metadata snapshots
aptos_snapshots    --  28 rows: Hamming swarm wallet balances
multisig_probes    --   5 rows: Multisig contract health probes
mnx_snapshots      --   1 row:  MNX market placeholder (unavailable)
```

## Quick Queries

```sql
-- Most starred repos in sweep
SELECT org_or_user, repo_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF3 color distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1, 2;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;

-- Aptos balance summary
SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;
```
