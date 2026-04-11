# LATEST_SWEEP — 2026-04-11T12:25:32Z

## Summary

World-increment sweep + Hamming swarm snapshot.
DuckDB ducklake: `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

| Source | Type | Repos | Total Stars | GF3 Trit | GF3 Color | GF3 Name |
|--------|------|-------|-------------|----------|-----------|----------|
| plurigrid | org | 98 | 62 | +1 | #b8bb26 | PLUS |
| kubeflow | org | 47 | 33852 | -1 | #cc241d | MINUS |
| TeglonLabs | org | 4 | 2 | 0 | #d3869b | ERGODIC |
| bmorphism | user | 99 | 246 | +1 | #b8bb26 | PLUS |
| zubyul | user | 45 | 14 | -1 | #cc241d | MINUS |
| migalkin | user (zubyul social) | 19 | 277 | 0 | #d3869b | ERGODIC |
| DJedamski | user (zubyul social) | 6 | 3 | +1 | #b8bb26 | PLUS |
| wasita | user (zubyul social) | 9 | 2 | -1 | #cc241d | MINUS |
| kristinezheng | user (zubyul social) | 6 | 0 | 0 | #d3869b | ERGODIC |
| M1shaaa | user (zubyul social) | 8 | 0 | +1 | #b8bb26 | PLUS |
| AustinCStone | user (zubyul social) | 40 | 108 | -1 | #cc241d | MINUS |

**Total repos indexed: 381** across 11 orgs/users.

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15565 | - |
| kubeflow/pipelines | 4119 | Python |
| kubeflow/spark-operator | 3111 | Python |
| kubeflow/trainer | 2080 | Go |
| kubeflow/katib | 1676 | Python |
| kubeflow/examples | 1458 | Jsonnet |
| kubeflow/manifests | 1010 | YAML |
| kubeflow/arena | 808 | Go |
| kubeflow/kale | 682 | Python |
| kubeflow/mpi-operator | 522 | Go |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (APT)

| World | Address (short) | Balance APT |
|-------|-----------------|-------------|
| bob | `0x0a3c00c5...512d5d` | 12.65700700 |
| F | `0x18a14b5b...c3cf71` | 1.96051600 |
| L | `0x7c2eaeaf...37eba9` | 1.92726900 |
| J | `0x4d964db8...e87f54` | 1.89509300 |
| alice | `0xc793acde...24cc7b` | 0.43643352 |
| O | `0x73252b60...25a89d` | 0.21013600 |
| K | `0xa732040a...425dc4` | 0.16196100 |
| P | `0x6218792d...1ec948` | 0.14013600 |
| M | `0x6fed37a7...b7f2e9` | 0.11228500 |
| N | `0xe7dde6da...551b2c` | 0.10612100 |
| Q | `0xac40fa50...5c89a9` | 0.10324000 |
| S | `0xb8753014...9d0386` | 0.09178800 |
| R | `0x7ce605cc...d76e10` | 0.09021700 |
| T | `0x35781dc0...3f4588` | 0.07371300 |
| U | `0x75860da4...ef9956` | 0.05577300 |
| A | `0x8699edc0...be9d7a` | 0.05176700 |
| V | `0xb59dd817...9af2c3` | 0.04783299 |
| Y | `0xd8e32848...2444c4` | 0.04444900 |
| X | `0xa95cbbd1...33047d` | 0.04257700 |
| W | `0x5f32aef7...ccc7b0` | 0.04070500 |
| B | `0x3f892ebe...77cb13` | 0.03625600 |
| Z | `0x7af0ef6e...4e197c` | 0.02326800 |
| E | `0xdc1d9d53...958d36` | 0.01256100 |
| D | `0xf7765624...fcfdd1` | 0.01162900 |
| C | `0x38b99e63...91535e` | 0.01018500 |
| G | `0x69a394c0...cc7f32` | 0.00068100 |
| H | `0xce67c327...e5300f` | 0.00068100 |
| I | `0x070fe5d7...0c1fc9` | 0.00068100 |

**Total APT across all addresses: 20.344962 APT**

### Multisig Contract Probes

| Pair | Address (short) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |

All 5 multisig accounts are healthy with 2-of-N signature requirement.

### MNX Markets

`https://testnet.mnx.fi` — Next.js SPA, no REST API endpoint available.
All probed paths (`/api/markets`, `/api/v1/markets`) return the SPA HTML shell.
Status: **unavailable** (SPA, data requires browser execution).

---

## DuckDB Schema

```
world_increments  — 11 rows  (GF3 color-chain sweep metadata)
repo_snapshots    — 381 rows (GitHub repo snapshots)
aptos_snapshots   —  28 rows (Hamming swarm APT balances)
multisig_probes   —   5 rows (Aptos multisig health)
mnx_snapshots     —   1 row  (MNX market status)
```

GF3 color chain: `id%3==0` → ERGODIC (#d3869b), `id%3==1` → PLUS (#b8bb26), `id%3==2` → MINUS (#cc241d)
