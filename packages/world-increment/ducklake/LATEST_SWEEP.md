# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-22

## Sweep Metadata
- **Date:** 2026-06-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 334 |
| Total Repo Snapshots | 334 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

```
id%3==0 → trit=0   ERGODIC  #d3869b  111 increments
id%3==1 → trit=+1  PLUS     #b8bb26  112 increments
id%3==2 → trit=-1  MINUS    #cc241d  111 increments
```

GF(3) sequence: PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → …

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 7 |
| DJedamski | social graph | 4 |
| wasita | social graph | 6 |
| kristinezheng | social graph | 4 |
| M1shaaa | social graph | 3 |
| AustinCStone | social graph | 8 |
| **TOTAL** | | **334** |

### Notable Repos (Top Stars)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| migalkin/NodePiece | 144 | Python | Compositional KG Representations (ICLR'22) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation (TensorFlow) |
| migalkin/StarE | 89 | Python | EMNLP 2020: Hyper-Relational KGs |
| migalkin/kgcourse2021 | 25 | HTML | Knowledge Graphs course materials (Russian) |
| AustinCStone/StereoVisionMRF | 11 | Python | MRF depth inference from stereo images |
| migalkin/NBFNet_mlx | 10 | Python | Neural Bellman-Ford nets on Apple Silicon (MLX) |
| TeglonLabs/mathpix-gem | 2 | Ruby | Math OCR to LaTeX/SMILES (security-first Ruby gem) |
| wasita/magic-garden | 2 | Python | Auto-purchasing bot for Discord magic garden game |
| TeglonLabs/jank-crane | 0 | C++ | crane-jank converged-IR hub, GF3 convergence maps |

### TeglonLabs Repos

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1`. Every address returned no `CoinStore<AptosCoin>` resource — **all balances: 0 APT**. Accounts exist on-chain but have not been initialized with APT coin storage.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts active and healthy. All require **2 signatures**.

| Pair | Address | Threshold | Status |
|------|---------|-----------|--------|
| A-B | 0x0da4...7003 | 2-of-N | ✓ healthy |
| A-G | 0xf56c...0096 | 2-of-N | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2-of-N | ✓ healthy |
| S-T | 0x3b1c...7883 | 2-of-N | ✓ healthy |
| V-W | 0x40fa...eb6d | 2-of-N | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active on the testnet deployment. The endpoint returns a 401 auth wall requiring Vercel CLI, Vercel MCP Server, Trusted Sources OIDC token, or a protection bypass token. No market data captured. `mnx_snapshots` table empty.

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

```
id mod 3 == 0 → trit=0,  color=#d3869b, name=ERGODIC
id mod 3 == 1 → trit=+1, color=#b8bb26, name=PLUS
id mod 3 == 2 → trit=-1, color=#cc241d, name=MINUS
```
