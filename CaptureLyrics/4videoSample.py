"""
almo,st succeeded, but its too slow.

the freaking video has 25frame/sec.
it basically just prints one frame every one second now.
the renewal takes place every one second.

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
startFlag=1
# Read until video is completed
while(cap.isOpened()):
    nowTime= time.time()
    if (int(nowTime-startTime) > latency):         # if latency > 1, the frame is newly read.
        ret, frame = cap.read()
        startTime= nowTime
        print(startTime)
    else:                                               # if not, the frame is maintained as the previous one.
        if startFlag == 1:
            ret, frame= cap.read()
            startFlag-=1
            print(startFlag)                            # in the fresh start, you need to avoid calling the 
                # "frame" because at the moment it is "None"
        else:
            frame= frame                                    # problem here, the first frame is undefined.
    # Capture frame-by-frame

    if ret == True:
        if (int(nowTime)-int(startTime) > latency):
            # Display the resulting frame
            cv2.imshow('Frame', frame)  # this means that the display take place only when the latency > 1
   
            # Press Q on keyboard to  exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    
        # Break the loop
    else: 
        print("else activated")
        break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()