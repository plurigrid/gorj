# World-Increment Sweep — 2026-06-23

## Sweep Metadata
- **Date:** 2026-06-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 404 (cumulative) |
| This Sweep Repo Snapshots | 381 |
| Cumulative Repo Snapshots | 1,325 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain (this sweep, first 12 and last 3)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1  | plurigrid/asi | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid/place | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid/eirobri | 0 | `#d3869b` | **ERGODIC** |
| 4  | plurigrid/nash-portal | +1 | `#b8bb26` | **PLUS** |
| 5  | plurigrid/gorj | -1 | `#cc241d` | **MINUS** |
| 6  | plurigrid/zig-syrup | 0 | `#d3869b` | **ERGODIC** |
| 7  | plurigrid/asi-skills | +1 | `#b8bb26` | **PLUS** |
| 8  | plurigrid/bci-blue-share | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid/nanoclj-zig | 0 | `#d3869b` | **ERGODIC** |
| 10 | plurigrid/spi-race | +1 | `#b8bb26` | **PLUS** |
| ... | ... | ... | ... | ... |
| 379 | AustinCStone/lexer | 0 | `#d3869b` | **ERGODIC** |
| 380 | AustinCStone/HTTPCache | +1 | `#b8bb26` | **PLUS** |
| 381 | (sweep complete) | -1 | `#cc241d` | **MINUS** |

GF(3) rule: `id%3==0` → ERGODIC `#d3869b` | `id%3==1` → PLUS `#b8bb26` | `id%3==2` → MINUS `#cc241d`

---

## Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,739 | — | 2026-06-18 |
| kubeflow/pipelines | 4,157 | Python | 2026-06-23 |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-23 |
| kubeflow/trainer | 2,119 | Go | 2026-06-22 |
| kubeflow/katib | 1,685 | Python | 2026-06-23 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-06-18 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-22 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 97 |
| kubeflow | org | 49 |
| bmorphism | user | 100 |
| zubyul | user | 50 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **390** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-23)

All 28 wallets queried: alice, bob, A–Z. **All returned 0 APT** — `CoinStore` resource not found or zero balance. Accounts may be uninitialized for APT.

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✅ healthy |
| V-W | 0x40fad7b4... | 2 | ✅ healthy |

**All 5 multisig contracts operational: 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment protection active. No API accessible without bypass token or trusted-source OIDC. `mnx_snapshots` table empty.

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

## Notable Highlights (2026-06-23)

- **plurigrid/gorj**: 766 open issues, pushed today — forj + Rama topology nREPL routing + GF(3) trit coloring
- **bmorphism/Gay.jl**: 187 open issues, pushed today — wide-gamut splittable determinism (2→+1 stars since Apr)
- **kubeflow/sdk**: 120 stars, 134 open issues — new Universal Python SDK pushed today
- **kubeflow/pipelines**: 4,157 stars (↑38 from Apr) — active development
- **bmorphism/ocaml-mcp-sdk**: 61 stars (↑1) — OCaml SDK for MCP
- **AustinCStone/TextGAN**: 92 stars — stable classic GAN for text
- **M1shaaa/M1shaaa**: profile repo pushed today (2026-06-23)
