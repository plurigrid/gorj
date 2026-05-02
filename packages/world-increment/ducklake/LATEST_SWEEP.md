# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-02

## Sweep Metadata
- **Date:** 2026-05-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 15 |
| kubeflow | org | 12 |
| TeglonLabs | org | 4 |
| bmorphism | user | 11 |
| zubyul | user | 8 |
| migalkin | user (zubyul graph) | 4 |
| DJedamski | user (zubyul graph) | 2 |
| wasita | user (zubyul graph) | 4 |
| kristinezheng | user (zubyul graph) | 2 |
| M1shaaa | user (zubyul graph) | 2 |
| AustinCStone | user (zubyul graph) | 4 |
| **TOTAL** | | **66 repos stored** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 22 |
| +1 | `#b8bb26` | PLUS | 22 |
| -1 | `#cc241d` | MINUS | 22 |

Perfectly balanced ternary distribution across all 66 increments.

### Notable Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15615 | — | 2026-04-29 |
| kubeflow/pipelines | 4130 | Python | 2026-05-01 |
| kubeflow/spark-operator | 3121 | Python | 2026-04-28 |
| kubeflow/trainer | 2095 | Go | 2026-05-01 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-28 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| plurigrid/asi | 17 | HTML | 2026-04-26 |
| plurigrid/gorj | 0 | Clojure | 2026-05-02 |

### Most Active (recent pushes)

- `plurigrid/gorj` — pushed 2026-05-02 (today)
- `kubeflow/hub` — pushed 2026-05-01
- `kubeflow/pipelines` — pushed 2026-05-01
- `kubeflow/trainer` — pushed 2026-05-01
- `bmorphism/magic-world-org` — pushed 2026-05-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com` with 1s delay between calls.
The CoinStore resource returned null for all addresses — no on-chain APT coin store registered.

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | unfunded |
| bob | 0.0 | unfunded |
| A–Z (26 addresses) | 0.0 each | unfunded |

**Total APT across swarm: 0.0 APT**

### Multisig Contract Probes

All 5 multisig contracts healthy, each requiring **2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883` | 2 | ✓ |
| V-W | `0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d` | 2 | ✓ |

**5/5 multisig contracts healthy** — all 2-of-N threshold, contracts confirmed on-chain.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a **Next.js SPA** — no REST API endpoints accessible at `/api/markets` or `/api/v1/markets`. Market data unavailable via plain HTTP; requires JS execution or WebSocket. Recorded as `unavailable` in `mnx_snapshots`.

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 66 | GF(3)-colored repo push events |
| `repo_snapshots` | 66 | Full repo metadata per increment |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig contract health checks |
| `mnx_snapshots` | 1 | MNX market data (SPA, unavailable) |

---

## GF(3) Assignment Rule

```
id mod 3 == 0  →  trit=0,  color=#d3869b,  name=ERGODIC
id mod 3 == 1  →  trit=+1, color=#b8bb26,  name=PLUS
id mod 3 == 2  →  trit=-1, color=#cc241d,  name=MINUS
```
