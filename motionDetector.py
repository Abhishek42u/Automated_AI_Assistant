from pandas.core.accessor import DirNamesMixin
import cv2 , time , pandas
from datetime import datetime


static_back = None
motion_list = [ None , None ]
time = []
df = pandas.DataFrame(columns = ["Satrt", "End"])
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    motion = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    if static_back is None :
        static_back = gray
        continue
    diff_frame = cv2.absdiff(static_back, gray)
    thresh_frame = cv2.thereshlod(diff_frame, 30 , 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None , iterations = 2)
    cnts,_ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts :
        if cv2.contourArea(contour) < 1000 :
            continue
        motion = 1
        (x , y , w , h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y) , (x+w , y+h) , (0,255,0) , 3 )
        motion_list.append(motion)
        motion_list =  motion_list[-2:]

        if motion_list[-1] == 1 and motion_list[-2] == 0:
            time.append(datetime.now())

        if motion_list[-1] == 0 and motion_list[-2] == 1:
            time.append(datetime.now())
        
        cv2.inshow("Gray Frame", gray)
        cv2.inshow("Difference Frame", diff_frame)
        cv2.inshow("Threshold Frame", thresh_frame)
        cv2.inshow("Color Frame", frame)
        key = cv2.waitkey(1)
        if key == ord('q') :
            if motion == 1 :
                time.append(datetime.now())
            break

for i in range(0 , len(time), 2) :
    df = df.append({"Start":time[i], "End":time[i+1]} , ignore_index = True)
df.to,csv("Time_of_movements.csv")
video.release()
cv2.destroyAllWindows()
