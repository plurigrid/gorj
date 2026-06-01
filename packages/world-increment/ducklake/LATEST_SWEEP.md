# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-01T02:14 UTC  
**Branch:** world-increment/sweep-2026-06-01  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 20 |
| kubeflow | org | 15 |
| TeglonLabs | org | 4 |
| bmorphism | user | 15 |
| zubyul | user | 10 |
| migalkin | user | 6 |
| DJedamski | user | 4 |
| wasita | user | 5 |
| kristinezheng | user | 3 |
| M1shaaa | user | 3 |
| AustinCStone | user | 5 |
| **Total** | | **90** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,696 | — |
| kubeflow/pipelines | 4,149 | Python |
| kubeflow/spark-operator | 3,124 | Python |
| kubeflow/trainer | 2,109 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,463 | Jsonnet |
| migalkin/NodePiece | 144 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| AustinCStone/TextGAN | 92 | Python |
| plurigrid/asi | 23 | HTML |

### GF(3) Color Chain

```
id % 3 == 0 → trit=0  ERGODIC  #d3869b  (30 records)
id % 3 == 1 → trit=1  PLUS     #b8bb26  (30 records)
id % 3 == 2 → trit=-1 MINUS    #cc241d  (30 records)
```
Perfect balance: 30 / 30 / 30.

### Notable Activity (2026)

- **plurigrid/gorj** (this repo): 285 open issues, pushed 2026-06-01 — Clojure/Rama/GF(3) active
- **plurigrid/eirobri**: 28 open issues — EiRoBri replay world
- **bmorphism/Gay.jl**: 189 open issues — wide-gamut SPI color sampling
- **kubeflow/pipelines**: pushed 2026-06-01 — continuous ML pipeline activity
- **zubyul/voice-observatory**: passive macOS TUI for voice-download pathways

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A-Z) queried via Aptos mainnet fullnode.

| World | Balance (APT) | Status |
|-------|-------------|--------|
| alice | 0.0 | no CoinStore |
| bob | 0.0 | no CoinStore |
| A through Z (26 addresses) | 0.0 each | no CoinStore |

All addresses return 0 APT — coin stores not initialized on mainnet for these addresses.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...7003 | 2 | YES |
| A-G | 0xf56c4a1c...0096 | 2 | YES |
| Y-Z | 0xd3ffe181...b883 | 2 | YES |
| S-T | 0x3b1c3ae9...7883 | 2 | YES |
| V-W | 0x40fad7b4...eb6d | 2 | YES |

All 5 multisig contracts healthy — each requires 2 signatures (2-of-N).

### MNX Markets (testnet.mnx.fi)

Next.js SPA. REST paths (/markets, /v1/markets) return 404. Market data served exclusively via WebSocket at wss://api.testnet.mnx.fi (confirmed via CSP headers). No REST market data available.

**Status:** Unavailable via REST — SPA + WebSocket architecture.

---

## DuckDB Schema

```
world_increments  -- 90 rows: GF(3) colored repo event stream
repo_snapshots    -- 90 rows: repo metadata at snapshot time
aptos_snapshots   -- 28 rows: hamming swarm wallet balances
multisig_probes   --  5 rows: 2-of-N signature requirements
mnx_snapshots     --  0 rows: unavailable (WebSocket SPA)
```

## Query Examples

```sql
-- GF(3) trit distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2;

-- Top active repos
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- Hamming swarm summary
SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
