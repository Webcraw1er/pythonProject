import os

FolderPath= "./folders/weafeSS"
FolderPath2= "./folders/favsvLR"

print(os.getcwd())

os.mkdir(FolderPath)
os.mkdir(FolderPath2)

os.chdir(FolderPath)           # make png files in the folder.
i=0
for i in range(4):
    f= open("{0}.png".format(i), "x")
    f.close()
    i+=1

os.chdir("..")
os.chdir("..")
print(os.getcwd())
os.chdir(FolderPath2)
print(os.getcwd())
for i in range(4):
    f= open("{0}.txt".format(i), "x")
    f.close()
    i+=1