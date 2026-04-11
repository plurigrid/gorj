# World Increment Sweep + Hamming Swarm Snapshot
**Sweep Date:** 2026-04-11  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.1 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC `#d3869b` | id%3==1 → trit=1 PLUS `#b8bb26` | id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | Org | 98 |
| kubeflow | Org | 47 |
| TeglonLabs | Org | 4 |
| bmorphism | User | 99 |
| zubyul | User | 45 |
| migalkin | User (social) | 19 |
| DJedamski | User (social) | 6 |
| wasita | User (social) | 0 (no public repos) |
| kristinezheng | User (social) | 6 |
| M1shaaa | User (social) | 8 |
| AustinCStone | User (social) | 40 |
| **TOTAL** | | **372** |

### Top Repos by Stars
| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | - | 15,565 | 2,626 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,119 | 1,984 | 2026-04-11 |
| kubeflow/spark-operator | Python | 3,111 | 1,483 | 2026-04-10 |
| kubeflow/trainer | Go | 2,080 | 944 | 2026-04-10 |
| kubeflow/katib | Python | 1,676 | 521 | 2026-04-02 |
| kubeflow/examples | Jsonnet | 1,458 | 755 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,010 | 1,069 | 2026-04-09 |
| kubeflow/arena | Go | 808 | 190 | 2026-04-10 |
| kubeflow/kale | Python | 682 | 156 | 2026-04-10 |
| migalkin/NodePiece | Python | 143 | - | 2022-02-02 |
| migalkin/StarE | Python | 88 | - | 2023-12-01 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-01-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2 | 2026-03-16 |
| plurigrid/asi | HTML | 16 | 5 | 2026-04-10 |

### Notable Recent Activity (Apr 2026)
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) trit coloring (pushed 2026-04-11)
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure in Zig 0.15, interaction nets, fuel-bounded eval
- `plurigrid/asi-skills` — 69 skills with Galois Hole Type accessibility
- `bmorphism/boxxy` — Move language (pushed 2026-04-09)
- `bmorphism/postweb` — evolved from prepostweb (Go, pushed 2026-04-09)
- `zubyul/big-bad-plurigrid-quiz` — Emacs Lisp (pushed 2026-04-09)
- `kubeflow/pipelines` — active ML pipeline work (pushed 2026-04-11)
- `M1shaaa/M1shaaa` — GitHub profile config (pushed 2026-04-11)
- `kristinezheng/kristinezheng.github.io` — portfolio site (pushed 2026-04-09)

### DuckDB Tables
- `world_increments`: 382 rows (GF(3) color-coded repo events, cumulative)
- `repo_snapshots`: 842 rows (full repo metadata, cumulative)

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-11)
All 28 addresses (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 addresses returned **0.00000000 APT** — CoinStore resource not yet registered (accounts likely pre-funded or awaiting initialization).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.00000000 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.00000000 |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0.00000000 |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | 0.00000000 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | 0.00000000 |
| D | 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 | 0.00000000 |
| E | 0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36 | 0.00000000 |
| F | 0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71 | 0.00000000 |
| G | 0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32 | 0.00000000 |
| H | 0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f | 0.00000000 |
| I | 0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9 | 0.00000000 |
| J | 0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54 | 0.00000000 |
| K | 0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4 | 0.00000000 |
| L | 0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9 | 0.00000000 |
| M | 0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9 | 0.00000000 |
| N | 0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c | 0.00000000 |
| O | 0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d | 0.00000000 |
| P | 0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948 | 0.00000000 |
| Q | 0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9 | 0.00000000 |
| R | 0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10 | 0.00000000 |
| S | 0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386 | 0.00000000 |
| T | 0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588 | 0.00000000 |
| U | 0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956 | 0.00000000 |
| V | 0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3 | 0.00000000 |
| W | 0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0 | 0.00000000 |
| X | 0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d | 0.00000000 |
| Y | 0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4 | 0.00000000 |
| Z | 0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c | 0.00000000 |

### Multisig Contract Probes — 5/5 HEALTHY
Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | HEALTHY |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | HEALTHY |

All 5 multisig accounts require **2-of-N signatures** and are live on Aptos mainnet.

### MNX Markets (testnet.mnx.fi — "The AI Exchange")
Platform: Next.js SPA — perpetual/futures trading across 40+ markets (AI, Stocks, Politics, Commodities).

| Ticker | Name | Category | Price | 24h Change | 24h Volume |
|--------|------|----------|-------|------------|------------|
| OAI26 | OpenAI Final 2026 Valuation | Valuations | $529B | +0.38% | $293.6M |
| ANT26 | Anthropic Final 2026 Valuation | Valuations | $419B | — | $289.2M |
| AAPL | Apple | Stocks | $260.83 | +0.40% | $294.9M |
| ASML | ASML Holding | Stocks | $1,500 | +2.34% | $294.3M |
| NVDA | NVIDIA | Stocks | $188.63 | +2.91% | $293.1M |
| DEM28 | Democrat 2028 Presidency | Politics | 51% | — | — |
| TWNINV | China-Taiwan Invasion | Politics | 17% | — | — |
| GOLD | Gold | Commodities | — | — | — |
| SILVER | Silver | Commodities | — | — | — |
| OIL | Oil | Commodities | — | — | — |

Additional categories present: AI benchmarks (FrontierMath, Arc AGI 2, Epoch Capabilities Index), Treasury ETFs, Volatility indices.

---

## DuckDB Schema Summary
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

## Useful Queries
```sql
-- Repo counts by source (this sweep)
SELECT org_or_user, COUNT(DISTINCT full_name) as repos
FROM repo_snapshots GROUP BY org_or_user ORDER BY repos DESC;

-- GF(3) trit distribution
SELECT gf3_trit, gf3_color, gf3_name, COUNT(*)
FROM world_increments GROUP BY 1,2,3 ORDER BY 1;

-- Aptos swarm health
SELECT COUNT(*) as total, SUM(balance_apt) as total_apt FROM aptos_snapshots;

-- Multisig health
SELECT COUNT(*) as probed,
       SUM(CASE WHEN healthy THEN 1 ELSE 0 END) as healthy
FROM multisig_probes;
```
