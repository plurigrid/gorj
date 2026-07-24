# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 7 |
| Total Repo Snapshots | 311 (1,255 rows incl. prior runs) |
| Sources Covered | 3 orgs + 4 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Total APT Balance | 0.0 |
| Multisig Health | 5/5 healthy |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 7 Increments (this run)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism | user | 100 | 0 | `#d3869b` | **ERGODIC** |
| 4  | zubyul | user | 49 | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs | org | 5 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user (social) | 5 | 0 | `#d3869b` | **ERGODIC** |
| 7  | AustinCStone | user (social) | 3 | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

**Note:** Social graph users DJedamski, wasita, kristinezheng, M1shaaa are outside this session's GitHub API scope — not snapshotted this run.

---

### Top Repos by Source

#### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| asi-skills | Julia | 3 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| gorj | Clojure | 1 | 2026-07-24 ← THIS REPO (1,361 open issues) |

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,789 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-24 |
| spark-operator | Python | 3,143 | 2026-07-17 |
| trainer | Go | 2,153 | 2026-07-24 |
| katib | Python | 1,692 | 2026-07-22 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

#### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-24 (187 open issues) |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| shitcoin | Python | 5 | 2026-04-08 |
| open-location-code-zig | Zig | 3 | 2025-12-30 |

#### migalkin (social graph, 5 snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

#### AustinCStone (social graph, 3 snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| byteruckus | HTML | 0 |
| EpsteinSearch | Python | 0 |
| bmforkupdate | Python | 0 |

---

### Cluster Analysis: plurigrid / bmorphism / zubyul

Shared themes across the triad:
- **Gay.jl / SplitMix64 / GF(3) trits** — deterministic color sampling with Galois geometry
- **OCapN / Spritely Syrup / CapTP** — secure distributed object capability protocols
- **Jank (C++ Clojure IR)** — plurigrid/gorj, TeglonLabs/jank-crane
- **MCP servers** — proliferating: coin-flip-mcp, monad-mcp-server, ocaml-mcp-sdk, anti-bullshit-mcp-server, forj itself
- **Move / Aptos** — zubyul/GayMove, zubyul/vibesnipe, bmorphism/boxxy, bmorphism/vibesnipe-market

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-24)

All 28 wallets probed via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A–Z (26 wallets) | 0x8699...–0x7af0... | 0.0 each |

**All 28 wallets: 0.0 APT.** No CoinStore resource found — addresses either not initialized on mainnet or carrying zero APT balance.

### Multisig Contract Probes (Aptos mainnet)

Probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures. All contracts are live and responding on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

Site is live (HTTP 200, Next.js SPA). No public REST API endpoint found at `/api/markets` or `/api/v1/markets` — the frontend is a client-rendered SPA that loads data via internal APIs not accessible without session credentials. **No market data extracted this run — mnx_snapshots table empty.**

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,789 stars (+224 since Apr 12) — ML platform for Kubernetes
- **kubeflow/pipelines**: 4,169 stars — most-starred pipeline project, pushed 2026-07-24
- **kubeflow/trainer**: 2,153 stars — AI training on Kubernetes (renamed from training-operator)
- **plurigrid/asi**: 31 stars (+15 since Apr 12) — topological chemputer
- **plurigrid/gorj**: 1,361 open issues — active development
- **bmorphism/Gay.jl**: 187 open issues, pushed 2026-07-24 — high activity
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR 2022)
- **5/5 multisigs healthy** — Hamming swarm 2-of-N contracts all responsive
- **28/28 wallets 0.0 APT** — swarm accounts not funded on mainnet
