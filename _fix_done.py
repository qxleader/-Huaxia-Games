import io
p = r'E:\54188\项目文件\华夏游戏官网\登录注册.html'
s = io.open(p, encoding='utf-8').read()
old = "  document.getElementById('form-login').style.display='none';\n  document.getElementById('form-reg').style.display='none';\n  document.querySelector('.tabs').style.display='none';\n"
new = "  document.getElementById('form-login').style.display='none';\n"
assert old in s, "done() block not found"
s = s.replace(old, new, 1)
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print("done() fixed; form-reg refs left:", s.count("form-reg"))
