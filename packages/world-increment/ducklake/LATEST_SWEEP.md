# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-29  
**GF(3) Color Chain:** ERGODIC #d3869b → PLUS #b8bb26 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshot

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 47 |
| AustinCStone | user_social | 8 |
| wasita | user_social | 7 |
| migalkin | user_social | 7 |
| DJedamski | user_social | 5 |
| TeglonLabs | org | 4 |
| kristinezheng | user_social | 4 |
| M1shaaa | user_social | 3 |
| **Total** | | **334** |

### GF(3) Increment Chain

| id | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | 2 | #cc241d | MINUS |
| 3 | bmorphism | 0 | #d3869b | ERGODIC |
| 4 | zubyul | 1 | #b8bb26 | PLUS |
| 5 | TeglonLabs | 2 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | 1 | #b8bb26 | PLUS |
| 8 | wasita | 2 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone | 2 | #cc241d | MINUS |

### Notable Repos

**plurigrid** (100 repos): Active org — recently pushed: `zig-syrup`, diverse languages including Clojure, Rust, Python.

**bmorphism** (100 repos): Active user — recently pushed: `nanoclj-zig`, wide range of experimental projects.

**zubyul** (49 repos): Recent activity: `voice-observatory` (Python, 2026-04-24), `ghostel-emacs-worlds` (GLSL, 2026-04-24), `nash-web`/`nash-tui` (Rust, 2026-04-13).

**kubeflow** (47 repos): ML infrastructure org — `hub` most recently pushed.

**TeglonLabs** (4 repos): `mathpix-gem` (Ruby, ★2, 11 open issues), `coin-flip-mcp` (JavaScript, 2 forks), `monad-mcp-server`, `topoi` (Python).

**migalkin** (7 sampled): Knowledge graph researcher — `NodePiece` (★143), `StarE` (★89), `kgcourse2021` (★25), `NBFNet_mlx` (★10).

**AustinCStone** (8 sampled): `TextGAN` (★92, 30 forks), `StereoVisionMRF` (★11), `EpsteinSearch` (2026-02-11).

**wasita** (7 sampled): `wasita.github.io` (Svelte, updated 2026-04-28), `magic-garden` (Python bot ★2).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`. All wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`, indicating accounts are not yet funded on mainnet.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 (unfunded) |
| bob | 0x0a3c...512d | 0.0 (unfunded) |
| A–Z | 0x8699...–0x7af0... | 0.0 (all unfunded) |

**Aptos ledger state at query time:**
- Epoch: 15617
- Block height: 739,614,037
- Timestamp: 2026-04-29T13:11:46Z

### Multisig Contract Probes

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

**All multisig contracts: 2-of-n threshold, all healthy.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — all API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned no data. The testnet SPA does not expose a public REST API at these endpoints.

---

## DuckDB Schema (world-increments.duckdb)

```
world_increments  — 11 rows  (GF3 color-chain increments per source)
repo_snapshots    — 334 rows (snapshotted repos with stars/forks/language/pushed_at)
aptos_snapshots   — 28 rows  (hamming swarm wallet balances)
multisig_probes   —  5 rows  (multisig threshold probes, all healthy)
mnx_snapshots     —  0 rows  (MNX unavailable)
```
