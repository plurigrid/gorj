# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-14T15:12Z  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Top Stars |
|--------|------|-------------------|-----------|
| plurigrid | org | 54 (101 total) | vcg-auction ★7, agent ★5, ontology ★8 |
| kubeflow | org | 27 | kubeflow/kubeflow ★15722, pipelines ★4153, spark-operator ★3127 |
| TeglonLabs | org | 5 | mathpix-gem ★2, jank-crane ★0 |
| bmorphism | user | 17 | ocaml-mcp-sdk ★61, anti-bullshit-mcp ★23, risc0-cosmwasm ★23 |
| zubyul | user | 10 | gay-world ★1 |
| migalkin | social | 5 | NodePiece ★144, StarE ★89 |
| wasita | social | 3 | wasita.github.io ★1, magic-garden ★2 |
| kristinezheng | social | 2 | (MIT/BCI research) |
| M1shaaa | social | 2 | (lab research) |
| DJedamski | social | 2 | (data science) |
| AustinCStone | social | 2 | TextGAN ★92 |

### Notable Activity (Recently Pushed)

- **plurigrid/gorj** — pushed 2026-06-14 (today), 573 open issues — forj + Rama topology nREPL + GF(3) trit coloring
- **bmorphism/Gay.jl** — pushed 2026-06-14, 189 open issues — wide-gamut color sampling with splittable determinism
- **kubeflow/pipelines** — pushed 2026-06-14, 480 open issues — 4153 stars
- **TeglonLabs/jank-crane** — pushed 2026-06-08 — crane-jank converged-IR hub with GF3 convergence maps

### GF(3) Color Chain (This Run — 130 new increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 50 |
| +1 | `#b8bb26` | PLUS | 52 |
| -1 | `#cc241d` | MINUS | 51 |

### DuckDB Cumulative State

| Table | Rows |
|-------|------|
| world_increments | 153 |
| repo_snapshots | 1074 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses in the Hamming swarm (alice, bob, A–Z) returned **0 APT** — the `CoinStore<AptosCoin>` resource is not registered on these addresses (accounts have not received or sent APT on mainnet). This is expected for uninitialized accounts.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

All 5 pairwise multisig accounts are **healthy** — `num_signatures_required` returns `2` for all.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — testnet.mnx.fi is protected by Vercel deployment authentication. The site returns an auth challenge page requiring a Vercel bypass token or OIDC trusted source. No market data extracted. MNX snapshots table is empty for this run.

---

## Summary

- **GitHub sweep**: 130 new repo snapshots across 11 sources (3 orgs, 2 users, 6 social graph nodes). plurigrid/gorj (this repo) is the most recently active plurigrid project. kubeflow/kubeflow at ★15,722 is the dominant project in the graph. bmorphism's ocaml-mcp-sdk (★61) is the most active social node.
- **Hamming swarm**: All 28 Aptos wallet addresses have 0 APT (uninitialized CoinStore). All 5 multisig contracts are healthy (2-of-2 sigs required).
- **MNX**: Inaccessible due to Vercel auth gate.
