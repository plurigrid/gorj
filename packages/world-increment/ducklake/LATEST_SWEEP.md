# World Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-08-07 UTC  
**Run type:** Automated scheduled sweep (world-increment + hamming-swarm)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | GF3 |
|--------|------|-------|-----|
| plurigrid | org | 100 | PLUS (#b8bb26) |
| kubeflow | org | 49 | MINUS (#cc241d) |
| TeglonLabs | org | 5 | ERGODIC (#d3869b) |
| bmorphism | user | 50 | PLUS (#b8bb26) |
| zubyul | user | 49 | MINUS (#cc241d) |
| migalkin | social | 5 | ERGODIC (#d3869b) |
| DJedamski | social | 4 | PLUS (#b8bb26) |
| wasita | social | 4 | MINUS (#cc241d) |
| AustinCStone | social | 4 | ERGODIC (#d3869b) |
| kristinezheng | social | 5 | ERGODIC (#d3869b) |
| M1shaaa | social | 4 | PLUS (#b8bb26) |

**Total repo_snapshots:** 1223  
**Total world_increments:** 34

### Notable Repos (Most Active / High Stars)

- **plurigrid/gorj** — Clojure, 1 star, last pushed 2026-08-07 *(this repo!)*
- **plurigrid/place** — TeX, 2 stars, last pushed 2026-08-02
- **plurigrid/asi** — HTML, 59 stars, 13 forks — *"everything is topological chemputer!"*
- **kubeflow/kubeflow** — 15,805 stars, 2,691 forks — flagship ML toolkit for K8s
- **kubeflow/pipelines** — 4,180 stars, 2,081 forks — ML Pipelines
- **kubeflow/spark-operator** — 3,144 stars, 1,511 forks
- **bmorphism/Gay.jl** — Julia, 2 stars, 188 open issues — *wide-gamut color sampling, last pushed 2026-08-07*
- **bmorphism/ocaml-mcp-sdk** — OCaml, 61 stars — *Jane Street OxCaml MCP SDK*
- **bmorphism/anti-bullshit-mcp-server** — JavaScript, 23 stars, 7 forks
- **TeglonLabs/jank-crane** — C++, last pushed 2026-06-08 — *GF3 convergence maps*
- **migalkin/NodePiece** — Python, 144 stars, ICLR'22
- **wasita/xoxowasita-analysis** — last pushed 2026-08-06 *(very recent)*

### GF(3) Color Chain
```
id%3==0 → trit=0  ERGODIC  #d3869b
id%3==1 → trit=1  PLUS     #b8bb26
id%3==2 → trit=-1 MINUS    #cc241d
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets, alice–Z)

All 28 Hamming swarm wallets probed on Aptos mainnet.

| Range | Status |
|-------|--------|
| alice, bob | 0.0 APT each |
| A–Z (26 wallets) | 0.0 APT each |

**Total APT held across swarm: 0.0**  
All wallets exist on-chain (API responded) but hold zero APT balance.

### Multisig Contract Probes (5/5 healthy)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

All 5 multisig contracts require 2-of-N signatures and are responding correctly.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — Next.js SPA, no public REST API endpoint found.  
Paths probed: `/api/markets`, `/api/v1/markets` — both returned HTML (SPA shell).  
No market data could be extracted. `mnx_snapshots` table remains empty.

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments    (34 rows)
├── repo_snapshots      (1223 rows)
├── aptos_snapshots     (28 rows)
├── multisig_probes     (5 rows)
└── mnx_snapshots       (0 rows — SPA unavailable)
```

---

*Sweep completed autonomously. Next sweep will increment the GF3 color chain.*
