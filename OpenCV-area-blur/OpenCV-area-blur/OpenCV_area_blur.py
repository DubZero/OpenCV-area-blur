import numpy as np
import sys
import cv2
image = cv2.imread("D:\\OpenCV\\2.jpg")
radius = int(input("Input blur radius in pixels: "))

if radius <= 0:
	sys.exit()

def CircleBlur(image,radius):
	blur_image = cv2.GaussianBlur(image, (7,27), 10)
	mask = createMask(image,radius)
	#Smoothing borders
	cv2.GaussianBlur(mask, (101, 101), 111, dst=mask)
	res = blendMask(image,blur_image, mask)
	return res

def createMask(image,radius):
	height, width, channels = image.shape
	circleCenterX = round(width / 2)
	circleCenterY = round(height / 2)
	mask = np.zeros_like(image)	
	center = int(circleCenterX), int(circleCenterY)
	cv2.circle(mask, center, radius, (255, 255, 255), -1)
	return mask

def blendMask(image1,image2,mask):
	result = []
	matrix = np.full_like(mask[:, :, 0], 255)
	for c in range(0, image1.shape[2]):
		a = image1[:, :, c]
		b = image2[:, :, c]
		m = mask[:, :, c]
		res = cv2.add(
			cv2.multiply(b, cv2.divide(matrix - m, 255.0, dtype=cv2.CV_32F), dtype=cv2.CV_8U),
			cv2.multiply(a, cv2.divide(m, 255.0, dtype=cv2.CV_32F), dtype=cv2.CV_8U),
			dtype=cv2.CV_8U)
		result += [res]
	res = cv2.merge(result)
	return res

blur = CircleBlur(image,radius)

cv2.imshow('mask',blur)

print('Press any key..')
cv2.waitKey()
cv2.destroyAllWindows()