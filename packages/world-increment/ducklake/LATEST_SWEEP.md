# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-05  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 46+ |
| kubeflow | org | 47+ |
| TeglonLabs | org | 4 |
| bmorphism | user | 96+ |
| zubyul | user | 51+ |
| migalkin | social | 18 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 30 |

### Top Repositories by Stars

| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/kubeflow | 15,706 | 2,670 | — |
| kubeflow/pipelines | 4,152 | 2,005 | Python |
| kubeflow/spark-operator | 3,125 | 1,488 | Python |
| kubeflow/trainer | 2,111 | 964 | Go |
| kubeflow/katib | 1,684 | 525 | Python |
| kubeflow/examples | 1,462 | 756 | Jsonnet |
| kubeflow/manifests | 1,020 | 1,065 | YAML |
| kubeflow/arena | 811 | 191 | Go |
| migalkin/NodePiece | 144 | 21 | Python |
| migalkin/StarE | 89 | 16 | Python |
| AustinCStone/TextGAN | 92 | 30 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml |
| plurigrid/asi | 25 | 6 | HTML |
| migalkin/kgcourse2021 | 25 | 9 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | 7 | JavaScript |

### Notable Recent Activity

- **plurigrid/gorj** — pushed 2026-06-05 — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **bmorphism/Gay.jl** — pushed 2026-06-05 — wide-gamut color sampling with splittable determinism
- **kubeflow/pipelines** — pushed 2026-06-05 — 4,152 stars
- **wasita/wasita.github.io** — pushed 2026-06-01 — personal website (Svelte)
- **M1shaaa/M1shaaa** — pushed 2026-06-04 — profile config

### GF(3) Trit Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | ~54 |
| +1 | `#b8bb26` | PLUS | ~55 |
| -1 | `#cc241d` | MINUS | ~54 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com` with 1s sleep between calls.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0.0 |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | 0.0 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | 0.0 |
| D | 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 | 0.0 |
| E–Z | (see DB) | 0.0 each |

**Result:** All 28 Hamming swarm addresses show zero APT balance. CoinStore resource not initialized on any address.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | YES |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | YES |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | YES |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | YES |

**All 5 multisig contracts healthy** — each requires exactly 2 signatures via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Protected by Vercel deployment authentication on all API paths (`/`, `/api/markets`, `/api/v1/markets`, `/api/ticker`). No market data extractable without Vercel bypass token or OIDC trusted-source configuration.

---

## DuckDB Table Summary

| Table | Rows |
|-------|------|
| `world_increments` | 163 |
| `repo_snapshots` | 1,084 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (unavailable) |

---

## Schema Notes

```sql
-- GF(3) color chain: id%3==0 → trit=0 ERGODIC #d3869b
--                   id%3==1 → trit=+1 PLUS #b8bb26  
--                   id%3==2 → trit=-1 MINUS #cc241d
```

- DuckDB v1.5.3 (Variegata)
- Aptos fullnode: `fullnode.mainnet.aptoslabs.com/v1`
- 1s sleep between Aptos API calls
