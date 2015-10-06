import cv2

'''
Purpose: Get the coordinates of the pixels of an image on click. The coordinates of these pixels are stored in a list.
'''


# List of pixel coordinates
coords = []

def click_coords(event, x, y, flags, param):
	# Collect and print pixel coordinates on click

	if event == cv2.EVENT_LBUTTONDOWN:
		coords.append([x,y])
		print([x,y])

# test image
w_name = 'thrandy'
img = cv2.imread('C:\\Users\\M\\Desktop\\thrandy.jpg')

# show image and set callback for mouse events
cv2.imshow(w_name,img)
cv2.setMouseCallback(w_name,click_coords)
cv2.waitKey()