# World-Increment Sweep — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via Python duckdb package)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment:** id=13 — **PLUS** (GF3 trit=1, color=#b8bb26)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 945 |
| Aptos Wallet Snapshots | 28 (NULL balance — egress blocked) |
| Multisig Probes | 5 (unhealthy — egress blocked) |
| MNX Market Snapshots | 0 (unavailable — egress blocked) |

---

## GF(3) Color Chain — Increment #13

| Field | Value |
|-------|-------|
| id | 13 |
| trit | 1 |
| color | #b8bb26 |
| name | **PLUS** |
| source_type | sweep_agent |
| event_type | network_blocked_egress |
| repo | plurigrid/gorj |
| actor | zubyul |
| snapshot_hash | derived from SHA 5b28fe0… |

GF(3) chain continues: `…ERGODIC(12) → PLUS(13) → …`

---

## JOB 1: GitHub Social Graph Sweep

### Access Status

| Source | Type | Status |
|--------|------|--------|
| plurigrid/gorj | repo | **MCP only** — 1 repo accessible |
| plurigrid (full org) | org | BLOCKED — api.github.com denied by egress policy |
| kubeflow | org | BLOCKED — 403 from proxy |
| TeglonLabs | org | BLOCKED — 403 from proxy |
| bmorphism | user | BLOCKED — 403 from proxy |
| zubyul | user | BLOCKED — 403 from proxy |
| migalkin | social graph | BLOCKED — 403 from proxy |
| DJedamski | social graph | BLOCKED — 403 from proxy |
| wasita | social graph | BLOCKED — 403 from proxy |
| kristinezheng | social graph | BLOCKED — 403 from proxy |
| M1shaaa | social graph | BLOCKED — 403 from proxy |
| AustinCStone | social graph | BLOCKED — 403 from proxy |

### Accessible Data: plurigrid/gorj (via GitHub MCP)

- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL
- **Language:** Clojure
- **Last pushed:** 2026-05-08T14:04:34Z
- **Latest commit:** `5b28fe0` — chore: ignore duckdb binary in repo root
- **Active branches:** 60+ world-increment/sweep-\* branches (April–May 2026)
- **Recent commit authors:** claude (automated sweeps), zubyul

### Recent Commit History (plurigrid/gorj)

| Date | SHA | Message |
|------|-----|---------|
| 2026-05-08 | 5b28fe0 | chore: ignore duckdb binary in repo root |
| 2026-04-14 | ebf263f | world-increment ducklake: sync world.duckdb sweep state |
| 2026-04-14 | b434a43 | Merge sweep state into master |
| 2026-04-12 | 631518b | world-increment sweep 2026-04-12: insert id=12 ERGODIC |
| 2026-04-10 | c4238bc | world-increments.duckdb: sync latest sweep state |
| 2026-04-08 | bbcce38 | Merge sweep state into master |

### Prior Sweep Coverage (from DB)

The existing `repo_snapshots` table (944 rows prior to this sweep) reflects the April 2026 sweep with coverage across:
plurigrid (100), bmorphism (100), TeglonLabs (53), kubeflow (47), AustinCStone (43), migalkin (30), wasita (29), zubyul (24), kristinezheng (18), M1shaaa (16), DJedamski (11).

This sweep adds 1 row for `plurigrid/gorj` (id=474) to mark the 2026-07-13 checkpoint.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Status: BLOCKED** — `fullnode.mainnet.aptoslabs.com` denied by egress policy (403 from proxy).

All 28 addresses (alice, bob, A–Z) recorded with `balance_apt = NULL` as sentinel for this sweep cycle.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793ac…4cc7b | NULL (blocked) |
| bob | 0x0a3c00…512d5d | NULL (blocked) |
| A | 0x8699ed…9d7a | NULL (blocked) |
| B | 0x3f892e…cb13 | NULL (blocked) |
| C | 0x38b99e…535e | NULL (blocked) |
| D | 0xf77656…cfdd1 | NULL (blocked) |
| E | 0xdc1d9d…8d36 | NULL (blocked) |
| F | 0x18a14b…cf71 | NULL (blocked) |
| G | 0x69a394…7f32 | NULL (blocked) |
| H | 0xce67c3…5300f | NULL (blocked) |
| I | 0x070fe5…1fc9 | NULL (blocked) |
| J | 0x4d964d…7f54 | NULL (blocked) |
| K | 0xa73204…25dc4 | NULL (blocked) |
| L | 0x7c2eae…eba9 | NULL (blocked) |
| M | 0x6fed37…7f2e9 | NULL (blocked) |
| N | 0xe7dde6…51b2c | NULL (blocked) |
| O | 0x73252b…5a89d | NULL (blocked) |
| P | 0x621879…ec948 | NULL (blocked) |
| Q | 0xac40fa…c89a9 | NULL (blocked) |
| R | 0x7ce605…76e10 | NULL (blocked) |
| S | 0xb87530…0386 | NULL (blocked) |
| T | 0x357810…4588 | NULL (blocked) |
| U | 0x758600…f9956 | NULL (blocked) |
| V | 0xb59dd8…af2c3 | NULL (blocked) |
| W | 0x5f32ae…c7b0 | NULL (blocked) |
| X | 0xa95cbb…3047d | NULL (blocked) |
| Y | 0xd8e328…444c4 | NULL (blocked) |
| Z | 0x7af0ef…197c | NULL (blocked) |

### Multisig Contract Probes

**Status: BLOCKED** — same egress policy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f4…87003 | NULL | false |
| A-G | 0xf56c4a…0096 | NULL | false |
| Y-Z | 0xd3ffe1…5b883 | NULL | false |
| S-T | 0x3b1c3a…7883 | NULL | false |
| V-W | 0x40fad7…0eb6d | NULL | false |

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` blocked by egress policy. No market data captured.

---

## Egress Policy Note

The session's network policy allows `pypi.org`, `files.pythonhosted.org`, and GitHub MCP (injected token) but denies direct outbound HTTPS to:
- `api.github.com` (GitHub REST API — needed for org/user repo sweeps)
- `objects.githubusercontent.com` (GitHub release CDN — DuckDB CLI download failed)
- `fullnode.mainnet.aptoslabs.com` (Aptos mainnet RPC)
- `testnet.mnx.fi` (MNX markets)

To enable full sweeps, add these hosts to the session's egress allowlist.

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

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent on 2026-07-13*
