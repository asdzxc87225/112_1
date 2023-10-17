import cv2

img=cv2.imread('./img/Baboo128_24.bmp',1)
print(img.ndim)
print(id(img))
print(img.shape)
print(img.dtype)

