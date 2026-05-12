# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-05-12  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 10 (top by stars) |
| TeglonLabs | org | 4 |
| bmorphism | user | 12 (top by activity) |
| zubyul | user | 8 (top public) |
| migalkin | user (social graph) | 5 |
| AustinCStone | user (social graph) | 4 |
| DJedamski | user (social graph) | 4 |
| M1shaaa | user (social graph) | 4 |
| wasita | user (social graph) | 6 |
| kristinezheng | user (social graph) | 4 |
| **TOTAL** | | **161** |

> Note: GitHub unauthenticated API rate limit was exhausted (0/60); all queries completed via MCP GitHub tools.

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,629 | — |
| kubeflow/pipelines | 4,139 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,097 | Go |
| kubeflow/katib | 1,683 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |

### GF(3) Color Chain Distribution
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 53 |
| 1 | #b8bb26 | PLUS | 54 |
| -1 | #cc241d | MINUS | 54 |

**Total world increments:** 161

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses queried (alice, bob, A–Z). All returned `null` balance — accounts either do not exist on mainnet or hold zero APT in the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...512d | NULL |
| A–Z | 0x8699...–0x7af0... | NULL (all) |

### Multisig Contract Probes (Aptos Mainnet)
All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`. All healthy.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
`https://testnet.mnx.fi` is a Next.js SPA. No REST/JSON API endpoints found at `/api/markets` or `/api/v1/markets`. Market data **unavailable** — recorded as placeholder in `mnx_snapshots`.

---

## DuckDB Tables Summary

```
world_increments  -- 161 rows  (GF3-tagged repo push events)
repo_snapshots    -- 161 rows  (org, full_name, language, stars, forks, issues, pushed_at)
aptos_snapshots   --  28 rows  (alice, bob, A-Z; all balance_apt = NULL)
multisig_probes   --   5 rows  (all sigs_required=2, healthy=true)
mnx_snapshots     --   1 row   (unavailable placeholder)
```

## Notes
- Aptos balances: The Hamming swarm addresses have no APT balance on mainnet as of sweep date. This may indicate testnet-only activity or unconfigured accounts.
- All 5 multisig contracts (2-of-N) are live and responding on Aptos mainnet.
- MNX testnet is frontend-only; no programmatic market data API discovered.
