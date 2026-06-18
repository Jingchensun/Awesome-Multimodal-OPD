#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily refresher / generator for Awesome Multimodal On-Policy Distillation.

Reads  : papers.json                      (single source of truth — edit this to add papers)
Fetches: GitHub stars   (GitHub REST API, uses $GITHUB_TOKEN if available)
         Citations+date (Semantic Scholar Graph API, by arXiv id)
Writes : data/stats.json                  (cached numbers, preserved on fetch failure)
         README.md                        (regenerated)
         index.html                       (regenerated interactive page)

Citation note: counts come from Semantic Scholar (free, CI-friendly). Google Scholar
has no public API and blocks datacenter IPs, so it cannot be scraped reliably from
GitHub Actions. Set CITATION_SOURCE=scholar and install `scholarly` to try GS locally.

Run: python scripts/update_stats.py
"""
import json, os, sys, time, html, urllib.request, urllib.error, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers.json")
STATS  = os.path.join(ROOT, "data", "stats.json")
README = os.path.join(ROOT, "README.md")
HTMLF  = os.path.join(ROOT, "index.html")
REPO   = "Jingchensun/Awesome-Multimodal-OPD"
GH_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

def log(*a): print(*a, file=sys.stderr)

def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as f: return json.load(f)
    except Exception: return default

# ---------------- fetchers ----------------
def fetch_citations_dates(ids, prev):
    """Semantic Scholar batch -> {id:{citations,date}}. Falls back to prev on failure."""
    out = {}
    try:
        body = json.dumps({"ids": ["arXiv:" + i for i in ids]}).encode()
        req = urllib.request.Request(
            "https://api.semanticscholar.org/graph/v1/paper/batch?fields=citationCount,publicationDate",
            data=body, headers={"Content-Type": "application/json"})
        data = json.load(urllib.request.urlopen(req, timeout=90))
        for i, d in zip(ids, data):
            cit = (d or {}).get("citationCount")
            pub = (d or {}).get("publicationDate")
            out[i] = {
                "citations": cit if cit is not None else prev.get(i, {}).get("citations"),
                "date": pub or prev.get(i, {}).get("date") or date_from_id(i),
            }
    except Exception as e:
        log("Semantic Scholar fetch failed:", e, "-> keeping previous citations/dates")
        for i in ids:
            out[i] = {"citations": prev.get(i, {}).get("citations"),
                      "date": prev.get(i, {}).get("date") or date_from_id(i)}
    return out

def fetch_stars(repo, prev_val):
    if not repo: return None
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "opd-refresher"}
    if GH_TOKEN: headers["Authorization"] = "Bearer " + GH_TOKEN
    try:
        req = urllib.request.Request("https://api.github.com/repos/" + repo, headers=headers)
        d = json.load(urllib.request.urlopen(req, timeout=30))
        return d.get("stargazers_count", prev_val)
    except Exception as e:
        log(f"stars fetch failed for {repo}: {e} -> keeping previous")
        return prev_val

def date_from_id(i):
    return f"20{i[:2]}-{i[2:4]}"

# ---------------- helpers ----------------
def human(n):
    if n is None: return "—"
    if n >= 1000: return f"{n/1000:.1f}k".replace(".0k", "k")
    return str(n)

def arxiv_url(i): return f"https://arxiv.org/abs/{i}"

# ---------------- main refresh ----------------
def refresh():
    src = load_json(PAPERS, None)
    if not src: log("papers.json missing"); sys.exit(1)
    papers = src["papers"]
    prev = load_json(STATS, {})
    ids = [p["id"] for p in papers]

    cd = fetch_citations_dates(ids, prev)
    stats = {}
    for p in papers:
        i, repo = p["id"], p.get("repo")
        stars = fetch_stars(repo, prev.get(i, {}).get("stars")) if repo else None
        stats[i] = {"stars": stars,
                    "citations": cd[i]["citations"],
                    "date": cd[i]["date"]}
        time.sleep(0.05)
    stats["_updated"] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    os.makedirs(os.path.dirname(STATS), exist_ok=True)
    with open(STATS, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    return src, stats

# ---------------- README ----------------
def build_readme(src, stats):
    cats = src["categories"]; papers = src["papers"]
    by = {c["key"]: [] for c in cats}
    for p in papers: by[p["category"]].append(p)
    for k in by: by[k].sort(key=lambda p: -(stats.get(p["id"], {}).get("citations") or -1))
    total = len(papers)
    nweb = sum(1 for p in papers if p["id"] in ("2412.01694", "2508.04416", "2603.21426"))
    updated = stats.get("_updated", "")
    preview = f"https://htmlpreview.github.io/?https://github.com/{REPO}/blob/main/index.html"
    pages = f"https://{REPO.split('/')[0].lower()}.github.io/{REPO.split('/')[1]}/"

    L = []; w = L.append
    w("# 🖼️ Awesome Multimodal On-Policy Distillation")
    w("")
    w("> A curated, **auto-refreshed** list of **multimodal On-Policy Distillation (OPD / OPSD)** papers — "
      "organized by **Image QA · Video QA · Audio QA** (plus generation, speculative decoding, and embodied/VLA).")
    w("")
    w(f"![papers](https://img.shields.io/badge/papers-{total}-4E6813?style=for-the-badge) "
      f"![web--added](https://img.shields.io/badge/web--added-{nweb}-2E86C1?style=for-the-badge) "
      f"![updated](https://img.shields.io/badge/stats_updated-{updated.split(' ')[0].replace('-', '.')}-purple?style=for-the-badge)")
    w("")
    w(f"### 👉 [**Browse interactively (HTML)**]({preview})")
    w("")
    w(f"Open the searchable, filterable visual reader — one click, no install: **[{preview}]({preview})**  ")
    w(f"(If GitHub Pages is enabled for this repo, it is also served at [{pages}]({pages}).)")
    w("")
    w("Compiled by filtering the multimodal entries of three awesome lists and augmented with web search: "
      "[thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD) · "
      "[chrisliu298/awesome-on-policy-distillation](https://github.com/chrisliu298/awesome-on-policy-distillation) · "
      "[nick7nlp/Awesome-LLM-On-Policy-Distillation](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation).")
    w("")
    w("**What is OPD?** `C1`: the student samples its own trajectories `y ~ π_student(·|x)` during training; "
      "`C2`: a teacher provides per-token / sequence-level supervision on those **student-generated** samples. "
      "**OPSD** is the special case where the teacher is the *same model* conditioned on privileged information.")
    w("")
    w("Each paper is summarized along **four questions**: ① Problem & why it matters · ② Method & key contribution · "
      "③ Task / dataset / model · ④ Limitations & future work. ⭐ Stars and Citations are **refreshed daily** by "
      "[a GitHub Action](.github/workflows/refresh.yml).")
    w("")
    w(f"> 🔄 **Stats last updated: {updated}** · ⭐ stars via GitHub API · Citations via Semantic Scholar "
      "(Google Scholar has no public API and is blocked in CI; see [`scripts/update_stats.py`](scripts/update_stats.py)).")
    w("")
    # overview
    w("## 📊 Overview")
    w("")
    w("| Subfield | # |")
    w("| :-- | :--: |")
    for c in cats: w(f"| {c['title']} | {len(by[c['key']])} |")
    w(f"| **Total** | **{total}** |")
    w("")
    # sections
    for c in cats:
        w(f"## {c['title']}")
        w("")
        w(c["desc"])
        w("")
        w("| Paper | arXiv | Date | Code | ⭐ Stars | Citations | Type |")
        w("| :-- | :--: | :--: | :--: | :--: | :--: | :--: |")
        for p in by[c["key"]]:
            s = stats.get(p["id"], {})
            web = "🔎 " if p["id"] in ("2412.01694","2508.04416","2603.21426") else ""
            ttl = p["title"].replace("|", "/")
            repo = p.get("repo")
            code = f"[GitHub](https://github.com/{repo})" if repo else "—"
            stars = human(s.get("stars")) if repo else "—"
            cit = s.get("citations"); cit = str(cit) if cit is not None else "—"
            w(f"| {web}{ttl} | [link]({arxiv_url(p['id'])}) | {s.get('date','—')} | {code} | {stars} | {cit} | {p['strict']} |")
        w("")
        for p in by[c["key"]]:
            s = stats.get(p["id"], {}); web = "🔎 " if p["id"] in ("2412.01694","2508.04416","2603.21426") else ""
            repo = p.get("repo")
            links = f"[arXiv]({arxiv_url(p['id'])})" + (f" · [code](https://github.com/{repo})" if repo else "")
            meta = f"`{p['venue']}` · 📅 {s.get('date','—')} · {links}"
            if repo: meta += f" · ⭐ {human(s.get('stars'))}"
            cit = s.get('citations'); meta += f" · cited {cit if cit is not None else '—'} · `{p['strict']}`"
            w("<details>")
            w(f"<summary><b>{web}{p['title']}</b></summary>")
            w("")
            w(meta)
            w("")
            w(f"- **① Problem & importance**: {p['q1']}")
            w(f"- **② Method & contribution**: {p['q2']}")
            w(f"- **③ Task / dataset / model**: {p['q3']}")
            w(f"- **④ Limitations & future work**: {p['q4']}")
            w("")
            w("</details>")
            w("")
        w("")
    w("## 🙏 Acknowledgments & Notes")
    w("")
    w("- Paper sources and four-point summaries are compiled from the three source awesome lists, the papers' arXiv "
      "abstracts, and public materials; errors are possible — **please refer to the original papers**.")
    w("- 🔎 Web-added entries: [AoTD](https://arxiv.org/abs/2412.01694) · "
      "[VITAL / Thinking With Videos](https://arxiv.org/abs/2508.04416) · "
      "[β-KD (Uncertainty-Aware KD, CVPR 2026)](https://arxiv.org/abs/2603.21426).")
    w("- ⭐ stars and citations auto-update daily via GitHub Actions; numbers are a snapshot and change over time.")
    w("- To add a paper: edit [`papers.json`](papers.json) and the table/HTML regenerate automatically.")
    w("")
    w("## 📄 License")
    w("")
    w("[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) "
      "Released under CC0 (public-domain dedication).")
    w("")
    with open(README, "w", encoding="utf-8") as f: f.write("\n".join(L))
    log("wrote README.md")

# ---------------- HTML ----------------
def build_html(src, stats):
    cats = src["categories"]; papers = src["papers"]
    by = {c["key"]: [] for c in cats}
    for p in papers: by[p["category"]].append(p)
    for k in by: by[k].sort(key=lambda p: -(stats.get(p["id"], {}).get("citations") or -1))
    updated = stats.get("_updated", "")
    total = len(papers)

    def esc(s): return html.escape(s or "", quote=True)
    def t(en, zh):
        return f'<span class="i18n" data-en="{esc(en)}" data-zh="{esc(zh)}">{esc(en)}</span>'

    QL = [("q1","① Problem & importance","① 问题与重要性"),
          ("q2","② Method & contribution","② 方法与贡献"),
          ("q3","③ Task / dataset / model","③ 任务 / 数据集 / 模型"),
          ("q4","④ Limitations & future","④ 局限与未来")]

    def card(p):
        s = stats.get(p["id"], {}); idv = p["id"]; repo = p.get("repo")
        web = '<span class="src-web">🔎 web</span>' if idv in ("2412.01694","2508.04416","2603.21426") else ""
        b = [f'<a class="b b-arxiv" href="{arxiv_url(idv)}" target="_blank">arXiv {idv}</a>',
             f'<span class="b b-date">📅 {s.get("date","—")}</span>',
             f'<span class="b b-venue">{esc(p["venue"])}</span>',
             f'<span class="b b-cite">🔖 {t("cited","被引")} {s.get("citations") if s.get("citations") is not None else "—"}</span>']
        if repo:
            b.append(f'<a class="b b-gh" href="https://github.com/{repo}" target="_blank">⭐ {human(s.get("stars"))} · {esc(repo)}</a>')
        else:
            b.append(f'<span class="b b-nogh">📄 {t("paper-only","暂无代码")}</span>')
        b.append(f'<span class="b b-strict">{t(p.get("strict","OPD"), p.get("strict_zh") or p.get("strict","OPD"))}</span>')
        qrows = "".join(
            f'<p><b class="q {qk}">{t(en,zh)}</b>{t(p.get(qk,""), p.get(qk+"_zh",""))}</p>'
            for qk,en,zh in QL)
        hay = (p["title"]+" "+p["sub"]+" "+p["venue"]+" "+idv+" "+(repo or "")
               +p["q1"]+p["q2"]+p["q3"]+p["q4"]
               +p.get("q1_zh","")+p.get("q2_zh","")+p.get("q3_zh","")+p.get("q4_zh","")).lower()
        return (f'<div class="card" data-hay="{esc(hay)}"><div class="card-head">'
                f'<h3>{esc(p["title"])}{web}</h3><span class="tag">{esc(p["sub"])}</span></div>'
                f'<div class="badges">{"".join(b)}</div><div class="qa">{qrows}</div></div>')

    nav = "".join(f'<a href="#{c["key"]}">{t(c["title"], c["title_zh"])}</a>' for c in cats)
    secs = []
    for c in cats:
        cards = "\n".join(card(p) for p in by[c["key"]])
        secs.append(f'<section id="{c["key"]}"><div class="sec-head"><h2>{t(c["title"], c["title_zh"])} '
                    f'<span class="count">{len(by[c["key"]])}</span></h2>'
                    f'<p class="sec-desc">{t(c["desc"], c["desc_zh"])}</p></div><div class="grid">{cards}</div></section>')

    head_sub = t(f"{total} multimodal OPD/OPSD papers · Image QA · Video QA · Audio QA · generation · speculative decoding · embodied/VLA. Each summarized by four questions, with arXiv date, GitHub stars and citations.",
                 f"{total} 篇多模态 OPD/OPSD 论文 · 图像/视频/语音问答 · 生成 · 投机解码 · 具身/VLA。每篇四问速览，含 arXiv 日期、GitHub Star 与被引数。")
    upd = t(f"Stats last updated: {updated} · stars via GitHub API · citations via Semantic Scholar",
            f"数据更新于：{updated} · Star 来自 GitHub API · 被引来自 Semantic Scholar")
    doc = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome Multimodal On-Policy Distillation</title><style>
:root{{--bg:#0e1116;--card:#181d26;--bd:#2a3240;--fg:#e6e9ef;--mut:#9aa6b8;--acc:#7aa2ff;--acc2:#9b8cff}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font-family:-apple-system,"PingFang SC","Microsoft YaHei","Segoe UI",Roboto,Arial,sans-serif;line-height:1.7;font-size:15px}}
header{{padding:32px 22px 16px;border-bottom:1px solid var(--bd);background:linear-gradient(180deg,#14202a,#0e1116)}}
header h1{{margin:0 0 6px;font-size:25px}}header p{{margin:4px 0;color:var(--mut);font-size:13.5px}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 18px 80px}}
.toolbar{{position:sticky;top:0;z-index:20;background:rgba(14,17,22,.92);backdrop-filter:blur(8px);padding:12px 18px;border-bottom:1px solid var(--bd)}}
.toolrow{{display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
#q{{flex:1;min-width:240px;max-width:520px;padding:10px 14px;border-radius:10px;border:1px solid var(--bd);background:#11161f;color:var(--fg);font-size:14px}}
#lang{{padding:9px 14px;border-radius:10px;border:1px solid var(--bd);background:#1a2440;color:#cfe0ff;font-size:13px;cursor:pointer;white-space:nowrap}}
#lang:hover{{border-color:var(--acc)}}
.nav{{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}}
.nav a{{font-size:12.5px;color:var(--mut);text-decoration:none;border:1px solid var(--bd);padding:4px 9px;border-radius:20px;background:#11161f}}
.nav a:hover{{color:var(--fg);border-color:var(--acc)}}
section{{margin:28px 0 10px;scroll-margin-top:130px}}.sec-head h2{{font-size:18.5px;margin:0 0 2px}}
.count{{font-size:12px;color:var(--mut);font-weight:400;border:1px solid var(--bd);border-radius:12px;padding:1px 8px;margin-left:6px}}
.sec-desc{{color:var(--mut);font-size:13px;margin:0 0 14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(430px,1fr));gap:14px}}
.card{{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:15px 16px}}
.card:hover{{border-color:#3a4761}}.card-head{{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}}
.card-head h3{{margin:0;font-size:15px;line-height:1.4}}
.tag{{flex:none;font-size:11px;color:var(--acc2);border:1px solid #3a3560;background:#1c1930;border-radius:8px;padding:2px 8px;white-space:nowrap}}
.badges{{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 12px}}
.b{{font-size:11.5px;padding:3px 8px;border-radius:7px;text-decoration:none;border:1px solid var(--bd);color:var(--fg);white-space:nowrap}}
.b-arxiv{{background:#19233a;border-color:#2e4470;color:#bcd0ff}}.b-venue{{background:#1d2433;color:var(--mut)}}
.b-date{{background:#16231d;border-color:#2f5a3e;color:#a8e6c0}}
.b-cite{{background:#23201a;border-color:#5a4a2a;color:#ffd9a0}}.b-gh{{background:#161b22;border-color:#33415c;color:#cbd5e6;max-width:100%;overflow:hidden;text-overflow:ellipsis}}
.b-nogh{{background:#1b1f27;color:var(--mut)}}.b-strict{{background:#241a26;border-color:#5a3a5e;color:#e6a9e0}}
.qa p{{margin:0 0 9px;font-size:13.3px;color:#d7dce6}}.qa .q{{display:block;font-size:11.5px;margin-bottom:1px}}
.q1{{color:#7ad6a0}}.q2{{color:#7aa2ff}}.q3{{color:#e6b673}}.q4{{color:#e08aa0}}
.src-web{{font-size:10px;color:#9ec5ff;border:1px solid #2e4470;background:#16203a;border-radius:6px;padding:1px 6px;margin-left:7px}}
footer{{color:var(--mut);font-size:12.5px;text-align:center;padding:30px 18px;border-top:1px solid var(--bd)}}a{{color:var(--acc)}}.hidden{{display:none!important}}
@media(max-width:700px){{.grid{{grid-template-columns:1fr}}}}
</style></head><body>
<header><div class="wrap" style="padding-bottom:0">
<h1>🖼️ Awesome Multimodal On-Policy Distillation</h1>
<p>{head_sub}</p>
<p style="font-size:12.5px">🔄 {upd} · <a href="https://github.com/{REPO}" target="_blank">{t("source repo","源仓库")}</a></p>
</div></header>
<div class="toolbar"><div class="wrap" style="padding:0"><div class="toolrow">
<input id="q"><button id="lang">🌐 中文</button></div><div class="nav">{nav}</div>
</div></div>
<div class="wrap">{"".join(secs)}</div>
<footer>{t("Auto-generated from papers.json · stats refreshed daily by GitHub Actions · refer to original papers for details","由 papers.json 自动生成 · 数据由 GitHub Actions 每日刷新 · 详情以原论文为准")}</footer>
<script>
const PH={{en:"🔍 filter by keyword (VQA / video / dataset / model / arXiv id…)",zh:"🔍 关键词过滤（VQA / 视频 / 数据集 / 模型 / arXiv 号…）"}};
let lang=localStorage.getItem('opd_lang')||'en';
function applyLang(){{
  document.documentElement.lang = (lang==='zh'?'zh-CN':'en');
  document.querySelectorAll('.i18n').forEach(e=>{{e.textContent=e.dataset[lang]||e.dataset.en;}});
  document.getElementById('q').placeholder=PH[lang];
  document.getElementById('lang').textContent = lang==='en' ? '🌐 中文' : '🌐 EN';
  localStorage.setItem('opd_lang',lang);
}}
document.getElementById('lang').addEventListener('click',()=>{{lang=(lang==='en'?'zh':'en');applyLang();}});
const q=document.getElementById('q');
q.addEventListener('input',()=>{{const v=q.value.trim().toLowerCase();
document.querySelectorAll('.card').forEach(c=>c.classList.toggle('hidden',v&&!c.dataset.hay.includes(v)));
document.querySelectorAll('section').forEach(s=>{{const a=[...s.querySelectorAll('.card')].some(c=>!c.classList.contains('hidden'));s.classList.toggle('hidden',v&&!a);}});}});
applyLang();
</script></body></html>"""
    with open(HTMLF, "w", encoding="utf-8") as f: f.write(doc)
    log("wrote index.html")


def main():
    src, stats = refresh()
    build_readme(src, stats)
    build_html(src, stats)
    n = sum(1 for k in stats if k != "_updated")
    log(f"done: {n} papers, updated {stats.get('_updated')}")

if __name__ == "__main__":
    main()
