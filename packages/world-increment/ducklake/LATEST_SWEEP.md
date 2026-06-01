# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-01

## Sweep Metadata
- **Date:** 2026-06-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-06-01-1912`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1,335 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 10 |
| +1 | `#b8bb26` | PLUS | 12 |
| -1 | `#cc241d` | MINUS | 12 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...` (34 increments)

### GF(3) Color Chain — Sources

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

### Repo Counts by Source

| Source | Type | Repos (unique) |
|--------|------|----------------|
| plurigrid | org | ~101 |
| bmorphism | user | ~102 |
| kubeflow | org | ~48 |
| AustinCStone | user | ~40 |
| TeglonLabs | org | 4 |
| zubyul | user | ~49 |
| migalkin | user | ~19 |
| wasita | user | ~11 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| kubeflow/kubeflow | — | 15,699 | 2,669 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,151 | 2,003 | 2026-06-01 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 | 2026-06-01 |
| kubeflow/trainer | Go | 2,109 | 963 | 2026-05-30 |
| kubeflow/katib | Python | 1,685 | 525 | 2026-05-29 |
| kubeflow/examples | Jsonnet | 1,462 | 755 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,019 | 1,065 | 2026-05-29 |

### Notable Recent Activity (2026)

- **bmorphism/Gay.jl** (Julia) — pushed 2026-06-01 · wide-gamut color sampling with splittable determinism + LispSyntax
- **wasita/wasita.github.io** (Svelte) — pushed 2026-06-01 · personal website
- **M1shaaa/M1shaaa** — pushed 2026-06-01 · GitHub profile config
- **zubyul/voice-observatory** (Python) — pushed 2026-04-24 · passive macOS TUI for voice-download pathways
- **plurigrid/place** (TeX) — pushed 2026-05-21
- **kristinezheng/kristinezheng.github.io** (HTML) — pushed 2026-05-14

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-01)

Queried 28 addresses (alice, bob, A–Z) at `fullnode.mainnet.aptoslabs.com`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793... | 0.00000000 |
| bob | 0x0a3c... | 0.00000000 |
| A | 0x8699... | 0.00000000 |
| B | 0x3f89... | 0.00000000 |
| C | 0x38b9... | 0.00000000 |
| D | 0xf776... | 0.00000000 |
| E | 0xdc1d... | 0.00000000 |
| F | 0x18a1... | 0.00000000 |
| G | 0x69a3... | 0.00000000 |
| H | 0xce67... | 0.00000000 |
| I | 0x070f... | 0.00000000 |
| J | 0x4d96... | 0.00000000 |
| K | 0xa732... | 0.00000000 |
| L | 0x7c2e... | 0.00000000 |
| M | 0x6fed... | 0.00000000 |
| N | 0xe7dd... | 0.00000000 |
| O | 0x7325... | 0.00000000 |
| P | 0x6218... | 0.00000000 |
| Q | 0xac40... | 0.00000000 |
| R | 0x7ce6... | 0.00000000 |
| S | 0xb875... | 0.00000000 |
| T | 0x3578... | 0.00000000 |
| U | 0x7586... | 0.00000000 |
| V | 0xb59d... | 0.00000000 |
| W | 0x5f32... | 0.00000000 |
| X | 0xa95c... | 0.00000000 |
| Y | 0xd8e3... | 0.00000000 |
| Z | 0x7af0... | 0.00000000 |

**All 28 wallets: 0 APT** — accounts have no APT coin store initialized on mainnet.

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4... | 2 | ✅ |
| A-G | 0xf56c... | 2 | ✅ |
| Y-Z | 0xd3ff... | 2 | ✅ |
| S-T | 0x3b1c... | 2 | ✅ |
| V-W | 0x40fa... | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on each.**

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no JSON API accessible**  
`testnet.mnx.fi` serves a Next.js client-side app ("The AI Exchange"). All API paths return the HTML shell; no market data extractable without a headless browser. Recorded as unavailable.

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,699 stars — flagship ML platform for Kubernetes, still actively pushed
- **kubeflow/pipelines**: 4,151 stars — pushed 2026-06-01 (today)
- **kubeflow/spark-operator**: 3,125 stars — pushed 2026-06-01 (today)
- **bmorphism/Gay.jl**: Julia, pushed 2026-06-01 — wide-gamut color + Pigeons.jl splittable PRNG
- **M1shaaa/M1shaaa**: pushed 2026-06-01 — active profile config
- **Hamming swarm**: 28 wallets all at 0 APT; all 5 multisig contracts live with 2-of-N threshold
- **MNX testnet**: SPA, no JSON API; flagged unavailable in mnx_snapshots

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-06-01.*
