# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-06T12:30:00Z  
**Branch:** world-increment/sweep-2026-05-06  
**GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured | Top Stars |
|--------|------|---------------|-----------|
| plurigrid | org | 100 | asi (19★) |
| kubeflow | org | 47 | kubeflow/kubeflow (15,565★), pipelines (4,119★) |
| TeglonLabs | org | 4 | mathpix-gem (2★) |
| bmorphism | user | 19 | ocaml-mcp-sdk (60★), anti-bullshit-mcp (23★) |
| zubyul | user | 7 | WGCNA (2★), gay-world (1★) |
| migalkin | user | 5 | NodePiece (143★), StarE (89★) |
| DJedamski | user | 3 | Getting-and-Cleaning-Data (1★) |
| wasita | user | 4 | magic-garden (2★) |
| kristinezheng | user | 3 | Portfolio (0★) |
| M1shaaa | user | 2 | lab-bookshelf- (0★) |
| AustinCStone | user | 5 | TextGAN (92★), StereoVisionMRF (11★) |

**Total repos captured:** 199  
**Total world_increments:** 199 (GF(3) trit-colored)

### Notable Repos

- **migalkin/NodePiece** (143★, Python) — Compositional Knowledge Graph embeddings, ICLR'22
- **AustinCStone/TextGAN** (92★, Python) — TF GAN for text generation
- **migalkin/StarE** (89★, Python) — Hyper-relational KG message passing, EMNLP 2020
- **bmorphism/ocaml-mcp-sdk** (60★, OCaml) — Jane Street oxcaml_effect MCP SDK
- **plurigrid/gorj** (0★, Clojure) — forj + Rama + GF(3) gay trit coloring [this repo]
- **zubyul/tilelang-kernels** (Python) — TileLang GPU kernels for GF(3) trit classification on NVIDIA GB10 Blackwell
- **bmorphism/Gay.jl** (1★, Julia) — Wide-gamut color sampling w/ splittable determinism

### GF(3) Trit Distribution (199 increments)
- trit=0 ERGODIC #d3869b: 67 repos (ids divisible by 3)
- trit=1 PLUS #b8bb26: 67 repos (ids ≡ 1 mod 3)
- trit=-1 MINUS #cc241d: 65 repos (ids ≡ 2 mod 3)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...4cc7b | 0.0 | account exists, no CoinStore |
| bob | 0x0a3c...512d5d | 0.0 | account exists, no CoinStore |
| A | 0x8699...9d7a | null | CoinStore not found |
| B | 0x3f89...cb13 | null | CoinStore not found |
| C | 0x38b9...535e | null | CoinStore not found |
| D | 0xf776...cdd1 | null | CoinStore not found |
| E | 0xdc1d...8d36 | null | CoinStore not found |
| F | 0x18a1...3cf71 | null | CoinStore not found |
| G | 0x69a3...c7f32 | null | CoinStore not found |
| H | 0xce67...5300f | null | CoinStore not found |
| I | 0x070f...1fc9 | null | CoinStore not found |
| J | 0x4d96...7f54 | null | CoinStore not found |
| K | 0xa732...5dc4 | null | CoinStore not found |
| L | 0x7c2e...eba9 | null | CoinStore not found |
| M | 0x6fed...f2e9 | null | CoinStore not found |
| N | 0xe7dd...1b2c | null | CoinStore not found |
| O | 0x7325...a89d | 0.0 | account exists |
| P | 0x6218...c948 | 0.0 | account exists |
| Q | 0xac40...c89a9 | 0.0 | account exists |
| R | 0x7ce6...76e10 | 0.0 | account exists |
| S | 0xb875...d0386 | 0.0 | account exists |
| T | 0x3578...f4588 | 0.0 | account exists |
| U | 0x7586...f9956 | 0.0 | account exists |
| V | 0xb59d...af2c3 | 0.0 | account exists |
| W | 0x5f32...cc7b0 | 0.0 | account exists |
| X | 0xa95c...3047d | 0.0 | account exists |
| Y | 0xd8e3...444c4 | 0.0 | account exists |
| Z | 0x7af0...e197c | 0.0 | account exists |

**Summary:** 28 addresses probed. O–Z (14 addresses) have registered accounts with 0.0 APT. alice and bob have accounts but no AptosCoin CoinStore registered. A–N (14 addresses) returned no CoinStore resource on mainnet (accounts may be pre-registration or on a different chain).

### Multisig Contract Probes (5 pairs)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy.** Each requires 2-of-2 signatures. Probed via `0x1::multisig_account::num_signatures_required` on Aptos mainnet fullnode.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — Next.js SPA. `/api/markets` and `/api/v1/markets` returned 404. Root HTML is client-rendered; no embedded market data in initial SSR payload. Market data requires client-side JS execution.

---

## DuckDB Ducklake

**File:** `packages/world-increment/ducklake/world-increments.duckdb`  
**DuckDB version:** v1.5.2 (Variegata)

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 199 | GF(3)-colored event log |
| `repo_snapshots` | 199 | GitHub repo metadata snapshot |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig contract health checks |
| `mnx_snapshots` | 0 | MNX market data (SPA, unavailable) |

### Sample Queries

```sql
-- Top repos by stars
SELECT org_or_user, repo_name, stars, language
FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF(3) trit distribution
SELECT gf3_trit, gf3_color, gf3_name, COUNT(*) AS cnt
FROM world_increments GROUP BY 1,2,3 ORDER BY gf3_trit;

-- Aptos accounts with non-null balances
SELECT world, address, balance_apt
FROM aptos_snapshots WHERE balance_apt IS NOT NULL
ORDER BY world;

-- All healthy multisig pairs
SELECT pair, address, sigs_required
FROM multisig_probes WHERE healthy = true;

-- Repos pushed today (2026-05-06)
SELECT org_or_user, repo_name, pushed_at
FROM repo_snapshots WHERE pushed_at LIKE '2026-05-06%';
```

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**
