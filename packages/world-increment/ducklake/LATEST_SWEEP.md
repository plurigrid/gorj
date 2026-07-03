# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-07-03 11:10:55 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Metric | Value |
|--------|-------|
| Total world-increment events | 342 |
| Total repo snapshots | 1263 |
| Sources scanned | plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| PLUS | `#b8bb26` | PLUS | 115 |
| MINUS | `#cc241d` | MINUS | 114 |
| ERGODIC | `#d3869b` | ERGODIC | 113 |

### Repos by Source

| Source | Repo Count |
|--------|------------|
| plurigrid | 300 |
| bmorphism | 300 |
| kubeflow | 142 |
| TeglonLabs | 111 |
| zubyul | 97 |
| AustinCStone | 89 |
| migalkin | 65 |
| wasita | 63 |
| kristinezheng | 38 |
| M1shaaa | 34 |
| DJedamski | 24 |

### Top 15 Repos by Stars

| Owner | Repo | Language | ★ Stars | Forks |
|-------|------|----------|---------|-------|
| kubeflow | kubeflow | - | 15760 | 2682 |
| kubeflow | kubeflow | - | 15572 | 2633 |
| kubeflow | kubeflow | - | 15565 | 2626 |
| kubeflow | pipelines | Python | 4167 | 2021 |
| kubeflow | pipelines | Python | 4119 | 1984 |
| kubeflow | pipelines | Python | 4119 | 1985 |
| kubeflow | spark-operator | Python | 3132 | 1496 |
| kubeflow | spark-operator | Python | 3114 | 1483 |
| kubeflow | spark-operator | Python | 3111 | 1483 |
| kubeflow | trainer | Go | 2129 | 975 |
| kubeflow | trainer | Go | 2082 | 945 |
| kubeflow | trainer | Go | 2080 | 944 |
| kubeflow | katib | Python | 1688 | 529 |
| kubeflow | katib | Python | 1678 | 521 |
| kubeflow | katib | Python | 1676 | 521 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` on CoinStore — these are unfunded/unregistered addresses with no APT balance.

| World | Address | Balance (APT) |
|-------|---------|--------------|
| A | `0x8699edc0960dd5...` | 0.00000000 |
| B | `0x3f892ebe6e4516...` | 0.00000000 |
| C | `0x38b99e63ada9b6...` | 0.00000000 |
| D | `0xf77656248f64d5...` | 0.00000000 |
| E | `0xdc1d9d533bac35...` | 0.00000000 |
| F | `0x18a14b5b4bec11...` | 0.00000000 |
| G | `0x69a394c0b0ac84...` | 0.00000000 |
| H | `0xce67c327a7844e...` | 0.00000000 |
| I | `0x070fe5d74e4eda...` | 0.00000000 |
| J | `0x4d964db8f53837...` | 0.00000000 |
| K | `0xa732040a6b0d55...` | 0.00000000 |
| L | `0x7c2eaeafad9725...` | 0.00000000 |
| M | `0x6fed37a7553ef1...` | 0.00000000 |
| N | `0xe7dde6da0a65f5...` | 0.00000000 |
| O | `0x73252b6011a751...` | 0.00000000 |
| P | `0x6218792de4a9bc...` | 0.00000000 |
| Q | `0xac40fa50b81b4c...` | 0.00000000 |
| R | `0x7ce605cc8fda4f...` | 0.00000000 |
| S | `0xb8753014e4888e...` | 0.00000000 |
| T | `0x35781dc0e42fef...` | 0.00000000 |
| U | `0x75860da47565f6...` | 0.00000000 |
| V | `0xb59dd8170321df...` | 0.00000000 |
| W | `0x5f32aef70f5ba5...` | 0.00000000 |
| X | `0xa95cbbd116548a...` | 0.00000000 |
| Y | `0xd8e32848f1dffa...` | 0.00000000 |
| Z | `0x7af0ef6e1bd706...` | 0.00000000 |
| alice | `0xc793acdec12b4a...` | 0.00000000 |
| bob | `0x0a3c00c58fdf90...` | 0.00000000 |

### Multisig Contract Probes (Aptos mainnet)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007...` | 2 | ✅ |
| A-G | `0xf56c4a1c090621...` | 2 | ✅ |
| Y-Z | `0xd3ffe1812b2df4...` | 2 | ✅ |
| S-T | `0x3b1c3ae905d44c...` | 2 | ✅ |
| V-W | `0x40fad7b423a843...` | 2 | ✅ |

**All 5 multisig contracts report 2-of-2 signatures required. Status: HEALTHY.**

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — testnet.mnx.fi requires Vercel authentication. No market data could be retrieved.

---

## DuckDB Schema

Tables in `packages/world-increment/ducklake/world-increments.duckdb`:
- `world_increments` — GF(3) color-chain events (ERGODIC/PLUS/MINUS)
- `repo_snapshots` — GitHub repo metadata snapshots
- `aptos_snapshots` — Aptos wallet balance probes
- `multisig_probes` — Aptos multisig contract health checks
- `mnx_snapshots` — MNX market data (unavailable this run)
