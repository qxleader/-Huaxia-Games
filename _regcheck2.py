import io, re
src = r'E:\54188\项目文件\华夏游戏官网\_shots\_regcheck.html'
dst = r'E:\54188\项目文件\华夏游戏官网\_shots\_regcheck2.html'
s = io.open(src, encoding='utf-8').read()
# 去掉 <script>...</script> 块
s = re.sub(r'<script>.*?</script>', '', s, flags=re.S)
io.open(dst, 'w', encoding='utf-8', newline='').write(s)
print("no-script variant written, script removed:", '<script>' not in s)
