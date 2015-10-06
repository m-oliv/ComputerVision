import cv2
import time
import numpy as np

'''
Purpose: capture a give number of pictures from two cameras connected to the same computer.
Note: the camera index in VideoCapture might need to be adjusted.
'''


# Initialize cameras (2 cameras - for stereo 3D)
c1 = cv2.VideoCapture(1)
c2 = cv2.VideoCapture(2)

# set the number of images to capture
num_samples = 2

# open stream
time.sleep(5)
_,f1 = c1.read()
_,f2 = c2.read()

# capture n images and save them to file
for i in range(0,num_samples):
    print("Iteration %d"%(i+1))
    time.sleep(5)
    print("Get Ready..")
    time.sleep(5)

    # capture frames
    _,f1 = c1.read()
    _,f2 = c2.read()
    # write frames to a file
    print("Saving pictures...")
    cv2.imwrite("output/calibration_pics/c1/c1t%d.png"%(i),f1)
    cv2.imwrite("output/calibration_pics/c2/c2t%d.png"%(i),f2)
    print("Pictures saved.")
