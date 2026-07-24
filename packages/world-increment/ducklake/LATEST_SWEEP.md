# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 405 |
| Total Repo Snapshots (unique) | 647 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Snapshotted | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 / 5 healthy |
| MNX Markets | SPA — no API data |

---

## GF(3) Color Chain — 405 Increments

Each repo push event in this sweep is assigned a GF(3) trit and color:

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| PLUS | +1 | `#b8bb26` | 136 |
| MINUS | -1 | `#cc241d` | 135 |
| ERGODIC | 0 | `#d3869b` | 134 |

Assignment rule: `id mod 3 == 0 → ERGODIC`, `id mod 3 == 1 → PLUS`, `id mod 3 == 2 → MINUS`

---

## Top Repos by Stars (2026-07-24 snapshot)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|------------|
| kubeflow/kubeflow | 15,792 | — | 2026-07-10 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-24 ✓ today |
| kubeflow/spark-operator | 3,143 | Python | 2026-07-17 |
| kubeflow/trainer | 2,153 | Go | 2026-07-24 ✓ today |
| kubeflow/katib | ~1,680 | Python | 2026-07 |
| migalkin/NodePiece | 143 | Python | — |
| migalkin/StarE | 88 | Python | — |
| AustinCStone/TextGAN | 92 | Python | — |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | — |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |

## Activity Signals (most recent pushes)

| Repo | Last Pushed | Note |
|------|-------------|------|
| M1shaaa/M1shaaa | 2026-07-24T13:28Z | Active today |
| kubeflow/pipelines | 2026-07-24T18:57Z | Active today |
| kubeflow/trainer | 2026-07-24T02:02Z | Active today |
| wasita/wasita.github.io | 2026-07-21T15:52Z | 3 days ago |
| kristinezheng/kristinezheng.github.io | 2026-07-01 | — |
| TeglonLabs/jank-crane | 2026-06-08 | crane-jank GF3 converged-IR hub |

---

## Repo Counts by Source (2026-07-24)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 (103 total on GH) |
| bmorphism | user | 100 (106 total) |
| TeglonLabs | org | 5 |
| kubeflow | org | 49 |
| AustinCStone | social graph | 41 |
| migalkin | social graph | 19 |
| wasita | social graph | 12 |
| zubyul | user | 49 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| DJedamski | social graph | 6 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances — 28 wallets

**All 28 wallets show 0.00000000 APT** at snapshot time (2026-07-24). Accounts exist on-chain but hold no native APT coin balance.

Wallets: alice, bob, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z

### Multisig Contract Probes

**All 5 probed — all healthy (2-of-2 signatures required)**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no accessible JSON API**. The testnet.mnx.fi endpoint returns a Next.js SPA. No market data was extractable from static responses; `/api/markets` returned HTML. Recorded as unavailable in `mnx_snapshots`.

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

## Notable Highlights (2026-07-24)
- **kubeflow/kubeflow**: 15,792 stars (+227 since April sweep) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars — ML pipeline pushed **today** (2026-07-24T18:57Z)
- **kubeflow/trainer**: 2,153 stars — pushed today (2026-07-24T02:02Z)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **TeglonLabs/jank-crane**: `crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow` (C++, 2026-06-08)
- **M1shaaa/M1shaaa**: profile repo updated **today at 13:28Z**
- **Hamming swarm**: All 28 Aptos wallets at 0 APT; all 5 multisigs healthy (2-of-2)
- **MNX testnet**: SPA only, no market API accessible

*Previous sweep: 2026-04-12 (12 increments, 471 repo snapshots). This sweep: 405 increments, 647 unique repos.*
