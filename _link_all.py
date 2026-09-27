import io, re, glob, os
d = r'E:\54188\项目文件\华夏游戏官网'
skip = {'网易游戏官网_游戏热爱者.html','注册.html','登录注册.html','开发者中心.html'}
files = sorted(f for f in glob.glob(os.path.join(d,'*.html')) if os.path.basename(f) not in skip)

# ---------- 1) 补全 资助中心 / 平台下载 页脚：锚点链接改为直达子页 ----------
fix_platform = [
 (r'<li><a href="华夏游戏官网.html#studios">工作室</a></li><li><a href="华夏游戏官网.html#caotai">草台剧场</a></li><li><a href="华夏游戏官网.html#about">承天学院</a></li>',
  r'<li><a href="工作室.html">工作室</a></li><li><a href="草台剧场.html">草台剧场</a></li><li><a href="承天学院.html">承天学院</a></li>'),
 (r'<li><a href="华夏游戏官网.html#jiuzhou">九州分区</a></li><li><a href="华夏游戏官网.html#events">创作赛事</a></li>',
  r'<li><a href="九州分区.html">九州分区</a></li><li><a href="赛事中心.html">创作赛事</a></li>'),
]
for f in ('资助中心.html','平台下载.html'):
    p = os.path.join(d,f)
    s = io.open(p, encoding='utf-8').read()
    for o,n in fix_platform:
        s = s.replace(o,n)
    io.open(p,'w',encoding='utf-8',newline='').write(s)

# ---------- 2) 首页：菜单加入口 + 页脚补全 ----------
hp = os.path.join(d,'华夏游戏官网.html')
s = io.open(hp, encoding='utf-8').read()
# 菜单：在“资助”后加“创作者”
assert '<li><a href="资助中心.html">资助</a></li>' in s
s = s.replace('<li><a href="资助中心.html">资助</a></li>',
              '<li><a href="资助中心.html">资助</a></li>\n      <li><a href="开发者中心.html">创作者</a></li>', 1)
# 页脚功能入口补全
old_fn = '<div><h5>功能入口</h5><ul><li><a href="九州分区.html">九州分区</a></li><li><a href="赛事中心.html">创作赛事</a></li><li><a href="资助中心.html">资助中心</a></li><li><a href="华夏游戏官网.html#library">公共素材库</a></li><li><a href="平台下载.html">平台启动器下载</a></li></ul></div>'
new_fn = '<div><h5>功能入口</h5><ul><li><a href="九州分区.html">九州分区</a></li><li><a href="赛事中心.html">创作赛事</a></li><li><a href="资助中心.html">资助中心</a></li><li><a href="公共素材库.html">公共素材库</a></li><li><a href="资金公示.html">资金公示</a></li><li><a href="线下活动.html">线下活动</a></li><li><a href="平台下载.html">平台启动器下载</a></li></ul></div>'
assert old_fn in s, "homepage 功能入口 not found"
s = s.replace(old_fn, new_fn, 1)
# 页脚账号组补全
old_ac = '<div><h5>账号</h5><ul><li><a href="登录注册.html">登录 / 注册</a></li><li><a href="新闻日志.html">平台动态</a></li><li><a href="关于我们.html">关于我们</a></li><li><a href="javascript:void(0)" data-toast>投稿与版权指引</a></li><li><a href="javascript:void(0)" data-toast>资助协议</a></li></ul></div>'
new_ac = '<div><h5>账号 · 支持</h5><ul><li><a href="登录注册.html">登录 / 注册</a></li><li><a href="个人主页.html">个人主页</a></li><li><a href="创作者后台.html">创作者后台</a></li><li><a href="讨论区.html">讨论区</a></li><li><a href="启动器游戏库.html">启动器游戏库</a></li><li><a href="新闻日志.html">平台动态</a></li><li><a href="帮助中心.html">帮助中心</a></li><li><a href="关于我们.html">关于我们</a></li></ul></div>'
assert old_ac in s, "homepage 账号 not found"
s = s.replace(old_ac, new_ac, 1)
# 进站动效：只显示一次（localStorage）
old_boot = """/* 进站终端动效 */
(function(){
  var boot=document.getElementById('boot');if(!boot)return;
  var lines=boot.querySelectorAll('.boot-line'),c=0;"""
new_boot = """/* 进站终端动效（首次访问显示，之后不再弹出） */
(function(){
  var boot=document.getElementById('boot');if(!boot)return;
  try{if(localStorage.getItem('hx_boot_seen')){boot.parentNode.removeChild(boot);return;}localStorage.setItem('hx_boot_seen','1');}catch(e){}
  var lines=boot.querySelectorAll('.boot-line'),c=0;"""
assert old_boot in s, "boot block not found"
s = s.replace(old_boot, new_boot, 1)
io.open(hp,'w',encoding='utf-8',newline='').write(s)

# ---------- 3) 全局：把所有页脚「功能入口」组注入 开发者中心 ----------
for f in files:
    p = os.path.join(d, os.path.basename(f))
    s = io.open(p, encoding='utf-8').read()
    if '<h5>功能入口</h5><ul>' in s and '<a href="开发者中心.html">开发者中心</a>' not in s:
        s = s.replace('<h5>功能入口</h5><ul>',
                      '<h5>功能入口</h5><ul><li><a href="开发者中心.html">开发者中心</a></li>', 1)
        io.open(p,'w',encoding='utf-8',newline='').write(s)

print("done")
