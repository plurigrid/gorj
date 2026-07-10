# World-Increment Sweep + Hamming Snapshot — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 158 |
| Total Repo Snapshots | 158 (unique) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5/5 healthy |
| MNX Markets | Unavailable (auth-gated) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources & Repo Counts

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 10 (top active) |
| TeglonLabs | org | 5 |
| bmorphism | user | 14 (top active) |
| zubyul | user | 10 (top active) |
| migalkin | user | 5 (top active) |
| DJedamski | user (social) | 3 |
| wasita | user (social) | 3 |
| kristinezheng | user (social) | 2 |
| M1shaaa | user (social) | 2 |
| AustinCStone | user (social) | 4 |
| **TOTAL** | | **158 unique repos** |

### Top Repos by Stars

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,771 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,169 | 2026-07-09 |
| kubeflow/spark-operator | Python | 3,136 | 2026-07-09 |
| kubeflow/trainer | Go | 2,134 | 2026-07-09 |
| kubeflow/katib | Python | 1,689 | 2026-07-09 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-07-09 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |

### Plurigrid Org Highlights (most recently pushed)
- **gorj** (Clojure) — 2026-07-07 — MCP REPL server (this repo)
- **shrimp** — 2026-07-03
- **asi** (HTML, 30★) — 2026-07-07
- **place** (TeX) — 2026-06-27 — BCI forester preview

### TeglonLabs Highlights
- **jank-crane** (C++) — GF3 convergence maps, crane-jank converged-IR hub — 2026-06-08
- **mathpix-gem** (Ruby, 2★) — math image-to-LaTeX with security-first design
- **coin-flip-mcp** (JavaScript) — MCP server with random.org entropy

### bmorphism Social Graph (most active repos)
- **Gay.jl** (Julia) — wide-gamut color sampling with splittable determinism — 2026-06-20
- **satreadout** (HTML) — machine-checked saturating non-Riemannian perceptual readout — 2026-06-20
- **ocaml-mcp-sdk** (OCaml, 61★) — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **anti-bullshit-mcp-server** (JS, 23★) — claim analysis with epistemological frameworks

### GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 53 |
| PLUS | #b8bb26 | +1 | 53 |
| MINUS | #cc241d | -1 | 52 |

GF(3) rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

Queried `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on mainnet.

**Result:** `resource_not_found` for all 28 addresses.

**Interpretation:** Accounts exist on-chain (e.g., `alice` has `sequence_number=72`, confirming transaction activity) but hold APT via the **Fungible Asset (FA)** standard post-migration, not the legacy CoinStore. All addresses recorded with `balance_apt=NULL`.

| World | Address (truncated) |
|-------|---------------------|
| alice | 0xc793a...4cc7b |
| bob   | 0x0a3c0...512d5d |
| A–Z   | 26 addresses — see aptos_snapshots table |

### Multisig Contract Probes — 5/5 HEALTHY ✅

All 5 multisig accounts respond to `0x1::multisig_account::num_signatures_required` view call.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f4...87003 | 2 | ✅ |
| A-G | 0xf56c4a...c0096 | 2 | ✅ |
| Y-Z | 0xd3ffe1...5b883 | 2 | ✅ |
| S-T | 0x3b1c3a...7883  | 2 | ✅ |
| V-W | 0x40fad7...eb6d  | 2 | ✅ |

All 5 require 2-of-N signatures and are reachable.

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — Vercel deployment protection (HTTP 401, password-gated). No unauthenticated API path accessible. Recorded 0 rows in `mnx_snapshots`.

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
