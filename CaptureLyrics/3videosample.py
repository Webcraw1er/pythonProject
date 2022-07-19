"""
this code does show the frames with 1sec latency, but every 1frame takes one freaking second!
"""


# importing libraries
import cv2
import numpy as np
import time

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('videos/1minMovie.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
    print("Error opening video  file")
startTime= time.time()
latency=0.9
# Read until video is completed
while(cap.isOpened()):
    nowTime= time.time()
    if (int(nowTime)-int(startTime) > latency):
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
        startTime= nowTime
        print(startTime)

   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()

