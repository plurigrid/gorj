# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-28  
**Run type:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapped | Total Stars |
|--------|------|---------------|-------------|
| kubeflow | org | 104 (cumulative) | 94,776 |
| migalkin | user | 65 (cumulative) | 830 |
| bmorphism | user | 210 (cumulative) | 354 |
| AustinCStone | user | 90 (cumulative) | 322 |
| plurigrid | org | 210 (cumulative) | 115 |
| zubyul | user | 58 (cumulative) | 27 |
| DJedamski | user | 25 (cumulative) | 16 |
| TeglonLabs | org | 111 (cumulative) | 14 |
| wasita | user | 65 (cumulative) | 10 |
| M1shaaa | user | 35 (cumulative) | 0 |
| kristinezheng | user | (new this run) | — |

### This Run — New World-Increments (IDs 2–12)

| ID | GF3 Name | GF3 Color | Source | Type |
|----|----------|-----------|--------|------|
| 2 | MINUS | #cc241d | kubeflow | org |
| 3 | ERGODIC | #d3869b | TeglonLabs | org |
| 4 | PLUS | #b8bb26 | bmorphism | user |
| 5 | MINUS | #cc241d | zubyul | user |
| 6 | ERGODIC | #d3869b | migalkin | user |
| 7 | PLUS | #b8bb26 | DJedamski | user |
| 8 | MINUS | #cc241d | wasita | user |
| 9 | ERGODIC | #d3869b | kristinezheng | user |
| 10 | PLUS | #b8bb26 | M1shaaa | user |
| 11 | MINUS | #cc241d | AustinCStone | user |
| 12 | ERGODIC | #d3869b | bmorphism (update) | user |

**GF(3) trit chain:** 0=ERGODIC #d3869b · 1=PLUS #b8bb26 · −1=MINUS #cc241d

### Notable Repos (this run)

**Most recently pushed:**
- `plurigrid/gorj` — 2026-06-28T03:15:07Z (873 open issues, Clojure)
- `plurigrid/asi` — 2026-06-28T00:42:34Z (26 stars, HTML)
- `bmorphism/Gay.jl` — 2026-06-28T00:39:14Z (187 issues, Julia)
- `kubeflow/hub` — 2026-06-27T17:16:47Z (174 stars, Go)
- `kubeflow/pipelines` — 2026-06-27T15:18:12Z (4158 stars, Python)

**Most starred this run:**
- `kubeflow/kubeflow` — 15,749 stars
- `kubeflow/pipelines` — 4,158 stars
- `kubeflow/spark-operator` — 3,129 stars
- `migalkin/NodePiece` — 144 stars (ICLR'22 knowledge graphs)
- `bmorphism/ocaml-mcp-sdk` — 61 stars

### Social Graph Summary (zubyul connections)

| User | Notable Repos |
|------|---------------|
| migalkin | NodePiece 144★, StarE 89★ — knowledge graph ML |
| DJedamski | Kaggle/data science |
| wasita | Svelte personal site, magic-garden bot 2★ |
| kristinezheng | MIT cognitive science, Lookit studies |
| M1shaaa | Yale psychology, Lookit dev |
| AustinCStone | TextGAN 92★, StereoVisionMRF 11★, ML/CV |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Endpoint:** `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore%3C0x1::aptos_coin::AptosCoin%3E`

All 28 Hamming-swarm addresses (alice, bob, A–Z) returned **HTTP 404 Not Found**.
These accounts are not registered on Aptos mainnet (no CoinStore for AptosCoin).

| Label | Address (first 10 chars) | Balance |
|-------|--------------------------|---------|
| alice | 0xc793acde… | 404 |
| bob | 0x0a3c00c5… | 404 |
| A–Z (26 wallets) | various | 404 (all) |

### Multisig Contract Probes

**Function:** `0x1::multisig_account::num_signatures_required`
**All 5 probed contracts healthy (2-of-2 threshold).**

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428… | 2 | healthy |
| A-G | 0xf56c4a1c… | 2 | healthy |
| Y-Z | 0xd3ffe181… | 2 | healthy |
| S-T | 0x3b1c3ae9… | 2 | healthy |
| V-W | 0x40fad7b4… | 2 | healthy |

### MNX Markets

`https://testnet.mnx.fi/api/markets` → **HTTP 401 Unauthorized**
API requires authentication. `mnx_snapshots` table is empty this run.

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1,012 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
