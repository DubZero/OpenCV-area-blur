import numpy as np
import sys
import cv2
image = cv2.imread("D:\\OpenCV\\1.jpg")
image_gray = cv2.imread("D:\\OpenCV\\1.jpg",0)
edges = cv2.Canny(image_gray,100,350)

blur_img = cv2.blur(image,(20,20))
height, width = edges.shape

for h in range(height):
	for w in range(width):
		if edges[h,w] == 255:
			blur_img[h,w] = image[h,w]

cv2.imshow('image',blur_img)
print('Press any key..')
cv2.waitKey()
cv2.destroyAllWindows()