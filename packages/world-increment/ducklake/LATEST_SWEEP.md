# World-Increment Sweep — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **GF(3) Increment:** #13 · PLUS · #b8bb26 (trit=1)
- **Snapshot hash:** `6581cf166ebd61c5`
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 945 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 (all healthy) |
| MNX Markets | unavailable (SPA only) |

---

## JOB 1: GitHub Social Graph Sweep

**Status: Scope-restricted** — session token bound to `plurigrid/gorj` only.
Cross-org/user queries for `plurigrid`, `kubeflow`, `TeglonLabs`, `bmorphism`,
`zubyul`, and social graph users (`migalkin`, `DJedamski`, `wasita`,
`kristinezheng`, `M1shaaa`, `AustinCStone`) were blocked:

> "This GitHub API path is not available: sessions are bound to their configured
> repositories. Use repository-scoped endpoints (repos/{owner}/{repo}/...)"

**Accessible repo:** `plurigrid/gorj` — 20 recent commits retrieved via MCP.
Last push: 2026-05-08 (chore: ignore duckdb binary in repo root).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, ledger ~6535307127)

All 28 addresses returned `resource_not_found` for APT coin store —
no APT holdings across the entire swarm.

**Total APT: 0.0**

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address | Sigs Required |
|------|---------|---------------|
| A-B  | 0x0da4...003 | 2 |
| A-G  | 0xf56c...096 | 2 |
| Y-Z  | 0xd3ff...883 | 2 |
| S-T  | 0x3b1c...883 | 2 |
| V-W  | 0x40fa...b6d | 2 |

### MNX Markets — Unavailable

`testnet.mnx.fi` serves a Next.js SPA; no JSON API accessible at
`/api/markets` or `/api/v1/markets`.

---

## GF(3) Color Chain — Latest 4 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |
| **13** | **plurigrid/gorj** | **hamming_snapshot** | **+1** | **`#b8bb26`** | **PLUS** |

GF(3) chain (full): `PLUS → MINUS → ERGODIC` × 4 cycles + **PLUS** (id=13)

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-07-30)
- **Increment 13**: PLUS (#b8bb26) — opens 5th GF(3) cycle; first hamming swarm snapshot
- **Multisig swarm**: 5 contracts probed (A-B, A-G, Y-Z, S-T, V-W), all requiring 2-of-N sigs, all healthy
- **Aptos swarm**: 28 addresses (alice, bob, A–Z) — all APT coin stores unfunded at ledger ~6.5B
- **MNX**: testnet.mnx.fi SPA-only, no API data extractable
- **GitHub**: session scoped to plurigrid/gorj only; cross-org sweep deferred to next authorized session
- **gorj** last commit: 2026-05-08 chore: ignore duckdb binary in repo root
