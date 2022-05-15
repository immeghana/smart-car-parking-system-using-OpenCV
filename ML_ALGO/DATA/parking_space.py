import pickle
import cv2 as cv



def get_frame(filename):
    cap=cv.VideoCapture(filename)
    if not cap.isOpened():
        print("Error opening video  file")
    i=0
    while cap.isOpened():
        ret, frame = cap.read()
        if i==0 :
            cv.imwrite("car.png",frame)
        cv.imshow('Frame', frame)
        i=i+1

        if cv.waitKey(25) & 0xFF == ord('q'):
            break


#get_frame("car1.webm")
try :
    with open("parking_space.conf",'rb') as f:
        POS_LIST=pickle.load(f)
except :
    POS_LIST = []

W=40
H=94

def mark_slots(event,x,y,flags,params):

    if event==cv.EVENT_LBUTTONDOWN:
        POS_LIST.append([x,y])
    if event==cv.EVENT_RBUTTONDOWN :
        i=0
        for (x_l,y_l) in POS_LIST :

            if x_l<x<x_l+W and y_l<y<y_l+H:
                POS_LIST.pop(i)
            i=i+1
    with open("parking_space.conf","wb") as f:
        pickle.dump(POS_LIST,f)


#cv.rectangle(img,(176,65),(216,159),(255,0,255),2)

while 1:
   img = cv.imread("car.png")
   for i in POS_LIST :
      cv.rectangle(img, i, (i[0]+W,i[1]+H), (255, 0, 255), 2)

   cv.imshow("Img", img)
   cv.setMouseCallback("Img",mark_slots)
   cv.waitKey(1)
   if cv.waitKey(25) & 0xFF == ord('q'):
       break
