# World-Increment Sweep — 2026-06-28

## Sweep Metadata
- **Date:** 2026-06-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 14 |
| Total Repo Snapshots | 256 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Snapshots | 0 (auth-gated) |

---

## GF(3) Color Chain — All 14 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | aptos-mainnet (chain) | wallet_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 13 | aptos-multisig (chain) | multisig_probe | +1 | `#b8bb26` | **PLUS** |
| 14 | mnx-testnet (market) | market_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) rule: `id%3==1→PLUS(+1,#b8bb26)`, `id%3==2→MINUS(-1,#cc241d)`, `id%3==0→ERGODIC(0,#d3869b)`

---

## JOB 1: GitHub Social Graph Sweep

### Orgs

#### plurigrid (56 repos stored)
Most active today: `gorj` (882 open issues, pushed 2026-06-28), `asi` (26★, pushed 2026-06-28), `place` (pushed 2026-06-27), `eirobri` (30 issues).
Languages: Clojure, Rust, Julia, Zig, Haskell, Scheme, Python.
Core themes: GF(3) gay trit coloring, Spritely/OCapN, Rama topology, open games, nanoclj-zig.

#### kubeflow (49 repos stored)
Top by stars: `kubeflow` (15,750★), `pipelines` (4,158★), `spark-operator` (3,129★), `trainer` (2,125★), `katib` (1,687★).
Most active: `pipelines` (pushed 2026-06-27), `hub` (2026-06-27), `trainer` (2026-06-26), `spark-operator` (2026-06-26).
Active MCP work: `mcp-server` (17★), `mcp-apache-spark-history-server` (178★).

#### TeglonLabs (5 repos)
- `jank-crane` (C++, 2026-06-08) — crane-jank converged-IR hub, loopify pass spec, GF3 convergence maps
- `mathpix-gem` (Ruby, 2026-01-01, 2★) — mathematical OCR
- `coin-flip-mcp` (JavaScript, 2025-09-21) — random.org coin flips
- `topoi` (Python, 2025-01-24)
- `monad-mcp-server` (2025-05-14)

### Users

#### bmorphism (50 repos stored)
Top: `ocaml-mcp-sdk` (61★), `anti-bullshit-mcp-server` (23★), `risc0-cosmwasm-example` (23★), `say-mcp-server` (20★), `babashka-mcp-server` (19★).
Most active: `Gay.jl` (187 open issues, pushed 2026-06-28), `satreadout` (2026-06-20), `bci-preview` (2026-06-20).
MCP server collection: 10+ JS/Python MCP servers spanning Manifold, Penrose, Penumbra, ElevenLabs, Flox, GitHub Gists, marginallia, time.

#### zubyul (36 repos stored)
Themes: world-building (gay-world, cat-world, cascade-world), Gay.jl color sampling, NASH token TUI, OpenBCI/brain, tilelang GPU kernels.
Active: `plurigrid-site` (11 issues), `vibesnipe`, `nash-tui`/`nash-web`, `voice-observatory`.

### Zubyul Social Graph

| User | Repos | Notable |
|------|-------|---------|
| migalkin | 10 stored | NodePiece (144★), StarE (89★), kgcourse2021 (25★) — KG/GNN researcher |
| DJedamski | 6 | Data science/Kaggle, mostly 2014-2018 |
| wasita | 11 | wasita.github.io (active 2026-06-25), magic-garden bot, send2kobo |
| kristinezheng | 5 | MIT cognitive science, Lookit studies |
| M1shaaa | 8 | Lab bookshelf TypeScript, Yale coursework |
| AustinCStone | 17 stored | TextGAN (92★), bmfork/bmforkupdate (direct bmorphism link) |

**Social graph link discovered:** `AustinCStone/bmfork` and `AustinCStone/bmforkupdate` are direct forks of bmorphism's repos, establishing a confirmed edge in the social graph: `zubyul → AustinCStone → bmorphism`.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses probed)

All 28 addresses (alice, bob, A–Z) returned **null** from `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
The accounts have no registered APT CoinStore resource on mainnet — either unfunded or using a different coin module.
1 second sleep between each call (28 seconds total probe time).

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** and **active on Aptos mainnet**, each requiring **2-of-N signatures**:

| Pair | Address | sigs_required | healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...3f859cc | 2 | ✓ |
| Y-Z | 0xd3ffe181...e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| V-W | 0x40fad7b4...c80eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — site returns Vercel deployment protection auth wall.
Endpoints `/api/markets` and `/api/tickers` both require authentication.
0 rows stored in `mnx_snapshots`.

---

## DuckDB Schema

```sql
world_increments(id PK, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id PK, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(id, timestamp, world, address, balance_apt)
multisig_probes(id, timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(id, timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Findings

1. **plurigrid/gorj** (this repo) has 882 open issues — highest among plurigrid repos, pushed today.
2. **bmorphism/Gay.jl** has 187 open issues, pushed 2026-06-28 — actively maintained today.
3. **TeglonLabs/jank-crane** (newest, 2026-06-08) implements GF3 convergence maps — thematically aligned with this sweep.
4. **AustinCStone** has `bmfork` and `bmforkupdate` — confirmed social graph edge to bmorphism.
5. All 5 Aptos multisig pairs live and require exactly 2 signatures.
6. Hamming swarm wallets (A-Z) have no initialized APT CoinStore on mainnet.
7. kubeflow/kubeflow is the most-starred repo in the social graph at 15,750★.
8. **kubeflow MCP frontier**: both `mcp-server` and `mcp-apache-spark-history-server` (178★) are active as of this week.
