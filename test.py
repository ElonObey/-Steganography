from random import randint
from PIL import Image, ImageDraw


try:
    img = Image.open(input("Image name: "))
except FileNotFoundError:
        print("Файла не существует")
else:
    print(img)