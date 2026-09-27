import io, re, glob, os
d = r'E:\54188\项目文件\华夏游戏官网'
files = sorted(f for f in glob.glob(os.path.join(d,'*.html')) if os.path.basename(f) not in ('网易游戏官网_游戏热爱者.html',))
pages = {os.path.basename(f).replace('.html','') for f in files}
for f in files:
    name = os.path.basename(f)
    s = io.open(f, encoding='utf-8').read()
    has_nav = 'class="nav' in s or '<header' in s
    has_footer = '<footer' in s
    links = set(re.findall(r'href="([^"#]+)\.html', s))
    reachable = {l for l in links if l in pages}
    missing_nav = not has_nav
    print(f"{name:16s} nav={'Y' if has_nav else 'N'} footer={'Y' if has_footer else 'N'} links={len(links)} reachable={len(reachable)} -> {','.join(sorted(reachable)[:12])}")
