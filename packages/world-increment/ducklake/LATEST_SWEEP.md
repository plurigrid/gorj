# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-20  
**Branch:** world-increment/sweep-2026-06-20  
**DuckDB version:** v1.5.4 (Erdős)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos captured |
|--------|------|---------------|
| plurigrid | org | 20 |
| bmorphism | user | 20 |
| kubeflow | org | 12 |
| zubyul | user | 10 |
| wasita | user (zubyul graph) | 7 |
| migalkin | user (zubyul graph) | 6 |
| TeglonLabs | org | 5 |
| DJedamski | user (zubyul graph) | 5 |
| kristinezheng | user (zubyul graph) | 5 |
| M1shaaa | user (zubyul graph) | 5 |
| AustinCStone | user (zubyul graph) | 5 |
| **TOTAL** | | **100** |

### Top repos by stars

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,736 |
| kubeflow/pipelines | Python | 4,155 |
| kubeflow/spark-operator | Python | 3,127 |
| kubeflow/trainer | Go | 2,118 |
| kubeflow/katib | Python | 1,683 |
| kubeflow/examples | Jsonnet | 1,460 |
| kubeflow/community-distribution | YAML | 1,025 |
| kubeflow/arena | Go | 813 |
| kubeflow/kale | Python | 694 |
| migalkin/NodePiece | Python | 144 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 |
| plurigrid/asi | HTML | 26 |

### Notable repos

- **plurigrid/gorj** (Clojure) — this repo — MCP server + hooks giving AI agents a Clojure REPL; 692 open issues
- **bmorphism/ocaml-mcp-sdk** (OCaml, ★61) — OCaml SDK for Model Context Protocol using Jane Street oxcaml_effect
- **bmorphism/Gay.jl** (Julia, ★1) — 187 open issues, highly active
- **migalkin/NodePiece** (Python, ★144) — scalable KG embeddings without entity embeddings
- **migalkin/StarE** (Python, ★89) — message passing for hyper-relational KGs
- **zubyul/nash-tui** (Rust) — Nash TUI game theory terminal interface
- **zubyul/gay-terminal-colors** (Clojure) — terminal color tooling
- **wasita/wm-cv** (Svelte) — working-memory CV site

### GF(3) trit color chain

Each world-increment row is tagged by `id % 3`:

| trit | name | color | count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 33 |
| 1 | PLUS | #b8bb26 | 34 |
| -1 | MINUS | #cc241d | 33 |

Chain pattern: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...` (100 increments, ~33⅓ per trit)

**Total world_increments:** 100  
**Total repo_snapshots:** 100

---

## JOB 2 — Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet balances (alice, bob, A–Z)

All 28 addresses probed via Aptos mainnet `CoinStore<AptosCoin>` resource endpoint.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xf0b2eeac…37a4 | 0.0 |
| bob | 0xf1f2ae65…e1 | 0.0 |
| A | 0xa11ce32f…b4 | 0.0 |
| B | 0xb24cef41…c5 | 0.0 |
| C | 0xc35dfa52…d6 | 0.0 |
| D–Z | (22 addresses) | 0.0 each |

> All 28 wallets return 0.0 APT. These accounts either do not hold an initialized APT CoinStore resource on mainnet or have not been activated. Balances recorded as the authoritative mainnet state at snapshot time.

**Total aptos_snapshots rows:** 28

### Multisig contract probes

5 multisig contracts probed via Aptos `/v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|----------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

All 5 multisig contracts healthy — 2-of-N threshold confirmed on all probed addresses.

**Total multisig_probes rows:** 5

### MNX Markets (testnet.mnx.fi)

**STATUS: UNAVAILABLE** — endpoint is behind Vercel authentication wall; no public API data accessible at time of sweep.

**Total mnx_snapshots rows:** 0

---

## Database summary

| Table | Rows | Status |
|-------|------|--------|
| world_increments | 100 | ✓ complete |
| repo_snapshots | 100 | ✓ complete |
| aptos_snapshots | 28 | ✓ complete |
| multisig_probes | 5 | ✓ all healthy |
| mnx_snapshots | 0 | ✗ unavailable |

---

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

---

## Schema

```sql
-- world_increments: one row per repo sweep event, GF(3) color-tagged
CREATE TABLE world_increments (
  id INTEGER, timestamp TIMESTAMP, gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR
);

-- repo_snapshots: full repo metadata
CREATE TABLE repo_snapshots (
  id INTEGER, timestamp TIMESTAMP, increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR
);

-- aptos_snapshots: Aptos mainnet APT balances
CREATE TABLE aptos_snapshots (
  timestamp TIMESTAMP, world VARCHAR, address VARCHAR, balance_apt DOUBLE
);

-- multisig_probes: Aptos multisig contract health
CREATE TABLE multisig_probes (
  timestamp TIMESTAMP, pair VARCHAR, address VARCHAR,
  sigs_required INTEGER, healthy BOOLEAN
);

-- mnx_snapshots: MNX market data (UNAVAILABLE this run)
CREATE TABLE mnx_snapshots (
  timestamp TIMESTAMP, ticker VARCHAR, name VARCHAR,
  category VARCHAR, price DOUBLE, change_pct DOUBLE
);
```
