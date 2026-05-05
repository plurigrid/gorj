# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-05

## Sweep Metadata
- **Date:** 2026-05-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Historical range:** 2026-04-10 → 2026-05-05

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 231 |
| New Increments (today) | 208 |
| Total Repo Snapshots (cumulative) | 1,092 |
| New Repo Snapshots (today) | 148 |
| Event Rows (today) | 60 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — Today's 208 New Increments

| GF3 Trit | Color | Name | Count (today) |
|----------|-------|------|--------------|
| 0 | `#d3869b` | **ERGODIC** | 69 |
| +1 | `#b8bb26` | **PLUS** | 70 |
| -1 | `#cc241d` | **MINUS** | 69 |

GF(3) rule: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

---

## JOB 1: GitHub Social Graph Sweep

### Today's Repo Captures

| Source | Type | Repos Today | Notes |
|--------|------|------------|-------|
| TeglonLabs | org | 53 | Full capture |
| wasita | user | 31 | Full capture |
| migalkin | user | 30 | Full capture |
| kristinezheng | user | 18 | Full capture |
| M1shaaa | user | 16 | Full capture |
| plurigrid | org | 0 new | Rate-limited; 100 repos from prior sweep |
| kubeflow | org | 0 new | Rate-limited; 47 repos from prior sweep |
| bmorphism | user | 0 repos | Rate-limited; 30 public events captured |
| zubyul | user | 0 repos | Rate-limited; 30 public events captured |
| DJedamski | user | 0 | Rate-limited |
| AustinCStone | user | 0 | Rate-limited |

### Top Repos by Stars (All-Time Snapshot)
| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,572 | — |
| kubeflow | pipelines | 4,119 | Python |
| kubeflow | spark-operator | 3,114 | Python |
| kubeflow | trainer | 2,082 | Go |
| kubeflow | katib | 1,678 | Python |
| migalkin | NodePiece | 143 | Python |
| migalkin | StarE | 89 | Python |
| migalkin | kgcourse2021 | 25 | HTML |

### Today's New Repos — Highlights

**TeglonLabs (53 repos)**
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |
| coin-flip-mcp | JavaScript | 0 |

**migalkin (30 repos)**
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |

**wasita (31 repos)**
| Repo | Language | Stars |
|------|----------|-------|
| magic-garden | Python | 2 |
| wasita.github.io | Svelte | 1 |
| dartbrains | Jupyter Notebook | 1 |

### GitHub Events (bmorphism + zubyul, 60 total)
| Event Type | Count |
|-----------|-------|
| CreateEvent | 16 |
| PullRequestEvent | 15 |
| DeleteEvent | 14 |
| PushEvent | 11 |
| WatchEvent | 2 |
| ForkEvent | 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 addresses returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 5,141,354,731.  
Accounts exist on-chain but have never received APT (coin store uninitialized).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac… | 0.00 |
| bob | 0x0a3c00… | 0.00 |
| A | 0x8699ed… | 0.00 |
| B | 0x3f892e… | 0.00 |
| C | 0x38b99e… | 0.00 |
| D | 0xf77656… | 0.00 |
| E | 0xdc1d9d… | 0.00 |
| F | 0x18a14b… | 0.00 |
| G | 0x69a394… | 0.00 |
| H | 0xce67c3… | 0.00 |
| I | 0x070fe5… | 0.00 |
| J | 0x4d964d… | 0.00 |
| K | 0xa73204… | 0.00 |
| L | 0x7c2eae… | 0.00 |
| M–Z | (14 addresses) | 0.00 each |

**Total swarm balance: 0.00000000 APT**

### Multisig Contract Probes (5 pairs — all HEALTHY)

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4… | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a… | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1… | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a… | 2 | ✓ HEALTHY |
| V-W | 0x40fad7… | 2 | ✓ HEALTHY |

All probed via `0x1::multisig_account::num_signatures_required` — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE (SPA)** — `testnet.mnx.fi` is a Next.js single-page application.  
No JSON API endpoints found at `/api/markets` or `/api/v1/markets`.  
Market data requires browser execution; noting as unavailable.

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
- **kubeflow/kubeflow**: 15,572 stars — flagship ML platform for Kubernetes (updated from prior sweep)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings (new this sweep)
- **TeglonLabs/coin-flip-mcp**: MCP tooling from zubyul's social graph
- **All 5 multisigs**: 2-of-N threshold confirmed healthy at ledger v5,141,354,731
- **Hamming swarm**: 28 wallets, all uninitialized — zero APT balance across entire swarm
