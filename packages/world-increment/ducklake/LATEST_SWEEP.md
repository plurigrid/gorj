# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-09

## Sweep Metadata
- **Date:** 2026-05-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 60 (representative sample) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | wasita (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | kristinezheng (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | M1shaaa (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | AustinCStone (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | DJedamski (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## JOB 1: GitHub Social Graph — Top Repos by Source

### plurigrid (100 repos total, 15 sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-05-09 |
| asi | HTML | 21 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-04-26 |
| asi-skills | Julia | 3 | 2026-04-26 |

### kubeflow (48 repos total, 10 sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,628 | 2026-05-07 |
| pipelines | Python | 4,137 | 2026-05-08 |
| spark-operator | Python | 3,125 | 2026-05-08 |
| trainer | Go | 2,096 | 2026-05-09 |
| arena | Go | 810 | 2026-05-07 |

### bmorphism (101 repos total, 11 sampled)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| say-mcp-server | JavaScript | 20 | 2026-03-19 |
| babashka-mcp-server | JavaScript | 18 | 2026-03-26 |
| risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |

### AustinCStone (40 repos, 3 sampled)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

**All 28 addresses returned NULL** — `CoinStore<AptosCoin>` resource not found.  
Addresses have no initialized APT balance on mainnet (zero-balance or uninitialized accounts).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793ac… | NULL |
| bob | 0x0a3c00… | NULL |
| A–Z | (26 addresses) | NULL (all) |

### Multisig Contract Probes

**5/5 healthy. All require 2-of-N signatures.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

### MNX Markets

**Unavailable** — `testnet.mnx.fi` is a Next.js SPA. Paths `/api/markets`, `/api/tickers`, `/api/v1/markets` all return the HTML shell. Market data requires browser-side JS execution.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(id, timestamp, world, address, balance_apt)
multisig_probes(id, timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(id, timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
- `id mod 3 == 0` → trit=0,  color=#d3869b, name=ERGODIC

## Notable Highlights
- **kubeflow/kubeflow**: 15,628★ flagship ML platform for Kubernetes (updated 2026-05-07)
- **kubeflow/pipelines**: 4,137★ pushed 2026-05-08
- **migalkin/NodePiece**: 144★ — ICLR'22 compositional KG embeddings, still active
- **bmorphism/ocaml-mcp-sdk**: 61★ — OCaml MCP SDK with oxcaml_effect, updated 2026-05-08
- **AustinCStone/TextGAN**: 92★ — text GAN from 2016, still accumulating citations
- **plurigrid/gorj**: This very repo — 130 open issues, pushed today 2026-05-09
- **All 5 multisigs**: Healthy at 2-of-N threshold (A-B, A-G, Y-Z, S-T, V-W)
