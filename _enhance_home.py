import io

p = r'E:\54188\项目文件\华夏游戏官网\华夏游戏官网.html'
s = io.open(p, encoding='utf-8').read()

# ---------- 1) 回纹暗纹 SVG data-uri（percent-encode） ----------
def uri(txt):
    return txt.replace('<', '%3C').replace('>', '%3E').replace('#', '%23').replace('"', "'").replace(' ', '%20')
huitexture = ("<svg xmlns='http://www.w3.org/2000/svg' width='200' height='200'>"
  "<g fill='none' stroke='%23C8C8C8' stroke-width='1.1'>"
  "<path d='M44 20h112v62H44z'/><path d='M44 118h112v62H44z'/>"
  "<path d='M20 44h62v112H20z'/><path d='M118 44h62v112h-62z'/>"
  "<circle cx='100' cy='100' r='7'/>"
  "</g></svg>")

# ---------- 2) 新增 <style> + boot + bgtexture HTML，插到 hero 前 ----------
style_html = """
<style>
/* ===== 科幻国风·深化 ===== */
/* 进站终端动效遮罩 */
#boot{position:fixed;inset:0;z-index:9999;background:#0d0c0a;display:flex;align-items:center;justify-content:center;transition:opacity .8s ease}
#boot.done{opacity:0;pointer-events:none}
.boot-box{width:min(560px,86vw);padding:2.2rem 2.4rem;border:1px solid var(--line);border-radius:10px;background:rgba(20,17,13,.6);position:relative;overflow:hidden;box-shadow:0 0 40px var(--zhu-glow)}
.boot-line{opacity:0;font-family:ui-monospace,Consolas,Menlo,monospace;font-size:.86rem;color:var(--silver);letter-spacing:.12em;line-height:2.4;transition:opacity .18s ease}
.boot-line.on{opacity:1}
.boot-line b{color:var(--zhu-hi);font-weight:400}
.boot-scan{position:absolute;left:0;right:0;top:0;height:34%;background:linear-gradient(180deg,rgba(168,52,36,.22),transparent);animation:bootscan 1.6s ease-in-out infinite}
@keyframes bootscan{0%{transform:translateY(-120%)}100%{transform:translateY(320%)}}
.boot-seal{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-family:"Noto Serif SC",serif;font-weight:900;font-size:3.4rem;color:var(--zhu);opacity:.14;letter-spacing:.2em}
/* 背景回纹暗纹 */
#bgtexture{position:fixed;inset:0;z-index:0;pointer-events:none;opacity:.05;background-image:url("data:image/svg+xml,""" + uri(huitexture) + """);background-size:200px 200px}
/* 全局点击纹章 */
.click-orn{position:fixed;z-index:9998;pointer-events:none;width:54px;height:54px;color:var(--zhu-hi);opacity:0;animation:orn .8s ease-out forwards}
.click-orn svg{width:100%;height:100%}
@keyframes orn{0%{transform:translate(-50%,-50%) scale(.4) rotate(-12deg);opacity:.9}100%{transform:translate(-50%,-50%) scale(1.55) rotate(14deg);opacity:0}}
</style>

<div id="boot">
  <div class="boot-box">
    <div class="boot-seal">华</div>
    <div class="boot-scan"></div>
    <div class="boot-line"><b>▸</b> 华夏游戏 · 安全终端 v0.8</div>
    <div class="boot-line"><b>▸</b> 正在建立安全连接 ……</div>
    <div class="boot-line"><b>▸</b> 指纹校验 ▓▓▓▓▓▓▓▓▓▓ <b>通过</b></div>
    <div class="boot-line"><b>▸</b> 身份核验完成，欢迎进入<b>华夏游戏</b></div>
  </div>
</div>
<div id="bgtexture"></div>

<section class="hero" id="top">
"""

anchor = '<section class="hero" id="top">\n'
assert anchor in s, "hero anchor not found"
s = s.replace(anchor, style_html, 1)

