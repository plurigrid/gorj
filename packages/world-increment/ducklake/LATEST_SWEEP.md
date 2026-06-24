# World-Increment Sweep + Hamming Swarm Snapshot
**Run date:** 2026-06-24  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 11 World Increments

| id | GF3 trit | Color | Name | Source | Repos |
|----|----------|-------|------|--------|-------|
| 1 | +1 | #b8bb26 | PLUS | org/plurigrid | 28 |
| 2 | -1 | #cc241d | MINUS | org/kubeflow | 20 |
| 3 | 0 | #d3869b | ERGODIC | org/TeglonLabs | 5 |
| 4 | +1 | #b8bb26 | PLUS | user/bmorphism | 20 |
| 5 | -1 | #cc241d | MINUS | user/zubyul | 14 |
| 6 | 0 | #d3869b | ERGODIC | user/migalkin | 5 |
| 7 | +1 | #b8bb26 | PLUS | user/DJedamski | 3 |
| 8 | -1 | #cc241d | MINUS | user/wasita | 5 |
| 9 | 0 | #d3869b | ERGODIC | user/kristinezheng | 4 |
| 10 | +1 | #b8bb26 | PLUS | user/M1shaaa | 3 |
| 11 | -1 | #cc241d | MINUS | user/AustinCStone | 6 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

**Total repos snapshotted: 113**

### Notable Repos by Source

**plurigrid** (101 total, 28 sampled) — most active: `gorj` (788 open issues, pushed 2026-06-24), `eirobri` (30 issues), `asi` (26★). Key projects: nanoclj-zig, zig-syrup, Gay.jl ecosystem, nash-portal.

**kubeflow** (48 total, 20 sampled) — most active: `pipelines` (4157★), `kubeflow` meta (15742★), `spark-operator` (3128★), `trainer` (2119★), `katib` (1685★). Active MCP work: `mcp-server` (17★), `mcp-apache-spark-history-server` (178★).

**TeglonLabs** (5 repos) — `jank-crane` (C++, GF3 convergence maps, pushed 2026-06-08), `mathpix-gem` (Ruby, 2★), `coin-flip-mcp` (JS, 2 forks), `monad-mcp-server`, `topoi`.

**bmorphism** (100+ total, 20 sampled) — active: `Gay.jl` (187 open issues!), `ocaml-mcp-sdk` (61★), `anti-bullshit-mcp-server` (23★), `say-mcp-server` (20★), `babashka-mcp-server` (19★). Heavy MCP server output.

**zubyul** (49 total, 14 sampled) — active: `plurigrid-site` (11 open issues), `vibesnipe`, `nash-tui`/`nash-web`. Lots of Gay.jl, GLSL, Move, Rust work.

**Social graph (zubyul connections):**
- **migalkin** — KG researcher: `NodePiece` (144★), `StarE` (89★), `RWL` (Weisfeiler-Leman Relational)
- **DJedamski** — Data science / Kaggle competitions
- **wasita** — Active 2026: `proj-template` (Jun 2026), `magic-garden` discord bot, `send2kobo`
- **kristinezheng** — MIT cognitive science, Lookit studies
- **M1shaaa** — Yale / `lab-bookshelf-` TypeScript project
- **AustinCStone** — `TextGAN` (92★), `StereoVisionMRF`; recent `bmfork`/`bmforkupdate` work

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.

**Result: all balances = 0.0 APT**

The `CoinStore<AptosCoin>` resource was absent or returned 0 for every address. These accounts either have not been funded on mainnet or hold other token types (e.g. MoveToken, fungible assets).

| Range | Count | Balances |
|-------|-------|---------|
| alice, bob | 2 | 0.0 APT each |
| A–Z | 26 | 0.0 APT each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ healthy |

All 5 multisig accounts live on Aptos mainnet, requiring **2-of-N signatures**. All healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` returns HTTP 401 (Vercel deployment protection). The testnet deployment requires Vercel authentication. API paths `/api/markets` and `/api/v1/markets` both return the same 401 page. No market data could be extracted.

---

## DuckDB Schema Summary

```sql
world_increments: 11 rows  (GF3 color-coded source snapshots)
repo_snapshots:  113 rows  (GitHub repos: stars/forks/issues/pushed_at)
aptos_snapshots:  28 rows  (Hamming swarm wallet balances, all 0.0 APT)
multisig_probes:   5 rows  (all require 2 sigs, all healthy)
mnx_snapshots:     0 rows  (unavailable — 401 Vercel auth)
```

Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`  
Sequences: `increment_seq`, `repo_seq`

---

## Key Signals

1. **plurigrid/gorj** is the most issue-heavy repo (788 open issues, pushed 2026-06-24) — active development hub
2. **bmorphism/Gay.jl** has 187 open issues — living spec/discussion tracker, forked by zubyul
3. **kubeflow MCP ecosystem** rapidly growing: `mcp-server`, `mcp-apache-spark-history-server` (178★) are new as of 2026
4. **All 28 Hamming swarm addresses hold 0 APT** on mainnet — swarm may hold other assets or operate on testnet
5. **All 5 multisig contracts healthy** with 2-sig threshold — governance infrastructure intact
6. **MNX testnet** gated behind Vercel auth — cannot sweep market data without token
7. **AustinCStone** recently created `bmfork`/`bmforkupdate` (May 2025) — connection to bmorphism work
8. **TeglonLabs/jank-crane** references GF3 convergence maps — direct tie to plurigrid/gorj ontology
