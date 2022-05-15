import cv2 as cv
import numpy as np
import pickle

W = 35
H = 81
POS_LIST=[]
img = cv.imread("Parking_line.png")
#print(img)
gra=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(img.shape)#(336,596) no of rows ,col and channels-H=336 AND W=596
max_H=img.shape[0]
max_W=img.shape[1]
edges=cv.Canny(img,50, 200, None, 3)
lines = cv.HoughLinesP(edges, 1, np.pi / 180, 50,maxLineGap=1)
print(type(lines))
#cv.rectangle(img,(0,0),(596,336),(0,255,255),1)
for line in lines:
    x1, y1, x2, y2 = line[0]
    if abs(y1-y2)>5 :
     cv.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3, cv.LINE_AA)
     #cv.rectangle(img,(x1,y1),(x1+40,y1+20),(255,255,255),1)
     if  (x1+W)<max_W and (y1+H)<max_H :
          (b,g,r)=img[y1 + H,x1 + W]
          if b>=150 and g>=150 and r>=150:
            cv.rectangle(gra, (x1,y1), (x1 + W, y1 + H), (255, 255, 255), 2)
            #cv.rectangle(img,(x1,y1), (x1 + W, y1 + H), (0, 0, 0), 2)
            POS_LIST.append([x1, y1])

with open("parking_space2.conf","wb") as f:
    pickle.dump(POS_LIST,f)
cv.imshow("Lines ", img)
cv.imshow("G",gra)
cv.waitKey(0)
cv.destroyAllWindows()
