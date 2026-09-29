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
import json, os, re, sys, time, html, urllib.request, urllib.error, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPERS = os.path.join(ROOT, "papers.json")
STATS  = os.path.join(ROOT, "data", "stats.json")
README = os.path.join(ROOT, "README.md")
HTMLF  = os.path.join(ROOT, "index.html")
REPO   = "Jingchensun/Awesome-Multimodal-OPD"
GH_TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
WEB_IDS = ("2412.01694", "2508.04416")  # entries added via web search (not in source repos)

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
        for attempt in range(4):  # the keyless endpoint is often rate-limited (429)
            try:
                data = json.load(urllib.request.urlopen(req, timeout=90)); break
            except urllib.error.HTTPError as e:
                if e.code != 429 or attempt == 3: raise
                time.sleep(20 * (attempt + 1))
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
        log(f"stars API failed for {repo}: {e} -> trying repo page")
    # fallback: read the counter from the repo page (no API rate limit; handy for local runs)
    try:
        req = urllib.request.Request("https://github.com/" + repo, headers={"User-Agent": "Mozilla/5.0"})
        page = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
        m = re.search(r'id="repo-stars-counter-star"[^>]*title="([\d,]+)"', page)
        if m: return int(m.group(1).replace(",", ""))
    except Exception as e:
        log(f"stars page failed for {repo}: {e} -> keeping previous")
    return prev_val

def date_from_id(i):
    return f"20{i[:2]}-{i[2:4]}"

# ---------------- helpers ----------------
def human(n):
    if n is None: return "—"
    if n >= 1000: return f"{n/1000:.1f}k".replace(".0k", "k")
    return str(n)

def arxiv_url(i): return f"https://arxiv.org/abs/{i}"

