# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-04

## Sweep Metadata
- **Date:** 2026-05-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Session:** https://claude.ai/code/session_014CxTqJtSQ1GJtW5edEFFLf

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 26 |
| Total Repo Snapshots | 945 |
| New Increments This Run | 3 (ids 13–15) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA — no JSON API exposed |

---

## JOB 1: GitHub Social Graph Sweep

### Notes
- GitHub REST API is rate-limited for unauthenticated access from this IP
- GitHub MCP tools (scoped to `plurigrid/gorj`) used for commit and branch data
- Previous sweep data (2026-04-12) covers: plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone (471+ repos)

### plurigrid/gorj — Recent Activity (via MCP)
| SHA | Message | Date |
|-----|---------|------|
| ebf263f | world-increment ducklake: sync world.duckdb sweep state | 2026-04-14 |
| b434a43 | Merge sweep state into master | 2026-04-14 |
| e76792f | world-increments.duckdb: sync latest sweep state | 2026-04-14 |
| 631518b | world-increment sweep 2026-04-12: insert id=12 ERGODIC + regen LATEST_SWEEP.md | 2026-04-12 |
| c4238bc | world-increments.duckdb: sync latest sweep state | 2026-04-10 |
| bbcce38 | Merge sweep state into master | 2026-04-08 |

### Active Sweep Branches (sample, 63 total)
- `world-increment/sweep-2026-05-04-1509` (most recent before this run)
- `world-increment/sweep-2026-05-04-1427`
- `world-increment/sweep-2026-05-04-0119`
- `world-increment/sweep-2026-05-03-2331`

---

## GF(3) Color Chain — New Increments (ids 13–15)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid/gorj (repo) | commit_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | hamming_swarm (wallet) | aptos_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | aptos_mainnet (multisig) | multisig_probe | 0 | `#d3869b` | **ERGODIC** |

GF(3) continuation: `... ERGODIC(12) → PLUS(13) → MINUS(14) → ERGODIC(15)`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`,
indicating no APT balance / uninitialized CoinStore on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793ac…24cc7b | 0.0 |
| bob   | 0x0a3c00…512d5d | 0.0 |
| A     | 0x8699ed…9d7a   | 0.0 |
| B     | 0x3f892e…cb13   | 0.0 |
| C     | 0x38b99e…535e   | 0.0 |
| D     | 0xf77656…cfdd1  | 0.0 |
| E     | 0xdc1d9d…8d36   | 0.0 |
| F     | 0x18a14b…cf71   | 0.0 |
| G     | 0x69a394…c7f32  | 0.0 |
| H     | 0xce67c3…5300f  | 0.0 |
| I     | 0x070fe5…1fc9   | 0.0 |
| J     | 0x4d964d…7f54   | 0.0 |
| K     | 0xa73204…25dc4  | 0.0 |
| L     | 0x7c2eae…eba9   | 0.0 |
| M     | 0x6fed37…7f2e9  | 0.0 |
| N     | 0xe7dde6…51b2c  | 0.0 |
| O     | 0x73252b…a89d   | 0.0 |
| P     | 0x621879…ec948  | 0.0 |
| Q     | 0xac40fa…c89a9  | 0.0 |
| R     | 0x7ce605…76e10  | 0.0 |
| S     | 0xb87530…d0386  | 0.0 |
| T     | 0x35781d…3f4588 | 0.0 |
| U     | 0x75860d…ef9956 | 0.0 |
| V     | 0xb59dd8…af2c3  | 0.0 |
| W     | 0x5f32ae…cc7b0  | 0.0 |
| X     | 0xa95cbb…3047d  | 0.0 |
| Y     | 0xd8e328…2444c4 | 0.0 |
| Z     | 0x7af0ef…197c   | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts require **2 signatures** — all healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4f4…87003 | 2 | true |
| A-G  | 0xf56c4a…0096  | 2 | true |
| Y-Z  | 0xd3ffe1…b883  | 2 | true |
| S-T  | 0x3b1c3a…7883  | 2 | true |
| V-W  | 0x40fad7…eb6d  | 2 | true |

### MNX Markets (testnet.mnx.fi)
Status: **SPA — no JSON API endpoint exposed.** The site returns a Next.js single-page application; `/api/markets` and `/api/v1/markets` yield no structured data.

---

## DuckDB Table State

| Table | Rows |
|-------|------|
| world_increments | 26 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
