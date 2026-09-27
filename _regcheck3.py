import io, re
src = r'E:\54188\项目文件\华夏游戏官网\_shots\_regcheck2.html'
dst = r'E:\54188\项目文件\华夏游戏官网\_shots\_regcheck3.html'
s = io.open(src, encoding='utf-8').read()
# 删除整个登录表单块（含 tab 登录tab改为none，保留注册tab.on）
s = re.sub(r'<form id="form-login" class="form" style="display:none" onsubmit="submitLogin\(event\)">.*?</form>\s*', '', s, flags=re.S)
io.open(dst, 'w', encoding='utf-8', newline='').write(s)
print("login form removed:", 'form-login' not in s, "; reg kept:", 'form-reg' in s)
