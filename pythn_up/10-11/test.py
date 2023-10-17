import cv2 
import numpy as np
def ex1():
    img1 = np.zeros((256,512,3),np.uint8)
    img2 = np.ones((150,300,3),dtype = 'uint8')

    img1 [ : ] = (0x74,0x75,0x74)
    img2.fill(255)
    cv2.line(img1,(10,10),(300,10),(0x00,0x00,0xff),5)
    cv2.rectangle(img1,(30,20),(150,120),(0x6a,0xcc,0x00),3)
    cv2.rectangle(img1,(200,20),(400,120),(0xd7,0x78,0x00),-1)
    cv2.circle(img1,(72,195),50,(0x9f,0xef,0xff),3)
    cv2.ellipse(img1,(300,200),(25,60),0,0,60,(0xb9,0x80,0x29),-1)
    cv2.ellipse(img1,(400,200),(25,60),30,0,270,(0x00,0x00,0xff),3)
    text= 'hello word'
    cv2.putText(img1,text,(190,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1,cv2.LINE_8)
    cv2.putText(img1,text,(190,175),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1,cv2.LINE_4)
    cv2.putText(img1,text,(190,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1,cv2.LINE_AA)


    cv2.imshow('img1',img1)
    cv2.imshow('img2',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    ex1()

    
