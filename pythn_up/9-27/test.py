import  cv2
import numpy
import os 

def show(img):
    print('shape = ',img.shape,'ndim = ',img.ndim)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    img1 = cv2.imread('../img/Lena.tiff',1)
    img2 = cv2.imread('../img/Lena.tiff',0)
    img3 = cv2.imread('../img/F16 256_8.bmp',1)
    img4 = cv2.imread('../img/F16 256_8.bmp',0)

    print('img1 : ',end = '')
    show(img1)
    print('img2 : ',end = '')
    show(img2)
    print('img3 : ',end = '')
    show(img3)
    print('img4 : ',end = '')
    show(img4)

    print('--------------------------------------------------------')
    cv2.imwrite('Dimg1.png',img1)
    print('img1:',os.path.getsize('Dimg1.png'))
    cv2.imwrite('Dimg2.png',img2)
    print('img2:',os.path.getsize('Dimg2.png'))
    cv2.imwrite('Dimg3.png',img3)
    print('img3:',os.path.getsize('Dimg3.png'))
    cv2.imwrite('Dimg4.png',img4)
    print('img4:',os.path.getsize('Dimg4.png'))
    print('--------------------------------------------------------')
    cv2.imwrite('Dimg5.jpg',img4,[int(cv2.IMWRITE_JPEG_QUALITY),10])
    cv2.imwrite('Dimg6.jpg',img4,[int(cv2.IMWRITE_JPEG_QUALITY),20])
    cv2.imwrite('Dimg7.jpg',img4,[int(cv2.IMWRITE_JPEG_QUALITY),70])

    img5 =cv2.imread('./Dimg5.jpg',0)
    img6 =cv2.imread('./Dimg6.jpg',0)
    img7 =cv2.imread('./Dimg7.jpg',0)
    print('img5 : ',end = '')
    show(img5)
    print('img6 : ',end = '')
    show(img6)
    print('img7 : ',end = '')
    show(img7)
    


