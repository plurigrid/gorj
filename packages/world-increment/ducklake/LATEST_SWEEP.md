# World-Increment Sweep + Hamming Snapshot

**Date/Time:** 2026-04-06 08:39:46 UTC

---

## GitHub Social Graph Sweep

### Sources Queried
**Organizations:** plurigrid, kubeflow, TeglonLabs
**Users:** bmorphism, kristinezheng, AustinCStone
**Rate-limited (partial/no data):** zubyul, migalkin, DJedamski, wasita, M1shaaa

### Total Repos Captured: 360

| Source | Type | Repo Count |
|--------|------|-----------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 46 |
| AustinCStone | user | 43 |
| kristinezheng | user | 18 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15553 | N/A |
| kubeflow/pipelines | 4118 | Python |
| kubeflow/spark-operator | 3111 | Python |
| kubeflow/trainer | 2074 | Go |
| kubeflow/katib | 1674 | Python |
| kubeflow/examples | 1459 | Jsonnet |
| kubeflow/manifests | 1009 | YAML |
| kubeflow/arena | 808 | Go |
| kubeflow/kale | 682 | Python |
| kubeflow/mpi-operator | 519 | Go |

### Recent Events (bmorphism)
- PushEvent → plurigrid/horse (2026-04-06T02:09:47Z)
- PushEvent → plurigrid/horse (2026-04-06T02:00:30Z)
- PushEvent → bmorphism/boxxy (2026-04-06T01:48:38Z)

---

## Aptos Wallet Balances (Hamming Swarm)

| Label | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acde...d624cc7b | 0.00000000 |
| bob | 0x0a3c00c5...05512d5d | 0.00000000 |
| A | 0x8699edc0...aebe9d7a | 0.00000000 |
| B | 0x3f892ebe...4577cb13 | 0.00000000 |
| C | 0x38b99e63...2691535e | 0.00000000 |
| D | 0xf7765624...d9fcfdd1 | 0.00000000 |
| E | 0xdc1d9d53...d0958d36 | 0.00000000 |
| F | 0x18a14b5b...74c3cf71 | 0.00000000 |
| G | 0x69a394c0...dbcc7f32 | 0.00000000 |
| H | 0xce67c327...94e5300f | 0.00000000 |
| I | 0x070fe5d7...c00c1fc9 | 0.00000000 |
| J | 0x4d964db8...93e87f54 | 0.00000000 |
| K | 0xa732040a...7a425dc4 | 0.00000000 |
| L | 0x7c2eaeaf...6337eba9 | 0.00000000 |
| M | 0x6fed37a7...49b7f2e9 | 0.00000000 |
| N | 0xe7dde6da...11551b2c | 0.00000000 |
| O | 0x73252b60...a525a89d | 0.00000000 |
| P | 0x6218792d...621ec948 | 0.00000000 |
| Q | 0xac40fa50...5e5c89a9 | 0.00000000 |
| R | 0x7ce605cc...36d76e10 | 0.00000000 |
| S | 0xb8753014...f99d0386 | 0.00000000 |
| T | 0x35781dc0...2d3f4588 | 0.00000000 |
| U | 0x75860da4...95ef9956 | 0.00000000 |
| V | 0xb59dd817...a89af2c3 | 0.00000000 |
| W | 0x5f32aef7...a6ccc7b0 | 0.00000000 |
| X | 0xa95cbbd1...be33047d | 0.00000000 |
| Y | 0xd8e32848...fa2444c4 | 0.00000000 |
| Z | 0x7af0ef6e...6e4e197c | 0.00000000 |

> Note: All queried addresses returned resource_not_found from Aptos mainnet, indicating zero APT balances.

---

## Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428...f4987003 | 2 | YES |
| A-G | 0xf56c4a1c...3fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe181...8e75b883 | 2 | YES |
| S-T | 0x3b1c3ae9...3ded7883 | 2 | YES |
| V-W | 0x40fad7b4...2c80eb6d | 2 | YES |

> All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`. All healthy with 2-of-N threshold.

---

## MNX Markets

**Status: unavailable** — `https://testnet.mnx.fi/api/markets` returns 404 (Next.js app with no matching route).

---

## GF(3) Color Chain Stats

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 120 |
| 1 | #b8bb26 | PLUS | 120 |
| 2 (−1) | #cc241d | MINUS | 120 |

**Total world_increments:** 360 (perfectly balanced across all three GF(3) states)

---

## Database

- **Path:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Tables:** `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
- **Sequences:** `increment_seq`, `repo_seq`
