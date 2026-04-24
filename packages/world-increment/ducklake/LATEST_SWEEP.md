# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-24  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Unique Repos | Max Stars | Total Forks |
|--------|------|-------------|-----------|-------------|
| plurigrid | org | 167 | 17 | 79 |
| bmorphism | user | 165 | 60 | 99 |
| TeglonLabs | org | 53 | 2 | 8 |
| kubeflow | org | 47 | 15,599 | 40,079 |
| zubyul | user | 45 | 2 | 4 |
| AustinCStone | social-graph | 43 | 92 | 110 |
| wasita | social-graph | 31 | 2 | 3 |
| migalkin | social-graph | 30 | 143 | 146 |
| kristinezheng | social-graph | 18 | 0 | 0 |
| M1shaaa | social-graph | 16 | 0 | 0 |
| DJedamski | social-graph | 11 | 2 | 5 |

**Total:** 626 unique repos across 11 nodes

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,599 | — | 2026-01-05 |
| kubeflow/pipelines | 4,125 | Python | 2026-04-23 |
| kubeflow/spark-operator | 3,118 | Python | 2026-04-21 |
| kubeflow/trainer | 2,090 | Go | 2026-04-23 |
| kubeflow/katib | 1,679 | Python | 2026-04-14 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,012 | YAML | 2026-04-11 |
| kubeflow/arena | 810 | Go | 2026-04-16 |
| kubeflow/kale | 685 | Python | 2026-04-22 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |
| plurigrid/asi | 17 | HTML | 2026-04-24 |

### GF(3) Color Chain (increment assignments)

| id%3 | Trit | Color | Name | Sources |
|------|------|-------|------|---------|
| 0 | 0 | `#d3869b` | ERGODIC | plurigrid, kubeflow, AustinCStone, M1shaaa |
| 1 | +1 | `#b8bb26` | PLUS | bmorphism, TeglonLabs, wasita, DJedamski |
| 2 | -1 | `#cc241d` | MINUS | zubyul, migalkin, kristinezheng |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

### Most Active (recently pushed)

- **plurigrid/asi** — HTML, 17★, pushed 2026-04-24
- **kubeflow/pipelines** — Python, 4125★, pushed 2026-04-23
- **kubeflow/trainer** — Go, 2090★, pushed 2026-04-23
- **plurigrid/gorj** — Clojure, 263 issues, pushed 2026-04-23
- **wasita/magic-garden** — Python, pushed 2026-04-22
- **kubeflow/kale** — Python, 685★, pushed 2026-04-22
- **migalkin/StarE** — Python, 89★, pushed 2026-04-16

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (2026-04-24)

> Method: `0x1::coin::balance` view function (not CoinStore resource — addresses use fungible-asset standard)  
> Ledger version ~4,984,957,709

| World | Address | APT Balance |
|-------|---------|-------------|
| bob | `0x0a3c...512d` | **12.65700700** |
| F | `0x18a1...3cf71` | 1.96051600 |
| L | `0x7c2e...eba9` | 1.92726900 |
| J | `0x4d96...7f54` | 1.89509300 |
| alice | `0xc793...4cc7b` | 0.43643352 |
| O | `0x7325...5a89d` | 0.21013600 |
| K | `0xa732...5dc4` | 0.16196100 |
| P | `0x6218...c948` | 0.14013600 |
| M | `0x6fed...7f2e9` | 0.11228500 |
| N | `0xe7dd...1b2c` | 0.10612100 |
| Q | `0xac40...89a9` | 0.10324000 |
| S | `0xb875...0386` | 0.09178800 |
| R | `0x7ce6...6e10` | 0.09021700 |
| T | `0x3578...4588` | 0.07371300 |
| U | `0x7586...9956` | 0.05577300 |
| A | `0x8699...9d7a` | 0.05176700 |
| V | `0xb59d...af2c3` | 0.04883299 |
| Y | `0xd8e3...444c4` | 0.04444900 |
| X | `0xa95c...047d` | 0.04257700 |
| W | `0x5f32...c7b0` | 0.04070500 |
| B | `0x3f89...cb13` | 0.03625600 |
| Z | `0x7af0...197c` | 0.02426800 |
| D | `0xf776...cfdd1` | 0.01162900 |
| C | `0x38b9...535e` | 0.01018500 |
| E | `0xdc1d...8d36` | 0.00937200 |
| H | `0xce67...300f` | 0.00168100 |
| I | `0x070f...1fc9` | 0.00068100 |
| G | `0x69a3...7f32` | 0.00068100 |

**Swarm Total: ~20.33 APT**  
**Top holder:** bob (12.657 APT, ~62% of swarm)  
**Smallest:** G/I (0.000681 APT each)

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** (all require 2-of-2 signatures):

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...7003` | 2 | ✓ HEALTHY |
| A-G | `0xf56c...0096` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ff...b883` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c...7883` | 2 | ✓ HEALTHY |
| V-W | `0x40fa...eb6d` | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no public REST API accessible.**  
The site is a Next.js app (`/_next/static/...`); `/api/markets` and `/api/v1/markets` return the HTML shell. Market data unavailable via direct API probe. `mnx_snapshots` table is empty (0 rows).

---

## DuckDB Table Counts

```
world_increments  — 34 rows  (11 sources, GF3 chain)
repo_snapshots    — 1,248 rows (304 unique repos, multi-pass ingestion)
aptos_snapshots   — 28 rows  (alice + bob + A–Z)
multisig_probes   — 5 rows   (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     — 0 rows   (SPA, unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent*  
*GitHub: MCP search_repositories | Aptos: fullnode.mainnet.aptoslabs.com v1/view*
