# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-12 14:14:50 UTC
**Session:** https://claude.ai/code/session_01RKiFNREwCTFuwLMLJoDZKg

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| # | Type | Source | GF3 ID | Trit | Color | Status |
|---|------|--------|--------|------|-------|--------|
| 1 | org  | plurigrid     | 13 | +1 PLUS    | #b8bb26 | ✓ MCP (gorj repo) |
| 2 | org  | kubeflow      | 14 | -1 MINUS   | #cc241d | rate-limited (unauthenticated) |
| 3 | org  | TeglonLabs    | 15 |  0 ERGODIC | #d3869b | rate-limited |
| 4 | user | bmorphism     | 16 | +1 PLUS    | #b8bb26 | rate-limited |
| 5 | user | zubyul        | 17 | -1 MINUS   | #cc241d | rate-limited |
| 6 | user | migalkin      | 18 |  0 ERGODIC | #d3869b | rate-limited |
| 7 | user | DJedamski     | 19 | +1 PLUS    | #b8bb26 | rate-limited |
| 8 | user | wasita        | 20 | -1 MINUS   | #cc241d | rate-limited |
| 9 | user | kristinezheng | 21 |  0 ERGODIC | #d3869b | rate-limited |
|10 | user | M1shaaa       | 22 | +1 PLUS    | #b8bb26 | rate-limited |
|11 | user | AustinCStone  | 23 | -1 MINUS   | #cc241d | rate-limited |

> GitHub REST API rate-limited at 60 req/hour for unauthenticated IPs. Full repo lists from kubeflow, TeglonLabs, bmorphism, zubyul, and Zubyul social graph require GITHUB_TOKEN.

### plurigrid/gorj (MCP Snapshot)
- **Branches:** 103 (including 100+ world-increment/sweep-* branches)
- **Last commit:** 2026-05-08T14:04:34Z — "chore: ignore duckdb binary in repo root"
- **Committer:** @claude
- **Branch pattern:** world-increment/sweep-YYYY-MM-DD-HHMM (active cadence since 2026-04-27)

### GF(3) Color Chain — DuckDB State
```
IDs 1–12  : prior sweeps (4 full GF(3) cycles)
IDs 13–24 : this sweep (IDs 13–23 = 11 sources, ID 24 = hamming_snapshot)
Total world_increments: 35
Total repo_snapshots:   945
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
Queried via `https://fullnode.mainnet.aptoslabs.com/v1/`  
Ledger version at time of sweep: **5,238,485,358** | Block height: **761,727,777** | Epoch: **15,774**

| World | Address (truncated) | APT Balance | Status |
|-------|---------------------|-------------|--------|
| alice | 0xc793...cc7b | 0.0 | resource_not_found |
| bob   | 0x0a3c...512d | 0.0 | resource_not_found |
| A     | 0x8699...9d7a | 0.0 | resource_not_found |
| B     | 0x3f89...b13  | 0.0 | resource_not_found |
| C     | 0x38b9...35e  | 0.0 | resource_not_found |
| D     | 0xf776...dd1  | 0.0 | resource_not_found |
| E     | 0xdc1d...d36  | 0.0 | resource_not_found |
| F     | 0x18a1...f71  | 0.0 | resource_not_found |
| G     | 0x69a3...f32  | 0.0 | resource_not_found |
| H     | 0xce67...00f  | 0.0 | resource_not_found |
| I     | 0x070f...fc9  | 0.0 | resource_not_found |
| J     | 0x4d96...f54  | 0.0 | resource_not_found |
| K     | 0xa732...dc4  | 0.0 | resource_not_found |
| L     | 0x7c2e...ba9  | 0.0 | resource_not_found |
| M     | 0x6fed...2e9  | 0.0 | resource_not_found |
| N     | 0xe7dd...b2c  | 0.0 | resource_not_found |
| O     | 0x7325...89d  | 0.0 | resource_not_found |
| P     | 0x6218...948  | 0.0 | resource_not_found |
| Q     | 0xac40...89a9 | 0.0 | resource_not_found |
| R     | 0x7ce6...e10  | 0.0 | resource_not_found |
| S     | 0xb875...386  | 0.0 | resource_not_found |
| T     | 0x3578...588  | 0.0 | resource_not_found |
| U     | 0x7586...956  | 0.0 | resource_not_found |
| V     | 0xb59d...2c3  | 0.0 | resource_not_found |
| W     | 0x5f32...7b0  | 0.0 | resource_not_found |
| X     | 0xa95c...47d  | 0.0 | resource_not_found |
| Y     | 0xd8e3...4c4  | 0.0 | resource_not_found |
| Z     | 0x7af0...97c  | 0.0 | resource_not_found |

> All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. These wallets have not initialized an APT CoinStore on mainnet.

### Multisig Contract Probes
All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...003 | 2 | ✅ |
| A-G  | 0xf56c...096 | 2 | ✅ |
| Y-Z  | 0xd3ff...883 | 2 | ✅ |
| S-T  | 0x3b1c...883 | 2 | ✅ |
| V-W  | 0x40fa...6d  | 2 | ✅ |

All 5 multisig accounts require **2 signatures** and are **healthy** (contracts respond on mainnet).

### MNX Markets (testnet.mnx.fi)
Status: **SPA — no REST API endpoints accessible**  
`https://testnet.mnx.fi/api/markets` returned Next.js SSR HTML (status 200). No machine-readable market data extracted. MNX appears to be a client-side rendered application with no public JSON API.

---

## DuckDB Summary

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments : 35 rows  (IDs 1–24 this sweep; 8 full GF(3) cycles)
  repo_snapshots   : 945 rows (plurigrid/gorj + historical org/user repos)
  aptos_snapshots  : 28 rows  (A–Z + alice/bob, all 0.0 APT)
  multisig_probes  :  5 rows  (A-B, A-G, Y-Z, S-T, V-W — all 2-of-N, healthy)
  mnx_snapshots    :  0 rows  (API unavailable — SPA only)
```