def rank_key(stats):
    """Sort key: GitHub stars (high -> low), then citations, then date. Paper-only entries go last."""
    def key(p):
        s = stats.get(p["id"], {})
        stars = s.get("stars") if p.get("repo") else None
        return (-1 if stars is None else stars, s.get("citations") or 0, s.get("date") or "")
    return key

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
                    "date": p.get("date") or cd[i]["date"]}  # arXiv date in papers.json wins
        time.sleep(0.05)
    stats["_updated"] = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    os.makedirs(os.path.dirname(STATS), exist_ok=True)
    with open(STATS, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    return src, stats

# ---------------- README ----------------
TOP_N = 10  # size of the cross-domain "most starred" table

def build_readme(src, stats):
    cats = src["categories"]; papers = src["papers"]
    by = {c["key"]: [] for c in cats}
    for p in papers: by[p["category"]].append(p)
    for k in by: by[k].sort(key=rank_key(stats), reverse=True)  # most-starred first
    total = len(papers)
    ncode = sum(1 for p in papers if p.get("repo"))
    updated = stats.get("_updated", "")
    preview = f"https://htmlpreview.github.io/?https://github.com/{REPO}/blob/main/index.html"
    pages = f"https://{REPO.split('/')[0].lower()}.github.io/{REPO.split('/')[1]}/"
    short = {c["key"]: c.get("short") or c["title"] for c in cats}

    def cell(x): return (x or "—").replace("|", "/")
    def paper_cell(p):
        web = " 🔎" if p["id"] in WEB_IDS else ""
        return f"[{cell(p['title'])}]({arxiv_url(p['id'])}){web}"
    def code_cell(p):
        s = stats.get(p["id"], {})
        return f"[⭐ {human(s.get('stars'))}](https://github.com/{p['repo']})"
    def cites(p):
        c = stats.get(p["id"], {}).get("citations")
        return str(c) if c is not None else "—"
    def date(p): return stats.get(p["id"], {}).get("date") or "—"

    L = []; w = L.append
    w('<h1 align="center">Awesome Multimodal On-Policy Distillation</h1>')
    w("")
    w('<p align="center">Multimodal <b>OPD / OPSD</b> papers across image, video, audio, generation and embodied AI —<br>'
      'ranked by GitHub stars, refreshed every day.</p>')
    w("")
    w('<p align="center">')
    w(f'  <a href="{pages}"><img src="https://img.shields.io/badge/Interactive_reader-EN_%2F_%E4%B8%AD%E6%96%87-1f6feb?style=flat-square" alt="Interactive reader"></a>')
    w(f'  <img src="https://img.shields.io/badge/papers-{total}-4E6813?style=flat-square" alt="papers">')
    w(f'  <img src="https://img.shields.io/badge/with_code-{ncode}-2E86C1?style=flat-square" alt="with code">')
    w(f'  <img src="https://img.shields.io/badge/updated-{updated.split(" ")[0].replace("-", ".")}-purple?style=flat-square" alt="updated">')
    w('</p>')
    w("")
    w('<p align="center">')
    w("  " + " · ".join(f'<a href="#{c["key"]}">{short[c["key"]]} ({len(by[c["key"]])})</a>' for c in cats))
    w('</p>')
    w("")
    w("> **On-policy distillation (OPD)** — the student learns from *its own* rollouts `y ~ π_student(·|x)`, "
      "while a teacher scores or corrects those student-generated samples. "
      "**OPSD** is the self-distillation case: the teacher is the same model, given privileged information.")
    w("")
    w(f"Search, filter and read a four-point summary of every paper in the **[interactive reader]({pages})** "
      f"([mirror]({preview})).")
    w("")
    top = sorted([p for p in papers if p.get("repo") and stats.get(p["id"], {}).get("stars") is not None],
                 key=rank_key(stats), reverse=True)[:TOP_N]
    if top:
        w("## 🔥 Most starred")
        w("")
        w("| # | Paper | Domain | Affiliation | Code |")
        w("| :-: | :-- | :-- | :-- | :-: |")
        for n, p in enumerate(top, 1):
            w(f"| {n} | {paper_cell(p)} | {short[p['category']]} | {cell(p.get('affiliation'))} | {code_cell(p)} |")
        w("")
    for c in cats:
        ps = by[c["key"]]
        coded = [p for p in ps if p.get("repo")]
        plain = sorted([p for p in ps if not p.get("repo")], key=lambda p: (date(p), p["id"]), reverse=True)
        w(f'<h2 id="{c["key"]}">{c["title"]}</h2>')
        w("")
        w(f"{c['desc']} **{len(ps)} papers**, {len(coded)} with code.")
        w("")
        if coded:
            w("| Paper | Affiliation | Date | Code | Cited |")
            w("| :-- | :-- | :-: | :-: | :-: |")
            for p in coded:
                w(f"| {paper_cell(p)} | {cell(p.get('affiliation'))} | {date(p)} | {code_cell(p)} | {cites(p)} |")
            w("")
        if plain:
            w("<details>")
            w(f"<summary>📄 {len(plain)} more without public code (newest first)</summary>")
            w("")
            w("| Paper | Affiliation | Date | Cited |")
            w("| :-- | :-- | :-: | :-: |")
            for p in plain:
                w(f"| {paper_cell(p)} | {cell(p.get('affiliation'))} | {date(p)} | {cites(p)} |")
            w("")
            w("</details>")
            w("")
    w("## Contributing")
    w("")
    w("Add an entry to [`papers.json`](papers.json) and open a PR. `README.md` and `index.html` are generated by "
      "[`scripts/update_stats.py`](scripts/update_stats.py), so please do not edit them by hand. "
      "Stars come from the GitHub API and citations from Semantic Scholar, refreshed daily by "
      "[a GitHub Action](.github/workflows/refresh.yml)"
      + (f" (last run: {updated})." if updated else "."))
    w("")
    w("## Acknowledgments")
    w("")
    w("Seeded from [thinkwee/AwesomeOPD](https://github.com/thinkwee/AwesomeOPD), "
      "[chrisliu298/awesome-on-policy-distillation](https://github.com/chrisliu298/awesome-on-policy-distillation) and "
      "[nick7nlp/Awesome-LLM-On-Policy-Distillation](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation), "
      "then extended with arXiv search (🔎 marks entries found by web search). "
      "Summaries are paraphrased from abstracts and may contain errors — the papers are the reference.")
    w("")
    w("## License")
    w("")
    w("[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) — public-domain dedication.")
    w("")
    with open(README, "w", encoding="utf-8") as f: f.write("\n".join(L))
    log("wrote README.md")

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome Multimodal On-Policy Distillation</title>
<style>
:root{--bg:#fafaf9;--panel:#fff;--line:#e5e5e2;--fg:#1c1c1a;--mut:#6b6b66;--acc:#2f5fd0;--soft:#f1f1ee;--star:#9a6700}
@media (prefers-color-scheme:dark){:root{--bg:#0f1115;--panel:#161920;--line:#262a33;--fg:#e7e9ee;--mut:#949aa8;--acc:#8ab0ff;--soft:#1d212a;--star:#e3b341}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Microsoft YaHei",Roboto,Arial,sans-serif}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:980px;margin:0 auto;padding:0 20px}
header{padding:44px 0 22px}
header h1{margin:0 0 8px;font-size:26px;letter-spacing:-.01em}
header p{margin:0;color:var(--mut);max-width:70ch}
.facts{margin-top:12px;font-size:13px;color:var(--mut)}
.facts b{color:var(--fg);font-weight:600}
.bar{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:12px 0}
.row1{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
#q{flex:1;min-width:200px;padding:8px 12px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--fg);font:inherit;font-size:14px}
#q:focus{outline:2px solid var(--acc);outline-offset:-1px}
select,button,.check{font:inherit;font-size:13px;padding:7px 11px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--fg);cursor:pointer}
.check{display:inline-flex;gap:6px;align-items:center;user-select:none}
.check input{margin:0}
.tabs{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.tab{padding:5px 12px;border-radius:999px;color:var(--mut)}
.tab[aria-pressed="true"]{background:var(--fg);color:var(--bg);border-color:var(--fg)}
.tab .n{opacity:.65;margin-left:4px;font-variant-numeric:tabular-nums}
section{margin:30px 0 0}
section>h2{margin:0;font-size:18px}
section>p{margin:2px 0 12px;color:var(--mut);font-size:13.5px}
.list{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.paper{border-top:1px solid var(--line)}
.paper:first-child{border-top:0}
.paper>summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:1fr auto;gap:4px 18px;padding:13px 16px}
.paper>summary::-webkit-details-marker{display:none}
.paper>summary:hover{background:var(--soft)}
.paper[open]>summary{background:var(--soft)}
.t{font-weight:600;line-height:1.4}
.m{grid-column:1;font-size:12.5px;color:var(--mut)}
.m i{font-style:normal;margin:0 6px;opacity:.5}
.nums{grid-row:1/3;grid-column:2;align-self:center;display:flex;gap:14px;font-size:13px;font-variant-numeric:tabular-nums;white-space:nowrap;color:var(--mut)}
.nums .s{color:var(--star);font-weight:600;min-width:58px;text-align:right}
.nums .c{min-width:64px;text-align:right}
.body{padding:4px 16px 18px;border-top:1px dashed var(--line)}
.qa{display:grid;grid-template-columns:1fr 1fr;gap:14px 28px;margin:12px 0 0}
.qa h4{margin:0 0 2px;font-size:11.5px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--mut)}
.qa p{margin:0;font-size:13.8px}
.links{display:flex;gap:16px;flex-wrap:wrap;margin-top:14px;font-size:13px}
.note{color:var(--mut)}
.empty{display:none;padding:40px 0;text-align:center;color:var(--mut)}
footer{margin:40px 0 60px;color:var(--mut);font-size:12.5px}
.hidden{display:none!important}
@media(max-width:640px){#q{flex-basis:100%}.qa{grid-template-columns:1fr}.paper>summary{grid-template-columns:1fr}.nums{grid-row:auto;grid-column:1;justify-content:flex-start}.nums .s,.nums .c{min-width:0;text-align:left}}
</style></head><body>
<header><div class="wrap">
<h1>Awesome Multimodal On-Policy Distillation</h1>
<p>@@INTRO@@</p>
<div class="facts"><b>@@TOTAL@@</b> @@L_PAPERS@@ · <b>@@NCODE@@</b> @@L_CODE@@ · @@L_UPDATED@@ @@UPDATED@@ · <a href="https://github.com/@@REPO@@">GitHub</a></div>
</div></header>
<div class="bar"><div class="wrap">
<div class="row1">
<input id="q" type="search" autocomplete="off">
<select id="sort" aria-label="Sort">
<option value="stars" data-en="Most starred" data-zh="按 Star 排序">Most starred</option>
<option value="date" data-en="Newest" data-zh="按时间排序">Newest</option>
<option value="cites" data-en="Most cited" data-zh="按被引排序">Most cited</option>
</select>
<label class="check"><input id="code" type="checkbox">@@L_ONLYCODE@@</label>
<button id="all" type="button"></button>
<button id="lang" type="button"></button>
</div>
<div class="tabs">@@TABS@@</div>
</div></div>
<main class="wrap">
@@SECTIONS@@
<div class="empty" id="empty">@@L_EMPTY@@</div>
<footer>@@FOOT@@</footer>
</main>
<script>
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const store={get(k,d){try{return localStorage.getItem(k)||d}catch(e){return d}},set(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
const TXT={en:{q:"Search title, affiliation, method, arXiv id…",open:"Expand all",close:"Collapse all",lang:"中文"},
           zh:{q:"搜索标题、单位、方法、arXiv 号…",open:"全部展开",close:"全部收起",lang:"EN"}};
let lang=store.get('opd_lang','en'), cat='all';
function applyLang(){
  document.documentElement.lang=lang==='zh'?'zh-CN':'en';
  $$('[data-en]').forEach(e=>{e.textContent=e.dataset[lang]||e.dataset.en});
  $('#q').placeholder=TXT[lang].q; $('#lang').textContent=TXT[lang].lang; syncAll();
  store.set('opd_lang',lang);
}
function syncAll(){
  const vis=$$('.paper:not(.hidden)');
  $('#all').textContent=TXT[lang][vis.length&&vis.every(p=>p.open)?'close':'open'];
}
function filter(){
  const v=$('#q').value.trim().toLowerCase(), code=$('#code').checked; let shown=0;
  $$('section').forEach(sec=>{
    let n=0;
    sec.querySelectorAll('.paper').forEach(p=>{
      const ok=(cat==='all'||sec.id===cat)&&(!code||p.dataset.stars!=='-1')&&(!v||p.dataset.hay.includes(v));
      p.classList.toggle('hidden',!ok); if(ok)n++;
    });
    sec.classList.toggle('hidden',!n); shown+=n;
  });
  $('#empty').style.display=shown?'none':'block'; syncAll();
}
function sort(){
  const k=$('#sort').value;
  $$('.list').forEach(l=>{
    [...l.children].sort((a,b)=>k==='date'?b.dataset.date.localeCompare(a.dataset.date):(+b.dataset[k]-+a.dataset[k])||b.dataset.date.localeCompare(a.dataset.date))
      .forEach(e=>l.appendChild(e));
  });
}
$('#q').addEventListener('input',filter);
$('#code').addEventListener('change',filter);
$('#sort').addEventListener('change',sort);
$('#lang').addEventListener('click',()=>{lang=lang==='en'?'zh':'en';applyLang()});
$('#all').addEventListener('click',()=>{const vis=$$('.paper:not(.hidden)'),o=!vis.every(p=>p.open);vis.forEach(p=>p.open=o);syncAll()});
$$('.paper').forEach(p=>p.addEventListener('toggle',syncAll));
$$('.tab').forEach(t=>t.addEventListener('click',()=>{cat=t.dataset.cat;$$('.tab').forEach(x=>x.setAttribute('aria-pressed',x===t));filter();window.scrollTo({top:0})}));
applyLang();
</script></body></html>"""

def build_html(src, stats):
    cats = src["categories"]; papers = src["papers"]
    by = {c["key"]: [] for c in cats}
    for p in papers: by[p["category"]].append(p)
    for k in by: by[k].sort(key=rank_key(stats), reverse=True)  # most-starred first
    updated = stats.get("_updated", "")
    total = len(papers)
    ncode = sum(1 for p in papers if p.get("repo"))

    def esc(s): return html.escape(s or "", quote=True)
    def t(en, zh, tag="span"):
        return f'<{tag} data-en="{esc(en)}" data-zh="{esc(zh or en)}">{esc(en)}</{tag}>'

    QL = [("q1", "Problem", "问题"), ("q2", "Method", "方法"),
          ("q3", "Setup", "任务 / 数据 / 模型"), ("q4", "Limitations", "局限")]

    def row(p):
        s = stats.get(p["id"], {}); idv = p["id"]; repo = p.get("repo")
        stars = s.get("stars") if repo else None
        cites = s.get("citations")
        date = s.get("date") or ""
        meta = [esc(x) for x in (p.get("affiliation"), date, p.get("venue")) if x and x != "—"]
        if p.get("sub") and p["sub"] not in (p.get("venue"), "arXiv.org"): meta.append(esc(p["sub"]))
        nums = (f'<span class="s">★ {human(stars)}</span>' if stars is not None else '<span class="s"></span>')
        nums += f'<span class="c">{t(f"{cites} cited", f"被引 {cites}") if cites is not None else ""}</span>'
        qa = "".join(f'<div>{t(en, zh, "h4")}{t(p.get(qk, ""), p.get(qk + "_zh", ""), "p")}</div>' for qk, en, zh in QL)
        links = [f'<a href="{arxiv_url(idv)}" target="_blank" rel="noopener">arXiv:{idv}</a>']
        if repo: links.append(f'<a href="https://github.com/{repo}" target="_blank" rel="noopener">github.com/{esc(repo)}</a>')
        if p.get("strict", "OPD") != "OPD":
            links.append(f'<span class="note">{t(p["strict"], p.get("strict_zh"))}</span>')
        if idv in WEB_IDS:
            links.append(f'<span class="note">{t("found by web search", "来自网络检索")}</span>')
        hay = " ".join([p["title"], p.get("sub", ""), p.get("venue", ""), idv, repo or "", p.get("affiliation", "")]
                       + [p.get(k + z, "") for k, _, _ in QL for z in ("", "_zh")]).lower()
        return (f'<details class="paper" data-stars="{-1 if stars is None else stars}" data-cites="{cites or 0}" '
                f'data-date="{esc(date)}" data-hay="{esc(hay)}"><summary>'
                f'<span class="t">{esc(p["title"])}</span><span class="nums">{nums}</span>'
                f'<span class="m">{"<i>·</i>".join(meta)}</span></summary>'
                f'<div class="body"><div class="qa">{qa}</div><div class="links">{"".join(links)}</div></div></details>')

    def tab(key, en, zh, n, on=False):
        return (f'<button type="button" class="tab" data-cat="{key}" aria-pressed="{"true" if on else "false"}">'
                f'{t(en, zh)}<span class="n">{n}</span></button>')
    tabs = tab("all", "All", "全部", total, True) + "".join(
        tab(c["key"], c.get("short") or c["title"], c["title_zh"].split(" ", 1)[-1], len(by[c["key"]])) for c in cats)
    secs = "\n".join(
        f'<section id="{c["key"]}">{t(c["title"], c["title_zh"], "h2")}{t(c["desc"], c["desc_zh"], "p")}'
        f'<div class="list">{"".join(row(p) for p in by[c["key"]])}</div></section>' for c in cats)

    fill = {
        "INTRO": t("On-policy distillation lets a student learn from its own rollouts while a teacher corrects them. "
                   "This page tracks the multimodal work: click any paper for a four-point summary.",
                   "在策略蒸馏（OPD）让学生在自己生成的轨迹上学习，由教师给出纠正信号。本页追踪其中的多模态工作，点击任意论文查看四点速览。"),
        "TOTAL": str(total), "NCODE": str(ncode), "UPDATED": esc(updated), "REPO": REPO,
        "L_PAPERS": t("papers", "篇论文"), "L_CODE": t("with code", "篇有代码"),
        "L_UPDATED": t("updated", "更新于"), "L_ONLYCODE": t("With code", "仅看有代码"),
        "L_EMPTY": t("No paper matches these filters.", "没有符合条件的论文。"),
        "FOOT": t("Generated from papers.json. Stars from GitHub, citations from Semantic Scholar, refreshed daily. "
                  "Summaries are paraphrased from the papers and may contain errors.",
                  "由 papers.json 自动生成。Star 来自 GitHub，被引来自 Semantic Scholar，每日刷新。摘要为转述，可能有误，请以原论文为准。"),
        "TABS": tabs, "SECTIONS": secs,
    }
    doc = PAGE
    for k, v in fill.items(): doc = doc.replace(f"@@{k}@@", v)
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
