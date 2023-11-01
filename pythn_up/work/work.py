import cv2
import numpy as np 


if __name__ == "__main__":
    x = 250
    y = 100
    img = np.zeros((256,512,3), np.uint8)
    img.fill(255)
    cv2.circle(img,(x,y),75,(0xff,0x94,0x28),-1)
    cv2.circle(img,(x,y),60,(0xff,0xff,0xff),-1)

    cv2.circle(img,(x,y),55,(0xff,0x94,0x28),-1)
    cv2.circle(img,(x,y),45,(0xff,0xff,0xff),-1)


    cv2.circle(img,(x,y),40,(0xff,0x94,0x28),-1)
    cv2.circle(img,(x,y),35,(0xff,0xff,0xff),-1)

    cv2.circle(img,(x,y),30,(0xff,0x94,0x28),-1)
    cv2.circle(img,(x,y),25,(0xff,0xff,0xff),-1)

    cv2.circle(img,(x,y),15,(0xff,0x94,0x28),-1)
    cv2.circle(img,(x,y),13,(0xff,0xff,0xff),-1)

    cv2.ellipse(img,(x,y),(75,75),95,0,80,(0xff,0xff,0xff),-1)
    cv2.circle(img,(x,y),5,(0xff,0x94,0x28),-1)
    cv2.ellipse(img,(280,172),(150,150),165,0,60,(0xff,0xff,0xff),-1)
    cv2.circle(img,(x,y),5,(0xff,0x94,0x28),-1)

    cv2.line(img,(x,y),(225,126),(0xff,0x94,0x28),2)
    cv2.line(img,(x-5,y+5),(212,113),(0xff,0x94,0x28),4)
    cv2.line(img,(x-5,y+5),(243,143),(0xff,0x94,0x28),4)
    cv2.line(img,(225,108),(243,128),(0xff,0x94,0x28),2)

    img1  = np.zeros((256,512,3),np.uint8)
    img1.fill(255)
    cv2.circle(img1,(x,y),55,(0xff,0x94,0x28),-1)

    cv2.ellipse(img1,(280,172),(150,150),225,0,70,(0xff,0xff,0xff),-1)
    cv2.ellipse(img1,(280-10,172),(150,150),225,0,70,(0xff,0xff,0xff),-1)

    poin = [199,151]

    cv2.ellipse(img1,poin,(10,10),230,0,90,(0xff,0x94,0x28),2)
    cv2.circle(img1,poin,4,(0xff,0x94,0x28),-1)
    cv2.line(img1,(191,144),(179,169),(0xff,0x94,0x28),2)
    cv2.line(img1,(191,144),(182,169),(0xff,0x94,0x28),2)

    cv2.line(img1,(208,145),(219,169),(0xff,0x94,0x28),2)
    cv2.line(img1,(208,145),(216,169),(0xff,0x94,0x28),2)

    cv2.imshow('img1',img1+img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

