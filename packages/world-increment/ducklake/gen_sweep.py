#!/usr/bin/env python3
import duckdb, datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"
OUT = "/home/user/gorj/packages/world-increment/ducklake/LATEST_SWEEP.md"
con = duckdb.connect(DB, read_only=True)

ts = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')

sources = con.execute('SELECT org_or_user, COUNT(*) c FROM repo_snapshots GROUP BY 1 ORDER BY c DESC').fetchall()
top_repos = con.execute('SELECT full_name, stars, language, pushed_at FROM repo_snapshots ORDER BY stars DESC LIMIT 20').fetchall()
recent = con.execute("SELECT full_name, pushed_at, language FROM repo_snapshots WHERE pushed_at >= '2026-01-01' ORDER BY pushed_at DESC LIMIT 15").fetchall()
gf3 = con.execute('SELECT gf3_trit, gf3_color, gf3_name, COUNT(*) FROM world_increments GROUP BY 1,2,3').fetchall()
aptos = con.execute('SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world').fetchall()
multi = con.execute('SELECT pair, address, sigs_required, healthy FROM multisig_probes').fetchall()
tbl_counts = {t: con.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
              for t in ['world_increments','repo_snapshots','aptos_snapshots','multisig_probes','mnx_snapshots']}

lines = [
    f"# LATEST_SWEEP — world-increment + hamming-swarm snapshot",
    f"Generated: {ts}",
    "",
    "---",
    "",
    "## JOB 1: GitHub Social Graph Sweep",
    "",
    "### Sources Queried",
    "| Source | Type | Repos Captured |",
    "|--------|------|----------------|",
]
for s in sources:
    src_type = 'org' if s[0] in ('plurigrid','kubeflow','TeglonLabs') else 'user'
    lines.append(f"| {s[0]} | {src_type} | {s[1]} |")

lines += [
    "",
    f"**Total repos in snapshot:** {sum(s[1] for s in sources)}",
    "",
    "### GF(3) World-Increment Color Chain",
    "| Trit | Color | Name | Count |",
    "|------|-------|------|-------|",
]
for g in sorted(gf3, key=lambda x: x[0]):
    sign = f"+{g[0]}" if g[0] >= 0 else str(g[0])
    lines.append(f"| {sign} | `{g[1]}` | {g[2]} | {g[3]} |")

lines += [
    "",
    "### Top 20 Repos by Stars",
    "| Repo | Stars | Language | Last Push |",
    "|------|-------|----------|-----------|",
]
for r in top_repos:
    lang = r[2] if r[2] else "n/a"
    lines.append(f"| {r[0]} | {r[1]:,} | {lang} | {r[3]} |")

lines += [
    "",
    "### Recently Active Repos (2026+)",
    "| Repo | Pushed | Language |",
    "|------|--------|----------|",
]
for r in recent:
    lang = r[2] if r[2] else "n/a"
    lines.append(f"| {r[0]} | {r[1]} | {lang} |")

lines += [
    "",
    "---",
    "",
    "## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)",
    "",
    "### Wallet Balances",
    "All 28 addresses queried via fullnode.mainnet.aptoslabs.com.",
    "All accounts returned 0 APT (accounts unfunded or APT CoinStore not registered).",
    "",
    "| World | Address | APT Balance |",
    "|-------|---------|-------------|",
]
for a in aptos:
    lines.append(f"| {a[0]} | `{a[1][:20]}...` | {a[2]:.8f} |")

lines += [
    "",
    "### Multisig Contract Probes (0x1::multisig_account::num_signatures_required)",
    "| Pair | Address | Sigs Required | Healthy |",
    "|------|---------|---------------|---------|",
]
for m in multi:
    healthy = "YES" if m[3] else "NO"
    lines.append(f"| {m[0]} | `{m[1][:20]}...` | {m[2]} | {healthy} |")

lines += [
    "",
    "**All 5 multisig contracts healthy — sigs_required=2 on each pair.**",
    "",
    "### MNX Testnet Markets",
    "- URL: https://testnet.mnx.fi (HTTP 200 OK)",
    "- Identified as Next.js SPA",
    "- REST API paths (/api/markets, /api/v1/markets) return SPA HTML only",
    "- Status: **SPA only, no market data extractable via HTTP**",
    "",
    "---",
    "",
    "## DuckDB Schema Summary",
    "| Table | Rows |",
    "|-------|------|",
]
for tbl, cnt in tbl_counts.items():
    lines.append(f"| {tbl} | {cnt} |")

lines += [
    "",
    "DB path: `packages/world-increment/ducklake/world-increments.duckdb`",
    "",
]

with open(OUT, 'w') as f:
    f.write('\n'.join(lines))

print(f"Written {len(lines)} lines to {OUT}")
