# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-08-09 13:14:09 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | user | 5 |
| DJedamski | user | 2 |
| wasita | user | 4 |
| kristinezheng | user | 2 |
| M1shaaa | user | 2 |
| AustinCStone | user | 4 |

**Total repos snapshotted:** 322 across 11 sources

### DuckDB Tables
- `world_increments`: 34 increment records (GF3 color chain applied)
- `repo_snapshots`: 322 repo records

### GF3 Color Chain
- id%3==0 → trit=0, ERGODIC `#d3869b`
- id%3==1 → trit=1, PLUS `#b8bb26`
- id%3==2 → trit=-1, MINUS `#cc241d`

### Notable Repos
- **plurigrid** (100 repos) — core org
- **kubeflow** (49 repos) — ML infrastructure
- **bmorphism** (100 repos) — key contributor
- **TeglonLabs/jank-crane** — GF3 convergence maps (pushed 2026-06-08)
- **migalkin/NodePiece** — 144 ⭐, knowledge graph embeddings
- **AustinCStone/TextGAN** — 92 ⭐, text GAN in TensorFlow
- **wasita/xoxowasita-analysis** — pushed 2026-08-06 (most recent)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Total APT across swarm:** 20.34477251 APT

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
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
| V | `0xb59dd817...9af2c3` | 0.04883299 |
| Y | `0xd8e32848...2444c4` | 0.04444900 |
| X | `0xa95cbbd1...33047d` | 0.04257700 |
| W | `0x5f32aef7...ccc7b0` | 0.04070500 |
| B | `0x3f892ebe...77cb13` | 0.03625600 |
| Z | `0x7af0ef6e...4e197c` | 0.02426800 |
| D | `0xf7765624...fcfdd1` | 0.01162900 |
| C | `0x38b99e63...91535e` | 0.01018500 |
| E | `0xdc1d9d53...958d36` | 0.00937200 |
| H | `0xce67c327...e5300f` | 0.00168100 |
| G | `0x69a394c0...cc7f32` | 0.00068100 |
| I | `0x070fe5d7...0c1fc9` | 0.00068100 |

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✅ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✅ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✅ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✅ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✅ |

**All 5 multisig contracts healthy** (5/5) — all require 2 signatures.

### MNX Markets

- **testnet.mnx.fi** — Next.js SPA (no public REST API). All paths return HTML shell.
  Market data unavailable via API probe; requires browser JS execution.

---

## DuckDB Schema

Location: `packages/world-increment/ducklake/world-increments.duckdb`

```
world_increments  — 34 rows  (GF3 color chain, source provenance)
repo_snapshots    — 322 rows (all GitHub repos snapshotted)
aptos_snapshots   — 28 rows  (Hamming swarm wallet balances)
multisig_probes   —  5 rows  (multisig health checks)
mnx_snapshots     —  1 row   (SPA unavailable marker)
```
