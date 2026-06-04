# World-Increment + Hamming Swarm Snapshot

**Generated:** 2026-04-30 21:20:06 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| TeglonLabs | org | 53 |
| AustinCStone | user | 43 |
| wasita | user | 31 |
| migalkin | user | 30 |
| kristinezheng | user | 18 |
| DJedamski | user | 11 |

**Total repos snapshotted:** 286

### GF(3) Trit Color Chain Distribution

| GF(3) Name | Color | Count |
|-----------|-------|-------|
| ERGODIC (trit=0) | ERGODIC #d3869b | 95 |
| MINUS (trit=-1) | MINUS #cc241d | 95 |
| PLUS (trit=1) | PLUS #b8bb26 | 96 |

### Top 15 Repos by Stars

| Repo | Stars | Language | Source |
|------|-------|----------|--------|
| migalkin/NodePiece | 143 | Python | migalkin |
| AustinCStone/TextGAN | 92 | Python | AustinCStone |
| migalkin/StarE | 89 | Python | migalkin |
| migalkin/kgcourse2021 | 25 | HTML | migalkin |
| plurigrid/asi | 17 | HTML | plurigrid |
| AustinCStone/StereoVisionMRF | 11 | Python | AustinCStone |
| migalkin/NBFNet_mlx | 10 | Python | migalkin |
| plurigrid/ontology | 7 | JavaScript | plurigrid |
| migalkin/RWL | 7 | Python | migalkin |
| plurigrid/asi-skills | 3 | Julia | plurigrid |
| migalkin/rambo | 3 | Rust | migalkin |
| AustinCStone/SpectralClustering | 3 | Python | AustinCStone |
| plurigrid/zig-syrup | 2 | Zig | plurigrid |
| TeglonLabs/vibespace | 2 | HTML | TeglonLabs |
| wasita/magic-garden | 2 | Python | wasita |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 49 |
| Rust | 12 |
| JavaScript | 11 |
| HTML | 10 |
| R | 7 |
| Jupyter Notebook | 7 |
| Clojure | 5 |
| Java | 5 |
| TeX | 4 |
| Svelte | 4 |

### Notes

- `bmorphism`, `zubyul`, `M1shaaa`: private or 0 public repos visible without auth
- `kubeflow`: API returned empty (rate-limited or requires auth)
- Events for `bmorphism` and `zubyul`: empty (private activity)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| A | `0x8699edc0...be9d7a` | 0.00000000 |
| B | `0x3f892ebe...77cb13` | 0.00000000 |
| C | `0x38b99e63...91535e` | 0.00000000 |
| D | `0xf7765624...fcfdd1` | 0.00000000 |
| E | `0xdc1d9d53...958d36` | 0.00000000 |
| F | `0x18a14b5b...c3cf71` | 0.00000000 |
| G | `0x69a394c0...cc7f32` | 0.00000000 |
| H | `0xce67c327...e5300f` | 0.00000000 |
| I | `0x070fe5d7...0c1fc9` | 0.00000000 |
| J | `0x4d964db8...e87f54` | 0.00000000 |
| K | `0xa732040a...425dc4` | 0.00000000 |
| L | `0x7c2eaeaf...37eba9` | 0.00000000 |
| M | `0x6fed37a7...b7f2e9` | 0.00000000 |
| N | `0xe7dde6da...551b2c` | 0.00000000 |
| O | `0x73252b60...25a89d` | 0.00000000 |
| P | `0x6218792d...1ec948` | 0.00000000 |
| Q | `0xac40fa50...5c89a9` | 0.00000000 |
| R | `0x7ce605cc...d76e10` | 0.00000000 |
| S | `0xb8753014...9d0386` | 0.00000000 |
| T | `0x35781dc0...3f4588` | 0.00000000 |
| U | `0x75860da4...ef9956` | 0.00000000 |
| V | `0xb59dd817...9af2c3` | 0.00000000 |
| W | `0x5f32aef7...ccc7b0` | 0.00000000 |
| X | `0xa95cbbd1...33047d` | 0.00000000 |
| Y | `0xd8e32848...2444c4` | 0.00000000 |
| Z | `0x7af0ef6e...4e197c` | 0.00000000 |
| alice | `0xc793acde...24cc7b` | 0.00000000 |
| bob | `0x0a3c00c5...512d5d` | 0.00000000 |

**Note:** All balances returned as 0 — addresses likely uninitialized on mainnet or do not hold APT in `CoinStore`.

### Multisig Contract Probes (Aptos Mainnet)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|--------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |

**All 5 multisig accounts responded with `num_signatures_required = 2` and are healthy.**

### MNX Markets (testnet.mnx.fi)

MNX testnet is a Next.js SPA. The root path returns HTML; no JSON API endpoint was discovered at `/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`, or `/api/v1/tickers`. Market data is rendered client-side and unavailable via simple HTTP.

---

## DuckDB Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

Tables:
- `world_increments` — GF(3)-colored increment log
- `repo_snapshots` — GitHub repo metadata
- `aptos_snapshots` — Hamming swarm wallet balances
- `multisig_probes` — Multisig contract health checks
- `mnx_snapshots` — MNX market data (unavailable this sweep)
