# -*- coding: utf-8 -*-
"""把白底水墨素材处理为透明背景，供深色国潮官网使用。"""
import os
from PIL import Image

BASE = r"E:\54188\项目文件\华夏游戏官网"
ASSETS = os.path.join(BASE, "assets")
os.makedirs(ASSETS, exist_ok=True)


def white_to_transparent(src, dst, whiteness_thresh=200, feather=12):
    """按墨色深浅生成 alpha：白色→透明，墨色→不透明，保留灰度渐变。"""
    img = Image.open(src).convert("RGBA")
    px = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            # 墨色深浅 = 与白色的距离
            darkness = 255 - min(r, g, b)
            if darkness <= whiteness_thresh:
                # 接近白色：线性渐变到透明，避免硬边
                t = (whiteness_thresh - darkness) / float(whiteness_thresh)
                alpha = int(255 * (1 - t) ** feather)
            else:
                alpha = 255
            px[x, y] = (r, g, b, alpha)
    img.save(dst, "PNG")
    print("saved", dst, img.size)


# 1) 墨龙原图（竖版，签名级素材）
white_to_transparent(
    os.path.join(BASE, "..", "华夏游戏", "1790452431701.png"),
    os.path.join(ASSETS, "dragon-ink.png"),
)

# 2) 墨龙 LOGO（带“华夏游戏·用心做好游戏”）
white_to_transparent(
    os.path.join(BASE, "logo1_d853983.png"),
    os.path.join(ASSETS, "logo.png"),
)

print("done")
