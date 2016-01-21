import cv2
import time
import numpy as np

# Initialize cameras
c1 = cv2.VideoCapture(1)
c2 = cv2.VideoCapture(2)

# set the number of samples
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
    cv2.imwrite("outputHT/calibration_pics/w1/c1t%d.png"%(i),f1)
    cv2.imwrite("outputHT/calibration_pics/w2/c2t%d.png"%(i),f2)
    print("Pictures saved.")
