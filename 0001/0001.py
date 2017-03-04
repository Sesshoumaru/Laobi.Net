from PIL import Image
import os

icon32folder = r"C:\Users\Administrator\Desktop\32"
icon16folder = r"C:\Users\Administrator\Desktop\16"


def resize_to16(img_name):
    """缩小图片
    :param img_name:图片名称
    """

    img32_name = os.path.join(icon32folder, img_name)
    img16_name = os.path.join(icon16folder, img_name)
    img32 = Image.open(img32_name);
    img16 = img32.resize((16, 16))
    img16.save(img16_name)
    print("成功缩小尺寸：", img_name)


if os.path.exists(icon32folder):
    if not os.path.exists(icon16folder):
        os.makedirs(icon16folder, exist_ok=True)
    os.chdir(icon32folder)
    for img in os.listdir(icon32folder):
        resize_to16(img)
    print("全部图标缩小成功")
