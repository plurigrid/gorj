# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-07-21 10:11 UTC

---

## JOB 1: GitHub Social Graph Sweep

### Summary
| Source | Repos Snapshotted | Total Stars |
|--------|-------------------|-------------|
| migalkin | 65 | 829 |
| bmorphism | 297 | 506 |
| AustinCStone | 90 | 308 |
| zubyul | 97 | 40 |
| DJedamski | 24 | 15 |
| wasita | 64 | 9 |
| TeglonLabs | 100 | 8 |
| kristinezheng | 38 | 0 |
| M1shaaa | 34 | 0 |

**Total this run:** 321 repo snapshots across 11 sources  
**DuckDB totals:** 34 world_increments, 1265 repo_snapshots (cumulative)

### Top Repos by Stars (this run)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| migalkin/NodePiece | Python | 144 | Parameter-efficient KG representations (ICLR 22) |
| migalkin/NodePiece | Python | 143 | Compositional and Parameter-Efficient Representations for La |
| migalkin/NodePiece | Python | 143 | Compositional and Parameter-Efficient Representations for La |
| AustinCStone/TextGAN | Python | 92 | A generative adversarial network for text generation, writte |
| AustinCStone/TextGAN | Python | 92 | A generative adversarial network for text generation, writte |
| AustinCStone/TextGAN | Python | 92 | GAN for text generation in TensorFlow |
| migalkin/StarE | Python | 89 | EMNLP 2020: Hyper-Relational Knowledge Graphs |
| migalkin/StarE | Python | 88 | EMNLP 2020: Message Passing for Hyper-Relational Knowledge G |
| migalkin/StarE | Python | 88 | EMNLP 2020: Message Passing for Hyper-Relational Knowledge G |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | OCaml SDK for Model Context Protocol using Jane Street's oxc |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | OCaml SDK for Model Context Protocol using Jane Street's oxc |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | OCaml SDK for Model Context Protocol using Jane Street''s ox |
| migalkin/kgcourse2021 | HTML | 25 | Материалы к курсу по Knowledge Graphs |
| migalkin/kgcourse2021 | HTML | 25 | Материалы к курсу по Knowledge Graphs |
| migalkin/kgcourse2021 | HTML | 24 | Materials for Knowledge Graphs course |

### GF(3) Color Chain Applied
- id%3==0 → trit=0 ERGODIC `#d3869b`
- id%3==1 → trit=1 PLUS `#b8bb26`
- id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 worlds: alice, bob, A–Z)
All 28 wallets returned `resource_not_found` from the Aptos mainnet fullnode.  
This indicates the CoinStore resource has not been initialized on-chain for any of these addresses  
(accounts may be pre-funded via another mechanism, or not yet active on mainnet).

*All balances: 0.00000000 APT (resource_not_found)*

### Multisig Contract Probes
| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |

All 5 multisig contracts healthy — each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)
**Status: Authentication Required** — all API endpoints (/, /api/markets, /api/v1/markets, /api/tickers)  
return HTTP 200 with an "Authentication Required" SPA. Market data unavailable without credentials.

---

## Database: `packages/world-increment/ducklake/world-increments.duckdb`
- `world_increments`: 34 rows (cumulative)
- `repo_snapshots`: 1265 rows (cumulative)
- `aptos_snapshots`: 28 rows (this run)
- `multisig_probes`: 5 rows (this run)
- `mnx_snapshots`: 1 row (this run — auth-required marker)
