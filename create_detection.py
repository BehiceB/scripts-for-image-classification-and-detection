
import os
import glob
import shutil
from tqdm import tqdm

txtNames=[]
n = 2 #order number
class_list=[0,1,2,3,4,5,6,7,8,9,10,11]
path_annotation = "C:/Users/asus/Desktop/yedek/fly00862/"
imgFiles=glob.glob('C:/Users/asus/Desktop/yedek/fly00862/*.jpg')
dir="C:/Users/asus/Desktop/sonhal/fly00862/"
#dir=os.makedirs("C:/Users/asus/Desktop/dene222/fly00009")
for subdir, dirs, files in os.walk(path_annotation):
    
    print(len(files))
    #orders = range(1, len(files) , n)
    #for order in orders:
    for file in files:
        if not file.endswith('.txt') : continue 
            
            #file=files[order]
        name=file[:-4]
        txtNames.append(name)
        # print(name)
        file1 = open(path_annotation + file, "r+") 
        file2 = open(dir + file, "w")
        Lines = file1.readlines()
        for i in range(len(Lines)):
            splitDataTag = Lines[i].split(" ")
            splitDataTag[0]= "0"
            Lines[i]=splitDataTag[0] +" "+ splitDataTag[1] +" " +splitDataTag[2] +" "+splitDataTag[3] +" "+splitDataTag[4]
                
            file2.write(Lines[i])
file1.close()
file2.close()
for i in range(len(txtNames)):
    name=txtNames[i]
    #print(name)
    for img in tqdm(imgFiles):
        temp=img.split('\\')
        name2=temp[1][:-4]
        if name == name2:

