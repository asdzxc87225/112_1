import numpy as np
import cv2
from PIL import ImageFont,ImageDraw,Image

img = np.zeros((400,700,3),np.uint8)
img[:] = (160,150,255)
#畫直線---------------------------------------------
cv2.line(img,(50,200),(50,350),(0,0,255),1)#畫線-紅色
cv2.line(img,(50,300),(80,180),(0,0,255),1)
cv2.line(img,(90,180),(90,380),(0,0,255),1)
cv2.line(img,(40,210),(90,370),(0,0,255),1)
cv2.line(img,(110,220),(110,320),(0,0,255),1)
cv2.line(img,(110,270),(120,200),(0,0,255),1)

cv2.line(img,(400,200),(400,350),(65,130,255),1)#畫線-橙色
cv2.line(img,(450,180),(450,380),(0,255,255),1)#畫線-黃色
cv2.line(img,(500,200),(500,350),(0,130,0),1)#畫線-綠色
cv2.line(img,(550,180),(550,380),(255,190,10),1)#畫線-藍色
cv2.line(img,(600,200),(600,350),(255,25,255),1)#畫線-桃紅色
#畫橢圓----------------------------------------------
cv2.ellipse(img,(440,170),(15,40),0,0,360,(0,0,255),1)#畫橢圓-紅色
cv2.ellipse(img,(440,170),(15,40),30,0,360,(0,0,255),1)
cv2.ellipse(img,(440,170),(15,40),60,0,360,(0,0,255),1)
cv2.ellipse(img,(440,170),(15,40),90,0,360,(0,0,255),1)
cv2.ellipse(img,(440,170),(15,40),120,0,360,(0,0,255),1)
cv2.ellipse(img,(440,170),(15,40),150,0,360,(0,0,255),1)

cv2.ellipse(img,(560,200),(14,39),0,0,360,(0,0,255),2)#畫橢圓-紅色-線寬2
cv2.ellipse(img,(560,200),(14,39),30,0,360,(0,0,255),2)
cv2.ellipse(img,(560,200),(13,37),30,0,360,(65,130,255),-1)#橢圓形30度填滿橙色
cv2.ellipse(img,(560,200),(14,39),60,0,360,(0,0,255),2)
cv2.ellipse(img,(560,200),(14,39),90,0,360,(0,0,255),2)
cv2.ellipse(img,(560,200),(14,39),120,0,360,(0,0,255),2)
cv2.ellipse(img,(560,200),(14,39),150,0,360,(0,0,255),2)
cv2.circle(img,(560,200),5,(0,0,255),-1)#中心圓形
cv2.circle(img,(560,200),10,(0,0,255),1)#中心外層圓形

cv2.ellipse(img,(410,275),(15,36),0,0,360,(0,130,0),1)#畫橢圓-綠色
cv2.ellipse(img,(410,275),(15,36),20,0,360,(0,130,0),1)
cv2.ellipse(img,(410,275),(15,36),40,0,360,(0,130,0),1)
cv2.ellipse(img,(410,275),(15,36),60,0,360,(0,130,0),1)
cv2.ellipse(img,(410,275),(15,36),80,0,360,(0,130,0),1)
cv2.ellipse(img,(410,275),(15,36),100,0,360,(0,130,0),1)
cv2.ellipse(img,(410,275),(15,36),120,0,360,(0,130,0),1)
cv2.ellipse(img,(410,275),(15,36),140,0,360,(0,130,0),1)
cv2.ellipse(img,(410,275),(15,36),160,0,360,(0,130,0),1)

cv2.ellipse(img,(490,230),(10,17),0,0,360,(255,190,10),1)#畫橢圓-藍色
cv2.ellipse(img,(490,230),(10,17),15,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),30,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),45,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),60,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),75,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),90,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),105,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),120,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),135,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),150,0,360,(255,190,10),1)
cv2.ellipse(img,(490,230),(10,17),165,0,360,(255,190,10),1)

cv2.ellipse(img,(630,300),(11,18),0,0,360,(0,255,255),1)#畫橢圓-右邊下面黃色
cv2.ellipse(img,(630,300),(11,18),15,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),30,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),45,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),60,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),75,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),90,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),105,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),120,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),135,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),150,0,360,(0,255,255),1)
cv2.ellipse(img,(630,300),(11,18),165,0,360,(0,255,255),1)

cv2.ellipse(img,(270,190),(11,48),0,0,360,(255,25,255),2)#畫橢圓-桃紅色
cv2.ellipse(img,(270,190),(11,48),45,0,360,(255,25,255),2)
cv2.ellipse(img,(270,190),(11,48),90,0,360,(255,25,255),2)
cv2.ellipse(img,(270,190),(11,48),135,0,360,(255,25,255),2)

