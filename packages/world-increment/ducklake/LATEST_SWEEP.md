# World Increment Sweep — Hamming Swarm Snapshot

**Timestamp:** 2026-04-28T14:13:41Z
**Increment ID:** 17 · GF(3) trit=-1 · **MINUS** · `#cc241d`

---

## JOB 1: GitHub Social Graph

> **Status: GitHub API rate-limited (unauthenticated)**
> No `gh` CLI available and no auth token present. Requests from this IP
> (34.121.238.53) hit the 60 req/hr unauthenticated cap. GitHub MCP OAuth
> flow was initiated but requires user browser interaction; proceeding with
> existing ducklake history (944 repo snapshots from prior sweeps).

**Sources targeted:**
- Orgs: `plurigrid`, `kubeflow`, `TeglonLabs`
- Users: `bmorphism`, `zubyul`
- Social graph: `migalkin`, `DJedamski`, `wasita`, `kristinezheng`, `M1shaaa`, `AustinCStone`
- Events: `bmorphism` public events, `zubyul` public events

**Existing ducklake state:** 944 repo snapshots · 23 world increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried via `0x1::coin::balance` view function at ledger ~v5037214241.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| bob   | 0x0a3c00...512d5d   | **12.6570** |
| F     | 0x18a14b...3cf71    | 1.9605 |
| L     | 0x7c2eae...eba9     | 1.9273 |
| J     | 0x4d964d...7f54     | 1.8951 |
| alice | 0xc793ac...4cc7b    | 0.4364 |
| O     | 0x73252b...a89d     | 0.2101 |
| K     | 0xa73204...25dc4    | 0.1620 |
| P     | 0x62187...ec948     | 0.1401 |
| M     | 0x6fed37...7f2e9    | 0.1123 |
| N     | 0xe7dde6...551b2c   | 0.1061 |
| Q     | 0xac40fa...c89a9    | 0.1032 |
| R     | 0x7ce605...76e10    | 0.0902 |
| S     | 0xb87530...d0386    | 0.0918 |
| T     | 0x35781d...3f4588   | 0.0737 |
| U     | 0x75860d...ef9956   | 0.0558 |
| A     | 0x8699ed...be9d7a   | 0.0518 |
| V     | 0xb59dd8...af2c3    | 0.0488 |
| X     | 0xa95cbb...33047d   | 0.0426 |
| Y     | 0xd8e328...2444c4   | 0.0444 |
| W     | 0x5f32ae...ccc7b0   | 0.0407 |
| B     | 0x3f892e...77cb13   | 0.0363 |
| Z     | 0x7af0ef...e197c    | 0.0243 |
| C     | 0x38b99e...91535e   | 0.0102 |
| D     | 0xf77656...cfdd1    | 0.0116 |
| E     | 0xdc1d9d...8d36     | 0.0094 |
| H     | 0xce67c3...5300f    | 0.0017 |
| G     | 0x69a394...ccc7f32  | 0.0007 |
| I     | 0x070fe5...c1fc9    | 0.0007 |

**Total swarm APT:** 20.3448

**Top 3:** "(((world || ':') || round(balance_apt, 4)) || ' APT')",bob:12.657 APT,F:1.9605 APT,L:1.9273 APT

---

### Multisig Contract Probes

All 5 multisig accounts returned 2-of-N threshold. Status: **all healthy**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4f4...87003    | 2 | ✓ |
| A-G  | 0xf56c4a...c0096    | 2 | ✓ |
| Y-Z  | 0xd3ffe1...5b883    | 2 | ✓ |
| S-T  | 0x3b1c3a...7883     | 2 | ✓ |
| V-W  | 0x40fad7...0eb6d    | 2 | ✓ |

---

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no REST API accessible**
All paths (`/`, `/api/markets`, `/api/v1/markets`, `/markets`) return
Next.js HTML. No JSON market data extractable via HTTP. Recorded as
`MNX_UNAVAILABLE` in `mnx_snapshots`.

---

## DuckDB Ducklake State

`packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (approx) |
|-------|--------------|
| world_increments | 24+ |
| repo_snapshots | 944 |
| aptos_snapshots | 28 (this sweep) |
| multisig_probes | 5 (this sweep) |
| mnx_snapshots | 1 (unavailable) |

---

## GF(3) Color Chain

```
id % 3 == 0 → trit=0  ERGODIC  #d3869b ████
id % 3 == 1 → trit=1  PLUS     #b8bb26 ████
id % 3 == 2 → trit=-1 MINUS    #cc241d ████  ← sweep #17
```

