import pickle
import cv2 as cv
import numpy as np
import math

def get_frame(filename):
    cap=cv.VideoCapture(filename)
    if not cap.isOpened():
        print("Error opening video  file")
    i=0
    while cap.isOpened():
        ret, frame = cap.read()
        if i==0 :
            cv.imwrite("Parking_line.png",frame)
        cv.imshow('Frame', frame)
        i=i+1

        if cv.waitKey(25) & 0xFF == ord('q'):
            break

#get_frame("C:\\Users\\NAVEEN\\PycharmProjects\\ML\\DATA\\test.webm")


cap=cv.VideoCapture("C:\\Users\\NAVEEN\\PycharmProjects\\ML\\DATA\\test.webm")
if not cap.isOpened():
    print("Error opening video  file")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    img_Blur=cv.GaussianBlur(gray,(5,5),1)
    img_Threshold=cv.adaptiveThreshold(img_Blur,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,19,16)
    img_median_Threshold=cv.medianBlur(img_Threshold,5)
    k=np.ones((3,3),np.uint8)
    img_dilated=cv.dilate(img_median_Threshold,k,iterations=1)
    edges=cv.Canny(img_Blur,50, 200, None, 3)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180, 50)
    #print(lines)
    '''for line in lines:
        x1,y1,x2,y2=line
        cv.line(frame, (x1,y1),(x2,y2), (0, 0, 255), 3, cv.LINE_AA)'''
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3,cv.LINE_AA)
        # cv2.putText(img,f"{i+1}",(x1,y1),fontFace=cv2.FONT_HERSHEY_SIMPLEX,color=(0,0,255),fontScale=1)
    cv.imshow('Frame', frame)
    cv.imshow("BLUR",img_Blur)
    cv.imshow("Threshold",img_Threshold)
    cv.imshow("Median Threshold", img_median_Threshold)
    cv.imshow("Dilate", img_dilated)
    cv.waitKey(100)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break