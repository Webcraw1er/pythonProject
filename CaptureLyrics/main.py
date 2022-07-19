import pytesseract as pg
import time
import os
import cv2

from capture import captureScreen
from delete import deleteFiles

print("hello.\nplease type \"delete\" for deleting all files in the folder, \nor \"capture\" to capture screens.")

while True:
    firstCommand = input("\"delete\" or \"capture\": ")
    if firstCommand == "delete":
        deleteFiles()
    elif firstCommand == "capture":
        captureScreen()
    print("invalid input. please type again.")
    if (firstCommand == "delete" or firstCommand == "capture"): 
        break
    



