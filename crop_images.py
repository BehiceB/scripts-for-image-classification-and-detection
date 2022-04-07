import pathlib
import sys
import os
import shutil
import cv2


n = 2 # order number
path= # the folder path which to add cropped images
filelist=[]
dir=os.makedirs(path)
created_dataset_path = path
pathlib.Path(created_dataset_path).mkdir(parents=True, exist_ok=True) 
class_list={0:"hiz_siniri_10", 1:"hiz_siniri_20", 2:"hiz_siniri_30", 3:"hiz_siniri_40", 4:"hiz_siniri_50",
             5:"hiz_siniri_60",6:"hiz_siniri_70", 7:"hiz_siniri_80", 8:"hiz_siniri_82",9:"hiz_siniri_yuz", 10:"hiz_siniri_120"}
path_annotation = # yolo format data annotation files path
path_images = # yolo format data image files path
for subdir, dirs, files in os.walk(path_annotation):
    # orders = range(1, len(files) , n)
    # for order in orders:
    for file in files: 
 
        if not file.endswith('.txt') : continue 
        
        # file=files[order]
        jpg_file=file.replace(".txt",".jpg")
        file1 = open(path_annotation + file, 'r') 
        Lines = file1.readlines() 
        for i in range(len(Lines)): 
            splitDataTag = Lines[i].split(" ") 
            if not (int(splitDataTag[0]) in class_list) :
                continue
                                
            else:
                                
                image = cv2.imread(path_images + jpg_file)

                height, width, channels = image.shape
                xc = float(splitDataTag[1])*width
                yc = float(splitDataTag[2])*height
                wc = float(splitDataTag[3])*width
                hc = float(splitDataTag[4])*height
                
                # you can check the image size so it's not too small.   
                #if not wc > 35 and hc > 35:
                #    continue
                        
                crop_for_save = image[abs(int(yc-hc/2)):abs(int(yc+hc/2)), abs(int(xc-wc/2)):abs(int(xc+wc/2))]
                cv2.imwrite(created_dataset_path + "/" + class_list[int(splitDataTag[0])]+"_"+ jpg_file ,crop_for_save)
        