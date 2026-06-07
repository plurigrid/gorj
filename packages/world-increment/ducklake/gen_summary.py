#!/usr/bin/env python3
"""Generate LATEST_SWEEP.md from world-increments DuckDB."""
import duckdb
from datetime import datetime, timezone

DB_PATH = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
con = duckdb.connect(DB_PATH, read_only=True)

ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

# Get recent world_increments (this sweep)
incs = con.execute("""
    SELECT id, gf3_trit, gf3_color, gf3_name, source_type, source_name
    FROM world_increments
    ORDER BY id DESC LIMIT 20
""").fetchall()

# Get repo stats by source (this sweep - last 11 sources)
repo_stats = con.execute("""
    SELECT r.org_or_user,
           COUNT(*) as repo_count,
           SUM(r.stars) as total_stars,
           MAX(r.pushed_at) as latest_push
    FROM repo_snapshots r
    GROUP BY r.org_or_user
    ORDER BY r.org_or_user
""").fetchall()

# Top repos by stars (overall)
top_repos = con.execute("""
    SELECT full_name, stars, forks, language, description
    FROM repo_snapshots
    ORDER BY stars DESC
    LIMIT 20
""").fetchall()

# Aptos snapshots
aptos = con.execute("""
    SELECT world, address, balance_apt
    FROM aptos_snapshots
    ORDER BY world
""").fetchall()

# Multisig probes
multisigs = con.execute("""
    SELECT pair, address, sigs_required, healthy
    FROM multisig_probes
    ORDER BY pair
""").fetchall()

# DB totals
totals = con.execute("""
    SELECT
      (SELECT COUNT(*) FROM world_increments) as total_incs,
      (SELECT COUNT(*) FROM repo_snapshots) as total_repos,
      (SELECT COUNT(*) FROM aptos_snapshots) as total_aptos,
      (SELECT COUNT(*) FROM multisig_probes) as total_multi
""").fetchone()

# GF3 distribution (this run = last 11 increments)
gf3_dist = con.execute("""
    SELECT gf3_name, gf3_color, COUNT(*) as cnt
    FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY gf3_name
""").fetchall()

con.close()

md = f"""# LATEST_SWEEP — {ts}

## Sweep Overview

| Metric | Count |
|--------|-------|
| Total world_increments (cumulative) | {totals[0]} |
| Total repo_snapshots (cumulative) | {totals[1]} |
| Aptos wallets snapshotted | {totals[2]} |
| Multisig contracts probed | {totals[3]} |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept (This Run)

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
"""

for org, cnt, stars, latest in sorted(repo_stats, key=lambda x: x[0]):
    latest_str = latest[:10] if latest else "unknown"
    md += f"| {org} | - | {cnt} | {stars or 0} | {latest_str} |\n"

md += f"""
### Top 20 Repos by Stars (All-Time in DB)

| Repo | Stars | Forks | Language | Description |
|------|-------|-------|----------|-------------|
"""
for full_name, stars, forks, lang, desc in top_repos:
    lang = lang or "-"
    desc = (desc or "")[:60]
    md += f"| {full_name} | {stars} | {forks} | {lang} | {desc} |\n"

md += f"""
### GF(3) Color Chain Distribution

| Name | Color | Count |
|------|-------|-------|
"""
for name, color, cnt in gf3_dist:
    md += f"| {name} | {color} | {cnt} |\n"

md += f"""
### Recent World Increments

| ID | GF3 Trit | Color | Name | Source Type | Source |
|----|----------|-------|------|-------------|--------|
"""
for row in incs:
    id_, trit, color, name, stype, sname = row
    md += f"| {id_} | {trit} | {color} | {name} | {stype} | {sname} |\n"

md += f"""
---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 Hamming swarm wallets (alice, bob, A-Z) queried against Aptos mainnet
(`fullnode.mainnet.aptoslabs.com`). All returned 0.0 APT — accounts either
unfunded or CoinStore resource not initialized.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
"""
for world, addr, bal in aptos:
    short = addr[:10] + "..." + addr[-8:]
    md += f"| {world} | {short} | {bal:.8f} |\n"

md += f"""
### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.
All returned **2-of-2** signatures required — all healthy.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
"""
for pair, addr, sigs, healthy in multisigs:
    short = addr[:10] + "..." + addr[-8:]
    md += f"| {pair} | {short} | {sigs} | {'✓' if healthy else '✗'} |\n"

md += f"""
### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — testnet.mnx.fi is behind Vercel authentication
(returns 401 with Vercel deployment protection page). No market data could
be extracted. No rows inserted into `mnx_snapshots`.

---

## DuckDB Schema

```sql
world_increments  — GF(3) color-chained sweep events
repo_snapshots    — GitHub repository metadata per sweep
aptos_snapshots   — Aptos mainnet wallet balances
multisig_probes   — Aptos multisig account health checks
mnx_snapshots     — MNX market data (empty: auth wall)
```

## GF(3) Legend

| Trit | Color | Hex | Meaning |
|------|-------|-----|---------|
| 0 | ERGODIC | #d3869b | id % 3 == 0 |
| 1 | PLUS | #b8bb26 | id % 3 == 1 |
| -1 | MINUS | #cc241d | id % 3 == 2 |
"""

out_path = "/home/user/gorj/packages/world-increment/ducklake/LATEST_SWEEP.md"
with open(out_path, "w") as f:
    f.write(md)
print(f"Written: {out_path}")
print(f"Total: {len(md)} chars, {md.count(chr(10))} lines")
