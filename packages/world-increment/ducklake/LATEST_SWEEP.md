# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 133 |
| Total Repo Snapshots | 133 |
| Sources Covered | 3 orgs + 8 users = 11 sources |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Market Data | UNAVAILABLE (auth required) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources & Coverage

| Source | Type | Repos Snapshotted | Total Stars | Latest Push |
|--------|------|-------------------|-------------|-------------|
| kubeflow | org | 20 of 48 | 33,123 | 2026-06-24T16:53Z |
| plurigrid | org | 25 of 100 | 69 | 2026-06-24T16:15Z |
| TeglonLabs | org | 5 of 5 | 2 | 2026-06-08T19:03Z |
| bmorphism | user | 20 of 100 | 207 | 2026-06-24T00:35Z |
| zubyul | user | 15 of 49 | 7 | 2026-04-24T05:56Z |
| migalkin | user | 8 of 19 | 280 | 2026-05-28T20:19Z |
| DJedamski | user | 6 of 6 | 3 | 2023-04-21T01:42Z |
| wasita | user | 11 of 11 | 5 | 2026-06-19T21:22Z |
| kristinezheng | user | 5 of 5 | 0 | 2026-06-07T22:53Z |
| M1shaaa | user | 8 of 8 | 0 | 2026-02-04T19:32Z |
| AustinCStone | user | 10 of 40 | 107 | 2026-04-01T07:39Z |

### Top Repos by Stars

| Repo | Stars | Language | Open Issues | Last Push |
|------|-------|----------|-------------|-----------|
| kubeflow/kubeflow | 15,742 | — | 0 | 2026-06-18 |
| kubeflow/pipelines | 4,157 | Python | 447 | 2026-06-24 |
| kubeflow/spark-operator | 3,128 | Python | 107 | 2026-06-24 |
| kubeflow/trainer | 2,119 | Go | 127 | 2026-06-24 |
| kubeflow/katib | 1,685 | Python | 112 | 2026-06-23 |
| kubeflow/examples | 1,460 | Jsonnet | 111 | 2025-04-14 |
| kubeflow/community-distribution | 1,028 | YAML | 22 | 2026-06-24 |
| migalkin/NodePiece | 144 | Python | 0 | 2026-05-07 |
| migalkin/StarE | 89 | Python | 1 | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 5 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 0 | 2026-03-16 |
| plurigrid/asi | 26 | HTML | 4 | 2026-06-10 |
| migalkin/kgcourse2021 | 25 | HTML | 0 | 2026-02-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 1 | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 1 | 2022-10-20 |

### Most Active Today (2026-06-24)
- `kubeflow/spark-operator` — 3,128★ Python
- `kubeflow/pipelines` — 4,157★ Python (447 open issues)
- `kubeflow/community-distribution` — 1,028★ YAML
- `kubeflow/hub` — 173★ Go (Model Registry)
- `kubeflow/sdk` — 121★ Python
- `kubeflow/mcp-server` — 17★ Python
- `kubeflow/trainer` — 2,119★ Go
- `kubeflow/notebooks` — 73★ (179 open issues)
- `plurigrid/gorj` — 0★ Clojure **(792 open issues — most in sweep)**
- `plurigrid/place` — 1★ TeX
- `bmorphism/Gay.jl` — 2★ Julia (187 open issues)

### Notable Observations
- **plurigrid/gorj** has 792 open issues today — highest of any repo in the sweep. This is the active working repo (forj + Rama + GF(3) coloring).
- **kubeflow** is extremely active with 8+ repos pushed today; now ships MCP servers (`kubeflow/mcp-server`, `kubeflow/mcp-apache-spark-history-server`).
- **bmorphism** pattern: 100 repos dominated by MCP servers and OCaml/Julia work. `ocaml-mcp-sdk` (61★) using Jane Street's oxcaml_effect is the standout.
- **migalkin** focuses on Knowledge Graph ML research; `NodePiece` (144★, ICLR'22) is the flagship.
- **TeglonLabs/jank-crane** (C++, GF3 convergence maps) is the newest org repo, pushed 2026-06-08.
- **zubyul** is polyglot and experimentally dense: Rust TUIs for NASH token, Julia GF(3) color, Python BCI, Zig, Move (Aptos). Most recent: `voice-observatory` (Python, 2026-04-24).
- **AustinCStone** links to bmorphism via `bmfork`/`bmforkupdate` repos; also has `EpsteinSearch` (Python, Feb 2026).
- **wasita** active Svelte/TypeScript developer with recent `proj-template` and `wasita.github.io` pushes.

### GF(3) World Increment Chain (133 increments)

Chain cycles: ERGODIC (#d3869b) → PLUS (#b8bb26) → MINUS (#cc241d) → repeat

| id%3 | trit | color | name | count |
|------|------|-------|------|-------|
| 0 | 0 | #d3869b | ERGODIC | 45 |
| 1 | +1 | #b8bb26 | PLUS | 44 |
| 2 | -1 | #cc241d | MINUS | 44 |

Increment #1 = plurigrid/gorj (ERGODIC, #d3869b)  
Increment #133 = AustinCStone/stonks (ERGODIC, #d3869b)  
GF(3) net: 45 ERGODIC − 44 PLUS − 44 MINUS → balanced field

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

**Queried:** Aptos mainnet fullnode at ledger version ~5,906,126,049  
**Status:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

This indicates the addresses exist on-chain but have not initialized the APT native coin store (zero APT, no on-chain APT activity, or accounts hold only non-APT assets).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...e197c | 0.0 |

**Total APT across swarm:** 0.0 APT  
**Swarm addresses with balance:** 0 of 28

### Multisig Contract Probes (5 contracts)

Probed `0x1::multisig_account::num_signatures_required` via Aptos View API.  
All 5 contracts returned `["2"]` — 2-of-N threshold. All healthy.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisigs healthy — consistent 2-of-N threshold across all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**  
`testnet.mnx.fi` is protected by Vercel deployment authentication. Both `/api/markets` and `/` return an auth-gated SPA requiring a Vercel OIDC token or bypass key. No market data extracted. `mnx_snapshots` table remains empty.

---

## DuckDB Schema

```sql
world_increments  -- 133 rows
  id INTEGER, timestamp TIMESTAMP, gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR

repo_snapshots    -- 133 rows
  id INTEGER, timestamp TIMESTAMP, increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR

aptos_snapshots   -- 28 rows
  timestamp TIMESTAMP, world VARCHAR, address VARCHAR, balance_apt DOUBLE

multisig_probes   -- 5 rows
  timestamp TIMESTAMP, pair VARCHAR, address VARCHAR,
  sigs_required INTEGER, healthy BOOLEAN

mnx_snapshots     -- 0 rows (unavailable)
  timestamp TIMESTAMP, ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent — 2026-06-24*
