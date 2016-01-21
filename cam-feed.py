import cv2

cv2.namedWindow("Camera 1")
cv2.namedWindow("Camera 2")
vc1 = cv2.VideoCapture(1)
vc2 = cv2.VideoCapture(2)

if vc1.isOpened(): # try to get the first frame
    rval1, frame1 = vc1.read()
else:
    rval1 = False

if vc2.isOpened(): # try to get the first frame
    rval2, frame2 = vc2.read()
else:
    rval2 = False

while rval1 and rval2:
    cv2.imshow("Camera 1", frame1)
    cv2.imshow("Camera 2", frame2)
    rval1, frame1 = vc1.read()
    rval2, frame2 = vc2.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("Camera 1")
cv2.destroyWindow("Camera 2")
