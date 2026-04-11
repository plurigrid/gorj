# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-11

## Sweep Metadata
- **Date:** 2026-04-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) rule:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=+1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| # | Source | Type | Public Repos | GF(3) Trit | Color |
|---|--------|------|-------------|------------|-------|
| 1 | plurigrid | org | 98 | +1 PLUS | #b8bb26 |
| 2 | bmorphism | user | 99 | -1 MINUS | #cc241d |
| 3 | zubyul | user | 45 | 0 ERGODIC | #d3869b |
| 4 | TeglonLabs | org | 4 | +1 PLUS | #b8bb26 |
| 5 | kubeflow | org | 47 | -1 MINUS | #cc241d |
| 6 | migalkin | user (zubyul graph) | 19 | 0 ERGODIC | #d3869b |
| 7 | DJedamski | user (zubyul graph) | 6 | +1 PLUS | #b8bb26 |
| 8 | wasita | user (zubyul graph) | 9 | -1 MINUS | #cc241d |
| 9 | kristinezheng | user (zubyul graph) | 6 | 0 ERGODIC | #d3869b |
| 10 | M1shaaa | user (zubyul graph) | 8 | +1 PLUS | #b8bb26 |
| 11 | AustinCStone | user (zubyul graph) | 40 | -1 MINUS | #cc241d |

**Total repos crawled:** ~381 public repos  
**Repo snapshots stored:** 53 representative repos in DuckDB

### GF(3) Color Chain — All 11 Increments

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1  | plurigrid | +1 | `#b8bb26` | **PLUS** |
| 2  | bmorphism | -1 | `#cc241d` | **MINUS** |
| 3  | zubyul | 0 | `#d3869b` | **ERGODIC** |
| 4  | TeglonLabs | +1 | `#b8bb26` | **PLUS** |
| 5  | kubeflow | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | -1 | `#cc241d` | **MINUS** |

### Top Starred Repos

| Repo | Stars | Forks | Language | Last Pushed |
|------|-------|-------|----------|-------------|
| kubeflow/kubeflow | 15,565 | 2,626 | — | 2026-04-09 |
| kubeflow/pipelines | 4,119 | 1,983 | Python | 2026-04-11 |
| kubeflow/spark-operator | 3,111 | 1,483 | Python | 2026-04-06 |
| kubeflow/trainer | 2,080 | 944 | Go | 2026-04-10 |
| kubeflow/katib | 1,676 | 521 | Python | 2026-04-10 |
| migalkin/NodePiece | 143 | 21 | Python | 2026-03-02 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2025-03-03 |
| migalkin/StarE | 88 | 16 | Python | 2026-02-22 |
| bmorphism/ocaml-mcp-sdk | 60 | 2 | OCaml | 2026-03-28 |
| plurigrid/asi | 16 | 5 | HTML | 2026-04-08 |

### Most Active Last 48h

| Repo | Pushed |
|------|--------|
| kubeflow/sdk | 2026-04-11T07:10:54Z |
| kubeflow/pipelines | 2026-04-11T04:43:24Z |
| plurigrid/gorj | 2026-04-10T23:11:44Z |
| kubeflow/model-registry | 2026-04-10T22:07:29Z |
| plurigrid/horse | 2026-04-10T21:52:25Z |

### Notable Patterns

- **plurigrid**: active Clojure/Zig/Rust ecosystem — `gorj` (GF3 REPL), `nanoclj-zig` (Zig Clojure interpreter), `zig-syrup` (OCapN Syrup)
- **bmorphism**: heavy MCP server output — `ocaml-mcp-sdk` (60★ OCaml), `say-mcp-server` (20★), `babashka-mcp-server` (18★)
- **kubeflow**: largest source by stars; new `kubeflow/mcp-server` (2026-04-08) signals MCP adoption in MLOps
- **zubyul social graph**: akademik cluster (kristinezheng/M1shaaa/DJedamski — ML/neuroscience/statistics) + wasita (Women in Network Science)
- **migalkin**: knowledge graph research lineage — NodePiece, StarE, NBFNet_mlx for Apple Silicon

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Method: `POST /v1/view` → `0x1::coin::balance<0x1::aptos_coin::AptosCoin>` (FA-compatible)  
Ledger version at query time: ~4,838,444,000

