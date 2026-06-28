# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-28  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Increment | GF3 Trit | Color | Source | Repos |
|-----------|----------|-------|--------|-------|
| 1 | +1 PLUS | #b8bb26 | AustinCStone | 5 |
| 2 | -1 MINUS | #cc241d | DJedamski | 6 |
| 3 | 0 ERGODIC | #d3869b | M1shaaa | 3 |
| 4 | +1 PLUS | #b8bb26 | TeglonLabs | 5 |
| 5 | -1 MINUS | #cc241d | bmorphism | 100 |
| 6 | 0 ERGODIC | #d3869b | kristinezheng | 5 |
| 7 | +1 PLUS | #b8bb26 | kubeflow | 48 |
| 8 | -1 MINUS | #cc241d | migalkin | 5 |
| 9 | 0 ERGODIC | #d3869b | plurigrid | 100 |
| 10 | +1 PLUS | #b8bb26 | wasita | 6 |
| 11 | -1 MINUS | #cc241d | zubyul | 49 |

**Total repos snapshotted:** 332

### Top Repos by Stars

| Org/User | Repo | Stars | Language | Last Push |
|----------|------|-------|----------|-----------|
| kubeflow | kubeflow | 15750 | — | 2026-06-18 |
| kubeflow | pipelines | 4158 | Python | 2026-06-27 |
| kubeflow | spark-operator | 3129 | Python | 2026-06-26 |
| kubeflow | trainer | 2125 | Go | 2026-06-26 |
| kubeflow | katib | 1687 | Python | 2026-06-23 |
| migalkin | NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone | TextGAN | 92 | Python | 2025-03-03 |
| migalkin | StarE | 89 | Python | 2026-04-16 |
| TeglonLabs | mathpix-gem | 2 | Ruby | 2026-01-01 |
| TeglonLabs | jank-crane | 0 | C++ | 2026-06-08 |

### Zubyul Social Graph Highlights

- **migalkin** — KG research (NodePiece ★144, StarE ★89, RWL, NBFNet_mlx) — active 2026
- **wasita** — Svelte/web projects (wasita.github.io active 2026-06, send2kobo, wm-cv)
- **kristinezheng** — MIT cognitive science, active website 2026-06
- **M1shaaa** — Yale, lookit/psych research projects
- **DJedamski** — Kaggle/ML (ncaa18, data science coursera projects)
- **AustinCStone** — TextGAN ★92, StereoVisionMRF ★11, bmorphism forks active 2026

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-28)

Queried via `0x1::coin::balance` view function (FA-compatible).

| World | APT Balance | Address (truncated) |
|-------|-------------|---------------------|
| bob | 12.65700700 | 0x0a3c00c58fdf9020... |
| F | 1.96051600 | 0x18a14b5b4bec118c... |
| L | 1.92726900 | 0x7c2eaeafad972549... |
| J | 1.89509300 | 0x4d964db8f5383740... |
| alice | 0.43643352 | 0xc793acdec12b4a63... |
| O | 0.21013600 | 0x73252b6011a75115... |
| K | 0.16196100 | 0xa732040a6b0d5590... |
| P | 0.14013600 | 0x6218792de4a9bc38... |
| M | 0.11228500 | 0x6fed37a7553ef16b... |
| N | 0.10612100 | 0xe7dde6da0a65f510... |
| Q | 0.10324000 | 0xac40fa50b81b4ca6... |
| S | 0.09178800 | 0xb8753014e4888ea4... |
| R | 0.09021700 | 0x7ce605cc8fda4f8e... |
| T | 0.07371300 | 0x35781dc0e42fef3f... |
| U | 0.05577300 | 0x75860da47565f650... |
| A | 0.05176700 | 0x8699edc0960dd5b9... |
| V | 0.04883299 | 0xb59dd8170321dfab... |
| Y | 0.04444900 | 0xd8e32848f1dffa81... |
| X | 0.04257700 | 0xa95cbbd116548ac9... |
| W | 0.04070500 | 0x5f32aef70f5ba530... |
| B | 0.03625600 | 0x3f892ebe6e45164e... |
| Z | 0.02426800 | 0x7af0ef6e1bd706f4... |
| D | 0.01162900 | 0xf77656248f64d5dd... |
| C | 0.01018500 | 0x38b99e63ada9b6fe... |
| E | 0.00937200 | 0xdc1d9d533bac3507... |
| H | 0.00168100 | 0xce67c327a7844e54... |
| I | 0.00068100 | 0x070fe5d74e4eda30... |
| G | 0.00068100 | 0x69a394c0b0ac8421... |

**Total swarm APT:** 20.34477251

### Multisig Contract Probes

All 5 probed contracts returned `sigs_required=2` and are healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da... | 2 | healthy |
| A-G | 0xf56c4a1c0906214f... | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df406... | 2 | healthy |
| S-T | 0x3b1c3ae905d44c3a... | 2 | healthy |
| V-W | 0x40fad7b423a84365... | 2 | healthy |

### MNX Markets

`https://testnet.mnx.fi` — returned **HTTP 401 Authentication Required**. No market data available without credentials.

---

## DuckDB Schema

```sql
world_increments  -- 11 rows: GF3 color chain per source
repo_snapshots    -- 332 rows: full repo metadata
aptos_snapshots   -- 28 rows: hamming swarm APT balances
multisig_probes   -- 5 rows: 2-of-N multisig health check
mnx_snapshots     -- 0 rows: unavailable (auth required)
```
