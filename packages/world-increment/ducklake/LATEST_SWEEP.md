# LATEST_SWEEP — 2026-08-07 22:22:30 UTC

## Overview

| Job | Status |
|-----|--------|
| GitHub Social Graph Sweep | COMPLETE |
| Hamming Swarm Snapshot (Aptos) | COMPLETE |
| Multisig Probes | COMPLETE |
| MNX Markets | SPA — no JSON API exposed |

## JOB 1: GitHub Social Graph Sweep

**Total repo records in DB:** 1264  
**Unique repos (lifetime):** 648

### Sources Swept (This Run)

| Source | Type | GF3 | Color | Repos |
|--------|------|-----|-------|-------|

### Top Repos by Stars

| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15805 |
| kubeflow/kubeflow | 15572 |
| kubeflow/kubeflow | 15565 |
| kubeflow/pipelines | 4181 |
| kubeflow/pipelines | 4119 |

### Recently Active (pushed >= 2026-08-01)

| Repo | Pushed | Stars |
|------|--------|-------|
| plurigrid/gorj | 2026-08-07 | 1 |
| kubeflow/blog | 2026-08-07 | 32 |
| kubeflow/sdk | 2026-08-07 | 136 |
| kubeflow/pipelines | 2026-08-07 | 4181 |
| kubeflow/kale | 2026-08-07 | 699 |
| kubeflow/trainer | 2026-08-07 | 2174 |
| kubeflow/internal-acls | 2026-08-07 | 19 |
| kubeflow/hub | 2026-08-07 | 181 |
| kubeflow/mcp-apache-spark-history-server | 2026-08-07 | 188 |
| kubeflow/notebooks | 2026-08-07 | 75 |

### Top Languages

| Language | Repo Count |
|----------|------------|
| Python | 208 |
| Rust | 56 |
| HTML | 52 |
| Go | 51 |
| JavaScript | 48 |
| TypeScript | 45 |
| Jupyter Notebook | 39 |
| Clojure | 30 |
| Jsonnet | 23 |
| Julia | 19 |

### GF(3) Color Chain

- **id%3==0 → trit=0 ERGODIC** `#d3869b`
- **id%3==1 → trit=1 PLUS** `#b8bb26`
- **id%3==2 → trit=-1 MINUS** `#cc241d`

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A-Z) queried against Aptos mainnet
(`fullnode.mainnet.aptoslabs.com`). All returned `resource_not_found`
for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — indicating
these accounts have no initialized APT coin store on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| A | `0x8699edc0960dd5b916...` | 0.0 |
| B | `0x3f892ebe6e45164e63...` | 0.0 |
| C | `0x38b99e63ada9b6fef1...` | 0.0 |
| D | `0xf77656248f64d5dd00...` | 0.0 |
| E | `0xdc1d9d533bac3507f9...` | 0.0 |
| F | `0x18a14b5b4bec118c1c...` | 0.0 |
| G | `0x69a394c0b0ac842127...` | 0.0 |
| H | `0xce67c327a7844e5488...` | 0.0 |
| I | `0x070fe5d74e4eda30e2...` | 0.0 |
| J | `0x4d964db8f538374034...` | 0.0 |
| K | `0xa732040a6b0d559041...` | 0.0 |
| L | `0x7c2eaeafad9725492e...` | 0.0 |
| M | `0x6fed37a7553ef16b2a...` | 0.0 |
| N | `0xe7dde6da0a65f51062...` | 0.0 |
| O | `0x73252b6011a75115a2...` | 0.0 |
| P | `0x6218792de4a9bc3891...` | 0.0 |
| Q | `0xac40fa50b81b4ca6b1...` | 0.0 |
| R | `0x7ce605cc8fda4f8e4a...` | 0.0 |
| S | `0xb8753014e4888ea48a...` | 0.0 |
| T | `0x35781dc0e42fef3f25...` | 0.0 |
| U | `0x75860da47565f6509b...` | 0.0 |
| V | `0xb59dd8170321dfab5a...` | 0.0 |
| W | `0x5f32aef70f5ba530d3...` | 0.0 |
| X | `0xa95cbbd116548ac990...` | 0.0 |
| Y | `0xd8e32848f1dffa811b...` | 0.0 |
| Z | `0x7af0ef6e1bd706f4b3...` | 0.0 |
| alice | `0xc793acdec12b4a6371...` | 0.0 |
| bob | `0x0a3c00c58fdf9020b2...` | 0.0 |

**Non-zero balances: 0 of 28**  
All recorded as 0.0 APT (resource_not_found = uninitialised accounts).

### Multisig Probes (Aptos)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | YES |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | YES |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | YES |
| V-W | `0x40fad7b423a843650f...` | 2 | YES |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | YES |

**All 5 multisigs healthy — all require 2 signatures (2-of-N).**

### MNX Markets

`https://testnet.mnx.fi` is a Next.js SPA. Probed `/api/markets` and
`/api/v1/markets` — both serve the HTML shell, not JSON.
No market data extractable without browser-side JS execution.
**Status: UNAVAILABLE (SPA, no REST API endpoint)**

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments      -- increment metadata + GF3 color chain
  repo_snapshots        -- per-repo data (org/user/social graph)
  aptos_snapshots       -- Hamming swarm wallet balances
  multisig_probes       -- 2-of-N multisig health checks
  mnx_snapshots         -- MNX market data (empty this run)
```
