import cv2
import numpy as np
# List of pixel coordinates
coords = []
coordsxyz = []
getXYZ = False

def click_coords(event, x, y, flags, param):
	# Collect and print pixel coordinates on click

	if event == cv2.EVENT_LBUTTONDOWN:
		print([x,y])
		if(getXYZ==True):
			num = raw_input('XYZ coords: ').split(',')
			l = [int(n) for n in num]
			coords.append([x,y])
			coordsxyz.append(l)

# test image
w_name = 'test'
cam = 2
#img = cv2.imread('C:\\Users\\M\\Desktop\\thrandy.jpg')
img = cv2.imread('img_teste/reais/reconstruct-c2/calib2.png')
# Get xyz coords (if they exist)
# Exception needs to be handled here in case there's no file to read
try:
	#coordsxyz = np.load('C:\\Users\\M\\Desktop\\t.npy')
	if (cam == 1):
		coordsxyz = np.load('projMatrices/V1-c1.npy')
	if (cam == 2):
		coordsxyz = np.load('projMatrices/V1-c2.npy')
except:
	coordsxyz = []
	getXYZ = True
	pass
	# show image and set callback for mouse events
	cv2.imshow(w_name,img)
	cv2.setMouseCallback(w_name,click_coords)
	cv2.waitKey()
	# Save the array with the pixel coords
	#np.save('C:\\Users\\M\\Desktop\\test.npy',np.array(coords))
	if(cam==1):
		np.save('projMatrices/V1-c1.npy',np.array(coords))
		np.save('projMatrices/V1-c1-xyz.npy',np.array(coordsxyz))
	if(cam==2):
		np.save('projMatrices/V1-c2.npy',np.array(coords))
		np.save('projMatrices/V1-c2-xyz.npy',np.array(coordsxyz))

# Save the array with the xyz coords
#np.save('C:\\Users\\M\\Desktop\\testXYZ.npy',np.array(coordsxyz))
#np.save('projMatrices/V1-c1-xyz.npy',np.array(coordsxyz))

print("Pixel coords:")
print(np.array(coords))
print("XYZ coords:")
print(np.array(coordsxyz))
