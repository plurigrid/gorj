# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-09T (automated sweep)  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 102 |
| kubeflow | org | 51 |
| TeglonLabs | org | 7 |
| bmorphism | user | 103 |
| zubyul | user | 51 |
| migalkin | user (social) | 6 |
| wasita | user (social) | 5 |
| kristinezheng | user (social) | 4 |
| AustinCStone | user (social) | 4 |
| M1shaaa | user (social) | 4 |
| DJedamski | user (social) | 3 |
| **Total** | | **340** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 112 |
| +1 | `#b8bb26` | PLUS | 114 |
| -1 | `#cc241d` | MINUS | 114 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,808 | — |
| kubeflow/pipelines | 4,182 | Python |
| kubeflow/spark-operator | 3,146 | Python |
| kubeflow/trainer | 2,177 | Go |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| TeglonLabs/mathpix-gem | 2 | Ruby |

### Notable Recent Activity

- **wasita/xoxowasita-analysis** — pushed 2026-08-06 (active 3 days ago)
- **wasita/wm-cv** — pushed 2026-08-07 (active 2 days ago)
- **migalkin/kgcourse2021** — pushed 2026-07-10 (Knowledge Graphs course)
- **TeglonLabs/jank-crane** — pushed 2026-06-08 (GF3 convergence maps, crane-jank IR hub)
- **AustinCStone/byteruckus** — created 2026-07-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) queried against Aptos mainnet.  
**Result: All balances = 0.0 APT** — CoinStore resources returned zero values for all addresses. Accounts exist on-chain but hold no liquid APT at this snapshot.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793acd… | 0.0 |
| bob | 0x0a3c00c… | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts healthy — all require **2 of N signatures**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f42… | 2 | ✓ |
| A-G | 0xf56c4a1… | 2 | ✓ |
| Y-Z | 0xd3ffe18… | 2 | ✓ |
| S-T | 0x3b1c3ae… | 2 | ✓ |
| V-W | 0x40fad7b… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `https://testnet.mnx.fi` serves a Next.js SPA (dark-mode UI detected). No REST API endpoints (`/api/markets`, `/api/v1/markets`) returned structured data; both paths return the same rendered HTML shell. Market data is loaded client-side and not accessible via curl. No ticker data captured.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| `world_increments` | 340 |
| `repo_snapshots` | 1,261 (648 distinct repos; duplication from paginated JSON) |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 1 (unavailable marker) |

---

## Summary

- **GitHub sweep**: 340 world-increment entries across 11 sources. Plurigrid and bmorphism most active with 100+ repos each. TeglonLabs jank-crane project (GF3 convergence maps) recently active. Social graph contacts wasita and kristinezheng show academic/research profiles.
- **Hamming swarm**: 28 Aptos addresses all at 0.0 APT. 5/5 multisig contracts responsive and require 2-of-N sigs (healthy).
- **MNX**: Testnet frontend live but no API endpoints accessible programmatically.
