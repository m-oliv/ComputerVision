import cv2
import numpy as np
import matplotlib.pyplot as plt

def houghTransf(img,thrs,r_ro=1, r_theta=1):
	'''
	Hough Transform Algorithm by Duda and Hart.
	
	Input:
		img -> the image in which we want to detect lines
		r_ro -> rho resolution (by default is set to 1)
		r_theta -> theta resolution (by default is set to 1)
		thrs -> threshold value used to determine if a peak was found in the accumulator
	Output:
		ml -> rho, theta parameters of the lines detected
		res -> the accumulator from the voting process (for test purposes)
	'''

	# size of the image
	lines, columns =img.shape

	# size of the accumulator

	# Theta can get values between zero and 180 degrees
	theta = np.linspace(0.0,179.0,np.ceil(179.0/r_theta)+1)
	# rho can get values between zero and sqrt((lines)^2 + (columns)^2) (size of the diagonal of the image)
	max_rho = np.sqrt((lines**2)+(columns**2))
	rho = np.linspace(0.0,max_rho,2*np.ceil(max_rho/r_ro))

	# create accumulator
	res = np.zeros((len(theta),len(rho)))
	
	# voting process of the Hough Transform
	for i in range(lines):
		for j in range(columns):
			if(img[i,j]<>0):
				for k in theta:
					# calculate rho:
					# rho = x * sen(theta) + y * cos(theta)
					# (the theta values are converted to radians)
					v_rho = round(i*np.sin(k*(np.pi/180)) + j*np.cos(k*(np.pi/180))) + len(rho)/2
					# increment position in the accumulator
					res[k,v_rho] += 1

	# get local maxima and convert to radians the theta parameters of the lines detected
	a = []
	for i in range(len(res)):
		for x in range(len(res[i])):
			if(res[i,x] > thrs):
				t = i * (np.pi/180)
				print [x-(len(rho)/2),t]
				a.append([x-(len(rho)/2),t])				
	ml = np.array(a)

	return ml, res


########################################################

# Input test image

img = cv2.imread('img_teste/reais/rubix_cube.jpg')
# Apply grayscale and Canny
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)

# set threshold
thrsh = 100

# Hough Transform
m,r = houghTransf(edges,thrsh)

# Draw detected lines on the original image
# Note: this is the same code used in the corresponding OpenCV example.

# Get two points to draw the lines
for rho,theta in m:
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))

	cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)

cv2.imwrite('output/hough-std/houghlines-reais-view1.png',img)

# Show the image with the detected lines
img = cv2.imread('output/hough-std/houghlines-reais-view1.png',1)
cv2.imshow('image',img)

k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