cv2.ellipse(img,(270,190),(10,17),0,0,360,(0,255,255),1)#畫橢圓-桃紅色中間黃色
cv2.ellipse(img,(270,190),(10,17),18,0,360,(0,255,255),1)
cv2.ellipse(img,(270,190),(10,17),36,0,360,(0,255,255),1)
cv2.ellipse(img,(270,190),(10,17),54,0,360,(0,255,255),1)
cv2.ellipse(img,(270,190),(10,17),72,0,360,(0,255,255),1)
cv2.ellipse(img,(270,190),(10,17),108,0,360,(0,255,255),1)
cv2.ellipse(img,(270,190),(10,17),126,0,360,(0,255,255),1)
cv2.ellipse(img,(270,190),(10,17),144,0,360,(0,255,255),1)
cv2.ellipse(img,(270,190),(10,17),162,0,360,(0,255,255),1)
#畫圓---------------------------------------------------
cv2.ellipse(img,(38,200),(27,27),0,0,360,(0,255,0),1)#左邊綠色的圓
cv2.ellipse(img,(38,200),(19,19),0,0,360,(0,255,0),2)
cv2.ellipse(img,(38,200),(10,10),0,0,360,(0,255,0),1)
cv2.ellipse(img,(38,200),(5,5),0,0,360,(0,255,0),-1)

cv2.ellipse(img,(120,165),(27,27),0,0,360,(255,190,10),1)#左邊藍色的圓
cv2.ellipse(img,(120,165),(19,19),0,0,360,(255,190,10),2)
cv2.ellipse(img,(120,165),(10,10),0,0,360,(255,190,10),1)
cv2.ellipse(img,(120,165),(5,5),0,0,360,(255,190,10),-1)

cv2.ellipse(img,(180,240),(20,20),0,0,360,(0,0,255),1)#左邊紅色圓圈
cv2.ellipse(img,(180,240),(14,14),0,0,360,(0,0,255),2)
cv2.ellipse(img,(180,240),(8,8),0,0,360,(0,0,255),1)
cv2.ellipse(img,(180,240),(4,4),0,0,360,(0,0,255),-1)

cv2.ellipse(img,(290,265),(18,18),0,0,360,(0,255,255),1)#中間偏下圓圈
cv2.ellipse(img,(290,265),(12,12),0,0,360,(0,255,255),2)
cv2.ellipse(img,(290,265),(7,7),0,0,360,(0,255,255),1)
cv2.ellipse(img,(290,265),(3,3),0,0,360,(0,255,255),-1)

cv2.ellipse(img,(440,170),(10,10),0,0,360,(0,0,255),2)
cv2.ellipse(img,(440,170),(5,5),0,0,360,(0,0,255),-1)

cv2.rectangle(img,(150,380),(670,380),(0,130,0),9)#底下綠色粗
cv2.rectangle(img,(160,390),(680,390),(0,130,0),1)#底下綠色細

#畫蝴蝶--------------------------------------------
cv2.ellipse(img,(630,100),(12,38),30,0,360,(0,0,255),1)
cv2.ellipse(img,(640,100),(12,38),54,0,360,(0,0,255),2)
cv2.ellipse(img,(640,140),(12,38),130,0,360,(0,0,255),2)
cv2.ellipse(img,(630,140),(12,38),150,0,360,(0,0,255),1)
cv2.ellipse(img,(630,140),(10,32),145,0,360,(255,25,255),-1)
cv2.ellipse(img,(630,140),(6,32),145,0,360,(0,0,255),-1)
cv2.ellipse(img,(630,100),(10,32),30,0,360,(255,25,255),-1)
cv2.ellipse(img,(630,100),(7,30),30,0,360,(0,0,255),-1)
cv2.line(img,(580,110),(610,120),(0,0,255),1)
cv2.line(img,(600,90),(610,120),(0,0,255),1)
cv2.ellipse(img,(580,110),(3,3),0,0,360,(0,0,255),-1)
cv2.ellipse(img,(600,90),(3,3),0,0,360,(255,25,255),-1)

text1 = ' ~~~ Life is not a Draem ~~~ '
text2 = '*****Just do it!     Just do it!     Just do it! *****'
text3 = '劉仁承'
fontPath3 = '/usr/share/fonts/opentype/NotoSansCJK-DemiLight.ttc'
ft3 = ImageFont.truetype(fontPath3,20)
cv2.putText(img, text1, (5,60), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1.5, (19,69,139), 1, cv2.LINE_AA)
cv2.putText(img, text2, (150,380), cv2.FONT_HERSHEY_TRIPLEX,0.5, (19,69,139), 1, cv2.LINE_AA)

imgP = Image.fromarray(img)
draw3 = ImageDraw.Draw(imgP)
draw3.text((590,355),text3,font = ft3,fill = (255,255,255))
img2 = np.array(imgP)

cv2.imshow('Ori',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()