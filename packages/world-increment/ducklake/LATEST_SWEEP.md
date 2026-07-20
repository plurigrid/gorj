# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 125 |
| Total Repo Snapshots | 125 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Trit Distribution

| Trit | Name | Color | Count |
|---|---|---|---|
| 0 | ERGODIC | `#d3869b` | 41 |
| +1 | PLUS | `#b8bb26` | 42 |
| -1 | MINUS | `#cc241d` | 42 |

### Top Repos by Source

**plurigrid** (33 snapshotted)
| Repo | Language | Stars | Latest Push |
|------|----------|-------|-------------|
| asi | HTML | 31 | 2026-07-17 |
| shrimp | — | 0 | 2026-07-03 |
| ontology | JavaScript | 8 | 2026-05-09 |
| nash-portal | Rust | 2 | 2026-05-19 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |

**kubeflow** (27 snapshotted)
| Repo | Language | Stars | Latest Push |
|------|----------|-------|-------------|
| kubeflow | — | 15,785 | 2026-07-20 |
| pipelines | Python | 4,169 | 2026-07-20 |
| spark-operator | Python | 3,140 | 2026-07-20 |
| trainer | Go | 2,152 | 2026-07-20 |
| katib | Python | 1,691 | 2026-07-18 |

**TeglonLabs** (5 snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| topoi | Python | 0 |

**bmorphism** (22 snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| Gay.jl | Julia | 2 (187 open issues!) |
| anti-bullshit-mcp-server | JavaScript | 22 |
| ocaml-mcp-sdk | OCaml | 61 |
| say-mcp-server | JavaScript | 20 |
| babashka-mcp-server | JavaScript | 19 |

**migalkin** (6 snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

**AustinCStone** (4 snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

### Notable Highlights
- **kubeflow/trainer** pushed 2026-07-20 — active development of distributed LLM training on K8s
- **bmorphism/Gay.jl** has 187 open issues — most active development in the GF(3) color system
- **plurigrid/asi** up to 31★ (was 16★ in Apr sweep) — fastest-growing plurigrid repo
- **plurigrid/shrimp** (Jul 2026) — newest repo, Jank worked example
- **TeglonLabs/jank-crane** (Jun 2026) — crane-jank converged-IR hub with GF(3) convergence maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z — 28 wallets)

Probed via Aptos mainnet fullnode (`ledger_version ~6,371,873,304`).
**All 28 wallets: 0.00 APT** (CoinStore resource not found — no native APT in `0x1::coin::CoinStore`).

| World | Address (prefix) | APT |
|-------|-----------------|-----|
| alice | 0xc793ac… | 0.00 |
| bob | 0x0a3c00… | 0.00 |
| A–Z (26 wallets) | 0x8699ed…–0x7af0ef… | 0.00 each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f4… | 2 | ✅ |
| A-G | 0xf56c4a… | 2 | ✅ |
| Y-Z | 0xd3ffe1… | 2 | ✅ |
| S-T | 0x3b1c3a… | 2 | ✅ |
| V-W | 0x40fad7… | 2 | ✅ |

All 5 multisig contracts healthy at 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Vercel authentication required. No market data accessible.

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
