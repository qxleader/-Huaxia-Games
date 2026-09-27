import io
p = r'E:\54188\项目文件\华夏游戏官网\华夏游戏官网.html'
s = io.open(p, encoding='utf-8').read()

# 1) 加固时间轴：min-width:0 防止内容列塌陷成竖排
s = s.replace(
".tl li{display:grid;grid-template-columns:110px 30px 1fr;gap:.9rem;align-items:start;padding:.45rem 0}",
".tl li{display:grid;grid-template-columns:110px 30px 1fr;gap:.9rem;align-items:start;padding:.45rem 0;min-width:0}"
)
s = s.replace(
".tl .cont b{color:var(--paper);font-weight:600;font-size:.96rem;display:block}",
".tl .cont{min-width:0}\n.tl .cont b{color:var(--paper);font-weight:600;font-size:.96rem;display:block}"
)
s = s.replace(
".tl .cont span{font-size:.78rem;color:var(--silver);opacity:.72}",
".tl .cont span{font-size:.78rem;color:var(--silver);opacity:.72;display:block;line-height:1.75}"
)
# 移动端时间轴：也补 min-width:0
s = s.replace(
".tl li{grid-template-columns:70px 24px 1fr;gap:.55rem}",
".tl li{grid-template-columns:70px 22px 1fr;gap:.55rem;min-width:0}"
)
# 2) 时间轴 reveal 改为向上浮现（不横向平移，更稳）
s = s.replace(
"['#log .tl li','rev-left']",
"['#log .tl li','rev-up']"
)

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print("ok; has 1fr conflicting block:", "grid-template-columns:1fr;border-left:2px solid var(--zhu-hi)" in s)
