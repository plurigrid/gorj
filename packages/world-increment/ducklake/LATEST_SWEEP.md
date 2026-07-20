# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-20  
**Sweep ID:** world-increment-20260720

---

## GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org/user | 250 | 138 |
| bmorphism | org/user | 250 | 377 |
| kubeflow | org/user | 143 | 102117 |
| TeglonLabs | org/user | 111 | 14 |
| zubyul | org/user | 97 | 40 |
| AustinCStone | org/user | 86 | 216 |
| wasita | org/user | 60 | 6 |
| migalkin | org/user | 60 | 554 |
| kristinezheng | org/user | 36 | 0 |
| M1shaaa | org/user | 32 | 0 |
| DJedamski | org/user | 22 | 14 |

**Total repo snapshots in ducklake:** 1147

### Top Plurigrid Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| plurigrid/asi | 31 | HTML | 2026-07-10 |
| plurigrid/asi | 16 | HTML | 2026-04-10T02:37:44Z |
| plurigrid/asi | 16 | HTML | 2026-04-13T07:04:34Z |
| plurigrid/ontology | 8 | JavaScript | 2025-05-27 |
| plurigrid/ontology | 7 | JavaScript | 2025-05-27T18:18:34Z |

### GF3 Color Chain
- `id % 3 == 0` → trit=0, ERGODIC `#d3869b`
- `id % 3 == 1` → trit=1, PLUS `#b8bb26`  
- `id % 3 == 2` → trit=-1, MINUS `#cc241d`

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z + alice/bob)

**28 addresses probed.** 28 returned `resource_not_found` (CoinStore not initialized — wallets hold 0 APT or are unfunded on mainnet).

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| V-W | 0x40fad7b4…eb6d | 2 | ✓ |
| S-T | 0x3b1c3ae9…7883 | 2 | ✓ |
| Y-Z | 0xd3ffe181…b883 | 2 | ✓ |
| A-G | 0xf56c4a1c…0096 | 2 | ✓ |
| A-B | 0x0da4f428…987003 | 2 | ✓ |

**All 5 multisigs: 2-of-2, healthy.**

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — endpoint returns HTTP 401 (Vercel auth wall). No market data captured.

---

## Notes

- DuckDB at `packages/world-increment/ducklake/world-increments.duckdb`
- Tables: `world_increments`, `repo_snapshots`, `aptos_snapshots`, `multisig_probes`, `mnx_snapshots`
- Aptos mainnet fullnode: `https://fullnode.mainnet.aptoslabs.com/v1` (ledger ~6.37B)
- All blockchain data is public on-chain
