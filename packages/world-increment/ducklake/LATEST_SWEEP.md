# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-12

## Sweep Metadata
- **Date:** 2026-06-12T03:07Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1275 |
| Unique Repos Indexed | 331 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (A–Z + alice + bob) |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain

GF(3) assignment rule:
- `id%3==0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id%3==1` → trit=1, color=`#b8bb26`, name=**PLUS**
- `id%3==2` → trit=-1, color=`#cc241d`, name=**MINUS**

34 increment rows spanning 11 sources:
`PLUS → MINUS → ERGODIC → ERGODIC → PLUS → PLUS → MINUS → ERGODIC → ERGODIC → PLUS → PLUS → MINUS → MINUS → ERGODIC → ...`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 40 |
| zubyul | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| kristinezheng | user | 5 |
| DJedamski | user | 6 |
| **TOTAL** | | **331** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,714 | Python | 2026-06-11 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-11 |
| kubeflow/spark-operator | 3,127 | Go | 2026-06-09 |
| kubeflow/trainer | 2,111 | Go | 2026-06-12 |

### Language Distribution (Top 10)

| Language | Repos |
|----------|-------|
| Python | 241 |
| HTML | 51 |
| Go | 50 |
| Rust | 47 |
| JavaScript | 44 |
| TypeScript | 42 |
| Jupyter Notebook | 39 |
| Clojure | 26 |
| Jsonnet | 23 |
| R | 22 |

### Notable Recent Activity
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): `crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow`
- **TeglonLabs/mathpix-gem** (Ruby, 2★): Mathematical OCR + LaTeX + SMILES
- **M1shaaa/M1shaaa** (pushed 2026-06-11): active profile config
- **kristinezheng/kristinezheng.github.io** (HTML, pushed 2026-06-07)
- **kubeflow/trainer** (Go, 2,111★, pushed 2026-06-12): most recently active kubeflow repo

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses probed on Aptos Mainnet (`fullnode.mainnet.aptoslabs.com/v1`).

**Result:** All 28 returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
CoinStore not initialized → accounts hold no APT. All balances: **0.000000 APT**.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.000000 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.000000 |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0.000000 |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | 0.000000 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | 0.000000 |
| D | 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 | 0.000000 |
| E | 0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36 | 0.000000 |
| F | 0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71 | 0.000000 |
| G | 0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32 | 0.000000 |
| H | 0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f | 0.000000 |
| I | 0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9 | 0.000000 |
| J | 0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54 | 0.000000 |
| K | 0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4 | 0.000000 |
| L | 0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9 | 0.000000 |
| M | 0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9 | 0.000000 |
| N | 0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c | 0.000000 |
| O | 0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d | 0.000000 |
| P | 0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948 | 0.000000 |
| Q | 0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9 | 0.000000 |
| R | 0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10 | 0.000000 |
| S | 0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386 | 0.000000 |
| T | 0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588 | 0.000000 |
| U | 0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956 | 0.000000 |
| V | 0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3 | 0.000000 |
| W | 0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0 | 0.000000 |
| X | 0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d | 0.000000 |
| Y | 0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4 | 0.000000 |
| Z | 0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c | 0.000000 |

### Multisig Contract Probes

All 5 contracts healthy — all return `sigs_required=2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — HTTP 401 (Vercel deployment protection, authentication required).
No market data accessible. Placeholder recorded in `mnx_snapshots`.

---

## DuckDB Schema

```
world_increments  : 34 rows  — GF(3)-colored increment events per source
repo_snapshots    : 1275 rows — repo metadata fan-out (331 unique repos × 3.85 pagination factor)
aptos_snapshots   : 28 rows  — Hamming swarm wallet balances (all 0 APT — CoinStore uninit)
multisig_probes   : 5 rows   — 2-of-N contracts all healthy
mnx_snapshots     : 1 row    — unavailable placeholder
```

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

## GF(3) Notable Highlights
- **kubeflow/kubeflow**: 15,714★ — flagship ML platform, pushed 2026-06-11 (MINUS chain)
- **kubeflow/trainer**: 2,111★, pushed 2026-06-12 — most recently active
- **migalkin** KG repos: NodePiece, StarE, ULTRA — knowledge graph embedding research
- **TeglonLabs/jank-crane**: GF3 convergence maps + loopify pass spec (most recent TeglonLabs push)
- **bmorphism/ocaml-mcp-sdk**: OCaml MCP SDK using Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92★ — text generation with GANs
- **Multisig swarm**: A-B, A-G, Y-Z, S-T, V-W — all 2-of-N, all online

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-06-12T03:07Z*
