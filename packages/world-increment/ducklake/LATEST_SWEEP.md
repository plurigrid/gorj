# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-25

## Sweep Metadata
- **Date:** 2026-06-25T07:30 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 56 |
| bmorphism | user | 100 |
| zubyul | user | 27 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| wasita | user | 32 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| **TOTAL** | | **481 repos** |

### Summary Counts
| Metric | Value |
|--------|-------|
| World Increments (this run) | 563 |
| Repo Snapshots (cumulative DB) | 1,425 |
| Public Events Captured | 59 |
| Distinct Repos in DB | 516 |

### GF(3) Color Chain — This Run
| GF3 Trit | Color Name | Hex | Count |
|----------|-----------|-----|-------|
| 0 | ERGODIC | #d3869b | 187 |
| +1 | PLUS | #b8bb26 | 188 |
| -1 | MINUS | #cc241d | 188 |

GF(3) assignment: `id mod 3 == 0 → ERGODIC, 1 → PLUS, 2 → MINUS`

### Most Recently Pushed Repos
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/gorj | Clojure | 0 | 2026-06-25T07:17Z |
| kubeflow/docs-agent | Python | 39 | 2026-06-25T05:33Z |
| kubeflow/sdk | Python | 121 | 2026-06-25T03:04Z |
| M1shaaa/M1shaaa | – | 0 | 2026-06-25T02:52Z |
| bmorphism/Gay.jl | Julia | 2 | 2026-06-25T00:40Z |

### Top Repos by Stars
| Repo | Org/User | Language | Stars |
|------|----------|----------|-------|
| kubeflow/kubeflow | kubeflow | – | 15,742 |
| kubeflow/pipelines | kubeflow | Python | 4,157 |
| kubeflow/spark-operator | kubeflow | Python | 3,128 |
| kubeflow/trainer | kubeflow | Go | 2,121 |
| kubeflow/katib | kubeflow | Python | 1,685 |

### Social Graph Activity
**bmorphism (29 recent events):**
- Starred: Qiskit/qiskit, PrimeIntellect-ai/prime-rl, lanl/color, bhauman/clojure-mcp-light
- Active pushes to: bmorphism/satreadout, bmorphism/bci-preview

**zubyul (30 recent events):**
- All events: `CreateEvent` on `plurigrid/gorj` — branch/tag creation activity on this repo today

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses — alice, bob, A–Z)

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...2d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**All 28 wallets: 0 APT on mainnet.** Wallets are on-chain but unfunded.

### Multisig Contract Probes
| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE — Vercel Authentication Required**  
The testnet SPA requires Vercel login. All API probes (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`, `/v1/markets`) returned empty/auth-gated responses. No market data captured this sweep.

---

## Notable Signals
- **plurigrid/gorj** most recently pushed repo (active today 07:17Z) — this sweep targets itself
- bmorphism watching **bhauman/clojure-mcp-light** — directly adjacent to forj/MCP toolchain
- bmorphism active on **satreadout** — SAT/BCI intersection work  
- All Hamming swarm multisigs: **2-of-N, healthy** — no degraded signers detected
- Zero APT across all 28 swarm wallets — unfunded on mainnet at snapshot time
- MNX testnet: auth-gated, inaccessible without Vercel session token

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
