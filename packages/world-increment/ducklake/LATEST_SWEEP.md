# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 (capped at 100) |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 (capped at 100) |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |
| **TOTAL (this sweep)** | | **291** |

### Cumulative DuckDB State
| Table | Row Count |
|-------|-----------|
| world_increments | 250 |
| repo_snapshots | 1171 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

### GF(3) Distribution (world_increments, cumulative)
| Class | Trit | Color | Count |
|-------|------|-------|-------|
| ERGODIC | 0 | #d3869b | 82 |
| PLUS | +1 | #b8bb26 | 84 |
| MINUS | -1 | #cc241d | 84 |

### Top Repos by Stars (this sweep)
| Repo | Language | Stars | Forks | Last Pushed |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15741 | 2680 | 2026-06-18 |
| kubeflow/pipelines | Python | 4157 | 2009 | 2026-06-23 |
| kubeflow/spark-operator | Python | 3128 | 1491 | 2026-06-24 |
| kubeflow/trainer | Go | 2119 | 971 | 2026-06-22 |
| kubeflow/katib | Python | 1685 | 527 | 2026-06-23 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| AustinCStone/StereoVisionMRF | Python | 11 | 4 | 2026-04-01 |
| migalkin/NBFNet_mlx | Python | 10 | 1 | 2026-03-11 |

### Notable Activity Delta Since 2026-04-12
- **kubeflow/kubeflow**: 15565 → 15741 stars (+176); kubeflow/spark-operator: 3111 → 3128 (+17)
- **migalkin/NodePiece**: 143 → 144 stars; migalkin/StarE: 88 → 89 stars
- **TeglonLabs/jank-crane**: NEW C++ repo added 2026-06-08 (crane-jank converged-IR hub, GF3 convergence maps)
- **wasita**: Active new projects (vocoder 2026-05-06, wm-cv 2026-05-13, send2kobo 2026-05-19, proj-template 2026-06-19)
- **bmorphism/ocaml-mcp-sdk** still top bmorphism repo at 60 stars
- **AustinCStone/bmfork** + **bmforkupdate**: new repos referencing bmorphism (2025-05)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 wallets)

**Status:** All 28 wallet queries returned NULL — Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`) not reachable from this sandboxed runner environment. Addresses recorded for audit trail; balances to be retrieved from an unrestricted network context.

```
alice  0xc793...cc7b → NULL APT
bob    0x0a3c...512d → NULL APT
A–Z    0x8699...197c → NULL APT (26 addresses)
```

### Multisig Contract Probes — ALL HEALTHY

All 5 multisig contracts responded successfully to `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

All pairs are **2-of-2 multisig**. All contracts reachable and responding.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — `testnet.mnx.fi` returns HTTP 401 (Vercel deployment protection active, requires authentication bypass token). No market data accessible. Recorded as `MNX_TESTNET_UNAVAILABLE` in mnx_snapshots table.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
