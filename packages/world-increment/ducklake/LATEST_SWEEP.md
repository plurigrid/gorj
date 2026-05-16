# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-16

## Sweep Metadata
- **Date:** 2026-05-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.x (current latest)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 40 |
| kubeflow | org | 19 |
| TeglonLabs | org | 4 |
| bmorphism | user | 20 |
| zubyul | user | 13 |
| migalkin | social-graph (zubyul) | 5 |
| DJedamski | social-graph (zubyul) | 2 |
| wasita | social-graph (zubyul) | 4 |
| kristinezheng | social-graph (zubyul) | 2 |
| M1shaaa | social-graph (zubyul) | 2 |
| AustinCStone | social-graph (zubyul) | 4 |
| **Total** | | **115** |

### GF(3) Color Chain Distribution (115 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 38 |
| 1 | `#b8bb26` | PLUS | 39 |
| -1 | `#cc241d` | MINUS | 38 |

### Notable Repos by Stars

| Full Name | Stars | Language | Pushed |
|-----------|-------|----------|--------|
| kubeflow/kubeflow | 15,635 | — | 2026-05-07 |
| kubeflow/pipelines | 4,139 | Python | 2026-05-15 |
| kubeflow/spark-operator | 3,125 | Python | 2026-05-15 |
| kubeflow/trainer | 2,098 | Go | 2026-05-15 |
| kubeflow/katib | 1,682 | Python | 2026-05-09 |
| kubeflow/examples | 1,463 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,017 | YAML | 2026-05-16 |
| kubeflow/arena | 810 | Go | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp | 23 | JavaScript | 2026-01-16 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |

### Most Active (Pushed May 2026)

- `kubeflow/manifests` — 2026-05-16 (TODAY)
- `plurigrid/gorj` — 2026-05-16 (THIS REPO)
- `bmorphism/Gay.jl` — 2026-05-16
- `kubeflow/pipelines` — 2026-05-15
- `kubeflow/spark-operator` — 2026-05-15
- `kubeflow/trainer` — 2026-05-15
- `bmorphism/oxgame` — 2026-05-15
- `wasita/wasita.github.io` — 2026-05-14
- `kubeflow/website` — 2026-05-14
- `kristinezheng/kristinezheng.github.io` — 2026-05-14

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses probed on Aptos mainnet (fullnode.mainnet.aptoslabs.com).
No `CoinStore<AptosCoin>` resource found on any address — accounts are uninitiated or hold non-APT assets.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793acd... | 0.0 |
| bob | 0x0a3c00c... | 0.0 |
| A–Z (26 addresses) | 0x8699edc...–0x7af0ef6... | 0.0 each |

**Total APT across swarm: 0.0 APT**

### Multisig Contract Probes (0x1::multisig_account)

All 5 multisig contracts **HEALTHY** — each requires 2-of-N signatures.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f42... | 2 | HEALTHY |
| A-G | 0xf56c4a1... | 2 | HEALTHY |
| Y-Z | 0xd3ffe18... | 2 | HEALTHY |
| S-T | 0x3b1c3ae... | 2 | HEALTHY |
| V-W | 0x40fad7b... | 2 | HEALTHY |

### MNX Markets

`testnet.mnx.fi` serves a Next.js SPA (dark theme). Neither `/api/markets` nor `/api/v1/markets` returns JSON — both return the SPA HTML shell. Market data loaded client-side only.
**Status: UNAVAILABLE (SPA only, no public REST API)**

---

## DuckDB Schema & Counts

```
world_increments   115 rows  — GF(3) colored repo push events
repo_snapshots     115 rows  — full repo metadata (stars, forks, lang, pushed_at)
aptos_snapshots     28 rows  — Hamming swarm APT balances at sweep time
multisig_probes      5 rows  — 2-of-N sig threshold for each pair
mnx_snapshots        0 rows  — MNX SPA, no REST API data
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,635 stars — flagship ML platform for Kubernetes (growing since April sweep)
- **kubeflow/pipelines**: 4,139 stars — most active ML pipeline project (pushed today)
- **bmorphism/Gay.jl**: 188 open issues — most active bmorphism repo right now
- **migalkin/NodePiece**: 144 stars — ICLR22 KG representation paper
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK with Jane Street oxcaml_effect
- **plurigrid/gorj**: THIS REPO — forj + Rama topology nREPL + GF(3) trit coloring
- **All multisig pairs**: 2-of-N healthy — Hamming swarm contracts operational
- **All APT balances**: 0.0 — swarm addresses uninitiated on mainnet
