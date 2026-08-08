# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-08-08  
**GF(3) Increment:** id=13 | trit=1 | **PLUS** `#b8bb26`  
**Sweep complete:** 35 total world_increments in ducklake

---

## JOB 1: GitHub Social Graph Sweep

### Source Access Summary

| Source | Type | Status |
|--------|------|--------|
| plurigrid/gorj | org/repo | ✅ Accessible (MCP-scoped) |
| kubeflow | org | ⛔ Proxy-restricted (non-repo endpoint) |
| TeglonLabs | org | ⛔ Proxy-restricted |
| bmorphism | user | ⛔ Proxy-restricted |
| zubyul | user | ⛔ Proxy-restricted |
| migalkin | user | ⛔ Proxy-restricted |
| DJedamski | user | ⛔ Proxy-restricted |
| wasita | user | ⛔ Proxy-restricted |
| kristinezheng | user | ⛔ Proxy-restricted |
| M1shaaa | user | ⛔ Proxy-restricted |
| AustinCStone | user | ⛔ Proxy-restricted |

> The proxy enforces repository-scoped endpoints only. Org/user repo listing endpoints return `"sessions are bound to their configured repositories"`. GitHub MCP access is scoped to `plurigrid/gorj`.

### plurigrid/gorj Snapshot

- **Latest commit:** `5b28fe016e0e` — 2026-05-08T14:04:34Z  
  `chore: ignore duckdb binary in repo root`  
- **Branches:** 50+ `world-increment/sweep-*` branches (2026-04-27 through 2026-05-02)  
- **Cadence:** Multiple sweeps/day; last master merge 2026-05-08  
- **Cumulative:** 945 repo_snapshots across all sweeps

### DuckDB State After This Sweep

```
world_increments : 35 rows (ids 1–13, incl. sweep_start + access_restricted markers)
repo_snapshots   : 945 rows (944 prior + 1 gorj this run)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 Hamming-swarm wallets queried against Aptos mainnet  
(`fullnode.mainnet.aptoslabs.com`).

| World | Balance (APT) |
|-------|--------------|
| alice | 0.0 |
| bob   | 0.0 |
| A–Z (26 wallets) | 0.0 each |

**Total APT held across swarm: 0.0 APT**  
All wallets are initialized on-chain (respond to resource queries) but hold no coins.

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...` | 2 | ✅ |
| A-G | `0xf56c4a1c...` | 2 | ✅ |
| Y-Z | `0xd3ffe181...` | 2 | ✅ |
| S-T | `0x3b1c3ae9...` | 2 | ✅ |
| V-W | `0x40fad7b4...` | 2 | ✅ |

**5/5 multisig contracts healthy. All enforce 2-of-2 signature threshold.**

### MNX Markets

`https://testnet.mnx.fi` — **unavailable as structured data**.  
Site responds as a single-page app (SPA); no JSON API paths  
(`/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`) returned parseable data.  
Status: recorded 0 mnx_snapshots.

### DuckDB Aptos/MNX State

```
aptos_snapshots  : 28 rows (all 0.0 APT, timestamp 2026-08-08)
multisig_probes  : 5 rows (all healthy, all 2-of-2)
mnx_snapshots    : 0 rows (SPA, no API accessible)
```

---

## GF(3) Color Chain (cumulative)

```
id % 3 == 0  →  trit=0   ERGODIC  #d3869b
id % 3 == 1  →  trit=1   PLUS     #b8bb26  ← this sweep (id=13)
id % 3 == 2  →  trit=-1  MINUS    #cc241d
```

Cycle position: sweep 13 completes the **5th full GF(3) cycle** (ids 1–12) and begins cycle 6 at PLUS.
