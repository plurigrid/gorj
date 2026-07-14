# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 162 |
| Total Repo Snapshots (cumulative) | 1,083 |
| New increments this sweep | 139 |
| Sources Covered | 3 orgs + 8 users + social graph |

---

## GF(3) Color Chain (this sweep, 139 new increments)

```
ERGODIC #d3869b (id%3==0) → PLUS #b8bb26 (id%3==1) → MINUS #cc241d (id%3==2) → repeat
```

---

## Top Repos by Source (2026-07-14)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-14 |
| place | TeX | 1 | 2026-07-14 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| eirobri | Clojure | 0 | 2026-07-14 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,777 | 2026-07-14 |
| pipelines | Python | 4,165 | 2026-07-14 |
| spark-operator | Python | 3,136 | 2026-07-14 |
| trainer | Go | 2,140 | 2026-07-14 |
| katib | Python | 1,690 | 2026-07-11 |
| community-distribution | YAML | 1,029 | 2026-07-13 |
| mcp-apache-spark-history-server | Python | 182 | 2026-07-07 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (50 repos, most recently active)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| Gay.jl | Julia | 2 | 2026-07-14 |
| gay-chat | Scheme | 0 | 2026-07-14 |
| whale | MATLAB | 2 | 2026-04-20 |

### zubyul (active public repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-world | Python | 1 | 2026-04-05 |
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| big-bad-plurigrid-quiz | Emacs Lisp | 0 | 2026-04-09 |

### Social graph (migalkin, wasita, AustinCStone, DJedamski, kristinezheng, M1shaaa)
| Repo | Language | Stars |
|------|----------|-------|
| migalkin/NodePiece | Python | 144 |
| migalkin/StarE | Python | 89 |
| AustinCStone/TextGAN | Python | 92 |
| wasita/wasita.github.io | Svelte | 1 |
| wasita/send2kobo | TypeScript | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

All 28 wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Interpretation:** Accounts are initialized on Aptos mainnet (ledger v6276817813) but have no APT CoinStore — consistent with accounts holding non-APT assets or never receiving native APT.

| World | Address | APT balance |
|-------|---------|-------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z | (see DB: aptos_snapshots) | 0.0 each |

### Multisig Contract Probes (5 pairs) — ALL HEALTHY

All 5 multisig contracts respond on-chain with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Behind Vercel deployment protection (HTTP 401). No market data extractable without a bypass token or Trusted Sources OIDC configuration.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-07-14)
- **plurigrid/gorj** (this repo) pushed today — forj + Rama topology nREPL routing + GF(3) gay trit coloring (1,167 open issues)
- **kubeflow/kubeflow** grew to 15,777 stars (was 15,565 on 2026-04-12)
- **kubeflow/trainer** most active kubeflow repo today
- **bmorphism/gay-chat** created today — gay://chat over Spritely Brassica Chat (Scheme)
- **bmorphism/Gay.jl** active today — 187 open issues, GF(3)-central
- **plurigrid/asi** grew to 30 stars (was 16 on 2026-04-12)
- **All 5 multisig pairs**: sigs_required=2, healthy — swarm consensus intact
- **MNX testnet**: Vercel-gated, requires bypass token to access
