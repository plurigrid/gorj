# World-Increment Sweep + Hamming Snapshot — 2026-06-22

## Sweep Metadata
- **Date:** 2026-06-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 101 |
| Total Repo Snapshots | 101 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution (101 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 33 |
| +1 | `#b8bb26` | PLUS | 34 |
| -1 | `#cc241d` | MINUS | 34 |

Chain rule: `id%3==1 → PLUS, id%3==2 → MINUS, id%3==0 → ERGODIC`

---

## Top Repos by Stars (2026-06-22 snapshot)

| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/kubeflow | — | 15,740 | 2,680 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,157 | 2,009 | 2026-06-22 |
| kubeflow/spark-operator | Python | 3,128 | 1,491 | 2026-06-22 |
| kubeflow/trainer | Go | 2,118 | 970 | 2026-06-22 |
| kubeflow/katib | Python | 1,685 | 527 | 2026-06-22 |
| kubeflow/examples | Jsonnet | 1,460 | 756 | 2025-04-14 |
| kubeflow/community-distribution | YAML | 1,027 | 1,065 | 2026-06-18 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |

---

## Repo Counts by Source

| Source | Type | Repos Snapshotted | Known Total |
|--------|------|-------------------|-------------|
| plurigrid | org | 24 | 101 |
| kubeflow | org | 15 | 48 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 15 | 105 |
| zubyul | user | 10 | 49 |
| migalkin | user | 7 | 19 |
| wasita | user | 6 | 11 |
| M1shaaa | user | 5 | 8 |
| AustinCStone | user | 5 | 40 |
| DJedamski | user | 5 | 6 |
| kristinezheng | user | 4 | 5 |
| **TOTAL** | | **101** | **397** |

---

## Notable Activity (2026-06-22)

- **plurigrid/gorj** (this repo): 749 open issues — active forj+Rama+GF(3) REPL development
- **kubeflow/katib**: pushed 20:07 UTC — ML autotuning infra active
- **kubeflow/trainer**: pushed 19:44 UTC — distributed training infra active
- **bmorphism/Gay.jl**: 187 open issues — GF(3) color system central hub, pushed 22 Jun
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1 from April) — OCaml MCP SDK (Jane Street oxcaml_effect)
- **TeglonLabs/jank-crane**: new repo (Jun 2026) — crane-jank IR hub, GF3 convergence maps
- **zubyul/voice-observatory**: new (Apr 2026) — passive macOS TUI for voice-download pathways

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 2026-06-22 UTC
**Result: All 28 addresses (alice, bob, A–Z) returned 0 APT.**

All Hamming swarm addresses have zero balances. Accounts are either uninitialized (no `CoinStore<AptosCoin>` resource registered) or intentionally empty — consistent with addresses being pre-allocated but not yet funded.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | 0.0 APT |
| bob | 0x0a3c...2d5d | 0.0 APT |
| A–Z | 26 addresses | 0.0 APT each |

### Multisig Contract Probes
All 5 multisig accounts respond and require **2 signatures** — all healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Vercel deployment protection active on all paths. Requires visitor password or Vercel OIDC trusted-source bypass token.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
