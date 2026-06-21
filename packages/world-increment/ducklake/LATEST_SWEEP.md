# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-06-21 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 24 |
| kubeflow | org | 19 |
| TeglonLabs | org | 5 |
| bmorphism | user | 14 |
| zubyul | user | 15 |
| migalkin | social graph | 5 |
| wasita | social graph | 5 |
| AustinCStone | social graph | 5 |
| kristinezheng | social graph | 2 |
| M1shaaa | social graph | 2 |
| DJedamski | social graph | 2 |

**Total world_increments this run:** 116  
**Total repo_snapshots (cumulative DB):** 1,037

### Notable Active Repos (pushed since 2026-06-01)
- `kubeflow/dashboard` — TypeScript, pushed 2026-06-21 (80 open issues)
- `kubeflow/katib` — Python, pushed 2026-06-20 (116 open issues, 1683 stars)
- `kubeflow/pipelines` — Python, pushed 2026-06-20 (449 open issues, 4155 stars)
- `bmorphism/Gay.jl` — Julia, pushed 2026-06-21 (**187 open issues** — highest in swarm)
- `bmorphism/satreadout` — HTML, pushed 2026-06-20 (machine-checked saturating non-Riemannian perceptual readout)
- `plurigrid/nanoclj-zig` — Zig, pushed 2026-04-25 (NaN-boxed Clojure in Zig 0.15)
- `plurigrid/zig-syrup` — Zig, pushed 2026-04-30 (OCapN Syrup with CapTP optimizations)
- `plurigrid/asi-skills` — Julia, pushed 2026-04-26 (69 skills with Galois Hole Type accessibility)
- `TeglonLabs/jank-crane` — C++, pushed 2026-06-08 (crane-jank converged-IR hub, GF3 convergence maps)
- `wasita/proj-template` — pushed 2026-06-19
- `bmorphism/oxgame` — OCaml, pushed 2026-05-15 (Stellar resolution and open-game composition)
- `zubyul/nash-tui` — Rust, pushed 2026-04-13 (NASH token TUI with GeckoTerminal candles)

### GF(3) Color Chain Applied
World increments follow GF(3) trit chain:
- **id%3=0 → trit=0, ERGODIC #d3869b**
- **id%3=1 → trit=1, PLUS #b8bb26**
- **id%3=2 → trit=-1 (2), MINUS #cc241d**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**28 addresses probed** (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`

| Status | Count |
|--------|-------|
| Zero balance (no CoinStore) | 28/28 |
| Non-zero balance | 0/28 |

All Hamming swarm wallets returned 0 APT — addresses have not yet received initial funding or CoinStore resources have not been initialized on mainnet.

### Multisig Contract Probes
**5 contracts probed** via `POST /v1/view → 0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...4987003` | 2 | HEALTHY |
| A-G | `0xf56c4a1c...bc0096` | 2 | HEALTHY |
| Y-Z | `0xd3ffe181...75b883` | 2 | HEALTHY |
| S-T | `0x3b1c3ae9...d7883` | 2 | HEALTHY |
| V-W | `0x40fad7b4...80eb6d` | 2 | HEALTHY |

All 5 multisig accounts require **2-of-N signatures** and responded successfully. Swarm multisig infrastructure is intact.

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — HTTP 401 Unauthorized on all probe paths (`/`, `/api/markets`). Testnet requires authentication. Recorded as N/A in `mnx_snapshots` table.

---

## DuckDB Table Summary

```sql
-- world_increments: 116 rows (this run)
-- repo_snapshots:   1037 rows (cumulative)
-- aptos_snapshots:  28 rows (this run)
-- multisig_probes:  5 rows (this run)
-- mnx_snapshots:    1 row (unavailable marker)
```

### Top Stars in Social Graph
| Repo | Stars | Lang |
|------|-------|------|
| kubeflow/kubeflow | 15,738 | — |
| kubeflow/pipelines | 4,155 | Python |
| kubeflow/spark-operator | 3,127 | Python |
| kubeflow/katib | 1,683 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| plurigrid/ontology | 8 | JavaScript |
