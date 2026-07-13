# World-Increment Sweep + Hamming Snapshot — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 1,264 |
| Total Repo Snapshots | 1,264 |
| Sources Covered | 3 orgs + 8 users (incl. zubyul social graph) |
| Total Stars | 103,971 |

### GF(3) Color Chain Distribution

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 113 |
| PLUS | +1 | `#b8bb26` | 115 |
| MINUS | -1 | `#cc241d` | 115 |

GF(3) rule: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

---

### Repo Counts by Source

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| kubeflow | org | 143 | 102,075 |
| migalkin | user (zubyul-social) | 65 | 829 |
| bmorphism | user | 300 | 508 |
| AustinCStone | user (zubyul-social) | 89 | 319 |
| plurigrid | org | 300 | 162 |
| zubyul | user | 97 | 40 |
| DJedamski | user (zubyul-social) | 24 | 15 |
| TeglonLabs | org | 111 | 14 |
| wasita | user (zubyul-social) | 63 | 9 |
| kristinezheng | user (zubyul-social) | 38 | 0 |
| M1shaaa | user (zubyul-social) | 34 | 0 |
| **TOTAL** | | **1,264** | **103,971** |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,773 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,168 | 2026-07-13 |
| kubeflow/spark-operator | Python | 3,137 | 2026-07-12 |
| kubeflow/trainer | Go | 2,138 | 2026-07-10 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |

### Notable: TeglonLabs (recently active)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| jank-crane | C++ | 0 | crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow |
| mathpix-gem | Ruby | 2 | Transform mathematical images to LaTeX (11 open issues) |
| coin-flip-mcp | JavaScript | 0 | MCP server for flipping coins with random.org |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | Topoi research repo |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice/bob)

**Result:** All 28 addresses returned `resource_not_found` from Aptos mainnet CoinStore.  
These accounts have not initialized a CoinStore for APT — either new/empty accounts or not yet registered on mainnet.

| World | Address (prefix) | Balance |
|-------|-----------------|---------|
| alice | 0xc793acde... | resource_not_found |
| bob | 0x0a3c00c5... | resource_not_found |
| A | 0x8699edc0... | resource_not_found |
| B–Z (×26) | 0x3f89... – 0x7af0... | resource_not_found |

### Multisig Contract Probes

All 5 multisig contracts responded **healthy** — each requires **2-of-N signatures**.

| Pair | Address (short) | Sigs Required | Status |
|------|----------------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✓ HEALTHY |

### MNX Testnet Markets

`https://testnet.mnx.fi` — **Unavailable**: Vercel password-protected deployment (HTTP 401).  
All probed paths (`/`, `/api/markets`, `/api/v1/markets`, `/markets`) return identical 401.  
No market data extractable without credentials.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## Notable Highlights
- **kubeflow/pipelines**: 4,168 stars, pushed 2026-07-13 — active today
- **kubeflow/spark-operator**: 3,137 stars, pushed 2026-07-12
- **TeglonLabs/jank-crane**: NEW repo (2026-06-08) — C++ GF3 convergence maps / IR hub
- **migalkin/kgcourse2021**: active 2026-07-10, still receiving traction (24 stars)
- **wasita/wasita.github.io**: active 2026-07-06, Svelte personal site with 8 open issues
- **All 5 Hamming multisigs**: healthy, 2-of-N threshold — swarm consensus intact
- **All 28 APT wallets**: zero/uninitialized on mainnet (CoinStore not found)
