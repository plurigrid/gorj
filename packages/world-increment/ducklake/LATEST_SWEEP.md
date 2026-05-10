# World-Increment Sweep + Hamming Snapshot — 2026-05-10

## Sweep Metadata
- **Date:** 2026-05-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GitHub API:** MCP search (unauthenticated GH rate-limited)
- **Aptos RPC:** fullnode.mainnet.aptoslabs.com

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| Total Repo Snapshots (cumulative) | 1060 |
| New Increments This Run | 11 |
| New Repo Snapshots This Run | 116 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — This Run (11 Increments)

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | bmorphism | user | -1 | `#cc241d` | **MINUS** |
| 3  | zubyul | user | 0 | `#d3869b` | **ERGODIC** |
| 4  | kubeflow | org | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs | org | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | AustinCStone | user | +1 | `#b8bb26` | **PLUS** |
| 8  | DJedamski | user | -1 | `#cc241d` | **MINUS** |
| 9  | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita | user | +1 | `#b8bb26` | **PLUS** |
| 11 | kristinezheng | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Top Repos by Source (2026-05-10 snapshot)

**plurigrid** (100 repos total, org)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 21 | 2026-05-07 |
| nash-portal | Rust | 2 | 2026-05-05 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| ontology | JavaScript | 8 | 2026-05-09 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| gorj | Clojure | 0 | 2026-05-08 |

**bmorphism** (101 repos total, user)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 18 | 2026-03-26 |
| manifold-mcp-server | JavaScript | 14 | 2026-04-15 |
| Gay.jl | Julia | 1 | 2026-04-17 |

**kubeflow** (48 repos total, org)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow | — | 15,628 |
| pipelines | Python | 4,137 |
| spark-operator | Python | 3,125 |
| trainer | Go | 2,097 |
| katib | Python | 1,683 |
| mcp-apache-spark-history-server | Python | 167 |

**migalkin** (19 repos, user) — Knowledge Graphs / GNNs
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece (ICLR'22) | Python | 144 |
| StarE (EMNLP'20) | Python | 89 |
| NBFNet_mlx | Python | 10 |

**AustinCStone** (40 repos, user)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

**Social Graph** (zubyul/wasita/kristinezheng/M1shaaa/DJedamski)
- `zubyul/gay-world` — goblin world builder, 1 ⭐
- `wasita/magic-garden` — Discord bot, 2 ⭐
- `wasita/wasita.github.io` — Svelte site, 1 ⭐
- `kristinezheng/lookit-jenga` — MIT cognitive science study

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-05-10)

All 28 addresses probed: `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`  
All returned `resource_not_found` — CoinStore not initialized (0 APT each).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...7b | 0.0 |
| bob | 0x0a3c...5d | 0.0 |
| A–Z (26) | various | 0.0 each |

**Total swarm APT:** 0.00000000

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...03 | 2 | ✓ |
| A-G | 0xf56c...96 | 2 | ✓ |
| Y-Z | 0xd3ff...83 | 2 | ✓ |
| S-T | 0x3b1c...83 | 2 | ✓ |
| V-W | 0x40fa...6d | 2 | ✓ |

**5/5 contracts healthy. All 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

Next.js SPA — no REST API accessible. `mnx_snapshots` empty this run.

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
