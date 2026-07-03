# World Increment Sweep + Hamming Snapshot

**Date:** 2026-07-03  
**Run type:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 (top 10 indexed) |
| kubeflow | org | 48 (top 10 indexed) |
| TeglonLabs | org | 5 (all indexed) |
| bmorphism | user | 105 (top 12 indexed) |
| zubyul | user | 49 (top 4 indexed) |
| migalkin | social graph | 19 (top 3 indexed) |
| wasita | social graph | 11 (top 2 indexed) |
| AustinCStone | social graph | 40 (top 2 indexed) |
| DJedamski | social graph | 6 (top 1 indexed) |
| kristinezheng | social graph | 5 (top 1 indexed) |
| M1shaaa | social graph | 8 (top 1 indexed) |

**Total world_increments:** 46 (GF3: 15xERGODIC #d3869b, 16xPLUS #b8bb26, 15xMINUS #cc241d)

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,760 | — |
| kubeflow | pipelines | 4,169 | Python |
| kubeflow | spark-operator | 3,132 | Python |
| kubeflow | trainer | 2,129 | Go |
| kubeflow | katib | 1,689 | Python |
| kubeflow | examples | 1,460 | Jsonnet |
| migalkin | NodePiece | 144 | Python |
| plurigrid | asi | 28 | HTML |
| bmorphism | anti-bullshit-mcp-server | 23 | JavaScript |
| AustinCStone | TextGAN | 92 | Python |

### Noteworthy Activity (as of 2026-07-03)

- **plurigrid/shrimp** — new repo created 2026-07-03: "Jank worked example: shrimp"
- **plurigrid/gorj** — 945 open issues; Clojure, this very repo
- **kubeflow/hub** — Model Registry, pushed 2026-07-03
- **kubeflow/mcp-apache-spark-history-server** — 180 stars, MCP for Spark
- **bmorphism/Gay.jl** — 187 open issues, active GF(3) color work
- **zubyul/voice-observatory** — companion to bmorphism/say-mcp-server, pushed 2026-04-24

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-03)

All 28 addresses probed via fullnode.mainnet.aptoslabs.com. All returned 0.00 APT.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...2d5d | 0.00 |
| A | 0x8699...9d7a | 0.00 |
| B | 0x3f89...b13 | 0.00 |
| C | 0x38b9...535e | 0.00 |
| D | 0xf776...fdd1 | 0.00 |
| E | 0xdc1d...8d36 | 0.00 |
| F | 0x18a1...f71 | 0.00 |
| G | 0x69a3...f32 | 0.00 |
| H | 0xce67...00f | 0.00 |
| I | 0x070f...fc9 | 0.00 |
| J | 0x4d96...f54 | 0.00 |
| K | 0xa732...dc4 | 0.00 |
| L | 0x7c2e...ba9 | 0.00 |
| M | 0x6fed...2e9 | 0.00 |
| N | 0xe7dd...b2c | 0.00 |
| O | 0x7325...89d | 0.00 |
| P | 0x6218...948 | 0.00 |
| Q | 0xac40...89a | 0.00 |
| R | 0x7ce6...e10 | 0.00 |
| S | 0xb875...386 | 0.00 |
| T | 0x3578...588 | 0.00 |
| U | 0x7586...956 | 0.00 |
| V | 0xb59d...c3 | 0.00 |
| W | 0x5f32...b0 | 0.00 |
| X | 0xa95c...47d | 0.00 |
| Y | 0xd8e3...c4 | 0.00 |
| Z | 0x7af0...97c | 0.00 |

**Total APT across 28 wallets: 0.00**

### Multisig Contract Probes

All 5 multisig contracts probed via 0x1::multisig_account::num_signatures_required.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

**5/5 multisig contracts responding, all 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

testnet.mnx.fi is behind Vercel deployment protection (authentication required).
API endpoints /api/markets and /api/v1/markets both return 401.
MNX market data unavailable — mnx_snapshots table empty.

---

## DuckDB Schema (world-increments.duckdb)

```
world_increments  — 46 rows  (GF3 color chain applied)
repo_snapshots    — 46 rows  (org/user, name, lang, stars, forks, issues)
aptos_snapshots   — 28 rows  (world A-Z + alice + bob, all 0 APT)
multisig_probes   —  5 rows  (all healthy, 2-of-2)
mnx_snapshots     —  0 rows  (unavailable, Vercel auth)
```

## GF(3) Color Chain Summary

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 15 |
| 1 | PLUS | #b8bb26 | 16 |
| -1 | MINUS | #cc241d | 15 |
