import os
import re

def deleteFiles():
    print("\ndeleteFiles activated.\ndeleting all files...\n")
    rootDir= "D:/Python/pythonProject/CaptureLyrics/folders"
    for (root, dirs, files) in os.walk(rootDir):
        for fileNames in files:
            if(fileNames.endswith(("txt", "png"))):
                print(fileNames, " deleted!")
                os.remove(os.path.join(root, fileNames))
    for (root, dirs, files) in os.walk(rootDir):
        for dirNames in dirs:
            if(dirNames.endswith(("SS", "LR"))):
                print(dirNames, " deleted!")
                os.rmdir(os.path.join(root, dirNames))
        #for dirNames in dirs:
        #    tempRoot= os.path.join(rootDir, dirNames)
        #    for fileNames in files:
        #        print("ok")
        #        print(os.path.join(tempRoot, fileNames))
        #        os.remove(os.path.join(tempRoot, fileNames))
    
    #SSfolder = re.search("SS$", dir)
    #LRfolder = re.search("LR$", dir)
    #print(SSfolder, LRfolder)
    quit()
