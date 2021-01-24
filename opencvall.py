#importing openv liabrary
import cv2

#taking trained data in variable
car_trained_data=cv2.CascadeClassifier('car.xml')
face_trained_data=cv2.CascadeClassifier('face.xml')
smile_trained_data=cv2.CascadeClassifier('smile.xml')
cat_trained_data=cv2.CascadeClassifier('cat.xml')

#giving video as input
video=cv2.VideoCapture('video.mp4')

#loop for each frame of video as it is not a picture
while True:
     
     #taking each frame with .read()
    sr,frame=video.read()
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #taking cordinates of frame for adding rectangle
    cars=car_trained_data.detectMultiScale(frame)
    face=face_trained_data.detectMultiScale(frame)
    smile=smile_trained_data.detectMultiScale(frame)
    cat=cat_trained_data.detectMultiScale(frame)


    #looping through cordinates
    for(x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,254),3)
    for(x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,222,55),2)
    for(x,y,w,h) in smile:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,213,24),2)
    for(x,y,w,h) in cat:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,24),2)
    

    #showing the video as output per frame
    cv2.imshow('image',frame)

    #wait key to stop it on the tab for time
    key=cv2.waitKey(1)

    #for quiting the tab (q)
    if key==81 or key==113:
        break;
    
    
    #and its over
    
        
    
