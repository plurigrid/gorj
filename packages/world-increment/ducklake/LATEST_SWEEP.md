# World-Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-08-04 03:15:48 UTC  
**Sweep ID:** #12 — GF(3) `ERGODIC` (trit=0, color=`#d3869b`)  
**Hash:** `sweep-2026-04-12`  
**Total sweeps in DB:** 24

---

## JOB 1: GitHub Social Graph Sweep

> **Note:** Session proxy restricts GitHub API to `plurigrid/gorj` scope only.  
> External orgs (kubeflow, TeglonLabs) and user graphs (bmorphism, zubyul, social graph) returned 403 from proxy.  
> Plurigrid org repos captured via GitHub MCP search (100 repos).

### Plurigrid Org Snapshot
**Repos:** 100 | **Total Stars:** 111 | **Total Forks:** 51

#### Top 15 Repos by Stars
| Repo | Language | ⭐ Stars | Forks | Issues | Last Push |
|------|----------|---------|-------|--------|-----------|
| asi | HTML | 58 | 13 | 4 | 2026-07-10 |
| ontology | JavaScript | 8 | 9 | 16 | 2025-05-27 |
| vcg-auction | Rust | 7 | 3 | 1 | 2023-03-16 |
| agent | Python | 5 | 1 | 6 | 2023-03-31 |
| StochFlow | Python | 4 | 1 | 0 | 2024-03-20 |
| microworlds | Rust | 4 | 5 | 3 | 2023-05-13 |
| asi-skills | Julia | 3 | 0 | 0 | 2026-04-26 |
| Plurigraph | JavaScript | 3 | 5 | 4 | 2025-01-05 |
| act | Python | 3 | 1 | 4 | 2024-07-26 |
| zig-syrup | Zig | 2 | 2 | 0 | 2026-07-28 |
| nash-portal | Rust | 2 | 2 | 1 | 2026-05-19 |
| org | Jupyter Notebook | 2 | 0 | 1 | 2023-11-07 |
| grid | TypeScript | 2 | 1 | 1 | 2023-01-02 |
| gorj | Clojure | 1 | 0 | 1614 | 2026-08-04 |
| nanoclj-zig | Zig | 1 | 1 | 20 | 2026-04-25 |

#### Language Breakdown
| Language | Repos | Total Stars |
|----------|-------|-------------|
| n/a | 28 | 0 |
| Rust | 12 | 14 |
| TypeScript | 10 | 3 |
| Clojure | 9 | 2 |
| Python | 8 | 12 |
| HTML | 5 | 59 |
| Scheme | 4 | 0 |
| JavaScript | 3 | 11 |
| Julia | 3 | 3 |
| Hy | 2 | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Wallets queried:** 28 | **Total APT:** 0.0000 APT

All 28 addresses returned 0 APT. The `0x1::coin::CoinStore<AptosCoin>` resource was not found on any address — these accounts likely use the newer Fungible Asset (FA) standard or hold no APT balance. The addresses are reachable on mainnet (API responded with `resource_not_found`, not `account_not_found`).

| World | Address |
|-------|---------|
| alice | `0xc793...4cc7b` |
| bob   | `0x0a3c...512d5d` |
| A–Z   | 26 addresses — all 0.0 APT |

### Multisig Contract Probes (5/5 Healthy)
| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | `0x0da4f428...987003` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ HEALTHY |

All 5 multisig contracts responded with `sigs_required=2`. Network is healthy.

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable — SPA returns HTML for all API paths. No public REST endpoint found.

---

## DuckDB State
| Table | Rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 1044 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
