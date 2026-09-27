import io, re
p = r'E:\54188\项目文件\华夏游戏官网\登录注册.html'
s = io.open(p, encoding='utf-8').read()

# 1) 移除 tabs（登录/注册切换），改为单标题
s = s.replace(
'    <div class="tabs"><div class="tab on" data-t="login" onclick="switchTab(\'login\')">登 录</div><div class="tab" data-t="reg" onclick="switchTab(\'reg\')">注 册</div></div>\n',
'    <div class="login-title"><span>登</span><span>录</span></div>\n')

# 2) 移除整个注册表单
s = re.sub(r'    <!-- 注册 -->\n    <form id="form-reg".*?</form>\n\n', '', s, flags=re.S)

# 3) 在登录按钮后加“立即注册”入口
s = s.replace(
'      <button class="btn" type="submit">登 录</button>\n    </form>',
'      <button class="btn" type="submit">登 录</button>\n      <div class="gologin">还没有账号？<a href="注册.html">立即注册 →</a></div>\n    </form>')

# 4) 移除已不再使用的 switchTab（避免引用已删除的 form-reg）
s = re.sub(r'function switchTab\(k\)\{.*?\}\n', '', s, flags=re.S)

# 5) 加 .login-title 与 .gologin 样式
s = s.replace(
'/* tabs */\n.tabs{display:flex;background:rgba(13,11,9,.6);border:1px solid var(--line);border-radius:10px;padding:.25rem;margin-bottom:1.5rem}\n.tab{flex:1;text-align:center;padding:.6rem 0;border-radius:7px;font-family:"Noto Serif SC",serif;font-size:.95rem;letter-spacing:.12em;color:var(--silver);cursor:pointer;transition:.2s}\n.tab.on{background:var(--zhu);color:#fff}',
'/* 登录标题 */\n.login-title{display:flex;justify-content:center;gap:.4rem;font-family:"Noto Serif SC",serif;font-size:1.3rem;letter-spacing:.3em;color:var(--paper);margin-bottom:1.5rem}\n.gologin{text-align:center;font-size:.8rem;margin-top:.4rem;color:var(--silver);opacity:.85}\n.gologin a{color:var(--zhu-hi)}\n.gologin a:hover{text-decoration:underline}')

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print("tabs removed:", '.tab on' not in s, "; reg form removed:", 'form-reg' not in s, "; gologin added:", '立即注册' in s)
