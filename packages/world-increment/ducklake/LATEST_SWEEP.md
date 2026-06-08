# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-08

## Sweep Metadata
- **Date:** 2026-06-08T05:11Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this sweep) | 63 |
| Repo Snapshots (this sweep) | 63 repos × GF(3) color-tagged |
| Sources Covered | 3 orgs (plurigrid, kubeflow, TeglonLabs) + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | UNAVAILABLE (Vercel auth 401) |

---

## GF(3) Color Chain — 2026-06-08 Sweep (63 increments)

| IDs | Source | Repos | ERGODIC | PLUS | MINUS |
|-----|--------|-------|---------|------|-------|
| 1-5 | TeglonLabs (org) | 5 | 2 | 2 | 1 |
| 6-25 | plurigrid (org) | 20 | 7 | 7 | 6 |
| 26-40 | kubeflow (org) | 15 | 5 | 5 | 5 |
| 41-50 | bmorphism (user) | 10 | 4 | 3 | 3 |
| 51-55 | zubyul (user) | 5 | 2 | 2 | 1 |
| 56-58 | migalkin (user) | 3 | 1 | 1 | 1 |
| 59-60 | kristinezheng | 2 | 1 | 1 | 0 |
| 61-62 | M1shaaa | 2 | 1 | 1 | 0 |
| 63 | AustinCStone | 2 | 1 | 1 | 0 |

**Totals this sweep:** 21 ERGODIC `#d3869b` + 21 PLUS `#b8bb26` + 21 MINUS `#cc241d` = 63

GF(3) rule: `id%3==0 → ERGODIC · id%3==1 → PLUS · id%3==2 → MINUS`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-06-08)
- **kubeflow/kubeflow**: 15,707 stars (+142 since Apr) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,152 stars — pushed 2026-06-06
- **kubeflow/spark-operator**: 3,126 stars — pushed 2026-06-04
- **migalkin/NodePiece**: 144 stars — KG embeddings, active
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK (Jane Street oxcaml)
- **AustinCStone/TextGAN**: 92 stars — GAN text generation
- **plurigrid/gorj**: 434 open issues — active GF(3)/nREPL hub (pushed 2026-06-08)
- **bmorphism/Gay.jl**: 189 open issues, pushed today — wide-gamut deterministic color
- **M1shaaa/M1shaaa**: pushed 2026-06-08T03:38 — active profile
- **kristinezheng/kristinezheng.github.io**: pushed 2026-06-07 — active portfolio
- **TeglonLabs/jank-crane**: C++ GF3 convergence maps, created and pushed today 2026-06-08

---

## Hamming Swarm Snapshot (2026-06-08)

### Aptos Mainnet Wallets

All 28 wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | `0xc793...cc7b` | 0.0 |
| bob | `0x0a3c...512d` | 0.0 |
| A–Z (26 wallets) | — | 0.0 each |

**Result:** All 28 wallets return 0 APT. Accounts are not initialized with APT CoinStore on mainnet, indicating these are test/placeholder addresses.

### Multisig Contract Health

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4...003` | 2 | ✅ |
| A-G | `0xf56c...096` | 2 | ✅ |
| Y-Z | `0xd3ff...883` | 2 | ✅ |
| S-T | `0x3b1c...883` | 2 | ✅ |
| V-W | `0x40fa...b6d` | 2 | ✅ |

All 5 multisig contracts live and healthy, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — HTTP 401, Vercel deployment protection active. The SPA requires either a Vercel bypass token, OIDC trust configuration, or the `vercel curl` CLI. No market data extracted.

---

## Repo Counts by Source (2026-06-08)

| Source | Type | Repos Fetched |
|--------|------|--------------|
| plurigrid | org | 101 |
| bmorphism | user | 103 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| AustinCStone | user | 40 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| **TOTAL** | | **395** |
