# World-Increment Sweep — 2026-07-18

## Sweep Metadata
- **Date:** 2026-07-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 (13 unique IDs; id=13 = this run) |
| Total Repo Snapshots | 944 (cumulative across all sweeps) |
| Total Aptos Snapshots | 28 |
| Total Multisig Probes | 5 |
| GitHub Scope | plurigrid/gorj (session-scoped; social graph carried from prior sweeps) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Increment 13 — PLUS

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid/gorj | sweep_run | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `... ERGODIC (12) → **PLUS (13)** → MINUS (14) → ERGODIC (15) → ...`

### Access Note
Session is scoped to `plurigrid/gorj`. External orgs (`kubeflow`, `TeglonLabs`) and user graphs (`bmorphism`, `zubyul`, `migalkin`, `DJedamski`, `wasita`, `kristinezheng`, `M1shaaa`, `AustinCStone`) are outside session scope. Repo snapshot count (944) is cumulative from all prior sweeps.

### Recent gorj Commits
| SHA | Message | Date |
|-----|---------|------|
| 5b28fe0 | chore: ignore duckdb binary in repo root | 2026-05-08 |
| ebf263f | world-increment ducklake: sync world.duckdb sweep state | 2026-04-14 |
| b434a43 | Merge sweep state into master | 2026-04-14 |
| e76792f | world-increments.duckdb: sync latest sweep state | 2026-04-14 |
| 631518b | world-increment sweep 2026-04-12: insert id=12 ERGODIC | 2026-04-12 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-18)

All 28 Hamming swarm addresses queried via `fullnode.mainnet.aptoslabs.com`. CoinStore resources responded for all — **all balances 0 APT**.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...512d | 0.0 |
| A–Z   | (26 addresses)      | 0.0 each |

**Total APT across all 28 addresses: 0.0 APT**

### Multisig Contract Probes (Aptos Mainnet, 2026-07-18)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All **healthy** — 2-of-2 threshold confirmed.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisig contracts healthy.**

### MNX Markets (testnet.mnx.fi)

**Unavailable** — Vercel authentication gate active. API paths `/api/markets` and `/api/v1/markets` returned no JSON data.

---

## Historical GF(3) Color Chain (IDs 1–13)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1  | plurigrid (org) | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism / sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| 13 | plurigrid/gorj (this run) | +1 | `#b8bb26` | **PLUS** |

GF(3) cycle: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Notable Highlights (carried from prior sweeps)
- **kubeflow/kubeflow**: 15,565 stars — ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK using oxcaml_effect
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **plurigrid/asi**: 16 stars — topological chemputer

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
