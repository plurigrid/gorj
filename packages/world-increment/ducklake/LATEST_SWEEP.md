# World-Increment Sweep — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) increment this run:** id=12 · trit=0 · `#d3869b` **ERGODIC**

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 944 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Rows | 1 (sentinel — unavailable) |

---

## Job 1 — GitHub Social Graph

**Session scope:** `plurigrid/gorj` only (MCP scoped; `gh` CLI unavailable in this environment).
Prior sweep snapshot of 944 repos across 3 orgs + 8 users retained in DB from April 2026 run.

### Open PRs — Accumulation Alert (10 unmerged today)

| PR | Branch | Created |
|----|--------|---------|
| #1433 | world-increment/sweep-2026-07-13-0313 | 2026-07-13T03:14Z |
| #1432 | world-increment/sweep-2026-07-13-0017 | 2026-07-13T00:18Z |
| #1431 | world-increment/sweep-2026-07-12-2311 | 2026-07-12T23:12Z |
| #1430 | world-increment/sweep-2026-07-12-2212 | 2026-07-12T22:12Z |
| #1429 | world-increment/sweep-2026-07-12-1911 | 2026-07-12T19:12Z |
| #1428 | world-increment/sweep-2026-07-12-1813 | 2026-07-12T18:14Z |
| #1427 | world-increment/sweep-2026-07-12-1713 | 2026-07-12T17:13Z |
| #1426 | world-increment/sweep-2026-07-12-1511 | 2026-07-12T15:13Z |
| #1425 | world-increment/sweep-2026-07-12-1216 | 2026-07-12T12:17Z |
| #1424 | world-increment/sweep-2026-07-12-1134 | 2026-07-12T11:35Z |

**None have been merged to master.** master remains at `5b28fe0`.

---

## Job 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses returned no `CoinStore` resource via the direct account resource endpoint.
Note: PR #1427 reported ~20.43 APT using the `0x1::coin::balance` view-function path — the two
call patterns give different results; the view-function path may be more reliable for future runs.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793acde... | N/A |
| bob   | 0x0a3c00c5... | N/A |
| A     | 0x8699edc0... | N/A |
| B     | 0x3f892ebe... | N/A |
| C     | 0x38b99e63... | N/A |
| D     | 0xf7765624... | N/A |
| E     | 0xdc1d9d53... | N/A |
| F     | 0x18a14b5b... | N/A |
| G     | 0x69a394c0... | N/A |
| H     | 0xce67c327... | N/A |
| I     | 0x070fe5d7... | N/A |
| J     | 0x4d964db8... | N/A |
| K     | 0xa732040a... | N/A |
| L     | 0x7c2eaeaf... | N/A |
| M     | 0x6fed37a7... | N/A |
| N     | 0xe7dde6da... | N/A |
| O     | 0x73252b60... | N/A |
| P     | 0x6218792d... | N/A |
| Q     | 0xac40fa50... | N/A |
| R     | 0x7ce605cc... | N/A |
| S     | 0xb8753014... | N/A |
| T     | 0x35781dc0... | N/A |
| U     | 0x75860da4... | N/A |
| V     | 0xb59dd817... | N/A |
| W     | 0x5f32aef7... | N/A |
| X     | 0xa95cbbd1... | N/A |
| Y     | 0xd8e32848... | N/A |
| Z     | 0x7af0ef6e... | N/A |

### Multisig Contract Probes (5/5 healthy)

All 5 pairs respond and require **2-of-2 signatures** — consistent across all sweeps.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B  | 0x0da4f428... | 2 | yes |
| A-G  | 0xf56c4a1c... | 2 | yes |
| Y-Z  | 0xd3ffe181... | 2 | yes |
| S-T  | 0x3b1c3ae9... | 2 | yes |
| V-W  | 0x40fad7b4... | 2 | yes |

### MNX Markets

`testnet.mnx.fi` — all REST API paths returned errors (Vercel auth wall or SPA with no public
endpoints). No market data captured. Consistent with all prior sweeps.

---

## GF(3) Color Chain

| id%3 | Trit | Color | Name |
|------|------|-------|------|
| 0 | 0 | `#d3869b` | ERGODIC |
| 1 | +1 | `#b8bb26` | PLUS |
| 2 | -1 | `#cc241d` | MINUS |

Current run: **id=12 → ERGODIC `#d3869b`**

---

## Recurring Observations

1. **MNX markets** — unavailable every run; needs authenticated session or not yet live.
2. **Aptos CoinStore** — direct resource endpoint returns 404 for all 28 addresses; view-function path found ~20 APT in prior run. Standardise on view-function path.
3. **PR accumulation** — 10 open PRs from today's sweeps, none merged into master. Consider merging the latest and closing the rest, or merging sweep data directly on master.
4. **GitHub scope** — org-level queries blocked in this session; social graph sweep needs broader access.
