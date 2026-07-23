# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-23

## Sweep Metadata
- **Date:** 2026-07-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 180 |
| Total Repo Snapshots | 157 |
| Sources Covered | 3 orgs + 8 users |

---

### GF(3) Color Chain Distribution

Increment IDs assigned sequentially per repo; GF(3) coloring by `id mod 3`:

| Trit | Color | Name | Count |
|------|-------|------|------:|
| 0 | `#d3869b` | ERGODIC | 59 |
| +1 | `#b8bb26` | PLUS | 61 |
| −1 | `#cc241d` | MINUS | 60 |

GF(3) chain: `PLUS → MINUS → ERGODIC → (repeating)`

---

### Repo Counts by Source

| Source | Type | Repos Snapshotted |
|--------|------|:-----------------:|
| plurigrid | org | 100 |
| kubeflow | org | 17 (top active) |
| TeglonLabs | org | 5 |
| bmorphism | user | 12 (top active) |
| zubyul | user | 6 (top active) |
| migalkin | user (social) | 4 |
| DJedamski | user (social) | 2 |
| wasita | user (social) | 3 |
| kristinezheng | user (social) | 2 |
| M1shaaa | user (social) | 2 |
| AustinCStone | user (social) | 4 |
| **TOTAL** | | **157** |

---

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|------:|----------|-----------|
| kubeflow/kubeflow | 15,789 | — | 2026-07-23 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-23 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-21 |
| kubeflow/trainer | 2,153 | Go | 2026-07-23 |
| kubeflow/katib | 1,692 | Python | 2026-07-20 |
| kubeflow/examples | 1,461 | Jsonnet | 2026-07-22 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-21 |
| kubeflow/arena | 815 | Go | 2026-07-21 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |

---

### Notable Social Graph Activity

- **bmorphism/Gay.jl** — Wide-gamut color sampling with splittable determinism (Julia); 187 open issues; pushed 2026-07-21
- **bmorphism/gay-chat** — gay://chat operationalization over Spritely Brassica Chat (Scheme); pushed 2026-07-14
- **bmorphism/anti-bullshit-mcp-server** — 22 stars, epistemological claim analysis MCP; pushed 2026-07-12
- **plurigrid/asi** — 31 stars, HTML; pushed 2026-07-10
- **plurigrid/gorj** — Clojure MCP REPL server (this repo); pushed 2026-07-23
- **wasita/wasita.github.io** — Personal site (Svelte); pushed 2026-07-21
- **migalkin/kgcourse2021** — Knowledge Graphs course materials; pushed 2026-07-10
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub with GF3 convergence maps; pushed 2026-06-08
- **zubyul/voice-observatory** — Passive macOS TUI observing voice-download pathways; pushed 2026-04-24
- **kubeflow/mcp-server** — MCP Server for AI-Assisted Development with Kubeflow; pushed 2026-07-21 (new!)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming-swarm addresses (alice, bob, A–Z) queried against Aptos mainnet fullnode.

**Result: All 28 wallets returned 0 APT** — accounts exist but have empty or unregistered CoinStore.

| World | Address | Balance (APT) |
|-------|---------|:-------------:|
| alice | 0xc793acdec12b4a63... | 0.000000 |
| bob | 0x0a3c00c58fdf9020... | 0.000000 |
| A | 0x8699edc0960dd5b9... | 0.000000 |
| B | 0x3f892ebe6e45164e... | 0.000000 |
| C | 0x38b99e63ada9b6fe... | 0.000000 |
| D | 0xf77656248f64d5dd... | 0.000000 |
| E | 0xdc1d9d533bac3507... | 0.000000 |
| F | 0x18a14b5b4bec118c... | 0.000000 |
| G | 0x69a394c0b0ac8421... | 0.000000 |
| H | 0xce67c327a7844e54... | 0.000000 |
| I | 0x070fe5d74e4eda30... | 0.000000 |
| J | 0x4d964db8f5383740... | 0.000000 |
| K | 0xa732040a6b0d5590... | 0.000000 |
| L | 0x7c2eaeafad972549... | 0.000000 |
| M | 0x6fed37a7553ef16b... | 0.000000 |
| N | 0xe7dde6da0a65f510... | 0.000000 |
| O | 0x73252b6011a75115... | 0.000000 |
| P | 0x6218792de4a9bc38... | 0.000000 |
| Q | 0xac40fa50b81b4ca6... | 0.000000 |
| R | 0x7ce605cc8fda4f8e... | 0.000000 |
| S | 0xb8753014e4888ea4... | 0.000000 |
| T | 0x35781dc0e42fef3f... | 0.000000 |
| U | 0x75860da47565f650... | 0.000000 |
| V | 0xb59dd8170321dfab... | 0.000000 |
| W | 0x5f32aef70f5ba530... | 0.000000 |
| X | 0xa95cbbd116548ac9... | 0.000000 |
| Y | 0xd8e32848f1dffa81... | 0.000000 |
| Z | 0x7af0ef6e1bd706f4... | 0.000000 |

---

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:------------:|:-------:|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c09062... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c... | 2 | ✓ |
| V-W | 0x40fad7b423a843... | 2 | ✓ |

**All 5 multisig contracts operational — 2-of-N threshold confirmed on mainnet.**

---

### MNX Markets (testnet.mnx.fi)

Probed `/api/markets`, `/api/v1/markets`, and root `/`. All endpoints served a Next.js SPA — no structured JSON market data accessible via public REST API.

**Status: SPA (unavailable via direct API)**

---

## DuckDB Schema

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
- `id mod 3 == 2` → trit=−1, color=`#cc241d`, name=MINUS

## DB Row Counts
| Table | Rows |
|-------|-----:|
| world_increments | 180 |
| repo_snapshots | 157 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-07-23*
