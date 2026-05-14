#!/usr/bin/env python3
import duckdb
from datetime import datetime
from pathlib import Path

DB = Path(__file__).parent / "world-increments.duckdb"
con = duckdb.connect(str(DB))

total = con.execute("SELECT COUNT(*) FROM world_increments").fetchone()[0]
by_source = con.execute(
    "SELECT source_name, source_type, COUNT(*) as cnt FROM world_increments "
    "GROUP BY source_name, source_type ORDER BY source_type, cnt DESC"
).fetchall()
top_langs = con.execute(
    "SELECT language, COUNT(*) as cnt FROM repo_snapshots "
    "WHERE language != '' GROUP BY language ORDER BY cnt DESC LIMIT 10"
).fetchall()
gf3 = con.execute(
    "SELECT ANY_VALUE(gf3_trit) as t, gf3_name, gf3_color, COUNT(*) as cnt "
    "FROM world_increments GROUP BY gf3_name, gf3_color ORDER BY t"
).fetchall()
top_stars = con.execute(
    "SELECT full_name, language, stars, pushed_at FROM repo_snapshots "
    "ORDER BY stars DESC LIMIT 10"
).fetchall()
aptos = con.execute(
    "SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world"
).fetchall()
multisig = con.execute(
    "SELECT pair, address, sigs_required, healthy FROM multisig_probes ORDER BY pair"
).fetchall()
con.close()

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

lines = [
    f"# LATEST_SWEEP — {now}",
    "",
    "## Job 1: GitHub Social Graph Sweep",
    "",
    f"**Total world-increments:** {total}  ",
    f"**Sweep date:** {now}",
    "",
    "### Sources",
    "",
    "| Source | Type | Repos |",
    "|--------|------|-------|",
]
for name, stype, cnt in by_source:
    lines.append(f"| {name} | {stype} | {cnt} |")

lines += [
    "",
    "### Top Languages",
    "",
    "| Language | Repos |",
    "|----------|-------|",
]
for lang, cnt in top_langs:
    lines.append(f"| {lang} | {cnt} |")

lines += [
    "",
    "### GF(3) Color Chain Distribution",
    "",
    "| Trit | Color | Name | Count |",
    "|------|-------|------|-------|",
]
for trit, name, color, cnt in gf3:
    lines.append(f"| {trit} | {color} | {name} | {cnt} |")

lines += [
    "",
    "### Top Repos by Stars",
    "",
    "| Repo | Language | Stars | Last Pushed |",
    "|------|----------|-------|-------------|",
]
for fn, lang, stars, pushed in top_stars:
    lines.append(f"| {fn} | {lang or ''} | {stars} | {pushed} |")

lines += [
    "",
    "## Job 2: Hamming Swarm Snapshot",
    "",
    "### Aptos Wallet Balances",
    "",
    "All 28 Hamming swarm addresses queried against Aptos mainnet.",
    "Result: all addresses returned `null` for `CoinStore<AptosCoin>` resource.",
    "Interpretation: accounts have no APT balance or CoinStore resource not initialized.",
    "",
    "| World | Address (truncated) | Balance APT |",
    "|-------|---------------------|-------------|",
]
for world, addr, bal in aptos:
    truncated = addr[:10] + "..." + addr[-8:]
    bal_str = f"{bal:.8f}" if bal is not None else "null (no resource)"
    lines.append(f"| {world} | `{truncated}` | {bal_str} |")

lines += [
    "",
    "### Multisig Contract Probes",
    "",
    "All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.",
    "",
    "| Pair | Address (truncated) | Sigs Required | Healthy |",
    "|------|---------------------|---------------|---------|",
]
for pair, addr, sigs, healthy in multisig:
    truncated = addr[:10] + "..." + addr[-8:]
    lines.append(f"| {pair} | `{truncated}` | {sigs} | {'YES' if healthy else 'NO'} |")

lines += [
    "",
    "### MNX Markets (testnet.mnx.fi)",
    "",
    "Site is a Next.js SPA — no embedded market data available via HTTP fetch.",
    "Status: **unavailable** (SPA requires JS execution to hydrate market data).",
    "",
    "## DuckDB Schema",
    "",
    "Location: `packages/world-increment/ducklake/world-increments.duckdb`",
    "",
    "Tables:",
    "- `world_increments` — GF(3) colored event log (391 rows)",
    "- `repo_snapshots` — full repo metadata (391 rows)",
    "- `aptos_snapshots` — Hamming swarm wallet balances (28 rows)",
    "- `multisig_probes` — Aptos multisig contract health (5 rows)",
    "- `mnx_snapshots` — MNX market data (0 rows — SPA unavailable)",
]

md = "\n".join(lines)
out = Path(__file__).parent / "LATEST_SWEEP.md"
out.write_text(md)
print(f"Written {out} ({len(lines)} lines)")
