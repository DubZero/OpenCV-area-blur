import numpy as np
import sys
import cv2
image = cv2.imread("D:\\OpenCV\\1.jpg")
radius = int(input("Input blur radius in pixels: "))

if radius <= 0:
	sys.exit()
def Isincircle(Xc,Yc,r,x,y):
	if (x - Xc)*(x - Xc) + (y-Yc)*(y-Yc) - r*r <= 0:
		return True
	else:
		return False

# create blur image of edges
def edgeBlur(image,radius):
	height, width, channels = image.shape
	circleCenterX = round(width / 2)
	circleCenterY = round(height / 2)
	sub_image = np.ndarray((height,width,3),dtype=np.uint8)
	for h in range(height):
		for w in range(width):
			if (Isincircle(circleCenterX,circleCenterY,round(radius*1.2),h,w) and not(Isincircle(circleCenterX,circleCenterY,round(radius*0.8),h,w))):
				sub_image[h,w] = image[h,w]	
	blur_img = cv2.blur(sub_image,(3,3))
	return blur_img

def CircleBlur(image,radius):
	blur_image = cv2.blur(image,(15,15))
	mask = createMask(image,radius)
	blur_image = cv2.subtract(blur_image,blur_image,blur_image,mask=mask)
	blur_image = cv2.add(blur_image,image,blur_image,mask = mask)
	blur_mask = cv2.blur(mask,(15,15))	
	return blur_image

def createMask(image,radius):
	height, width, channels = image.shape
	circleCenterX = round(width / 2)
	circleCenterY = round(height / 2)
	mask = np.ndarray((height,width),dtype=np.uint8)
	for h in range(height):
		for w in range(width):
			if(Isincircle(circleCenterX,circleCenterY,radius,h,w)):
				mask[h,w] = 255
	
	return mask

blur = CircleBlur(image,radius)

cv2.imshow('mask',blur)

print('Press any key..')
cv2.waitKey()
cv2.destroyAllWindows()