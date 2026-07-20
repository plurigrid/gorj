# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-20 UTC  
**GF(3) Color Chain:** ERGODIC `#d3869b` (id%3=0) | PLUS `#b8bb26` (id%3=1) | MINUS `#cc241d` (id%3=2)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 12 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 41 |

**Total repos snapshotted: 394**

### Notable Highlights

- **plurigrid (100 repos):** Active ML/systems/agent org; high push volume.
- **kubeflow (49 repos):** ML ops platform; steady activity across pipelines, katib, training-operator.
- **TeglonLabs (5 repos):** Recent: `jank-crane` (C++, GF3 convergence maps, pushed 2026-06-08), `mathpix-gem` (Ruby, 2 stars, 11 open issues).
- **bmorphism (100 repos):** Diverse; heavy AI/Clojure/systems focus.
- **zubyul (49 repos):** Active mix of research and ML repos.
- **M1shaaa:** Profile repo pushed **2026-07-20T13:57:41Z** — most recent activity in the social graph today.
- **kristinezheng:** Personal site pushed 2026-07-01.
- **wasita:** `wasita.github.io` (Svelte personal site) pushed 2026-07-16.

### DuckDB Tables Written

- `world_increments` — 394 rows (GF3-colored increment chain)
- `repo_snapshots` — 394 rows (language, stars, forks, issues, pushed_at)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A-Z) returned `null` from the CoinStore resource query — accounts exist on-chain but hold zero APT or have no registered APT CoinStore. This is expected for fresh/dedicated multisig participant addresses.

| World | Balance (APT) |
|-------|---------------|
| alice | null |
| bob | null |
| A-Z | null (all 26) |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** and require **2 signatures**:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...87003 | 2 | YES |
| A-G | 0xf56c...c0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All pairs use standard 2-of-N multisig confirmed via `0x1::multisig_account::num_signatures_required` view function.

### MNX Markets

`testnet.mnx.fi` is behind **Vercel deployment authentication** — not accessible without a bypass token or OIDC trusted-source credential. Market data unavailable this run. Recorded as unavailable marker in mnx_snapshots table.

### DuckDB Tables Written

- `aptos_snapshots` — 28 rows (all null balances)
- `multisig_probes` — 5 rows (all healthy, sigs_required=2)
- `mnx_snapshots` — 1 row (unavailable marker)

---

## Schema Quick Reference

```sql
-- Repo count by org/user
SELECT org_or_user, COUNT(*) as repos, MAX(pushed_at) as latest_push
FROM repo_snapshots GROUP BY org_or_user ORDER BY repos DESC;

-- Most active repos (by stars)
SELECT full_name, language, stars, pushed_at
FROM repo_snapshots WHERE stars > 0 ORDER BY stars DESC LIMIT 20;

-- GF3 distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
