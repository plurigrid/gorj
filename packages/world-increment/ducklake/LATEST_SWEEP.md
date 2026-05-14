# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-14

## Sweep Metadata
- **Date:** 2026-05-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-05-14 run)

| Metric | Value |
|--------|-------|
| World Increments added | 11 (cumulative: 34) |
| Repo Snapshots added | 57 (cumulative: 1,001) |
| Aptos wallets snapshotted | 28 (alice, bob, A-Z) |
| Multisig contracts probed | 5 (all healthy, 2-of-N) |
| MNX Markets | SPA — no raw API data |
| Sources covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 2026-05-14 Increments (IDs 12-22)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 12 | plurigrid (org) | 0 | `#d3869b` | **ERGODIC** |
| 13 | kubeflow (org) | +1 | `#b8bb26` | **PLUS** |
| 14 | TeglonLabs (org) | -1 | `#cc241d` | **MINUS** |
| 15 | bmorphism (user) | 0 | `#d3869b` | **ERGODIC** |
| 16 | zubyul (user) | +1 | `#b8bb26` | **PLUS** |
| 17 | migalkin (social) | -1 | `#cc241d` | **MINUS** |
| 18 | DJedamski (social) | 0 | `#d3869b` | **ERGODIC** |
| 19 | wasita (social) | +1 | `#b8bb26` | **PLUS** |
| 20 | kristinezheng (social) | -1 | `#cc241d` | **MINUS** |
| 21 | M1shaaa (social) | 0 | `#d3869b` | **ERGODIC** |
| 22 | AustinCStone (social) | +1 | `#b8bb26` | **PLUS** |

GF(3) color assignment: `id%3==0 -> ERGODIC #d3869b | id%3==1 -> PLUS #b8bb26 | id%3==2 -> MINUS #cc241d`

### Repos Snapshotted (this run — 57 new rows)

| Org/User | Type | Repos | Top repo by stars |
|----------|------|-------|-------------------|
| **plurigrid** | org | 15 | `asi` (21*), `ontology` (8*) |
| **kubeflow** | org | 12 | `kubeflow/kubeflow` (15,630*), `pipelines` (4,140*) |
| **TeglonLabs** | org | 4 | `mathpix-gem` (2*) |
| **bmorphism** | user | 8 | `ocaml-mcp-sdk` (61*), `anti-bullshit-mcp-server` (23*) |
| **zubyul** | user | 6 | `gay-world` (1*) |
| **migalkin** | social | 3 | `NodePiece` (144*), `StarE` (89*) |
| **DJedamski** | social | 2 | `Kaggle` (1*) |
| **wasita** | social | 4 | `magic-garden` (2*) |
| **kristinezheng** | social | 1 | `kristinezheng.github.io` |
| **M1shaaa** | social | 1 | `lab-bookshelf-` |
| **AustinCStone** | social | 1 | `EpsteinSearch` |

### Notable Highlights
- **kubeflow/kubeflow**: 15,630 stars — flagship ML platform for Kubernetes (updated 2026-05-14)
- **kubeflow/pipelines**: 4,140 stars / 1,992 forks — pushed 2026-05-13
- **kubeflow/mcp-apache-spark-history-server**: new 2025, 170 stars — AI-native Spark debugging
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **migalkin/NodePiece**: 144 stars — parameter-efficient KG representations (ICLR 2022)
- **plurigrid/gorj**: 193 open issues — active Clojure/GF(3)/Rama development
- **plurigrid/nanoclj-zig** + **bmorphism/nanoclj-zig**: dual active forks of NaN-boxed Clojure in Zig

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

All 28 accounts returned **0 APT**. Accounts exist on-chain but hold no native APT (may hold other assets or be unfunded).

| World | Address |
|-------|---------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e |
| D | 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 |
| E | 0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36 |
| F | 0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71 |
| G | 0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32 |
| H | 0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f |
| I | 0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9 |
| J | 0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54 |
| K | 0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4 |
| L | 0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9 |
| M | 0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9 |
| N | 0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c |
| O | 0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d |
| P | 0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948 |
| Q | 0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9 |
| R | 0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10 |
| S | 0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386 |
| T | 0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588 |
| U | 0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956 |
| V | 0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3 |
| W | 0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0 |
| X | 0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d |
| Y | 0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4 |
| Z | 0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c |

### Multisig Contract Probes

Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | **2** | HEALTHY |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | **2** | HEALTHY |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | **2** | HEALTHY |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | **2** | HEALTHY |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | **2** | HEALTHY |

All 5 multisig accounts require **2-of-N** threshold and respond to on-chain view calls.

### MNX Markets (testnet.mnx.fi)

Returns a Next.js SPA on all probed routes (`/`, `/api/markets`, `/api/v1/markets`). No raw JSON API surface exposed via curl. Recorded as `SPA_UNAVAILABLE` in `mnx_snapshots`.

---

## Schema Reference

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
