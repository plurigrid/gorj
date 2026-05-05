# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-05

## Sweep Metadata
- **Date:** 2026-05-05T04:xx UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-05-05 sweep)

| Metric | Value |
|--------|-------|
| New World Increments | 16 (11 sources + 5 bmorphism events) |
| New Repo Snapshots | 427 repos across 11 sources |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Pairs Probed | 5 |
| MNX Market Tickers | 17 |

---

## GF(3) Color Chain — 2026-05-05 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid (org) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism | ForkEvent: DavidJaz/DynamicalSystemsBook | 0 | `#d3869b` | **ERGODIC** |
| 13 | bmorphism | WatchEvent: DavidJaz/DynamicalSystemsBook | +1 | `#b8bb26` | **PLUS** |
| 14 | bmorphism | PushEvent: plurigrid/zig-syrup | -1 | `#cc241d` | **MINUS** |
| 15 | bmorphism | WatchEvent: hdresearch/ziggit | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | PushEvent: bmorphism/boxxy | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `PLUS→MINUS→ERGODIC×4 + ERGODIC→PLUS→MINUS→ERGODIC→PLUS (events)`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 addresses (alice, bob, A–Z)

All 28 addresses returned **0.0 APT** — accounts not funded / CoinStore not initialized on mainnet.

### Multisig Contract Probes — All HEALTHY

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi) — 17 tickers

**Top gainers:** MU +6.97% | USO +3.29% | DPREZ +2.00% | AMZN +1.66%  
**Top losers:** INTC -4.99% | SILVER -3.39% | ASML -3.09% | GOLD -1.52%  
**AI Valuations:** OAI26 $528B (+0.57%) | ANT26 $419B (-0.24%) | ECI26 170 (-0.58%)

| Ticker | Category | Price | Δ% |
|--------|----------|-------|----|
| OAI26 | AI | $528B | +0.57% |
| ANT26 | AI | $419B | -0.24% |
| ECI26 | AI | 170 | -0.58% |
| NVDA | Stocks | $197.83 | -0.21% |
| MSFT | Stocks | $413.01 | -0.12% |
| GOOGL | Stocks | $382.20 | -0.68% |
| AMZN | Stocks | $271.94 | +1.66% |
| META | Stocks | $608.89 | +0.08% |
| INTC | Stocks | $95.87 | -4.99% |
| TSM | Stocks | $400.32 | +0.60% |
| MU | Stocks | $577.15 | +6.97% |
| ASML | Stocks | $1,400 | -3.09% |
| GOLD | Commodities | $4,500 | -1.52% |
| SILVER | Commodities | $73.22 | -3.39% |
| USO | Commodities | $147.70 | +3.29% |
| DPREZ | Politics | 51% | +2.00% |
| INVADE27 | Politics | 17% | +0.61% |

---

## Notable Highlights

- **kubeflow/kubeflow**: 15,621 stars — flagship ML platform for Kubernetes
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **plurigrid/asi**: 17 stars — topological chemputer (pushed 2026-05-04)
- **bmorphism active**: ForkEvent + PushEvent on plurigrid/zig-syrup and bmorphism/boxxy
- **Hamming swarm**: All 5 multisig contracts confirm 2-of-2 signing — swarm coordination intact
- **MNX**: Micron surging +6.97%; Intel bleeding -4.99%; AI valuations diverging (OAI26 +0.57% vs ANT26 -0.24%)
