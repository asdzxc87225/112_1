import cv2 
import numpy as np
from  PIL import ImageFont,ImageDraw,Image
def ex1():
    #0. 建立空白影像
    img = np.zeros((400,500,3),np.uint8)
    cv2.imshow('Ori',img)

    #1.定義需要加入的文字及其自行
    fext = '   happy\nNew Year\n安安你好'
    #fontPath1 = 'C:\\Windows\\Fonts\\prist'
    #linux use
    fontPath1 = '/usr/share/fonts/opentype/NotoSansCJK-DemiLight.ttc'

    #2 定義字形變數
    fl1 = ImageFont.truetype(fontPath1,50 )

    #3 將numpy 陣列轉為PIL影像( )
    imgP = Image.fromarray(img)

    #4在PIL影像上加入文字
    draw1 = ImageDraw.Draw(imgP)
    draw1.text((30,30) , fext, font=fl1, fill=(0,100,0))

    #5將PIL影像轉回Numpy陣列
    img2 = np.array( imgP )
    cv2.imshow('After', img2)
    cv2.waitKey(0)
    cv2.destroyWindow()

def ex2():
    img = np.zeros((400,800,3),np.uint8)
    img[:] = (203,192,255)
    text1 = '招財進寶'
    text2 = '天天開心'
    text3 = 'Make a Wish'
    font1 = '/usr/share/fonts/opentype/NotoSansCJK-DemiLight.ttc'
    font2 = '/usr/share/fonts/opentype/NotoSansCJK-Black.ttc'
    font3 = '/usr/share/fonts/opentype/Chilanka-Regular.otf'

    font1S = ImageFont.truetype(font1,100)
    font2S = ImageFont.truetype(font2,100)
    font3S = ImageFont.truetype(font3,80)

    imgP = Image.fromarray(img)
    draw1 = ImageDraw.Draw(imgP)
    draw1.text((30,30), text1, font=font1S,fill=(0,0,0))
    draw1.text((30,150), text2, font=font2S,fill=(255,0,0))
    draw1.text((30,300), text3, font=font3S,fill=(221,0,221))

    img2 = np.array(imgP)
    cv2.imshow('After', img2)
    cv2.waitKey(0)
    cv2.destroyWindow()


if __name__ == "__main__":
    ex2()
