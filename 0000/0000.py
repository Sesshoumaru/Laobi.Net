from PIL import Image, ImageDraw, ImageFont

img = Image.open("龙猫.png")
w, h = img.size
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((w - 20, 10), '4', font=font, fill='red')
img.save("龙猫1.png")
