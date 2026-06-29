# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-29  
**GF(3) color chain:** ERGODIC=#d3869b | PLUS=#b8bb26 | MINUS=#cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Orgs Snapshotted

| Org/User | Repos | Notes |
|---|---|---|
| plurigrid | 102 | Most recent: `asi` (2026-06-29), `place` (2026-06-29), `gorj` (911 open issues) |
| kubeflow | 48 | Top: `kubeflow` (15750★), `pipelines` (4162★), `spark-operator` (3129★) |
| TeglonLabs | 5 | `jank-crane` (C++, GF3 crane-jank hub), `mathpix-gem` (Ruby, 2★), `coin-flip-mcp`, `monad-mcp-server`, `topoi` |

### Users Snapshotted

| User | Repos | Top Stars |
|---|---|---|
| bmorphism | 105 | `ocaml-mcp-sdk` (61★), `anti-bullshit-mcp-server` (23★), `Gay.jl` (2★, 187 issues) |
| zubyul | 49 | `gay-world` (1★), `tilelang-kernels`, `voice-observatory` |

### Zubyul Social Graph

| User | Repos | Notable |
|---|---|---|
| migalkin | 19 | `NodePiece` (144★ ICLR'22), `StarE` (89★ EMNLP'20), `NBFNet_mlx` (10★) |
| DJedamski | 6 | `kaggle_ncaa18`, `Kaggle`, data science / R repos |
| wasita | 11 | `magic-garden` (2★ discord bot), `send2kobo` (1★), personal site |
| kristinezheng | 5 | `kristinezheng.github.io`, `Green-Machine` (HackMIT 2021) |
| M1shaaa | 8 | `M1shaaa` profile, `lab-bookshelf-` (TypeScript), Yale Lookit research |
| AustinCStone | 40 | `TextGAN` (92★ TF GAN), `StereoVisionMRF` (11★), `EpsteinSearch` |

### GF(3) Increment Chain (this run)

| ID | Source | Trit | Color | Name |
|---|---|---|---|---|
| ..+1 | plurigrid | 0 | #d3869b | ERGODIC |
| ..+2 | kubeflow | 1 | #b8bb26 | PLUS |
| ..+3 | TeglonLabs | -1 | #cc241d | MINUS |
| ..+4 | bmorphism | 0 | #d3869b | ERGODIC |
| ..+5 | zubyul | 1 | #b8bb26 | PLUS |
| ..+6 | migalkin | -1 | #cc241d | MINUS |
| ..+7 | DJedamski | 0 | #d3869b | ERGODIC |
| ..+8 | wasita | 1 | #b8bb26 | PLUS |
| ..+9 | kristinezheng | -1 | #cc241d | MINUS |
| ..+10 | M1shaaa | 0 | #d3869b | ERGODIC |
| ..+11 | AustinCStone | 1 | #b8bb26 | PLUS |

### DuckDB Tables (cumulative ducklake)
- `world_increments`: 34 rows (GF3 increment records across sweeps)
- `repo_snapshots`: 1134 rows (cumulative across all sweeps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A-Z)

**Snapshot:** 2026-06-29 | **Network:** Aptos Mainnet  
All 28 addresses returned **0.0 APT** — CoinStore resources not initialized on mainnet.

| World | Balance (APT) |
|---|---|
| alice (0xc793...cc7b) | 0.0 |
| bob (0x0a3c...512d) | 0.0 |
| A–Z (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts **healthy** (sigs_required=2):

| Pair | Address (truncated) | Sigs | Status |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**: behind Vercel deployment protection. No market data extractable.

---

## DuckDB Schema

```
world-increments.duckdb
├── world_increments   (34 rows)   — GF3-colored increment events
├── repo_snapshots     (1134 rows) — cumulative repo snapshots (all sweeps)
├── aptos_snapshots    (28 rows)   — Hamming swarm wallet balances
├── multisig_probes    (5 rows)    — multisig contract health probes
└── mnx_snapshots      (0 rows)    — unavailable (Vercel auth)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS  
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