| World | Balance (APT) | Address |
|-------|---------------|---------|
| alice | 0.43643352 | 0xc793...cc7b |
| bob | **12.657007** | 0x0a3c...512d |
| A | 0.051767 | 0x8699...9d7a |
| B | 0.036256 | 0x3f89...b13 |
| C | 0.010185 | 0x38b9...535e |
| D | 0.011629 | 0xf776...fdd1 |
| E | 0.012561 | 0xdc1d...8d36 |
| F | **1.960516** | 0x18a1...cf71 |
| G | 0.000681 | 0x69a3...7f32 |
| H | 0.000681 | 0xce67...300f |
| I | 0.000681 | 0x070f...1fc9 |
| J | **1.895093** | 0x4d96...7f54 |
| K | 0.161961 | 0xa732...dc4 |
| L | **1.927269** | 0x7c2e...ba9 |
| M | 0.112285 | 0x6fed...2e9 |
| N | 0.106121 | 0xe7dd...1b2c |
| O | 0.210136 | 0x7325...89d |
| P | 0.140136 | 0x6218...948 |
| Q | 0.103240 | 0xac40...89a9 |
| R | 0.090217 | 0x7ce6...6e10 |
| S | 0.091788 | 0xb875...386 |
| T | 0.073713 | 0x3578...588 |
| U | 0.055773 | 0x7586...956 |
| V | 0.047833 | 0xb59d...2c3 |
| W | 0.040705 | 0x5f32...7b0 |
| X | 0.042577 | 0xa95c...47d |
| Y | 0.044449 | 0xd8e3...44c4 |
| Z | 0.023268 | 0x7af0...97c |

**Total swarm:** ~20.69 APT  
**bob**: 12.66 APT (dominant)  
**F, J, L**: ~1.9 APT each (second tier)  
**G/H/I**: 0.000681 APT each (dust — gas minimum only)

### Multisig Contract Probes

Method: `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | **2-of-2** | ✓ |
| A-G | 0xf56c...096 | **2-of-2** | ✓ |
| Y-Z | 0xd3ff...883 | **2-of-2** | ✓ |
| S-T | 0x3b1c...883 | **2-of-2** | ✓ |
| V-W | 0x40fa...b6d | **2-of-2** | ✓ |

All 5 multisig accounts are live on mainnet, all require 2-of-2 signatures.

### MNX Markets

- `testnet.mnx.fi/api/markets` → Next.js SPA (HTML), no public REST endpoint
- `mnx.fi` → SPA ("MNX - The AI Exchange"), same constraint
- **Status: UNAVAILABLE** — market data embedded in client bundle, no accessible JSON API

---

## DuckDB Schema Summary

```sql
world_increments  -- 11 rows  (org/user snapshots with GF3 coloring)
repo_snapshots    -- 53 rows  (repos with stars/forks/language/pushed_at)
aptos_snapshots   -- 28 rows  (alice, bob, A-Z balances at ledger ~4.84B)
multisig_probes   --  5 rows  (all 2-of-2, all healthy)
mnx_snapshots     --  0 rows  (SPA only, no REST API)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — most starred ML toolkit for Kubernetes (pushed 2026-04-09)
- **kubeflow/pipelines**: 4,119 stars — ML pipeline engine (active 2026-04-11)
- **kubeflow/mcp-server**: brand new (2026-04-08) — MCP adoption spreading to MLOps
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Aptos swarm**: bob dominates at 12.66 APT; F/J/L hold ~1.9 APT each; G/H/I are dust wallets
