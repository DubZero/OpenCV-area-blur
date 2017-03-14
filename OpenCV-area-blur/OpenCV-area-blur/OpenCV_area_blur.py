import numpy as np
import sys
import cv2
image = cv2.imread("D:\\OpenCV\\1.jpg")
radius = int(input("Input blur radius in pixels: "))
if radius <= 0:
	sys.exit()

# blur circle area
def circle_blur(image,radius):
	height, width, channels = image.shape
	circleCenterX = round(width / 2)
	circleCenterY = round(height / 2)
	sub_image = np.ndarray((height,width,3),dtype=np.uint8)

	for h in range(height):
		for w in range(width):
			if not(Isincircle(circleCenterX,circleCenterY,round(radius*0.8),h,w)):
				sub_image[h,w] = image[h,w]	
	blur_img = cv2.blur(sub_image,(10,10))
	blur_img = Concat_image(image,blur_img,radius)
	return blur_img	
				
# Check if pixel in the circle
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

# Concatinate old image with blur image and edge blur image
def Concat_image(image,blur_image,radius):
	height, width, channels = image.shape
	circleCenterX = round(width / 2)
	circleCenterY = round(height / 2)
	# concatinate old image with blur
	for h in range(height):
		for w in range(width):
			if not(Isincircle(circleCenterX,circleCenterY,radius,h,w)):
				image[h,w] = blur_image[h,w]
	# concatinate new image with edge blur image
	edge_img = edgeBlur(image,radius)
	for h in range(height):
		for w in range(width):
			if (Isincircle(circleCenterX,circleCenterY,round(radius*1.1),h,w) and not(Isincircle(circleCenterX,circleCenterY,round(radius*0.9),h,w))):
				image[h,w] = edge_img[h,w]	
	return image

cv2.imshow('image',image)
new_image = circle_blur(image,radius)
cv2.imshow('new',new_image)
print('Press any key..')
cv2.waitKey()
cv2.destroyAllWindows()