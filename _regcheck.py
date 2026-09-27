import io
src = r'E:\54188\项目文件\华夏游戏官网\登录注册.html'
dst = r'E:\54188\项目文件\华夏游戏官网\_shots\_regcheck.html'
s = io.open(src, encoding='utf-8').read()
# 强制注册 tab 显示
s = s.replace('<div class="tab on" data-t="login" onclick="switchTab(\'login\')">登 录</div>',
              '<div class="tab" data-t="login" onclick="switchTab(\'login\')">登 录</div>')
s = s.replace('<div class="tab" data-t="reg" onclick="switchTab(\'reg\')">注 册</div>',
              '<div class="tab on" data-t="reg" onclick="switchTab(\'reg\')">注 册</div>')
s = s.replace('<form id="form-login" class="form" onsubmit="submitLogin(event)">',
              '<form id="form-login" class="form" style="display:none" onsubmit="submitLogin(event)">')
s = s.replace('<form id="form-reg" class="form" style="display:none" onsubmit="submitReg(event)">',
              '<form id="form-reg" class="form" onsubmit="submitReg(event)">')
io.open(dst, 'w', encoding='utf-8', newline='').write(s)
print("written temp reg-default copy")
