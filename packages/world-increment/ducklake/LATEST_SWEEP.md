# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date/Time:** 2026-03-30T00:00:00Z (UTC)
**DuckDB:** `/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Sources Covered

| Source | Type | Repo Count |
|--------|------|-----------|
| plurigrid | org | 100 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| bmorphism | user | 100 |
| zubyul | user | 23 |
| migalkin | user (zubyul social) | 30 |
| DJedamski | user (zubyul social) | 11 |
| wasita | user (zubyul social) | 28 |
| kristinezheng | user (zubyul social) | 18 |
| M1shaaa | user (zubyul social) | 16 |
| AustinCStone | user (zubyul social) | 43 |

**Total repos snapshotted:** 468
**Public events fetched:** 30 each for bmorphism and zubyul (top 10 per user ingested as world_increments)

---

## Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15542 | - |
| kubeflow/pipelines | 4112 | Python |
| kubeflow/spark-operator | 3109 | Python |
| kubeflow/trainer | 2069 | Go |
| kubeflow/katib | 1673 | Python |
| kubeflow/examples | 1459 | Jsonnet |
| kubeflow/manifests | 1005 | YAML |
| kubeflow/arena | 810 | Go |
| kubeflow/kale | 681 | Python |
| kubeflow/mpi-operator | 519 | Go |

---

## Aptos Wallet Balances

All 28 addresses returned `resource_not_found` from the Aptos mainnet API, indicating no APT CoinStore resource exists for these addresses (accounts not initialized or using a different resource type).

| World Label | Address (truncated) | Balance (APT) | Status |
|-------------|---------------------|---------------|--------|
| alice | 0xc793acdec12b4a... | 0.0 | resource_not_found |
| bob | 0x0a3c00c58fdf90... | 0.0 | resource_not_found |
| A | 0x8699edc0960dd5... | 0.0 | resource_not_found |
| B | 0x3f892ebe6e4516... | 0.0 | resource_not_found |
| C | 0x38b99e63ada9b6... | 0.0 | resource_not_found |
| D | 0xf77656248f64d5... | 0.0 | resource_not_found |
| E | 0xdc1d9d533bac35... | 0.0 | resource_not_found |
| F | 0x18a14b5b4bec11... | 0.0 | resource_not_found |
| G | 0x69a394c0b0ac84... | 0.0 | resource_not_found |
| H | 0xce67c327a7844e... | 0.0 | resource_not_found |
| I | 0x070fe5d74e4eda... | 0.0 | resource_not_found |
| J | 0x4d964db8f53837... | 0.0 | resource_not_found |
| K | 0xa732040a6b0d55... | 0.0 | resource_not_found |
| L | 0x7c2eaeafad9725... | 0.0 | resource_not_found |
| M | 0x6fed37a7553ef1... | 0.0 | resource_not_found |
| N | 0xe7dde6da0a65f5... | 0.0 | resource_not_found |
| O | 0x73252b6011a751... | 0.0 | resource_not_found |
| P | 0x6218792de4a9bc... | 0.0 | resource_not_found |
| Q | 0xac40fa50b81b4c... | 0.0 | resource_not_found |
| R | 0x7ce605cc8fda4f... | 0.0 | resource_not_found |
| S | 0xb8753014e4888e... | 0.0 | resource_not_found |
| T | 0x35781dc0e42fef... | 0.0 | resource_not_found |
| U | 0x75860da47565f6... | 0.0 | resource_not_found |
| V | 0xb59dd8170321df... | 0.0 | resource_not_found |
| W | 0x5f32aef70f5ba5... | 0.0 | resource_not_found |
| X | 0xa95cbbd116548a... | 0.0 | resource_not_found |
| Y | 0xd8e32848f1dffa... | 0.0 | resource_not_found |
| Z | 0x7af0ef6e1bd706... | 0.0 | resource_not_found |

---

## Multisig Contract Probes

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Contract Address (truncated) | Sigs Required | Healthy |
|------|------------------------------|---------------|---------|
| A-B | 0x0da4f428a0c007... | 2 | true |
| A-G | 0xf56c4a1c090621... | 2 | true |
| Y-Z | 0xd3ffe1812b2df4... | 2 | true |
| S-T | 0x3b1c3ae905d44c... | 2 | true |
| V-W | 0x40fad7b423a843... | 2 | true |

All multisig contracts require 2-of-N signatures. All probes healthy.

---

## MNX Markets

**Status: UNAVAILABLE**

Both endpoints (`https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/v1/markets`) return an HTML page instead of JSON. The testnet.mnx.fi API is not exposing a REST-accessible markets endpoint at these paths.

---

## GF(3) Color Chain Legend

World increments are tagged with a GF(3) trit value based on `id % 3`:

| id % 3 | Trit | Color | Name | Meaning |
|--------|------|-------|------|---------|
| 0 | 0 | `#d3869b` (rose) | ERGODIC | Neutral/fixed point |
| 1 | +1 | `#b8bb26` (lime) | PLUS | Positive increment |
| 2 | -1 | `#cc241d` (red) | MINUS | Negative increment |

The GF(3) field ensures every world-increment is classified into one of three states forming a closed algebraic structure under addition mod 3.

---

## Summary Statistics

- **world_increments rows:** 31 (11 source sweeps + 20 event entries)
- **repo_snapshots rows:** 468
- **aptos_snapshots rows:** 28 (all zero balance, resource_not_found)
- **multisig_probes rows:** 5 (all healthy, sigs_required=2)
- **mnx_snapshots rows:** 0 (API unavailable)
