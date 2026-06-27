# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-27

## Sweep Metadata
- **Date:** 2026-06-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Ledger version (Aptos):** ~5,962,865,812

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all-time) | 36 |
| New Increments (this sweep) | 13 |
| Total Repo Snapshots (all-time) | 1,425 |
| New Repo Snapshots (this sweep) | 481 |
| Sources Covered | 3 orgs + 8 users + 2 event streams |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA, no JSON API) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — Increments 13–25

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 13 | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |
| 24 | bmorphism | event | 0 | `#d3869b` | **ERGODIC** |
| 25 | zubyul | event | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 56 |
| bmorphism | user | 100 |
| zubyul | user | 27 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| wasita | user | 32 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| **Total** | | **481** |

---

### Top Repos by Stars (this sweep)

| Source | Repo | Language | Stars | Last Push |
|--------|------|----------|-------|-----------|
| kubeflow | kubeflow | — | 15,748 | 2026-06-18 |
| kubeflow | pipelines | Python | 4,157 | 2026-06-26 |
| kubeflow | spark-operator | Python | 3,129 | 2026-06-26 |
| kubeflow | trainer | Go | 2,124 | 2026-06-26 |
| kubeflow | katib | Python | 1,687 | 2026-06-23 |
| kubeflow | examples | Jsonnet | 1,460 | 2025-04-14 |
| kubeflow | community-distribution | YAML | 1,028 | 2026-06-25 |
| kubeflow | arena | Go | 813 | 2026-06-26 |
| kubeflow | kale | Python | 694 | 2026-06-25 |
| migalkin | NodePiece | Python | 144 | 2022-02-02 |
| bmorphism | ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid | asi | HTML | 26 | 2026-06-26 |
| bmorphism | anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |

---

### plurigrid — Top Repos

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-26 |
| asi-skills | Julia | 3 | 2026-04-26 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| place | TeX | 1 | 2026-06-27 |
| UnwiringDiagrams.jl | Julia | 1 | 2026-04-26 |

---

### bmorphism — Recent Events (last 10)

| Event | Repo | Timestamp |
|-------|------|-----------|
| PushEvent | plurigrid/asi | 2026-06-26T02:57Z |
| PullRequestEvent | plurigrid/asi | 2026-06-26T02:48Z |
| PushEvent | plurigrid/asi | 2026-06-26T02:48Z |
| PullRequestEvent | plurigrid/asi | 2026-06-26T02:47Z |
| CreateEvent | plurigrid/asi | 2026-06-26T02:39Z |
| WatchEvent | Qiskit/qiskit | 2026-06-23T01:18Z |
| WatchEvent | PrimeIntellect-ai/prime-rl | 2026-06-21T04:41Z |
| PushEvent | bmorphism/satreadout | 2026-06-20T13:05Z |
| WatchEvent | lanl/color | 2026-06-20T10:43Z |
| WatchEvent | bhauman/clojure-mcp-light | 2026-06-20T09:15Z |

**Signal:** bmorphism is actively pushing to `plurigrid/asi` and watching Qiskit + prime-rl (AI/quantum theme).

### zubyul — Recent Events (last 10)

| Event | Repo | Timestamp |
|-------|------|-----------|
| PullRequestEvent | plurigrid/gorj | 2026-06-27T13:12Z |
| CreateEvent | plurigrid/gorj | 2026-06-27T13:12Z |
| PullRequestEvent | plurigrid/gorj | 2026-06-27T12:14Z |
| CreateEvent | plurigrid/gorj | 2026-06-27T12:13Z |
| PullRequestEvent | plurigrid/gorj | 2026-06-27T11:10Z |
| CreateEvent | plurigrid/gorj | 2026-06-27T11:10Z |
| PullRequestEvent | plurigrid/gorj | 2026-06-27T10:13Z |
| CreateEvent | plurigrid/gorj | 2026-06-27T10:12Z |
| PullRequestEvent | plurigrid/gorj | 2026-06-27T09:10Z |
| CreateEvent | plurigrid/gorj | 2026-06-27T09:10Z |

**Signal:** zubyul is opening PRs/branches on `plurigrid/gorj` at ~1h intervals all day 2026-06-27 — likely automated sweep runs.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — Mainnet

All 28 wallets (alice, bob, A–Z) returned `resource_not_found` at ledger ~5,962,865,812. These accounts have not been initialized on Aptos mainnet — no APT CoinStore resource exists.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

**Total APT across all wallets: 0.0** (all accounts uninitialized on mainnet)

---

### Multisig Contract Probes — Mainnet

All 5 multisig contracts are healthy (respond to `num_signatures_required` view function).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisigs require **2-of-N signatures**. All 5 contracts exist and are responding on mainnet.

---

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — the testnet serves a SPA (React/Next.js) with no accessible JSON API. Direct root fetch returns HTTP 401; all probed API paths (`/api/markets`, `/api/v1/markets`, `/api/pools`) return the SPA HTML shell. No market data could be extracted.

---

## Database State

```
world_increments : 36 rows (IDs 1–25 + prior)
repo_snapshots   : 1,425 rows
aptos_snapshots  : 28 rows
multisig_probes  : 5 rows
mnx_snapshots    : 1 row (unavailable sentinel)
```

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-06-27*
