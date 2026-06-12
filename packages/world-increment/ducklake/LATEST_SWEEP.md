# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-12  
**Branch:** world-increment/sweep-2026-06-12-0712  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Captured

| Source | Type | Repos | Last Snapshot |
|--------|------|-------|---------------|
| plurigrid | org | 200 | 2026-04-14 |
| kubeflow | org | 94 | 2026-04-14 |
| TeglonLabs | org | 111 | **2026-06-12** |
| bmorphism | user | 200 | 2026-04-14 |
| zubyul | user | 48 | 2026-04-14 |
| migalkin | user (social) | 79 | **2026-06-12** |
| DJedamski | user (social) | 28 | **2026-06-12** |
| wasita | user (social) | 71 | **2026-06-12** |
| kristinezheng | user (social) | 41 | **2026-06-12** |
| M1shaaa | user (social) | 40 | **2026-06-12** |
| AustinCStone | user (social) | 106 | **2026-06-12** |
| **TOTAL** | | **1,018** | |

### GF(3) Color Chain Distribution

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 31 |
| PLUS | +1 | `#b8bb26` | 33 |
| MINUS | -1 | `#cc241d` | 33 |

### Top Starred Repos (global, all sweeps)

| Repo | Language | ★ Stars |
|------|----------|---------|
| kubeflow/kubeflow | — | 15,572 |
| kubeflow/pipelines | Python | 4,119 |
| kubeflow/spark-operator | Python | 3,114 |
| kubeflow/trainer | Go | 2,082 |
| kubeflow/katib | Python | 1,678 |
| kubeflow/examples | Jsonnet | 1,459 |
| kubeflow/manifests | YAML | 1,010 |
| kubeflow/arena | Go | 809 |
| migalkin/NodePiece | Python | 144 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 |
| TeglonLabs/mathpix-gem | Ruby | 2 |

### Notable Fresh Activity (2026-06-12)

**TeglonLabs:**
- `jank-crane` (C++) — crane-jank converged-IR hub with GF3 convergence maps [2026-06-08]
- `mathpix-gem` (Ruby, ★2) — math image→LaTeX/SMILES OCR

**Zubyul social graph highlights:**
- `migalkin/NodePiece` ★144 — knowledge graph compositional embeddings (ICLR 2022)
- `migalkin/RWL` ★8 — Weisfeiler-Leman relational GNNs (LOG 2022, updated 2026-05-28)
- `wasita/wasita.github.io` — Svelte/SvelteKit site, active 2026-06-01
- `AustinCStone/EpsteinSearch` (Python) — pushed 2026-02-11
- `kristinezheng/kristinezheng.github.io` — updated 2026-06-07

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Ledger version at query time:** ~5.69B  
**Query:** `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<AptosCoin>`

### Wallet Balances

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | `0xc793acdec12b4a6371...` | null (uninitialized) |
| bob | `0x0a3c00c58fdf9020b2...` | null (uninitialized) |
| A | `0x8699edc0960dd5b916...` | null (uninitialized) |
| B | `0x3f892ebe6e45164e63...` | null (uninitialized) |
| C | `0x38b99e63ada9b6fef1...` | null (uninitialized) |
| D | `0xf77656248f64d5dd00...` | null (uninitialized) |
| E | `0xdc1d9d533bac3507f9...` | null (uninitialized) |
| F | `0x18a14b5b4bec118c1c...` | null (uninitialized) |
| G | `0x69a394c0b0ac842127...` | null (uninitialized) |
| H | `0xce67c327a7844e5488...` | null (uninitialized) |
| I | `0x070fe5d74e4eda30e2...` | null (uninitialized) |
| J | `0x4d964db8f538374034...` | null (uninitialized) |
| K | `0xa732040a6b0d559041...` | null (uninitialized) |
| L | `0x7c2eaeafad9725492e...` | null (uninitialized) |
| M | `0x6fed37a7553ef16b2a...` | null (uninitialized) |
| N | `0xe7dde6da0a65f51062...` | null (uninitialized) |
| O | `0x73252b6011a75115a2...` | null (uninitialized) |
| P | `0x6218792de4a9bc3891...` | null (uninitialized) |
| Q | `0xac40fa50b81b4ca6b1...` | null (uninitialized) |
| R | `0x7ce605cc8fda4f8e4a...` | null (uninitialized) |
| S | `0xb8753014e4888ea48a...` | null (uninitialized) |
| T | `0x35781dc0e42fef3f25...` | null (uninitialized) |
| U | `0x75860da47565f6509b...` | null (uninitialized) |
| V | `0xb59dd8170321dfab5a...` | null (uninitialized) |
| W | `0x5f32aef70f5ba530d3...` | null (uninitialized) |
| X | `0xa95cbbd116548ac990...` | null (uninitialized) |
| Y | `0xd8e32848f1dffa811b...` | null (uninitialized) |
| Z | `0x7af0ef6e1bd706f4b3...` | null (uninitialized) |

> All 28 addresses returned `resource_not_found` — coin stores are uninitialized on mainnet.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |

**All 5 multisig contracts are healthy** — each requires **2 signatures** and responded without error to `0x1::multisig_account::num_signatures_required`.

### MNX Testnet Markets

`https://testnet.mnx.fi/api/markets` — **UNAVAILABLE**  
Vercel deployment protection active (visitor password required). No market data retrieved.

---

## DuckDB Schema Summary

```sql
-- 1,018 rows across 11 sources
SELECT org_or_user, COUNT(*) FROM repo_snapshots GROUP BY 1;

-- 28 Aptos wallet snapshots (all null balances, uninitialized)
SELECT world, balance_apt FROM aptos_snapshots;

-- 5 multisig probes (all healthy, 2-of-N)
SELECT pair, sigs_required, healthy FROM multisig_probes;

-- GF3 color chain on world_increments (97 rows)
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2;
```

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*  
*2026-06-12T07:12 UTC*
