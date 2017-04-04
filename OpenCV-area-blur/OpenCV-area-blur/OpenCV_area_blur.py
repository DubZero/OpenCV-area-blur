import numpy as np
import sys
import cv2
def nothing(x):
	pass
def reDraw(event,x,y,flags,param):
	global image
	global blur_image
	global radius
	global kernel
	if event == cv2.EVENT_MOUSEMOVE:
		center = int(x), int(y)
		if(kernel == -1):
			kernel = 5
		if(radius == -1):
			radius = 120
		blur_image = cv2.blur(source_image, (kernel,kernel))
		image = CircleBlur(center)

source_image = cv2.imread("D:\\OpenCV\\2.jpg")
image = cv2.imread("D:\\OpenCV\\2.jpg")

x,y,c = source_image.shape


cv2.namedWindow('image')
cv2.resizeWindow('image', x,y)
# create trackbars
cv2.createTrackbar('radius','image',120,500,nothing)
cv2.createTrackbar('kernel','image',5,255,nothing)
cv2.setMouseCallback('image',reDraw)

def CircleBlur(center):
	
	mask = CreateMask(center)
	#Smoothing borders
	cv2.GaussianBlur(mask, (101, 101), 111, dst=mask)
	image = BlendByMask(source_image,blur_image, mask)
	return image

def CreateMask(center):
	height, width, channels = source_image.shape
	mask = np.zeros_like(source_image)	
	cv2.circle(mask, center, radius, (255, 255, 255), -1)
	return mask

def BlendByMask(image1,image2,mask):
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

while True:
	cv2.imshow('image',image)
	cv2.waitKey(50)	

	# get current positions of four trackbars
	radius = cv2.getTrackbarPos('radius','image')
	kernel = cv2.getTrackbarPos('kernel','image')

	
print('Press any key..')
cv2.waitKey()
cv2.destroyAllWindows()