# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-07-02 23:10 UTC  
**GF(3) color chain:** PLUS (#b8bb26) → MINUS (#cc241d) → ERGODIC (#d3869b) → repeat

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 28 |
| kubeflow | org | 24 |
| TeglonLabs | org | 5 |
| bmorphism | user | 26 |
| zubyul | user | 14 |
| migalkin | user (social) | 7 |
| DJedamski | user (social) | 5 |
| wasita | user (social) | 8 |
| kristinezheng | user (social) | 4 |
| M1shaaa | user (social) | 4 |
| AustinCStone | user (social) | 9 |
| **Total** | | **134 repos** |

### DuckDB Schema

- `world_increments` — 134 rows, GF(3) trit color chain indexed
- `repo_snapshots` — 134 rows, stars/forks/issues/pushed_at
- `aptos_snapshots` — 28 rows (alice,bob,A-Z)
- `multisig_probes` — 5 rows (all healthy)
- `mnx_snapshots` — 0 rows (SPA, no API available)

### Top Starred Repos (all sources)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,758 | — |
| kubeflow/pipelines | 4,167 | Python |
| kubeflow/spark-operator | 3,130 | Python |
| kubeflow/trainer | 2,129 | Go |
| kubeflow/katib | 1,688 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| migalkin/NodePiece | 144 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| AustinCStone/TextGAN | 92 | Python |

### Most Active plurigrid Repos (by open issues)

| Repo | Open Issues | Stars |
|------|-------------|-------|
| plurigrid/gorj | 926 | 0 |
| plurigrid/nanoclj-zig | 20 | 1 |
| plurigrid/ontology | 16 | 8 |
| plurigrid/place | 12 | 1 |
| plurigrid/eirobri | 30 | 0 |

### Notable New Repos (2026)

- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) gay trit coloring (926 open issues!)
- **bmorphism/satreadout** — Machine-checked saturating non-Riemannian perceptual readout (Lean 4.28)
- **zubyul/voice-observatory** — Passive macOS TUI observing voice-download pathways
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub with GF3 convergence maps
- **kubeflow/mcp-apache-spark-history-server** — 179 stars in <1yr

### GF(3) Color Chain Sample (first 9 increments)

| id | trit | color | name | repo |
|----|------|-------|------|------|
| 1 | +1 | #b8bb26 | PLUS | plurigrid/asi |
| 2 | -1 | #cc241d | MINUS | plurigrid/place |
| 3 | 0 | #d3869b | ERGODIC | plurigrid/eirobri |
| 4 | +1 | #b8bb26 | PLUS | plurigrid/nash-portal |
| 5 | -1 | #cc241d | MINUS | plurigrid/gorj |
| 6 | 0 | #d3869b | ERGODIC | plurigrid/zig-syrup |
| 7 | +1 | #b8bb26 | PLUS | plurigrid/asi-skills |
| 8 | -1 | #cc241d | MINUS | plurigrid/nanoclj-zig |
| 9 | 0 | #d3869b | ERGODIC | plurigrid/vivarium |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A-Z)

**Result:** All 28 accounts queried against Aptos mainnet (ledger v6,067,417,901, epoch 16,393, block 872,171,338).

All accounts **exist on-chain** but return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. This means the accounts use the newer **Fungible Asset (FA)** standard or were created without APT deposits. All balances recorded as `NULL`.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ |

**All 5 multisig contracts healthy** — all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — serves a SPA returning HTML for all API paths. No structured market data extractable. Recorded 0 rows in `mnx_snapshots`.

---

## DuckDB Location

`packages/world-increment/ducklake/world-increments.duckdb`

```sql
-- Summary by source
SELECT source_name, COUNT(*) as repos 
FROM world_increments wi JOIN repo_snapshots rs ON wi.id = rs.increment_id 
GROUP BY source_name ORDER BY repos DESC;

-- GF3 trit distribution
SELECT gf3_name, gf3_color, COUNT(*) as count 
FROM world_increments GROUP BY gf3_name, gf3_color;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
