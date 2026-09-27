import io
p = r'E:\54188\项目文件\华夏游戏官网\华夏游戏官网.html'
s = io.open(p, encoding='utf-8').read()

# 1) 新墨龙图：dragon-ink.png -> dragon-ink.jpg
assert 'assets/dragon-ink.png' in s, "png ref not found"
s = s.replace('assets/dragon-ink.png', 'assets/dragon-ink.jpg', 1)

# 2) 进度条：去掉独立无限动画，改为与切换计时器联动的 run/paused
old_css = ".cb-progress i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--zhu-hi),var(--zhu-deep));animation:cb 5.2s linear infinite}\n@keyframes cb{from{width:0}to{width:100%}}"
new_css = ".cb-progress i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--zhu-hi),var(--zhu-deep))}\n.cb-progress i.run{animation:cb 5.2s linear forwards}\n.cb-progress i.paused{animation-play-state:paused}\n@keyframes cb{from{width:0}to{width:100%}}"
assert old_css in s, "progress css not found"
s = s.replace(old_css, new_css, 1)

# 3) JS：进度条随 go/play/stop 同步
old_js = """  function go(i){cur=(i+slides.length)%slides.length;slides.forEach(function(s,k){s.classList.toggle('on',k===cur);});dotsync();}
  function next(){go(cur+1);}
  var banner=document.getElementById('banner');
  function play(){timer=setInterval(next,5200);}
  function stop(){clearInterval(timer);}"""
new_js = """  var pb=document.querySelector('.cb-progress i');
  function restart(){pb.classList.remove('run');void pb.offsetWidth;pb.classList.add('run');pb.classList.remove('paused');}
  function go(i){cur=(i+slides.length)%slides.length;slides.forEach(function(s,k){s.classList.toggle('on',k===cur);});dotsync();restart();}
  function next(){go(cur+1);}
  var banner=document.getElementById('banner');
  function play(){clearInterval(timer);restart();timer=setInterval(next,5200);}
  function stop(){clearInterval(timer);pb.classList.add('paused');}"""
assert old_js in s, "carousel js not found"
s = s.replace(old_js, new_js, 1)

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print("ok; dragon-ink.jpg:", 'assets/dragon-ink.jpg' in s, "; run class:", 'pb.classList.add(\'run\')' in s, "; paused:", 'pb.classList.add(\'paused\')' in s)
