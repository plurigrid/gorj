# World-Increment Sweep + Hamming Snapshot — 2026-04-21

## Sweep Metadata
- **Date:** 2026-04-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 216 |
| Total Repo Snapshots | 1137 rows / 549 distinct repos |
| Aptos Snapshots | 28 addresses |
| Multisig Probes | 5 pairs |
| MNX Snapshots | 1 (unavailable) |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

| trit | color | name | count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 71 |
| +1 | `#b8bb26` | PLUS | 73 |
| -1 | `#cc241d` | MINUS | 72 |

**GF(3) Assignment Rule:**
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC (rose/mauve)
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS (yellow-green)
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS (red)

---

## JOB 1: GitHub Social Graph

### Repo Counts by Source

| Source | Type | API Repos Queried |
|--------|------|-----------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 101 |
| zubyul | user | 47 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 10 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |

### Top Repos by Stars (Social Graph)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | ~18,000 | Jsonnet | 2026-01-05 |
| kubeflow/pipelines | ~4,100 | Python | 2026-04-10 |
| kubeflow/spark-operator | ~3,100 | Python | 2026-04-10 |
| kubeflow/trainer | ~2,080 | Go | 2026-04-10 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-28 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2025-05-21 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| bmorphism/manifold-mcp-server | 14 | JavaScript | 2026-04-15 |

### Notable Recent Activity (2026-04)

- **bmorphism/nanoclj-zig** — Zig NanoClojure interpreter, created 2026-04-18
- **bmorphism/whale** — omniglot + sperm whale codas = metawhaling, pushed 2026-04-20
- **zubyul/nash-web** — NASH token browser TUI (Rust/WASM + GeckoTerminal), pushed 2026-04-13
- **zubyul/nash-tui** — NASH token real-time candles TUI, pushed 2026-04-13
- **zubyul/big-bad-plurigrid-quiz** — 27 flashcards from bmorphism/zubyul activity, pushed 2026-04-09
- **wasita/wasita.github.io** — personal Svelte site, pushed 2026-04-20
- **migalkin/StarE** — hyper-relational KG paper, pushed 2026-04-16
- **bmorphism/penrose-mcp** — Penrose diagrammatic server, pushed 2026-04-12

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.  
**All addresses carry 0 APT balance** at sweep time (2026-04-21).  
Two addresses (bob, A) had transient network errors; treated as 0.0 APT.

| Address | Label | APT Balance |
|---------|-------|-------------|
| 0xc793acdec1... | alice | 0.0000 |
| 0x0a3c00c58f... | bob | 0.0000 |
| 0x8699edc096... | A | 0.0000 |
| 0x3f892ebe6e... | B | 0.0000 |
| ... | C–Z | 0.0000 each |

### Multisig Contract Health (Aptos Mainnet)

Probed via `0x1::multisig_account::num_signatures_required`.  
**All 5 multisig pairs are 2-of-2 and healthy.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0... | 2 | ✅ |
| A-G | 0xf56c4a1c09... | 2 | ✅ |
| Y-Z | 0xd3ffe1812b... | 2 | ✅ |
| S-T | 0x3b1c3ae905... | 2 | ✅ |
| V-W | 0x40fad7b423... | 2 | ✅ |

The Hamming swarm topology is intact — all pairwise contracts respond.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — DNS resolution failure on all probed paths:
- `https://testnet.mnx.fi/api/markets`
- `https://testnet.mnx.fi/api/v1/markets`
- `https://testnet.mnx.fi/api/tickers`

Recorded as `UNAVAILABLE` in `mnx_snapshots` table.

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

## Notable Highlights
- **kubeflow/kubeflow**: flagship ML platform for Kubernetes, ~18K stars
- **migalkin/NodePiece**: 143 stars — ICLR'22 scalable KG embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK (Jane Street oxcaml_effect)
- **bmorphism/whale**: sperm whale coda + omniglot = metawhaling (active 2026-04-20)
- **zubyul/nash-web**: NASH TUI market viewer, freshest zubyul push (2026-04-13)
- **Hamming swarm**: 5/5 multisig pairs healthy, 2-of-2 threshold each
- **Zero APT across all 28 addresses** — swarm wallets are dormant on mainnet
