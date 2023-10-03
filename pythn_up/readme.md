## 上課規則

- 平時 25
- 作業 30 上機,電子檔/紙本
- 其中 20 個人大作業
- 期末 25 組別報告

## 加分

1. 服務
1. 優良
1. 其他

## 扣分

1. 手機
1. 實物
1. 環境

上課時間下午0200到0430

---

# 影像處里

##  一  影像處理參數
![圖](./01.png)
WxH 4x5


### pixel.像數/畫數

影像的最小單元，會影響影大小。

### bit-depth 位元深度
每個pixel上顏色或亮度使用到的bit數
1. 當只有1bit的時候就被稱為黑白影像。
1. 8bit $2^8$ 灰階影像
1. 24bit就有$2^{24}$個表示又稱為全彩影像，bgr

所佔用的空間

- $4*5*2^1$bit
- $4*5*2^8$bit
- $4*5*2^{24}$bit

### 原點
在片的左上角，並在格子中。
### 座標1. (w*h) 水平 在 垂直 --> 單純指出某個座標or影像大小
1. (h*w) 垂直 在 水平 --> 之後會取出像數值來做處理
### 座標直

指的是顏色

### channel 通道
指的是將位元深度進行區分，如果是全彩的可分成BGR三個通道
1. f(h,w) = (b,g,r) # 全彩
1. f(h,w) = (0) # 灰階
1.


---

## open cv 參數

影像讀取的指令
```py
img=cv2.imread('Lena.tiff',1)
```

### img.shape
影像尺寸資料(h,w,c) 高 寬 通道數
- ![圖](./01.png)
- 全彩(5,4,3)
- 灰階(5,4)

### img.ndim
影像尺寸的為度
可以由尺判斷通道數。
不同特性的資料作法要注意。
```py
if (img.ndim == 3):
  全彩處里
else:
  灰階
```
### id(img)
在記憶體中的位址
![](./02.png)
```py
img1 = img
img2 = img.copy()
img1[10:30,10:40] = 255
img2[80:120,10:150] = 0
```
### type(img)
影像鄭列的資料型態


### img.dtype
影像鄭列中的元素的內容格式
- uint8 #無號的8bit整數資料

## 亮度 vs 顏色
要去學latex矩陣表示

- 相對位址
- 顏色: 彩度 , 亮度

彩度空間: hsv
亮度空間: yuv , ycbcy yiq



## 載入系統+ 變更工作路徑

```py
import os 
os.getcwd() #顯示
mywd = "/home/HserName" # 使用者的自訂路徑
os.chdir(mywd)#切換工作路徑

```

## 載入套件

```py
improt cv2
import numpy
```

## 讀取
cv2.imread('影像檔名',格式)


### 格式有3

1. cv2.IMEAD\_COLOR 以全彩/3通道來讀取
1. cv2.IMREAD\_GRAYSALE 灰階/1通道處理
1. cv2.INREAD\_UNCHANGED以省像本身尺寸來讀取

### 顯示秀圖

- cv2.namedWindow('視窗名',視窗格式)
- cv2.imshow('視窗名',影像陣列名)

#### 視窗格式有2

1. cv2.WINDOW\_AUTOSIZE 視窗隨影像大小開啟1
1. cc2.WINDOW\_NORMAL 視窗開啟之後可伸縮0

---

## 寫入

- cv2.imwrite('寫數影像檔名',影像陣列名)
檔名支援
- bmp
- tiff
- png
- jpg

## 等待&關閉

- cv2.waitKey(0)
- cv2.destroyAllWindows()

```py
img1 = cv2.imread('Lena.tiff',1)
img2 = cv2.imread('Lena.tiff',0)#或讀到Y
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

#觀察此時img1與img2的shape,ndim

img3 = cv2.imread('F16 256_8.bmp',1)
img3 = cv2.imread('F16 256_8.bmp',0)
# 觀察
cv2.imwrite('Dimg1.png',img1)
cv2.imwrite('Dimg2.png',img2)

```

## 補充
當要存檔的時候可以選用壓縮格式,jpg,這個下的指令如下
- cv2.imwrite('Lenal0.jpg',img1,[int(cv2.IMWRITE_JPEG_QUALITY),10])

1. 用Q=10,20,30來存檔
1. 觀察檔案大小(檔案總管中）
1. 顯示??


