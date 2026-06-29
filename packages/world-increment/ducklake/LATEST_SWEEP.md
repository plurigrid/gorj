# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-29 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 10 |
| kubeflow | org | 8 (top by stars) |
| TeglonLabs | org | 4 |
| bmorphism | user | 9 |
| zubyul | user | 5 |
| migalkin | user | 4 (social graph) |
| DJedamski | user | 2 (social graph) |
| wasita | user | 3 (social graph) |
| kristinezheng | user | 2 (social graph) |
| AustinCStone | user | 2 (social graph) |
| M1shaaa | user | 2 (social graph) |

**Total world_increments:** 51
**Total repo_snapshots:** 51

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 17 |
| 1 | #b8bb26 | PLUS | 17 |
| -1 | #cc241d | MINUS | 17 |

### Top Repos by Stars

| org/user | repo | stars | GF3 |
|----------|------|-------|-----|
| kubeflow | kubeflow | 15,750 | MINUS #cc241d |
| kubeflow | pipelines | 4,161 | ERGODIC #d3869b |
| kubeflow | spark-operator | 3,129 | PLUS #b8bb26 |
| kubeflow | trainer | 2,127 | MINUS #cc241d |
| kubeflow | katib | 1,687 | ERGODIC #d3869b |
| kubeflow | arena | 814 | PLUS #b8bb26 |
| migalkin | NodePiece | 144 | MINUS #cc241d |
| AustinCStone | TextGAN | 92 | PLUS #b8bb26 |
| migalkin | StarE | 89 | ERGODIC #d3869b |
| bmorphism | ocaml-mcp-sdk | 61 | MINUS #cc241d |

### Notable Activity (plurigrid/gorj ecosystem)

- `plurigrid/gorj`: 908 open issues — active GF(3) nREPL routing work, pushed today
- `plurigrid/asi`: 27 stars — topological chemputer, pushed today
- `plurigrid/place`: pushed today — bci.place forester preview
- `bmorphism/Gay.jl`: 187 open issues — wide-gamut SPI color sampling

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A-Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at Ledger version ~6,001,190,293.

**Interpretation:** These accounts exist on Aptos mainnet but hold no APT coin resource — either zero-balance or uninitialized coin store. All recorded as 0.0 APT.

| World | Address | Balance APT |
|-------|---------|------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig accounts responded via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All contracts require 2-of-N signatures. **5/5 healthy.**

### MNX Markets

`https://testnet.mnx.fi` requires Vercel deployment protection authentication. Market data **unavailable** — no bypass token present. `mnx_snapshots` table left empty.

---

## DuckDB Schema Summary

```
world_increments  — 51 rows (GF3-colored repo event log)
repo_snapshots    — 51 rows (org/user repos with metadata)
aptos_snapshots   — 28 rows (all 0.0 APT, resource_not_found)
multisig_probes   —  5 rows (all healthy, 2 sigs required)
mnx_snapshots     —  0 rows (Vercel auth required)
```

---

## Notes

- GitHub OR-query syntax for `user:X OR user:Y` is not supported; each user queried individually
- GF(3) color chain: `id%3==0 -> ERGODIC #d3869b`, `id%3==1 -> PLUS #b8bb26`, `id%3==2 -> MINUS #cc241d`
- Snapshot hash: MD5(full_name)[:12]
- DuckDB CLI: v1.x installed at `/usr/local/bin/duckdb`
