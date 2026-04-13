# World Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-04-13 21:15 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 0 |
| TeglonLabs | org | 53 |
| bmorphism | user | 0 |
| zubyul | user | 24 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| wasita | user | 31 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |

> Note: kubeflow (org, 403 rate-limited via unauthenticated API) and bmorphism (user, 403) returned no repo list; repo data was captured for all other sources. kubeflow repos were captured via separate available data.

### World Increments (DuckDB)

- **Total world_increments rows:** 358
- **Total repo_snapshots rows:** 797
- **GF(3) color chain distribution:**

| Color | Name | Trit | Count |
|-------|------|------|-------|
| #d3869b | ERGODIC | 0 | 119 |
| #b8bb26 | PLUS | +1 | 120 |
| #cc241d | MINUS | -1 | 119 |

### Top 10 Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| migalkin | NodePiece | 143 | Python |
| AustinCStone | TextGAN | 92 | Python |
| migalkin | StarE | 88 | Python |
| migalkin | kgcourse2021 | 25 | HTML |
| plurigrid | asi | 16 | HTML |
| AustinCStone | StereoVisionMRF | 11 | Python |
| migalkin | NBFNet_mlx | 10 | Python |
| plurigrid | ontology | 7 | JavaScript |
| migalkin | RWL | 7 | Python |
| plurigrid | asi-skills | 3 | Julia |

### Recent Event Activity

**bmorphism:** PushEvent×26, CreateEvent×1, PullRequestEvent×1, ForkEvent×1, WatchEvent×1

**zubyul:** PullRequestEvent×11, CreateEvent×11, PushEvent×7, ReleaseEvent×1

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A–Z) returned HTTP 404 from the Aptos mainnet node
(`fullnode.mainnet.aptoslabs.com`), indicating these accounts have not been
initialized on mainnet (no on-chain activity / zero-state accounts).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| A | 0x8699edc0960dd5b9… | 404 (uninitialized) |
| B | 0x3f892ebe6e45164e… | 404 (uninitialized) |
| C | 0x38b99e63ada9b6fe… | 404 (uninitialized) |
| D | 0xf77656248f64d5dd… | 404 (uninitialized) |
| E | 0xdc1d9d533bac3507… | 404 (uninitialized) |
| F | 0x18a14b5b4bec118c… | 404 (uninitialized) |
| G | 0x69a394c0b0ac8421… | 404 (uninitialized) |
| H | 0xce67c327a7844e54… | 404 (uninitialized) |
| I | 0x070fe5d74e4eda30… | 404 (uninitialized) |
| J | 0x4d964db8f5383740… | 404 (uninitialized) |
| K | 0xa732040a6b0d5590… | 404 (uninitialized) |
| L | 0x7c2eaeafad972549… | 404 (uninitialized) |
| M | 0x6fed37a7553ef16b… | 404 (uninitialized) |
| N | 0xe7dde6da0a65f510… | 404 (uninitialized) |
| O | 0x73252b6011a75115… | 404 (uninitialized) |
| P | 0x6218792de4a9bc38… | 404 (uninitialized) |
| Q | 0xac40fa50b81b4ca6… | 404 (uninitialized) |
| R | 0x7ce605cc8fda4f8e… | 404 (uninitialized) |
| S | 0xb8753014e4888ea4… | 404 (uninitialized) |
| T | 0x35781dc0e42fef3f… | 404 (uninitialized) |
| U | 0x75860da47565f650… | 404 (uninitialized) |
| V | 0xb59dd8170321dfab… | 404 (uninitialized) |
| W | 0x5f32aef70f5ba530… | 404 (uninitialized) |
| X | 0xa95cbbd116548ac9… | 404 (uninitialized) |
| Y | 0xd8e32848f1dffa81… | 404 (uninitialized) |
| Z | 0x7af0ef6e1bd706f4… | 404 (uninitialized) |
| alice | 0xc793acdec12b4a63… | 404 (uninitialized) |
| bob | 0x0a3c00c58fdf9020… | 404 (uninitialized) |

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da… | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f… | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a… | 2 | ✓ |
| V-W | 0x40fad7b423a84365… | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406… | 2 | ✓ |

All 5 multisig contracts (A-B, A-G, S-T, V-W, Y-Z) are **healthy** with `num_signatures_required = 2`.

### MNX Markets (testnet.mnx.fi)

Status: **unavailable** — all probed API paths returned HTTP 404. The testnet SPA
does not expose a public REST/JSON endpoint at the standard paths tested
(`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/v2/markets`).

---

## DuckDB Schema

Database: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 358 |
| repo_snapshots | 797 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
