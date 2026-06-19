# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-19

## Sweep Metadata
- **Date:** 2026-06-19 22:18 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1 — GitHub Social Graph Sweep

### GF(3) Color Chain — 11 Increments

| id | source | type | trit | color | hex | repos |
|----|--------|------|------|-------|-----|-------|
| 1 | plurigrid | org | 1 PLUS | PLUS | #b8bb26 | 100 |
| 2 | kubeflow | org | -1 MINUS | MINUS | #cc241d | 48 |
| 3 | TeglonLabs | org | 0 ERGODIC | ERGODIC | #d3869b | 5 |
| 4 | bmorphism | user | 1 PLUS | PLUS | #b8bb26 | 104 |
| 5 | zubyul | user | -1 MINUS | MINUS | #cc241d | 49 |
| 6 | DJedamski | user | 0 ERGODIC | ERGODIC | #d3869b | 6 |
| 7 | kristinezheng | user | 1 PLUS | PLUS | #b8bb26 | 5 |
| 8 | M1shaaa | user | -1 MINUS | MINUS | #cc241d | 8 |
| 9 | migalkin | user | 0 ERGODIC | ERGODIC | #d3869b | 19 |
| 10 | AustinCStone | user | 1 PLUS | PLUS | #b8bb26 | 41 |
| 11 | wasita | user | -1 MINUS | MINUS | #cc241d | 11 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

**Total repo snapshots:** 391

---

## Job 2 — Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) queried via REST API.

**Result:** All 28 accounts returned `balance_apt = 0.0` — no `CoinStore<AptosCoin>` resource registered (uninitialized mainnet accounts).

### Multisig Contract Probes (5 contracts)

Probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`:

| pair | sigs_required | healthy |
|------|---------------|---------|
| A-B | 2 | ✓ |
| A-G | 2 | ✓ |
| Y-Z | 2 | ✓ |
| S-T | 2 | ✓ |
| V-W | 2 | ✓ |

All 5 multisig contracts healthy, all require 2-of-2 signatures.

### MNX Markets (`testnet.mnx.fi`)

**Status:** Vercel-deployed, password-protected. No market data extractable.

---

## DuckDB Table Summary

| table | rows | status |
|-------|------|--------|
| world_increments | 11 | ✓ complete |
| repo_snapshots | 391 | ✓ complete |
| aptos_snapshots | 28 | ✓ complete (all 0 APT) |
| multisig_probes | 5 | ✓ complete (all healthy) |
| mnx_snapshots | 0 | ✗ blocked (password-protected) |

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
