# World-Increment Sweep + Hamming Swarm Snapshot
**Timestamp:** 2026-06-08T02:00:00Z  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Summary
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 101 |
| bmorphism | user | 100 |
| TeglonLabs | org | 54 |
| kubeflow | org | 47 |
| AustinCStone | user (zubyul graph) | 43 |
| zubyul | user | 40 |
| wasita | user (zubyul graph) | 32 |
| migalkin | user (zubyul graph) | 30 |
| kristinezheng | user (zubyul graph) | 18 |
| M1shaaa | user (zubyul graph) | 16 |
| DJedamski | user (zubyul graph) | 11 |
| **TOTAL** | | **492 unique repos** |

### GF(3) Trit Distribution
- **ERGODIC** (trit=0, #d3869b): 164 increments
- **PLUS** (trit=1, #b8bb26): 164 increments  
- **MINUS** (trit=-1, #cc241d): 164 increments

### Notable Repos by Source

**plurigrid** (101 repos): Active Clojure/Rust/Zig/Julia ecosystem around Gay.jl deterministic coloring, OCapN/Spritely protocols, and categorical systems. Top: `gorj` (431 open issues, pushed 2026-06-08), `asi` (25★), `ontology` (8★, 9 forks).

**bmorphism** (100 repos): Heavy MCP server suite, Gay.jl color theory, OCaml/Zig/Clojure/Rust. Top: `ocaml-mcp-sdk` (61★), `anti-bullshit-mcp-server` (23★), `risc0-cosmwasm-example` (23★), `say-mcp-server` (20★), `babashka-mcp-server` (19★). `Gay.jl` pushed 2026-06-08 with 189 open issues.

**kubeflow** (47 repos): Enterprise ML/Kubernetes org. Top: `kubeflow/kubeflow` (15,706★), `pipelines` (4,152★, 494 issues), `spark-operator` (3,126★), `trainer` (2,112★), `katib` (1,685★). Dashboard pushed 2026-06-08.

**TeglonLabs** (54 repos): `jank-crane` (C++, GF3 convergence maps, pushed 2026-06-08), `mathpix-gem` (Ruby, 2★), `coin-flip-mcp` (JS, 2 forks).

**zubyul** (40 repos): `nash-tui` (Rust NASH token TUI), `gay-world` (Python, 1★), `tilelang-kernels` (GPU GF(3) kernels), `vibesnipe` (Move). Active through 2026-04.

**migalkin** (30 repos): Knowledge graph research. Top: `NodePiece` (144★, ICLR'22), `StarE` (89★, EMNLP'20), `kgcourse2021` (25★).

**AustinCStone** (43 repos): ML/CV research. Top: `TextGAN` (92★), `StereoVisionMRF` (11★). bmorphism connection via `bmfork` repos.

**wasita** (32 repos): Svelte/TypeScript personal projects. `wasita.github.io`, `wm-cv`, `magic-garden` (2★, Discord bot). Active through 2026-06.

**kristinezheng** (18 repos): MIT cognitive science, Lookit studies. `kristinezheng.github.io` pushed 2026-06-07.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...c7b | null (no CoinStore) |
| bob | 0x0a3c...5d | null |
| A | 0x8699...7a | null |
| B | 0x3f89...13 | null |
| C | 0x38b9...5e | null |
| D | 0xf776...d1 | null |
| E | 0xdc1d...36 | null |
| F | 0x18a1...71 | null |
| G | 0x69a3...32 | null |
| H | 0xce67...0f | null |
| I | 0x070f...c9 | null |
| J | 0x4d96...54 | null |
| K | 0xa732...c4 | null |
| L | 0x7c2e...a9 | null |
| M | 0x6fed...e9 | null |
| N | 0xe7dd...2c | null |
| O | 0x7325...9d | null |
| P | 0x6218...48 | null |
| Q | 0xac40...a9 | null |
| R | 0x7ce6...10 | null |
| S | 0xb875...86 | null |
| T | 0x3578...88 | null |
| U | 0x7586...56 | null |
| V | 0xb59d...c3 | null |
| W | 0x5f32...b0 | null |
| X | 0xa95c...7d | null |
| Y | 0xd8e3...c4 | null |
| Z | 0x7af0...7c | null |

**Status:** All 28 Hamming wallets return null CoinStore — accounts exist on-chain but hold no liquid APT in the standard `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` module. Consistent with wallets using object-based fungible assets or accounts that have never received APT directly.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|:---:|:---:|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**Status:** All 5 multisig contracts healthy — each requires exactly **2 signatures** (2-of-N threshold). `0x1::multisig_account::num_signatures_required` responded successfully for all pairs.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — `testnet.mnx.fi` is behind Vercel deployment protection requiring authentication. All API paths (`/api/markets`, `/api/tickers`, `/`) returned an authentication gate page rather than market data. No mnx_snapshots inserted.

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments     492 rows  (GF3-colored repo increment log)
├── repo_snapshots       492 rows  (full repo metadata)
├── aptos_snapshots       28 rows  (Hamming wallet balance snapshot)
├── multisig_probes        5 rows  (multisig health probes, all 2-of-N)
└── mnx_snapshots          0 rows  (unavailable — Vercel auth required)
```

## GF(3) Chain Integrity

The 492 world increments cycle perfectly through GF(3):
- trit=0 (ERGODIC, #d3869b): id%3==0 → 164 repos
- trit=1 (PLUS, #b8bb26): id%3==1 → 164 repos
- trit=-1 (MINUS, #cc241d): id%3==2 → 164 repos
