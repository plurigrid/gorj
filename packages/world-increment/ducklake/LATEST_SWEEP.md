# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-24  
**DuckDB:** `world-increments.duckdb`  
**Tables:** `world_increments` (40 rows), `repo_snapshots` (40 rows), `aptos_snapshots` (28 rows), `multisig_probes` (5 rows)

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain
- id%3==0 → trit=0 **ERGODIC** #d3869b  
- id%3==1 → trit=1 **PLUS** #b8bb26  
- id%3==2 → trit=-1 **MINUS** #cc241d

### Org: plurigrid (10 repos snapshotted)

| repo | lang | ★ | pushed |
|------|------|---|--------|
| plurigrid/gorj | Clojure | 1 | 2026-07-24 |
| plurigrid/eirobri | Clojure | 0 | 2026-07-21 |
| plurigrid/place | TeX | 1 | 2026-07-14 |
| plurigrid/asi | HTML | 31 | 2026-07-10 |
| plurigrid/shrimp | — | 0 | 2026-07-03 |
| plurigrid/nash-portal | Rust | 2 | 2026-05-19 |
| plurigrid/zig-syrup | Zig | 2 | 2026-04-30 |
| plurigrid/asi-skills | Julia | 3 | 2026-04-26 |
| plurigrid/bci-blue-share | JavaScript | 0 | 2026-04-26 |
| plurigrid/nanoclj-zig | Zig | 1 | 2026-04-25 |

### Org: TeglonLabs (5 repos snapshotted)

| repo | lang | ★ | pushed |
|------|------|---|--------|
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 2026-01-01 |
| TeglonLabs/coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| TeglonLabs/monad-mcp-server | — | 0 | 2025-05-14 |
| TeglonLabs/topoi | Python | 0 | 2025-01-24 |

### Org: kubeflow (6 repos snapshotted, top by recency)

| repo | lang | ★ | pushed |
|------|------|---|--------|
| kubeflow/pipelines | Python | 4169 | 2026-07-24 |
| kubeflow/trainer | Go | 2153 | 2026-07-24 |
| kubeflow/spark-operator | Python | 3143 | 2026-07-17 |
| kubeflow/katib | Python | 1692 | 2026-07-22 |
| kubeflow/hub | Go | 178 | 2026-07-24 |
| kubeflow/mcp-server | Python | 29 | 2026-07-24 |

### User: bmorphism (5 repos snapshotted)

| repo | lang | ★ | pushed |
|------|------|---|--------|
| bmorphism/Gay.jl | Julia | 2 | 2026-07-24 |
| bmorphism/gay-chat | Scheme | 0 | 2026-07-14 |
| bmorphism/satreadout | HTML | 0 | 2026-06-20 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/world | Python | 0 | 2026-06-02 |

### User: zubyul (4 repos snapshotted)

| repo | lang | ★ | pushed |
|------|------|---|--------|
| zubyul/from-possible-worlds | TeX | 0 | 2026-07-18 |
| zubyul/voice-observatory | Python | 0 | 2026-04-24 |
| zubyul/nash-tui | Rust | 0 | 2026-04-13 |
| zubyul/gay-world | Python | 1 | 2026-03-26 |

### Social Graph: zubyul connections

| user | most recent repo | lang | pushed |
|------|-----------------|------|--------|
| migalkin | kgcourse2021 | HTML | 2026-07-10 |
| wasita | wasita.github.io | Svelte | 2026-07-21 |
| M1shaaa | M1shaaa | — | 2026-02-04 |
| kristinezheng | kristinezheng.github.io | HTML | 2026-07-01 |
| DJedamski | kaggle_ncaa18 | Jupyter Notebook | 2018-02-26 |
| AustinCStone | byteruckus | HTML | 2026-07-15 |

**Notable:** migalkin's NodePiece (144★) and StarE (89★) are most-starred in the social graph. bmorphism's ocaml-mcp-sdk has 61★. kubeflow/pipelines leads all with 4169★.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 wallets (alice, bob, A–Z) returned **0.00000000 APT**.  
The CoinStore resource was present but held zero balance. No active funds detected in the Hamming swarm on this sweep.

| range | count | total APT |
|-------|-------|-----------|
| alice/bob | 2 | 0.0 |
| A–Z | 26 | 0.0 |
| **TOTAL** | **28** | **0.0** |

### Multisig Contract Probes (5 pairs)

| pair | address | sigs_required | healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**All 5 multisigs healthy** — each requires 2-of-N signatures. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. The `/api/markets` and `/api/v1/markets` paths returned the SPA shell rather than JSON. **No market data was extractable** from the public API surface on this sweep. Status: **unavailable / SPA-only**.

---

## DuckDB Schema Summary

```
world_increments : 40 rows  (GF3-colored repo snapshot events)
repo_snapshots   : 40 rows  (full repo metadata)
aptos_snapshots  : 28 rows  (alice + bob + A-Z balances)
multisig_probes  :  5 rows  (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots    :  0 rows  (SPA unavailable)
```

GF(3) distribution across 40 world-increments:
- ERGODIC (trit=0, #d3869b): ids 3,6,9,...,39 → 13 entries
- PLUS (trit=1, #b8bb26): ids 1,4,7,...,40 → 14 entries
- MINUS (trit=-1, #cc241d): ids 2,5,8,...,38 → 13 entries
