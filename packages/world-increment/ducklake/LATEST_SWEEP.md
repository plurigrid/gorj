# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-16T00:10:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.2 Variegata)  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 20 |
| kubeflow | org | 15 |
| TeglonLabs | org | 10 |
| bmorphism | user | 8 |
| zubyul | user | 7 |
| migalkin | user (zubyul social) | 5 |
| DJedamski | user (zubyul social) | 3 |
| wasita | user (zubyul social) | 5 |
| kristinezheng | user (zubyul social) | 3 |
| M1shaaa | user (zubyul social) | 4 |
| AustinCStone | user (zubyul social) | 4 |
| **Total** | | **84 repos, 16 events → 100 world_increments** |

### GF(3) Color Chain — World Increments
- **ERGODIC #d3869b** (trit=0): ids 3,6,9,... — 33 entries
- **PLUS #b8bb26** (trit=1): ids 1,4,7,... — 34 entries
- **MINUS #cc241d** (trit=-1): ids 2,5,8,... — 33 entries

### Notable Active Repos (pushed last 48h)
| Repo | Lang | Stars | Last Push |
|------|------|-------|-----------|
| kubeflow/pipelines | Python | 4120 | 2026-04-15T23:45 |
| plurigrid/gorj | Clojure | 0 | 2026-04-15T23:11 |
| plurigrid/reafference | HTML | 0 | 2026-04-15T12:43 |
| plurigrid/nash-portal | Rust | 1 | 2026-04-15T05:39 |
| kubeflow/mcp-apache-spark-history-server | Python | 150 | 2026-04-15T21:18 |
| kubeflow/trainer | Go | 2085 | 2026-04-15T15:27 |

### Top Stars by Source
| Repo | Lang | Stars |
|------|------|-------|
| kubeflow/pipelines | Python | 4120 |
| kubeflow/spark-operator | Python | 3116 |
| kubeflow/trainer | Go | 2085 |
| kubeflow/katib | Python | 1678 |
| kubeflow/manifests | YAML | 1010 |
| kubeflow/mpi-operator | Go | 524 |
| migalkin/StarE | Python | 88 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 |
| plurigrid/asi | HTML | 17 |

### Recent Events (bmorphism + zubyul)
| Time | Event | Repo | Actor |
|------|-------|------|-------|
| 2026-04-15T23:12 | PullRequestEvent | plurigrid/gorj | zubyul |
| 2026-04-15T22:19 | PullRequestEvent | plurigrid/gorj | zubyul |
| 2026-04-15T19:21 | PullRequestEvent | plurigrid/gorj | zubyul |
| 2026-04-15T12:43 | PushEvent | plurigrid/reafference | bmorphism |
| 2026-04-15T08:37 | CommitCommentEvent | plurigrid/nash-portal | bmorphism |
| 2026-04-14T00:07 | PullRequestEvent | plurigrid/nash-portal | bmorphism |
| 2026-04-13T23:40 | IssuesEvent | plurigrid/nash-portal | bmorphism |
| 2026-04-12T05:18 | PushEvent | plurigrid/asi | bmorphism |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-04-16)
*Queried via `0x1::coin::balance` view function*

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob   | 0x0a3c...2d5d | **12.65700700** |
| A | 0x8699...9d7a | 0.05176700 |
| B | 0x3f89...b13 | 0.03625600 |
| C | 0x38b9...35e | 0.01018500 |
| D | 0xf776...dd1 | 0.01162900 |
| E | 0xdc1d...d36 | 0.00937200 |
| F | 0x18a1...f71 | **1.96051600** |
| G | 0x69a3...f32 | 0.00068100 |
| H | 0xce67...00f | 0.00168100 |
| I | 0x070f...c9 | 0.00068100 |
| J | 0x4d96...f54 | **1.89509300** |
| K | 0xa732...dc4 | 0.16196100 |
| L | 0x7c2e...ba9 | **1.92726900** |
| M | 0x6fed...e9 | 0.11228500 |
| N | 0xe7dd...b2c | 0.10612100 |
| O | 0x7325...89d | 0.21013600 |
| P | 0x6218...948 | 0.14013600 |
| Q | 0xac40...a9 | 0.10324000 |
| R | 0x7ce6...10 | 0.09021700 |
| S | 0xb875...386 | 0.09178800 |
| T | 0x3578...588 | 0.07371300 |
| U | 0x7586...956 | 0.05577300 |
| V | 0xb59d...b3 | 0.04883299 |
| W | 0x5f32...b0 | 0.04070500 |
| X | 0xa95c...47d | 0.04257700 |
| Y | 0xd8e3...c4 | 0.04444900 |
| Z | 0x7af0...97c | 0.02426800 |
| **TOTAL** | 28 wallets | **20.34477251 APT** |

**Top holders:** bob (12.657), F (1.961), L (1.927), J (1.895)  
**Dust wallets (<0.01 APT):** G, H, I  
**Dominant:** bob holds 62.2% of total swarm APT

### Multisig Contract Probes (5x 2-of-2)
| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

All 5 multisigs healthy — all 2-of-2 signature threshold.

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable via REST**  
The MNX testnet is a Next.js SPA with WebSocket-only backend (`wss://api.testnet.mnx.fi`).  
No REST `/markets`, `/tickers`, or `/api/*` endpoints respond.  
Market data requires live WebSocket connection — not captured in this sweep.

---

## DuckDB Table Summary
| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 100 | GF(3)-colored repo+event increments |
| repo_snapshots | 84 | Full repo metadata |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Multisig health probes |
| mnx_snapshots | 1 | MNX market (unavailable marker) |

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
