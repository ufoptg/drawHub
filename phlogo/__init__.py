from PIL import Image, ImageDraw, ImageFont
import os

font = ImageFont.truetype(os.path.dirname(__file__) + "/expressway rg.ttf", 110)

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def Gabung(fun):
    def gabung(arg):
        im, text1 = add_corners(arg[0], 17), arg[1]
        op = Image.new("RGB", (40, 20), color=(0, 0, 0))
        draw = ImageDraw.Draw(op)
        bbox = draw.textbbox((0, 0), text1, font=font)
        baru = Image.new("RGB", (im.width + bbox[2] + 210 + 20 + 130, 600), color=(0, 0, 0))
        draw = ImageDraw.Draw(baru)
        draw.text((150, 250), text1, (255, 255, 255), font=font)
        baru.paste(im, (150 + bbox[2] + 20, 230 + 10), im.convert("RGBA"))
        return baru
    return gabung(fun)

def generate(text1, text2):
    bbox_text2 = font.getbbox(text2)
    oren = Image.new("RGBA", (bbox_text2[2] - bbox_text2[0] + 20, 140), color=(240, 152, 0))
    draw = ImageDraw.Draw(oren)
    draw.text((10, int((oren.height - (bbox_text2[3] - bbox_text2[1])) / 2) - 10), text2, (0, 0, 0), font=font)
    return Gabung([oren, text1])
