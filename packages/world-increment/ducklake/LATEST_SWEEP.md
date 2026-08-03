# World Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried This Run
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 14 |
| kubeflow | org | 12 |
| TeglonLabs | org | 5 |
| bmorphism | user | 9 |
| zubyul | user | 7 |
| migalkin | social graph | 4 |
| wasita | social graph | 2 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 2 |
| **TOTAL new** | | **74** |

### Notable Repos by Stars
| Repo | Stars | Lang | Last Push |
|------|-------|------|-----------|
| kubeflow/kubeflow | 15,804 | — | 2026-07-10 |
| kubeflow/pipelines | 4,173 | Python | 2026-08-03 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-31 |
| kubeflow/trainer | 2,165 | Go | 2026-07-31 |
| kubeflow/katib | 1,694 | Python | 2026-08-02 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 58 | HTML | 2026-07-10 |
| kubeflow/docs-agent | 40 | Python | 2026-08-01 |
| kubeflow/mcp-server | 31 | Python | 2026-08-03 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | 23 | JS | 2026-01-16 |

### Most Active Today (pushed 2026-08-03)
- `plurigrid/gorj` — 1596 open issues (this repo)
- `kubeflow/pipelines` — 510 open issues, 4173 stars
- `kubeflow/mcp-server` — new MCP tooling for Kubeflow
- `bmorphism/Gay.jl` — 188 open issues, wide-gamut color SPI

### GF(3) Color Chain (this run, 54 new increments)
- Increment IDs mod 3: ERGODIC (#d3869b) | PLUS (#b8bb26) | MINUS (#cc241d)
- Chain cycles through sources: plurigrid → kubeflow → TeglonLabs → bmorphism → zubyul → social graph

### DuckDB After This Run
| Table | Cumulative Rows |
|-------|----------------|
| world_increments | 78 |
| repo_snapshots | 999 |
| aptos_snapshots | 28+ |
| multisig_probes | 5+ |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**Ledger version probed: ~6,589,291,789**  
**Endpoint:** `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (first 10 chars) | Balance (APT) |
|-------|--------------------------|---------------|
| alice | 0xc793acd... | 0.0 |
| bob | 0x0a3c00c... | 0.0 |
| A | 0x8699edc... | 0.0 |
| B | 0x3f892eb... | 0.0 |
| C | 0x38b99e6... | 0.0 |
| D | 0xf776562... | 0.0 |
| E | 0xdc1d9d5... | 0.0 |
| F | 0x18a14b5... | 0.0 |
| G | 0x69a394c... | 0.0 |
| H | 0xce67c32... | 0.0 |
| I | 0x070fe5d... | 0.0 |
| J | 0x4d964db... | 0.0 |
| K | 0xa732040... | 0.0 |
| L | 0x7c2eaea... | 0.0 |
| M | 0x6fed37a... | 0.0 |
| N | 0xe7dde6d... | 0.0 |
| O | 0x73252b6... | 0.0 |
| P | 0x6218792... | 0.0 |
| Q | 0xac40fa5... | 0.0 |
| R | 0x7ce605c... | 0.0 |
| S | 0xb875301... | 0.0 |
| T | 0x35781dc... | 0.0 |
| U | 0x75860da... | 0.0 |
| V | 0xb59dd81... | 0.0 |
| W | 0x5f32aef... | 0.0 |
| X | 0xa95cbbd... | 0.0 |
| Y | 0xd8e3284... | 0.0 |
| Z | 0x7af0ef6... | 0.0 |

**Status:** All 28 addresses return `resource_not_found` for the APT CoinStore module. Addresses exist on-chain but have no APT deposits / coin module not initialized.

### Multisig Contract Probes — ALL HEALTHY
| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f42... | 2 | ✓ healthy |
| A-G | 0xf56c4a1... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe18... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae... | 2 | ✓ healthy |
| V-W | 0x40fad7b... | 2 | ✓ healthy |

All 5 multisig contracts on Aptos mainnet respond with `sigs_required=2`. No degraded or missing contracts.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Site is a Next.js SPA. All paths return HTML, no JSON market API accessible. No `mnx_snapshots` rows inserted this run.

---

## Schema Reference
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
