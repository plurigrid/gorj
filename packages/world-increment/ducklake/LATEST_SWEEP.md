# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-04-18
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Surveyed

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 47 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 10 |
| kristinezheng | user (social) | 6 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |
| **Total** | | **387** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 136 |
| 1 | `#b8bb26` | PLUS | 137 |
| -1 | `#cc241d` | MINUS | 137 |

**Total world_increments:** 410

### Notable Repos by Recent Activity

- **M1shaaa/M1shaaa** — GitHub profile config, pushed 2026-04-18
- **wasita/wasita.github.io** — Svelte personal site, pushed 2026-04-13
- **wasita/ch3-lib** — Typst library, pushed 2026-04-12
- **kristinezheng/kristinezheng.github.io** — HTML portfolio, pushed 2026-04-09
- **TeglonLabs/mathpix-gem** — Ruby math OCR gem (★2), pushed 2026-01-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26 addrs) | ... | 0.0 each |

**Note:** All 28 addresses return 0.0 APT — CoinStore resources absent on mainnet, accounts unregistered.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All 5 multisig contracts live — all require **2-of-N** signatures.

### MNX Markets (testnet.mnx.fi)

- HTTP Status: 200 (SPA loads)
- /api/markets: UNAVAILABLE
- /api/tickers: UNAVAILABLE
- No market data extractable — JavaScript SPA with no public REST endpoints.

---

## DuckDB Schema

```
world_increments  410 rows  GF3-tagged repo snapshot events
repo_snapshots    387 unique repos across 11 sources
aptos_snapshots    28 rows  alice/bob + A-Z wallet balances
multisig_probes     5 rows  all healthy, sigs_required=2
mnx_snapshots       0 rows  API unavailable
```

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent — 2026-04-18.*
