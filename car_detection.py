#importing custom vision open cv
import cv2
#importing randrange function  for diffrent color
from random import randrange

#taking trained data from open cv
trained_data= cv2.CascadeClassifier('car.xml')
#taking video as input

read_frame=cv2.VideoCapture('video.mp4')
while True:
    #taking each frame as input
    sr,frame=read_frame.read()

    #reading frame and  converting data into black and white
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    #taking cordinates of cars in frame

    #detecting frames
    cars=trained_data.detectMultiScale(gray)

    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,254),)

    cv2.imshow('image',frame)
    key=cv2.waitKey(1)

    if key==81 or key==113:
        break;
