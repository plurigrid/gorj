# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-02  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.2 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 6 |
| wasita | user (social graph) | 5 |
| DJedamski | user (social graph) | 3 |
| kristinezheng | user (social graph) | 3 |
| AustinCStone | user (social graph) | 3 |
| M1shaaa | user (social graph) | 2 |
| **TOTAL** | | **322** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 107 |
| 1 | `#b8bb26` | PLUS | 108 |
| -1 | `#cc241d` | MINUS | 107 |

Rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,615 | 2026-04-29 |
| kubeflow/pipelines | Python | 4,130 | 2026-05-01 |
| kubeflow/spark-operator | Python | 3,121 | 2026-04-28 |
| kubeflow/trainer | Go | 2,095 | 2026-05-01 |
| kubeflow/katib | Python | 1,681 | 2026-04-14 |
| kubeflow/examples | Jsonnet | 1,460 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,013 | 2026-04-30 |
| migalkin/NodePiece | Python | 143 | 2026-03-02 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2026-03-16 |

### Notable Recent Activity

**plurigrid** (most recently pushed):
- `gorj` (Clojure) — forj + Rama topology nREPL + GF(3) trit coloring — pushed **2026-05-02**
- `zig-syrup` (Zig) — OCapN Syrup with CapTP optimizations — pushed 2026-04-30
- `asi-skills` (Julia) — 69 skills with Galois Hole Type accessibility — pushed 2026-04-26
- `asi` (HTML) — topological chemputer, 17★

**bmorphism** (most recently pushed):
- `Gay.jl` (Julia) — Wide-gamut SPI color sampling — pushed **2026-05-02**, 187 open issues
- `boxxy` (Move) — pushed 2026-04-30
- `ocaml-mcp-sdk` (OCaml) — Jane Street oxcaml_effect library, 60★
- `anti-bullshit-mcp-server` (JS) — claim validation MCP, 23★

**zubyul** (most recently pushed):
- `voice-observatory` (Python) — passive macOS TUI for voice-download pathways — pushed 2026-04-24
- `ghostel-emacs-worlds` (GLSL) — Ghostty + alice/bob emacs-mods — pushed 2026-04-24
- `nash-tui` / `nash-web` (Rust) — NASH token TUI + ratzilla WASM browser app

**TeglonLabs**:
- `mathpix-gem` (Ruby) — LaTeX/SMILES OCR gem, 2★, 11 open issues — pushed 2026-01-01
- `coin-flip-mcp` (JavaScript) — random.org MCP server, 2 forks — pushed 2025-09-21

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 Addresses (alice, bob, A–Z)

All wallets probed against Aptos mainnet fullnode.  
**Result: 0.0 APT across all 28 wallets.**  
The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found on any address — these are valid Aptos addresses that have not been funded on mainnet.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes — 5 Pairs

All probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.  
**All 5 contracts healthy: 2-of-N threshold confirmed.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi` is a Next.js SPA. All routes (`/api/markets`, `/api/v1/markets`, `/markets`, `/v1/markets`) return the HTML shell. No JSON market data accessible without executing the SPA JavaScript in a browser runtime.

---

## DuckDB Table Summary

```
world_increments  : 322 rows  (one per repo, GF(3) color-chained)
repo_snapshots    : 322 rows  (org/user, stars, forks, language, pushed_at)
aptos_snapshots   :  28 rows  (all 0.0 APT — unfunded addresses)
multisig_probes   :   5 rows  (all 2-sig-required, all healthy)
mnx_snapshots     :   0 rows  (SPA, no API accessible)
```

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

## Sample Queries

```sql
-- Most open issues
SELECT full_name, open_issues, language FROM repo_snapshots
ORDER BY open_issues DESC LIMIT 10;

-- GF(3) by source
SELECT org_or_user, gf3_name, COUNT(*) FROM world_increments
GROUP BY org_or_user, gf3_name ORDER BY org_or_user;

-- Healthy multisigs
SELECT pair, address, sigs_required FROM multisig_probes WHERE healthy = true;

-- Language distribution
SELECT language, COUNT(*) FROM repo_snapshots
WHERE language != '' GROUP BY language ORDER BY COUNT(*) DESC LIMIT 10;
```
