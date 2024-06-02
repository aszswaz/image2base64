import io
import os.path
import sys
import base64

from PIL import Image
import pyperclip

# 最大宽高
IMG_MAX = 700


def main():
    if len(sys.argv) != 2:
        cli_help()
        exit(1)
    arg = sys.argv[1:2][0]
    if arg == "help" or arg == "-h" or arg == "--help":
        cli_help()
        exit(0)

    # 读取文件
    with Image.open(arg) as img:
        # 缩放图片
        width, height = img.size
        while width > IMG_MAX or height > IMG_MAX:
            width = width * 0.9
            height = height * 0.9
        img = img.resize((int(width), int(height)))

        # 将图片数据进行 Base64 编码，图片格式固定为 JPEG
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        base64_str: str = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
        pyperclip.copy(base64_str)
        print(base64_str)
        print("\033[32m已复制到剪切板\033[0m")
        pass
    pass


def cli_help():
    """
    打印帮助信息
    """
    print(f"Usage: {os.path.basename(sys.argv[0])} <file>")
    print("    file 必须是图像文件")
    print("本工具用于将图片转换为 base64，以便将图片嵌入到 Markdown 文件")
    print(f"如果图片过大会自动对图片进行缩放，最大图片大小 {IMG_MAX} * {IMG_MAX}")
    pass


if __name__ == '__main__':
    main()
