def get_random_string_fixed(length):
    result = ""
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    import random
    for i in range(length):
        result += random.choice(chars)

    return result

def draw_random_code(code):
    from PIL import Image, ImageDraw, ImageFont
    size = (120, 24)
    img = Image.new('RGB',size)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    for index,item in enumerate(code):
        x = (index + 1) * 20 + 10
        draw.text((x, 8), item, font=font, fill='red')
    img.save("code.png")

if __name__ == "__main__":
    code = get_random_string_fixed(4)
    draw_random_code(code)