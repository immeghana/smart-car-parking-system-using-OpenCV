import pickle
import cv2 as cv

W = 35
H = 81

try :
    with open("parking_space2.conf",'rb') as f:
        POS_LIST=pickle.load(f)
except :
    POS_LIST = []

def mark_slots(event,x,y,flags,params):

    if event==cv.EVENT_LBUTTONDOWN:
        POS_LIST.append([x,y])
    if event==cv.EVENT_RBUTTONDOWN :
        i=0
        for (x_l,y_l) in POS_LIST :

            if x_l<x<x_l+W and y_l<y<y_l+H:
                POS_LIST.pop(i)
            i=i+1
    with open("parking_space2.conf","wb") as f:
        pickle.dump(POS_LIST,f)

while 1:
   img = cv.imread("Parking_line.png")
   for i in POS_LIST :
      cv.rectangle(img, i, (i[0]+W,i[1]+H), (255, 0, 255), 2)

   cv.imshow("Img", img)
   cv.setMouseCallback("Img",mark_slots)
   cv.waitKey(1)
   if cv.waitKey(25) & 0xFF == ord('q'):
       break