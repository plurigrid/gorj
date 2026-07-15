# World-Increment Sweep — 2026-07-15

## Sweep Metadata
- **Date:** 2026-07-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 26 (IDs 1–15, with prior multi-sweep rows) |
| New Increments (this run) | 3 (IDs 13–15) |
| Aptos Wallets Snapshotted | 28 |
| Multisig Pairs Probed | 5 |
| MNX Markets | unavailable (Vercel auth required) |
| GitHub Sweep | partial (org/user endpoints proxy-blocked; gorj only) |

---

## JOB 1: GitHub Social Graph Sweep

> **Note:** GitHub org/user list endpoints (`/orgs/{org}/repos`, `/users/{user}/repos`) are restricted by the environment proxy to the scoped repository (`plurigrid/gorj`). Queried via GitHub MCP instead.

### gorj (plurigrid/gorj) — Recent Commits

| SHA | Author | Date | Message |
|-----|--------|------|---------|
| 5b28fe0 | claude | 2026-05-08 | chore: ignore duckdb binary in repo root |
| ebf263f | claude | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| b434a43 | claude | 2026-04-14 | Merge sweep state into master |
| e76792f | claude | 2026-04-14 | world-increments.duckdb: sync latest sweep state |
| 631518b | claude | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |

---

## GF(3) Color Chain — New Increments (IDs 13–15)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | gorj (org) | github_partial_sweep | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos_swarm (hamming) | hamming_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | world (sweep) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continues: `… ERGODIC(12) → PLUS(13) → MINUS(14) → ERGODIC(15)`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-07-15)

All balances queried via `0x1::primary_fungible_store::balance` (fungible asset standard).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | 0.4364 |
| bob   | 0x0a3c…12d5 | **12.6570** |
| A | 0x8699…9d7a | 0.0518 |
| B | 0x3f89…b13 | 0.0363 |
| C | 0x38b9…35e | 0.0102 |
| D | 0xf776…dd1 | 0.0116 |
| E | 0xdc1d…d36 | 0.0094 |
| F | 0x18a1…f71 | **1.9605** |
| G | 0x69a3…f32 | 0.0007 |
| H | 0xce67…00f | 0.0017 |
| I | 0x070f…c9 | 0.0007 |
| J | 0x4d96…f54 | **1.8951** |
| K | 0xa732…dc4 | 0.1620 |
| L | 0x7c2e…ba9 | **1.9273** |
| M | 0x6fed…e9 | 0.1123 |
| N | 0xe7dd…b2c | 0.1061 |
| O | 0x7325…89d | 0.2101 |
| P | 0x6218…948 | 0.1401 |
| Q | 0xac40…a9 | 0.1032 |
| R | 0x7ce6…e10 | 0.0902 |
| S | 0xb875…386 | 0.0918 |
| T | 0x3578…588 | 0.0737 |
| U | 0x7586…956 | 0.0558 |
| V | 0xb59d…b3 | 0.0488 |
| W | 0x5f32…b0 | 0.0407 |
| X | 0xa95c…47d | 0.0426 |
| Y | 0xd8e3…4c4 | 0.0444 |
| Z | 0x7af0…97c | 0.0243 |
| **TOTAL** | | **20.3448 APT** |

Notable: bob holds 62% of total swarm balance (12.66 APT). F, J, L each ~1.9 APT.

---

### Multisig Contract Probes

All 5 multisig pairs are **healthy** (2-of-2 signatures required).

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…003 | 2 | healthy |
| A-G | 0xf56c…096 | 2 | healthy |
| Y-Z | 0xd3ff…883 | 2 | healthy |
| S-T | 0x3b1c…883 | 2 | healthy |
| V-W | 0x40fa…b6d | 2 | healthy |

---

### MNX Markets

`https://testnet.mnx.fi` — **unavailable** (Vercel authentication gate; no public API accessible).

---

## DB State After Sweep

| Table | Rows |
|-------|------|
| world_increments | 26 |
| repo_snapshots | 944 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (MNX unavailable) |
