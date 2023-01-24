import cv2
import numpy as np
import argparse
import datetime
import os
import time


cod=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('out.mp4',cod,20.0,(640,480))
start = datetime.datetime.now()

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
    help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
    help="max buffer size")
args = vars(ap.parse_args())
cap = cv2.VideoCapture(args["video"])



olower_range=np.array([4, 82, 158])
oupper_range=np.array([21, 240, 255])
glower_range=np.array([46, 56, 7])
gupper_range=np.array([101, 255, 97])
ylower_range=np.array([18, 140, 35])
yupper_range=np.array([54, 255, 226])


ret,frame=cap.read()
frame1=cv2.resize(frame,(640,480))

quadrant1 = (580, 440, 430, 220)
quadrant2 = (420, 460, 252, 260)
quadrant3 = (405, 7, 252, 230)
quadrant4 = (412, 7, 560, 210)


data=[]

def orangecolor(frame):
    color="Orange"
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,olower_range,oupper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            
            if (x>430 and y>220 and x+w<580 and y+h<440):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    
                    
                    cv2.putText(frame,("orange:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    data.append((timestamp, " First Quadrant", color))
            if (x>252 and y>260 and x+w<420 and y+h<460):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    cv2.putText(frame,("orange:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    
                    data.append((timestamp, color, " second Quadrant", color))
            if (x>405 and y>7 and x+w>405 and y+h<230):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                   
                    cv2.putText(frame,("orange:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    data.append((timestamp, color, " Third Quadrant", color))
                    
                    
            if (x>560 and y>7 and x+w<412 and y+h<210):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    cv2.putText(frame,("orange:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    data.append((timestamp, color, " Fourth Quadrant", color))
                    
                    
def greencolor(frame):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,glower_range,gupper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        color=" green "
        
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            
            if (x>430 & y>220 & x+w<580 & y+h<440):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    cv2.putText(frame,("green:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    data.append((timestamp, color, " First Quadrant", color))
                    
                    
            if (x>252 and y>260 and x+w<420 and y+h<460):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    cv2.putText(frame,("green:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    data.append((timestamp, color, " second Quadrant", color))
                    
                    
            if (x>252 and y>7 and x+w<405 and y+h<230):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    cv2.putText(frame,("green:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    data.append((timestamp, color, " Third Quadrant", color))
                   
                    
            if (x>460 and y>7 and x+w<612 and y+h<220):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    cv2.putText(frame,("green:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    data.append((timestamp, color, " Fourth Quadrant", color))
                    
                    
                    
def yellowcolor(frame):
    color="yellow"    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,ylower_range,yupper_range)
    _,mask1=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cnts,_=cv2.findContours(mask1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        x=600
        if cv2.contourArea(c)>x:
            x,y,w,h=cv2.boundingRect(c)
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                        
            if (x>430 and y>220 and x+w<580 and y+h<440):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                   
                    data.append((timestamp, color, " First Quadrant", color))
                    cv2.putText(frame,("yellow:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    
                    
            if (x>252 and y>260 and x+w<420 and y+h<460):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    data.append((timestamp, color, " second Quadrant", color))
                    
                    cv2.putText(frame,("yellow:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
            if (x>252 and y>7 and x+w<405 and y+h<230):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    
                    data.append((timestamp, color, " Third Quadrant", color))
                    cv2.putText(frame,("yellow:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    
                    
            if (x>560 and y>7 and x+w<412 and y+h<210):
                    
                    timestamp = (datetime.datetime.now()-start).total_seconds()
                    cv2.putText(frame,("yellow:"+str(timestamp)),(x,y -1),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                    
                    data.append((timestamp, color, " Fourth Quadrant", color))
                    
                    
                    


while True:
    ret,frame=cap.read()
    
    if args.get("video") and not ret:
        break
    
    frame=cv2.resize(frame,(640,480))
    

    cv2.rectangle(frame, quadrant1[:2], quadrant1[2:], (0, 255, 0), 2)
    cv2.rectangle(frame, quadrant2[:2], quadrant2[2:], (0, 255, 0), 2)
    cv2.rectangle(frame, quadrant3[:2], quadrant3[2:], (0, 255, 0), 2)
    cv2.rectangle(frame, quadrant4[:2], quadrant4[2:], (0, 255, 0), 2)
   
    yellowcolor(frame)
    orangecolor(frame)
    greencolor(frame)
      
    cv2.imshow("FRAME",frame)
    out.write(frame)
    if cv2.waitKey(32) & 0xFF==27:
        break

file=open('data.txt',"w")

file.write(" ")
for t in data:
        file.write(str(t)+"\n")

file.close
        
out.release()
cap.release()
cv2.destroyAllWindows()
