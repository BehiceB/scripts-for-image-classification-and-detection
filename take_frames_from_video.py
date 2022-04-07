import cv2
import os

KPS = 1 # Target Keyframes Per Second
VIDEO_PATH = "the video path which to get frames" 

IMAGE_PATH = "the folder path which to add frames" 
EXTENSION = ".jpg" #".png" etc.
cap = cv2.VideoCapture(VIDEO_PATH)
    # Set frames-per-second for capture
fps = round(cap.get(cv2.CAP_PROP_FPS))
hop = round(fps / KPS)
curr_frame = 0
while(True):
    
    ret, frame = cap.read()
    if not ret: break        
    name = IMAGE_PATH + "image" + str(curr_frame) + EXTENSION
    print('Creating... {0}'.format(name,))
    cv2.imwrite(name, frame)
    curr_frame += 1
cap.release()