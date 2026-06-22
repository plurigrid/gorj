# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-22 02:10 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Distinct Repos |
|--------|------|---------------|
| plurigrid | org | 168 |
| kubeflow | org | 50 |
| TeglonLabs | org | 54 |
| bmorphism | user | 166 |
| zubyul | user | 59 |
| migalkin | user (zubyul social) | 30 |
| DJedamski | user (zubyul social) | 11 |
| wasita | user (zubyul social) | 31 |
| kristinezheng | user (zubyul social) | 18 |
| M1shaaa | user (zubyul social) | 16 |
| AustinCStone | user (zubyul social) | 43 |

**Total repo entries ingested:** 1,324 rows (646 distinct repos, GF3 color chain applied)

### GF(3) Color Chain Distribution
| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 133 |
| PLUS | #b8bb26 | +1 | 135 |
| MINUS | #cc241d | -1 | 135 |

### Notable Repos (by Stars)
| Org/User | Repo | Stars | Language | Last Push |
|----------|------|-------|----------|-----------|
| kubeflow | kubeflow | 15,739 | — | 2026-06-18 |
| kubeflow | pipelines | 4,156 | Python | 2026-06-20 |
| kubeflow | spark-operator | 3,127 | Python | 2026-06-18 |
| kubeflow | trainer | 2,118 | Go | 2026-06-19 |
| kubeflow | katib | 1,684 | Python | 2026-06-20 |
| migalkin | various | 834 total | — | — |
| bmorphism | various | 516 total | — | — |

### Recently Active (TeglonLabs)
- **jank-crane** (C++): crane-jank converged-IR hub, GF3 convergence maps — pushed 2026-06-08
- **mathpix-gem** (Ruby): Mathematical OCR gem — pushed 2026-01-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice-Z, 28 addresses)

All 28 hamming-swarm addresses returned "Resource not found" from the Aptos mainnet fullnode —
these accounts have no CoinStore resource registered (no APT ever deposited on mainnet).
Balance recorded as NULL for all wallets.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793acdec12b4a6... | NULL |
| bob   | 0x0a3c00c58fdf902... | NULL |
| A-Z   | (all 26 addresses)  | NULL |

*All 28 addresses probed. Status: unfunded / no CoinStore resource on mainnet.*

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — 2-of-N threshold confirmed.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B  | 0x0da4f428a0c007... | 2 | OK |
| A-G  | 0xf56c4a1c090621... | 2 | OK |
| Y-Z  | 0xd3ffe1812b2df4... | 2 | OK |
| S-T  | 0x3b1c3ae905d44c... | 2 | OK |
| V-W  | 0x40fad7b423a843... | 2 | OK |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — testnet.mnx.fi is Vercel-auth-gated (HTTP 401).
No market data could be extracted. mnx_snapshots table is empty.

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| world_increments | 403 |
| repo_snapshots | 1,324 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Key Takeaways

1. **GitHub graph is active**: kubeflow is the highest-activity org (15k+ stars, active June 2026).
   TeglonLabs' jank-crane (GF3 convergence maps) was pushed just 14 days ago.
2. **Hamming swarm wallets are unfunded**: All 28 Aptos addresses (alice/bob + A-Z) have
   no APT balance on mainnet — likely pre-deployment or testnet-only addresses.
3. **Multisig infra is healthy**: All 5 multisig contracts (A-B, A-G, Y-Z, S-T, V-W)
   confirm 2-of-N signature policy active on mainnet.
4. **MNX testnet gated**: Requires Vercel bypass token — not publicly readable by agents.
