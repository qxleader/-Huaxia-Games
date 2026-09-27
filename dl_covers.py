# -*- coding: utf-8 -*-
"""下载生成的游戏封面到 assets 目录（本地相对路径引用）。"""
import os
import urllib.request

ASSETS = r"E:\54188\项目文件\华夏游戏官网\assets"
os.makedirs(ASSETS, exist_ok=True)

items = [
    ("https://aka.doubaocdn.com/s/15Hq5nprv9", "game-jiuhe.jpg"),
    ("https://aka.doubaocdn.com/s/MPhV6XOpXl", "game-jingu.jpg"),
    ("https://aka.doubaocdn.com/s/iCK72cNhgq", "game-quanxin.jpg"),
]

for url, name in items:
    dest = os.path.join(ASSETS, name)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as f:
            f.write(r.read())
        print("ok", name, os.path.getsize(dest))
    except Exception as e:
        print("fail", name, e)
