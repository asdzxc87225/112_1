import cv2
import numpy

def ex1():
    img = cv2.imread('../img/Lena.tiff',-1)
    cv2.imshow('orginal',img)
    r_mat=cv2.getRotationMatrix2D((50,10),30,1)
    r_img = cv2.warpAffine(img,r_mat,(img.shape[1],img.shape[0]))
    cv2.imshow("NEAREST",r_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def ex2():
    img = cv2.imread('../img/Lena.tiff',-1)
    cv2.imshow('orginal',img)
    print('orig img size',img.shape)

    #1
    scale=1.5
    w= int(img.shape[1]*scale)
    h= int(img.shape[0]*scale)
    dsize=(w,h)
    rsize_img1 = cv2.resize(img,dsize, interpolation = cv2.INTER_AREA)
    cv2.imshow('AREA',rsize_img1)

    #2 
    rsize_img2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
    cv2.imshow("NEAREST",rsize_img2)
    print(cv2.waitKey(0))
    cv2.destroyAllWindows()

def ex3():
    pass

if __name__ == "__main__":
    ex1()
    ex2()
