import cv2
import numpy as np 
from datetime import datetime as dt
import math

r = 200
c = 250
angle = (2 * math.pi)

window = np.zeros((500,500,3), np.uint8)
cv2.circle(window, (c,c), r ,(255,255,255),2)
cv2.circle(window, (c,c), 10 ,(200,200,200),-1)

for i in range(60):
    
    l = 10 if i % 5!=0 else 30
    color = (255,255,255) if i % 5 !=0 else (0,255,255)
    
    x = int(c + (r-l) * math.sin( i * angle/60))
    y = int(c - (r-l) * math.cos( i * angle/60))
    X = int(c + r * math.sin( i * angle/60))
    Y = int(c - r * math.cos( i * angle/60))
    cv2.line(window, (x,y), (X,Y), color, 4)
    
for i in range(1,13):
    
    x = int(c + (r - 50) * math.sin( i * angle/12))
    y = int(c - (r - 50) * math.cos( i * angle/12))
    
    cv2.putText(window, str(i), (x - 10, y + 10), cv2.FONT_HERSHEY_SIMPLEX, 1 , (255,255,0),2)
    
win = window.copy()
 
while True:
    window = win.copy()
    time = dt.now().strftime("%H:%M:%S")
    secs = dt.now().second
    mins = dt.now().minute
    hrs = dt.now().hour
    cv2.putText(window, time, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2)
    # seconds hand
    x = int(c + (r-35) * math.sin( secs * angle/60))
    y = int(c - (r-35) * math.cos( secs * angle/60))
    cv2.line(window, (c,c), (x,y), (0,255,0), 2)
    # minutes hand
    mins = mins + secs/60
    x = int(c + (r-70) * math.sin( mins * angle/60))
    y = int(c - (r-70) * math.cos( mins * angle/60))
    cv2.line(window, (c,c), (x,y), (255,2555,255), 3)
    # hours hand
    hrs = hrs + mins/60
    x = int(c + (r-120) * math.sin( hrs * angle/12))
    y = int(c - (r-120) * math.cos( hrs * angle/12))
    
    cv2.line(window, (c,c), (x,y), (0,0,255),8)
    
    cv2.imshow('Analog Clock',window)
    if cv2.waitKey(1)&0xFF==ord('q'):
        cv2.destroyAllWindows()
        break
        
