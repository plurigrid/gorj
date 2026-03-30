# World Increment Sweep — 2026-03-30

## Sweep Metadata
- **Date:** 2026-03-30T13:15:00Z
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Social Graph Sweep

### Coverage

| Type | Name | Status |
|------|------|--------|
| Org | plurigrid | OK — 20 repos captured |
| Org | kubeflow | OK — 20 repos captured |
| Org | TeglonLabs | OK — 7 repos captured |
| User | bmorphism | OK — 8 repos captured |
| User | zubyul | OK — 6 repos captured |
| User | migalkin | OK — 4 repos captured |
| User | DJedamski | OK — 3 repos captured |
| User | wasita | OK — 3 repos captured |
| User | kristinezheng | OK — 2 repos captured |
| User | M1shaaa | OK — 3 repos captured |
| User | AustinCStone | OK — 2 repos captured |

- **Total orgs queried:** 3
- **Total users queried:** 8
- **Total repos captured:** 78
- **Rate limit notes:** Unauthenticated GitHub API rate limits caused delays; all data eventually retrieved.

### Top 5 Repos by Stars

| # | full_name | Stars | Language |
|---|-----------|-------|----------|
| 1 | kubeflow/kubeflow | 15,542 | — |
| 2 | kubeflow/pipelines | 4,113 | Python |
| 3 | kubeflow/spark-operator | 3,110 | Python |
| 4 | kubeflow/trainer | 2,069 | Go |
| 5 | kubeflow/katib | 1,673 | Python |

### GF(3) Color Chain Distribution

| trit | color | name | count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 26 |
| 1 | #b8bb26 | PLUS | 26 |
| 2 | #cc241d | MINUS | 26 |

---

## Recent Events (bmorphism + zubyul)

### bmorphism (top 10)
| Event Type | Repo | Time |
|-----------|------|------|
| CreateEvent | plurigrid/asi | 2026-03-30T10:57:01Z |
| PushEvent | plurigrid/horse | 2026-03-30T08:44:00Z |
| PushEvent | plurigrid/horse | 2026-03-30T08:42:08Z |
| PullRequestEvent | plurigrid/horse | 2026-03-30T08:20:36Z |
| CreateEvent | plurigrid/horse | 2026-03-30T08:18:53Z |

### zubyul (top 10)
| Event Type | Repo | Time |
|-----------|------|------|
| CreateEvent | plurigrid/gorj | 2026-03-30T12:30:55Z |
| PullRequestEvent | plurigrid/gorj | 2026-03-30T10:31:00Z |
| PushEvent | plurigrid/gorj | 2026-03-30T10:22:55Z |
| PushEvent | plurigrid/horse | 2026-03-30T10:12:24Z |
| PullRequestEvent | plurigrid/gorj | 2026-03-30T09:31:18Z |

---

## Aptos Hamming Swarm Snapshot

All wallets queried against `fullnode.mainnet.aptoslabs.com`. No CoinStore resources found — accounts do not hold APT balances on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793acde... | 0.0 |
| bob | 0x0a3c00c5... | 0.0 |
| A | 0x8699edc0... | 0.0 |
| B | 0x3f892ebe... | 0.0 |
| C | 0x38b99e63... | 0.0 |
| D | 0xf7765624... | 0.0 |
| E | 0xdc1d9d53... | 0.0 |
| F | 0x18a14b5b... | 0.0 |
| G | 0x69a394c0... | 0.0 |
| H | 0xce67c327... | 0.0 |
| I | 0x070fe5d7... | 0.0 |
| J | 0x4d964db8... | 0.0 |
| K | 0xa732040a... | 0.0 |
| L | 0x7c2eaeaf... | 0.0 |
| M | 0x6fed37a7... | 0.0 |
| N | 0xe7dde6da... | 0.0 |
| O | 0x73252b60... | 0.0 |
| P | 0x6218792d... | 0.0 |
| Q | 0xac40fa50... | 0.0 |
| R | 0x7ce605cc... | 0.0 |
| S | 0xb8753014... | 0.0 |
| T | 0x35781dc0... | 0.0 |
| U | 0x75860da4... | 0.0 |
| V | 0xb59dd817... | 0.0 |
| W | 0x5f32aef7... | 0.0 |
| X | 0xa95cbbd1... | 0.0 |
| Y | 0xd8e32848... | 0.0 |
| Z | 0x7af0ef6e... | 0.0 |

---

## Multisig Probes

All probes queried via `0x1::multisig_account::num_signatures_required` on mainnet.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f428... | 2 | YES |
| A-G | 0xf56c4a1c... | 2 | YES |
| Y-Z | 0xd3ffe181... | 2 | YES |
| S-T | 0x3b1c3ae9... | 2 | YES |
| V-W | 0x40fad7b4... | 2 | YES |

All 5 multisig accounts exist on mainnet with 2-of-N threshold. All healthy.

---

## MNX Markets

**Status: UNAVAILABLE**

Both `https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/v1/markets` returned HTTP 404. The `api.testnet.mnx.fi` subdomain responded with `Cannot GET /api/markets`. No market data available.

---

## Database Summary

- **Location:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:**
  - `world_increments`: 78 rows (GF3-colored repo sweep records)
  - `repo_snapshots`: 78 rows (full repo metadata)
  - `aptos_snapshots`: 28 rows (all balances 0.0 APT)
  - `multisig_probes`: 5 rows (all healthy, sigs_required=2)
  - `mnx_snapshots`: 0 rows (service unavailable)

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=2 (representing -1), color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,542 stars — flagship ML toolkit for Kubernetes
- **kubeflow/pipelines**: 4,113 stars — ML pipelines on Kubernetes
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **migalkin/NodePiece**: 143 stars — Compositional KG representations (ICLR 22)
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) coloring
