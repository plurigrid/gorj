# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-09  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **297 repo snapshots** across 11 sources
- **11 world_increments** with GF(3) color chain

### Sources & GF(3) Colors

| id | source | type | repos | trit | color | name |
|----|--------|------|-------|------|-------|------|
| 1 | plurigrid | org | 30 | +1 | #b8bb26 | PLUS |
| 2 | kubeflow | org | 48 | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | org | 5 | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | user | 100 | +1 | #b8bb26 | PLUS |
| 5 | zubyul | user | 49 | -1 | #cc241d | MINUS |
| 6 | migalkin | user | 19 | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | user | 6 | +1 | #b8bb26 | PLUS |
| 8 | wasita | user | 11 | -1 | #cc241d | MINUS |
| 9 | kristinezheng | user | 5 | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | user | 8 | +1 | #b8bb26 | PLUS |
| 11 | AustinCStone | user | 30 | -1 | #cc241d | MINUS |

### Top Repos by Stars

| repo | stars | language | pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15709 | — | 2026-05-24 |
| kubeflow/pipelines | 4153 | Python | 2026-06-08 |
| kubeflow/spark-operator | 3126 | Python | 2026-06-08 |
| kubeflow/trainer | 2112 | Go | 2026-06-08 |
| kubeflow/katib | 1685 | Python | 2026-06-05 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |

### Notable Social Graph Signals

- **plurigrid/gorj** — 452 open issues, pushed 2026-06-09 (this very repo)
- **bmorphism/Gay.jl** — 189 open issues, active Julia GF(3) color library
- **M1shaaa/M1shaaa** — pushed 2026-06-09T02:48 (today, profile config update)
- **TeglonLabs/jank-crane** — pushed 2026-06-08 (newest org repo, C++ crane-jank IR hub)
- **kubeflow/dashboard** — pushed 2026-06-09T01:51 (most recent kubeflow push)
- **zubyul/voice-observatory** — passive macOS TUI for bmorphism/say-mcp-server

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm wallets (alice, bob, A-Z) returned **0.0 APT** at snapshot time (2026-06-09).

| wallet | address (prefix) | APT balance |
|--------|-----------------|-------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A | 0x8699ed… | 0.0 |
| B | 0x3f892e… | 0.0 |
| C–Z (24) | various | 0.0 each |

*All accounts exist on mainnet but hold zero APT coin balance.*

### Multisig Probes (5 pairs, all 2-of-2)

| pair | address (prefix) | sigs_required | healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

All multisig accounts use `0x1::multisig_account` with threshold 2/2.

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (authentication required). No market data extractable. Endpoints tried: root, `/api/markets`, `/api/v1/markets`.

---

## DuckDB Schema

```
world_increments  — 11 rows  (GF3 color chain per source)
repo_snapshots    — 297 rows (repo metadata snapshots)
aptos_snapshots   — 28 rows  (all 0.0 APT)
multisig_probes   — 5 rows   (all 2-of-2 healthy)
mnx_snapshots     — 1 row    (unavailable marker)
```

## GF(3) Color Legend

- **trit=0 ERGODIC** `#d3869b` — stable/neutral increment
- **trit=+1 PLUS** `#b8bb26` — positive/additive increment
- **trit=-1 MINUS** `#cc241d` — subtractive/contrastive increment
