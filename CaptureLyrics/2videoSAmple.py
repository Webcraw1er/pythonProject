# importing libraries
import cv2
import numpy as np
import time

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('videos/1minMovie.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
    print("Error opening video  file")
nowTime= time.time()
# Read until video is completed
while(cap.isOpened()):
      
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        
        # Display the resulting frame
        cv2.imshow('Frame', frame)
   
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    # Break the loop
    else: 
        break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()




"""
thisk is the sample of which the camera captures every single frame.

you implement the below block of code into this to look for any alterations every 1 second of latency,
if there's any, capture it, tesseract it, then save it.
you'll have to increment everytime the pyautogui senses the difference

"""

import time

fpsLimit = 1 # throttle limit
startTime = time.time()
cv = cv2.VideoCapture(0)
while True:
    frame = cv.read
    nowTime = time.time()
    if (int(nowTime - startTime)) > fpsLimit:
        # do other cv2 stuff....
        startTime = time.time() # reset time
