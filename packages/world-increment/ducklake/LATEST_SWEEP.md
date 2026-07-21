# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total Repos | Notable |
|--------|------|-------------|---------|
| plurigrid | org | 103 | asi ⭐31, ontology ⭐8, asi-skills ⭐3 |
| kubeflow | org | 49 | kubeflow ⭐15788, pipelines ⭐4169, spark-operator ⭐3142 |
| TeglonLabs | org | 5 | mathpix-gem ⭐2, jank-crane, coin-flip-mcp |
| bmorphism | user | 106 | ocaml-mcp-sdk ⭐61, anti-bullshit-mcp-server ⭐22, Gay.jl ⭐2 |
| zubyul | user | 49 | gay-world ⭐1, voice-observatory, ghostel-emacs-worlds |
| migalkin | user | 19 | NodePiece ⭐144, StarE ⭐89, kgcourse2021 ⭐24 |
| DJedamski | user | 6 | kaggle_ncaa18, Kaggle |
| wasita | user | 12 | magic-garden ⭐2, wasita.github.io ⭐1, send2kobo ⭐1 |
| kristinezheng | user | 5 | kristinezheng.github.io, lookit-jenga |
| M1shaaa | user | 8 | M1shaaa profile, lab-bookshelf- |
| AustinCStone | user | 41 | TextGAN ⭐92, byteruckus |

### Top Activity Today (2026-07-21)

- **bmorphism/Gay.jl** — updated 10:59 UTC today, 187 open issues, active Julia color-sampling work
- **kubeflow/kubeflow** — updated 09:44 UTC, 15,788 stars, ML toolkit for Kubernetes
- **kubeflow/spark-operator** — updated 08:57 UTC, 3,142 stars
- **kubeflow/sdk** — updated 09:05 UTC, 127 stars, new universal Python SDK

### GF(3) Color Chain Distribution

65 world-increment rows assigned across GF(3) trit color chain:

| GF(3) Name | Color | Trit | Count |
|-----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 21 |
| PLUS | #b8bb26 | +1 | 22 |
| MINUS | #cc241d | -1 | 22 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried all 28 addresses. All returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts exist on-chain
but CoinStore is not initialized (no APT ever deposited). Recorded as 0.0 APT.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63... | 0.0 (uninitialized) |
| bob | 0x0a3c00c58fdf9020... | 0.0 (uninitialized) |
| A–Z (26 addrs) | (see DB) | 0.0 each |

### Multisig Contract Probes

All 5 pairs are healthy — `num_signatures_required = 2` (2-of-2 multisig):

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✅ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✅ |
| V-W | 0x40fad7b423a84365... | 2 | ✅ |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment-protection.
Unauthenticated requests return 401. No market data was fetchable.
Requires Vercel bypass token or trusted-source OIDC config.

---

## DuckDB Schema

```sql
-- packages/world-increment/ducklake/world-increments.duckdb
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)             -- 65 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)             -- 65 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 0 rows
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,788 stars — flagship ML platform for Kubernetes (active today)
- **kubeflow/pipelines**: 4,169 stars — ML pipelines for Kubernetes
- **kubeflow/spark-operator**: 3,142 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars — compositional knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — generative adversarial network for text
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **bmorphism/anti-bullshit-mcp-server**: 22 stars — claim validation MCP (active July 12)
- **plurigrid/gorj**: this repo — 1,295 open issues, GF(3) compositional REPL orchestration
- **All multisig pairs**: 2-of-2, all healthy — Hamming swarm fully coherent
- **All 28 Aptos wallets**: CoinStore uninitialized — no APT balance recorded
