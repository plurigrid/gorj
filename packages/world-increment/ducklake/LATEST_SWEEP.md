# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-08  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.3 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 20 (top active) |
| zubyul | user | 42 |
| TeglonLabs | org | 5 |
| migalkin | user (social) | 6 |
| DJedamski | user (social) | 3 |
| wasita | user (social) | 5 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 3 |
| AustinCStone | user (social) | 5 |
| **TOTAL** | | **272** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,708 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-08 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-04 |
| kubeflow/trainer | 2,112 | Go | 2026-06-05 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | YAML | 2026-06-05 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| kubeflow/kale | 691 | Python | 2026-06-05 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-02 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/asi | 25 | HTML | 2026-04-26 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |
| plurigrid/gorj | 0 | Clojure | 2026-06-08 |

### Most Recently Pushed (≥ 2026-06-08)

- `kubeflow/internal-acls` — 2026-06-08T16:06:10Z
- `TeglonLabs/jank-crane` (C++, GF3 convergence maps) — 2026-06-08T15:47:21Z
- `kubeflow/hub` (Model Registry) — 2026-06-08T14:34:01Z
- `kubeflow/pipelines` — 2026-06-08T14:14:07Z
- `kubeflow/sdk` — 2026-06-08T03:07:18Z
- `plurigrid/gorj` — 2026-06-08 (this repo)

### GF(3) Color Chain Distribution

All 272 increments assigned by `id % 3`:

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 (ERGODIC) | `#d3869b` | ERGODIC | 91 |
| 1 (PLUS) | `#b8bb26` | PLUS | 91 |
| -1 (MINUS) | `#cc241d` | MINUS | 90 |

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, `#d3869b` ERGODIC
- `id mod 3 == 1` → trit=1, `#b8bb26` PLUS
- `id mod 3 == 2` → trit=-1, `#cc241d` MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com` with 1s sleep between calls.

**Result:** All 28 addresses returned 0.0 APT — no initialized `CoinStore<AptosCoin>` resource found on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisigs healthy — 2-of-N threshold confirmed on Aptos mainnet.**

### MNX Markets

`testnet.mnx.fi` returned Vercel authentication (HTTP 401). Market data unavailable without bypass token. `mnx_snapshots` table empty.

---

## DuckDB Table Summary

```
world_increments    272 rows  — GF(3) trit-colored increment log
repo_snapshots      272 rows  — repo metadata per increment
aptos_snapshots      28 rows  — hamming swarm wallet balances
multisig_probes       5 rows  — multisig health probes
mnx_snapshots         0 rows  — MNX markets (Vercel auth blocked)
```

---

*Generated 2026-06-08 by world-increment-sweep + hamming-swarm-snapshot agent — plurigrid/gorj*
