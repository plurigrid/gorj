# World Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-06-06  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.3 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| AustinCStone | social graph | 40 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| **TOTAL** | | **390 repos snapshotted** |

### GF(3) Color Chain Distribution (413 world increments)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 137 |
| +1 | `#b8bb26` | PLUS | 138 |
| -1 | `#cc241d` | MINUS | 138 |

Chain pattern: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...` (∞)

### Top Repos by Stars
| Repo | Language | Stars | Forks | Last Pushed |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15,706 | 2,671 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,153 | 2,006 | 2026-06-06 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 | 2026-06-04 |
| kubeflow/trainer | Go | 2,112 | 964 | 2026-06-05 |
| kubeflow/katib | Python | 1,685 | 526 | 2026-06-05 |
| kubeflow/examples | Jsonnet | 1,462 | 756 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,020 | 1,065 | 2026-06-05 |
| migalkin/NodePiece | Python | 143 | — | — |
| AustinCStone/TextGAN | Python | 92 | — | — |
| migalkin/StarE | Python | 88 | — | — |

### Notable bmorphism Repos
- `bmorphism/ocaml-mcp-sdk` — OCaml SDK for MCP (60★)
- `bmorphism/anti-bullshit-mcp-server` — JavaScript MCP server (23★)
- Diverse: OCaml, Zig, Python, Clojure, systems research focus

### Notable plurigrid Repos
- `plurigrid/gorj` — forj + Clojure REPL + GF(3) topology (this repo)
- `plurigrid/asi` — topological chemputer (16★, HTML)
- `plurigrid/ontology` — knowledge graph work (7★, JavaScript)
- `plurigrid/vivarium` — Clojure simulation framework

### TeglonLabs (2026 active)
| Repo | Language | Stars | Notes |
|------|----------|-------|-------|
| mathpix-gem | Ruby | 2 | LaTeX/SMILES OCR gem |
| coin-flip-mcp | JavaScript | 0 | MCP random.org integration |
| topoi | Python | 0 | — |
| monad-mcp-server | — | 0 | Monad MCP |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (alice–Z, 28 wallets)
**All 28 wallets probed** via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 5,607,643,536.

**Result:** All returned `resource_not_found` — no coin stores initialized on mainnet.  
Recorded as `NULL` in `aptos_snapshots`.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793…c7b | NULL |
| bob | 0x0a3c…d5d | NULL |
| A | 0x8699…d7a | NULL |
| B | 0x3f89…b13 | NULL |
| C | 0x38b9…35e | NULL |
| D | 0xf776…dd1 | NULL |
| E | 0xdc1d…d36 | NULL |
| F | 0x18a1…f71 | NULL |
| G | 0x69a3…f32 | NULL |
| H | 0xce67…00f | NULL |
| I | 0x070f…fc9 | NULL |
| J | 0x4d96…f54 | NULL |
| K | 0xa732…dc4 | NULL |
| L | 0x7c2e…ba9 | NULL |
| M | 0x6fed…2e9 | NULL |
| N | 0xe7dd…b2c | NULL |
| O | 0x7325…89d | NULL |
| P | 0x6218…948 | NULL |
| Q | 0xac40…89a | NULL |
| R | 0x7ce6…e10 | NULL |
| S | 0xb875…386 | NULL |
| T | 0x3578…588 | NULL |
| U | 0x7586…956 | NULL |
| V | 0xb59d…2c3 | NULL |
| W | 0x5f32…7b0 | NULL |
| X | 0xa95c…47d | NULL |
| Y | 0xd8e3…4c4 | NULL |
| Z | 0x7af0…97c | NULL |

### Multisig Contract Probes (5 pairs)
All contracts healthy — unanimous 2-of-2 threshold:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428…987003 | 2 | ✓ |
| A-G | 0xf56c4a1c…c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181…b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9…7883 | 2 | ✓ |
| V-W | 0x40fad7b4…eb6d | 2 | ✓ |

**Swarm consensus posture:** All 5 multisig pairs require unanimous (2/2) agreement — no quorum degradation detected.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Both `https://testnet.mnx.fi` and `https://testnet.mnx.fi/api/markets` return **HTTP 401 Unauthorized**.  
No public market data accessible without credentials. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Table Counts
```
world_increments   413 rows  (GF3-colored event log, per-repo increments)
repo_snapshots    1334 rows  (645 unique repos, multi-snapshot time-series)
aptos_snapshots     28 rows  (alice–Z, all NULL balance — uninitialized accounts)
multisig_probes      5 rows  (all 2-of-2, healthy)
mnx_snapshots        0 rows  (API unavailable)
```

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

## GF(3) Rule
- `id mod 3 == 0` → trit=0, `#d3869b`, ERGODIC
- `id mod 3 == 1` → trit=+1, `#b8bb26`, PLUS
- `id mod 3 == 2` → trit=-1, `#cc241d`, MINUS