# ---------- 3) 升级 #fx 粒子为 Three 风格网络粒子 ----------
old_particles = """/* Hero 粒子背景：缓慢上升的朱色光点 */
(function(){
  var cv=document.getElementById('fx');if(!cv)return;
  var ctx=cv.getContext('2d'),W,H,ps=[];
  function size(){W=cv.width=cv.offsetWidth;H=cv.height=cv.offsetHeight;}
  size();
  var N=Math.min(42,Math.max(16,Math.floor(W/55)));
  for(var i=0;i<N;i++){ps.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.7+.6,vx:(Math.random()-.5)*.22,vy:-Math.random()*.3-.08,a:Math.random()*.5+.18});}
  function draw(){ctx.clearRect(0,0,W,H);ps.forEach(function(p){p.x+=p.vx;p.y+=p.vy;if(p.y<-6){p.y=H+6;p.x=Math.random()*W;}if(p.x<-6)p.x=W+6;if(p.x>W+6)p.x=-6;ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,6.28);ctx.fillStyle='rgba(168,52,36,'+p.a+')';ctx.fill();});requestAnimationFrame(draw);}
  window.addEventListener('resize',size);
  draw();
})();"""
new_particles = """/* Hero 粒子网络（Three.js 风格：光点 + 朱色连线） */
(function(){
  var cv=document.getElementById('fx');if(!cv)return;
  var ctx=cv.getContext('2d'),W,H,ps=[],link=96;
  function size(){W=cv.width=cv.offsetWidth;H=cv.height=cv.offsetHeight;}
  size();
  var N=Math.min(46,Math.max(18,Math.floor(W/52)));
  for(var i=0;i<N;i++){ps.push({x:Math.random()*W,y:Math.random()*H,r:Math.random()*1.7+.6,vx:(Math.random()-.5)*.28,vy:(Math.random()-.5)*.28});}
  function draw(){
    ctx.clearRect(0,0,W,H);
    var i,j;
    for(i=0;i<N;i++){var p=ps[i];p.x+=p.vx;p.y+=p.vy;
      if(p.x<-8)p.x=W+8;if(p.x>W+8)p.x=-8;if(p.y<-8)p.y=H+8;if(p.y>H+8)p.y=-8;
      ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,6.28);ctx.fillStyle='rgba(200,200,200,.75)';ctx.fill();}
    for(i=0;i<N;i++){for(j=i+1;j<N;j++){var a=ps[i],b=ps[j],d=Math.hypot(a.x-b.x,a.y-b.y);
      if(d<link){ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.strokeStyle='rgba(168,52,36,'+(1-d/link)*.2+')';ctx.lineWidth=.6;ctx.stroke();}}}
    requestAnimationFrame(draw);
  }
  window.addEventListener('resize',size);
  draw();
})();"""
assert old_particles in s, "particle block not found"
s = s.replace(old_particles, new_particles, 1)

# ---------- 4) 追加 boot / 点击纹章 / hero 视差 JS ----------
add_js = """
/* 进站终端动效 */
(function(){
  var boot=document.getElementById('boot');if(!boot)return;
  var lines=boot.querySelectorAll('.boot-line'),c=0;
  function step(){
    if(c<lines.length){lines[c].classList.add('on');c++;setTimeout(step,330);}
    else{setTimeout(function(){boot.classList.add('done');setTimeout(function(){if(boot.parentNode)boot.parentNode.removeChild(boot);},850);},520);}
  }
  setTimeout(step,180);
})();
/* 全局点击：留下华夏回纹 */
document.addEventListener('click',function(e){
  var el=document.createElement('span');el.className='click-orn';
  el.style.left=e.clientX+'px';el.style.top=e.clientY+'px';
  el.innerHTML='<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="10" y="10" width="28" height="28" rx="2"/><rect x="17" y="17" width="14" height="14"/><path d="M24 5v38M5 24h38"/><circle cx="24" cy="24" r="3" fill="currentColor" stroke="none"/></svg>';
  document.body.appendChild(el);
  setTimeout(function(){el.remove();},860);
});
/* Hero 视差：向下滚动时墨龙区轻微上移（叙事纵深） */
(function(){
  var grid=document.querySelector('.hero-grid');
  if(!grid)return;
  var ticking=false;
  function par(){ticking=false;var y=window.scrollY;if(y>window.innerHeight)return;grid.style.transform='translateY('+(y*.16)+'px)';}
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(par);}},{passive:true});
})();
"""
assert '</script>' in s
s = s.replace('</script>\n</body>', add_js + '</script>\n</body>', 1)

io.open(p, 'w', encoding='utf-8', newline='').write(s)
print("ok; boot:", 'id="boot"' in s, "; bgtexture:", 'id="bgtexture"' in s, "; network:", 'Math.hypot' in s, "; click-orn:", 'click-orn' in s)
