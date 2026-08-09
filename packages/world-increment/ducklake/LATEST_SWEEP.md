# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-09T07:00 UTC  
**Branch:** world-increment/sweep  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Found | Top Repo |
|--------|------|-------------|----------|
| plurigrid | org | 103 | gorj (1737 open issues, pushed 2026-08-09) |
| kubeflow | org | 49 | kubeflow/kubeflow ⭐15808 |
| TeglonLabs | org | 5 | jank-crane (C++, GF3 convergence maps) |
| bmorphism | user | 106 | anti-bullshit-mcp-server ⭐23 |
| zubyul | user | 49 | gay-world (Goblin world builder) |
| migalkin | social | 19 | NodePiece ⭐144 (ICLR'22 KG embeddings) |
| wasita | social | 14 | magic-garden ⭐2 (active Aug 2026) |
| AustinCStone | social | 41 | TextGAN ⭐92 |
| DJedamski | social | 6 | Kaggle (inactive since 2018) |
| kristinezheng | social | 5 | kristinezheng.github.io (active Jul 2026) |
| M1shaaa | social | 8 | lab-bookshelf- (TypeScript) |

### Key Activity (pushed within 7 days of sweep)

- **plurigrid/gorj** — pushed 2026-08-09 (today!) — 1737 open issues  
- **plurigrid/place** — pushed 2026-08-09 — forester BCI preview  
- **kubeflow/spark-operator** ⭐3145 — pushed 2026-08-08  
- **kubeflow/docs-agent** ⭐40 — pushed 2026-08-08  
- **kubeflow/trainer** ⭐2176 — pushed 2026-08-08  
- **kubeflow/pipelines** ⭐4182 — pushed 2026-08-07  
- **wasita/wm-cv** — pushed 2026-08-07 (CV actively maintained)  
- **bmorphism/anti-bullshit-mcp-server** ⭐23 — pushed 2026-08-02  

### GF(3) Color Chain Distribution (62 new records this run)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 27 |
| 1 | `#b8bb26` | PLUS | 29 |
| 2 | `#cc241d` | MINUS | 29 |

**Cumulative world_increments:** 85 records  
**Cumulative repo_snapshots:** 1006 records  

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

All 28 Hamming swarm addresses probed on Aptos mainnet
(`/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`).

**Result: All wallets returned 0 APT** — no CoinStore resources found, wallets are either unfunded or have not been initialized on mainnet.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acde... | 0.0 |
| bob | 0x0a3c00c5... | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded **healthy** with `num_signatures_required = 2`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✅ healthy |
| V-W | 0x40fad7b4... | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi/api/markets` — **UNAVAILABLE** (SPA/Next.js, no REST endpoint exposed).  
The site is reachable and renders client-side; market data is loaded via browser JS, not accessible via curl.  
`mnx_snapshots` table empty this run.

---

## Database Summary

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 85 |
| repo_snapshots | 1006 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Notable Signals

1. **plurigrid/gorj has 1737 open issues** — unusually high, likely automated or tracking issues
2. **All 5 Aptos multisigs healthy** — 2-of-2 threshold across all pairs (A-B, A-G, Y-Z, S-T, V-W)
3. **kubeflow MCP ecosystem expanding** — `mcp-apache-spark-history-server` (⭐188) and `mcp-server` (⭐31) both active
4. **bmorphism/Gay.jl** (⭐2, 188 open issues) — active GF(3) color work, branched as `gay`
5. **wasita active Aug 2026** — academic work (xoxowasita-analysis, joint-planning-lit) pushed this week
