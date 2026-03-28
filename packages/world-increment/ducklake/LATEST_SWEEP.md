# World-Increment Sweep + Hamming Snapshot

**Sweep Date:** 2026-03-28
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repos Found Per Org/User

| org_or_user    | repos_fetched | total_stars | top repos                                                        |
|----------------|---------------|-------------|------------------------------------------------------------------|
| kubeflow       | 29            | 46,571      | kubeflow(15.5k), pipelines(4.1k), spark-operator(3.1k)          |
| bmorphism      | 26            | 282         | ocaml-mcp-sdk(60), anti-bullshit-mcp-server(23), risc0-cosmwasm(23) |
| migalkin       | 15            | 277         | NodePiece(143), StarE(88), kgcourse2021(25)                      |
| AustinCStone   | 15            | 107         | TextGAN(92), StereoVisionMRF(10), SpectralClustering(3)          |
| plurigrid      | 32            | 70          | asi(13), ontology(7), vcg-auction(7)                             |
| zubyul         | 15            | 14          | WGCNA(2), jonikas_lab_data_analysis(2)                           |
| TeglonLabs     | 8             | 6           | mathpix-gem(2), topoi, coin-flip-mcp                             |
| DJedamski      | 4             | 4           | Getting-and-Cleaning-Data(1), School(1)                          |
| wasita         | 4             | 2           | magic-garden(1), wins-search(1)                                  |
| kristinezheng  | 6             | 0           | Portfolio, kristinezheng.github.io                               |
| M1shaaa        | 5             | 0           | lab-bookshelf-, M1shaaa                                          |

**Total:** 11 sources, 159 repo snapshots, 23 world_increment rows stored in DuckDB.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets (alice, bob, A-Z) returned 0.0000 APT on mainnet.

| World | Address (truncated)  | Balance (APT) |
|-------|----------------------|---------------|
| alice | 0xc793...4cc7b       | 0.0000        |
| bob   | 0x0a3c...512d5d      | 0.0000        |
| A-Z   | (26 wallets)         | 0.0000 each   |

### Multisig Contract Probes (5 pairs)

All 5 probes returned `sigs_required=2`, all healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...7003       | 2             | true    |
| A-G  | 0xf56c...0096       | 2             | true    |
| Y-Z  | 0xd3ff...b883       | 2             | true    |
| S-T  | 0x3b1c...7883       | 2             | true    |
| V-W  | 0x40fa...eb6d       | 2             | true    |

### MNX Markets

**Status: Unavailable** - testnet.mnx.fi returns a Next.js SPA (HTML), not JSON API data.

---

## GF(3) Color Chain Legend

| id % 3 | Trit | Name    | Color   |
|--------|------|---------|---------|
| 0      | 0    | ERGODIC | #d3869b |
| 1      | +1   | PLUS    | #b8bb26 |
| 2      | -1   | MINUS   | #cc241d |

---

## DuckDB Tables

- `world_increments` - 23 rows (one per source org/user sweep)
- `repo_snapshots` - 159 rows (GitHub repo metadata snapshots)
- `aptos_snapshots` - 28 rows (hamming swarm wallet balances)
- `multisig_probes` - 5 rows (A-B, A-G, Y-Z, S-T, V-W pairs)
- `mnx_snapshots` - 1 row (status: SPA unavailable)
