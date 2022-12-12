
from random import randint
from PIL import Image, ImageDraw


def open_image():
    try:
        img = Image.open(input("Image name: "))
    except FileNotFoundError:
        print("Файл не найден")
    except Exception:
        print("Это вообще что такое? о.О")
    else:
        return img


def print_image(img):
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    size = 0
    print(pix)
    for y in range(height):
        for x in range(width):
            print(size, ": ", pix[x, y][0:3])
            size = size + 1


def print_line():
    print("="*20)


def enctyption():
    print_line()
    print("Блок шифровки")
    print_line()

    img = open_image()

    if img != None:
        draw = ImageDraw.Draw(img)
        width = img.size[0]
        height = img.size[1]

        print("width:", width)
        print("height:", height)

        pixels = img.load()
        file = open("keys.txt", "w")
        text = input("Enter text: ")

        for elements in text:
            # рандомная герерация координат пикселя
            key = (randint(0, width-1), randint(0, height-1))
            # ввод: координаты и вывод rgb (Отсчет сверху-слева)
            red, green = pixels[key][0:2]
            # print("red: ", red)
            # print("gr:", green)
            draw.point(key, (red, green, int(ord(elements))))
            # print(key)
            file.write(str(key) + '\n')
        img.save("new.png", "png")
        file.close()


def dectyption():
    print_line()
    print("Блок расшифровки")
    print_line()

    data = []
    mess = ""
    img = open_image()

    if img != None:
        pix = img.load()
        print("+"*20)
        print("Block B")
        print(pix[2, 0][0:3])
        file = open(input("Key's file: "), 'r')

        with open('keys.txt', 'r') as file:
            lines = file.readlines()
            print("Lines: ", lines)
            print(type(lines))
            for line in lines:
                data.append(line.strip('()\n').split(', '))
            print(data)
            print(type(data))
            print("-"*20)

            for key in data:
                print(key, type(key))
                x = int(key[0])
                y = int(key[1])
                # print(pix[x, y][2])
                letter = chr(pix[x, y][2])
                # print(letter, type(letter))
                print("Расшифр", letter)
                # print("Mass", mess, type(mess))
                mess += mess.join(str(letter))
            print("="*10)
            print("Расшифрованная строка: ", mess)

