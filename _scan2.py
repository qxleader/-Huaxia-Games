import io, re, glob, os
d = r'E:\54188\项目文件\华夏游戏官网'
files = sorted(f for f in glob.glob(os.path.join(d,'*.html')) if os.path.basename(f) not in ('网易游戏官网_游戏热爱者.html',))
for f in files:
    name = os.path.basename(f)
    s = io.open(f, encoding='utf-8').read()
    has_func = '功能入口' in s
    has_navmenu = 'class="menu"' in s
    print(f"{name:16s} footer功能入口={'Y' if has_func else 'N'} 顶部menu={'Y' if has_navmenu else 'N'}")
