import cv2
import time
import sys
 
file = sys.argv[1]
print(file)

pat = '/home/santosg/Python_Manim/media/videos/'+file+'/480p15/'

cap= cv2.VideoCapture(pat+file+'.mp4')


fps= int(cap.get(cv2.CAP_PROP_FPS))

print("This is the fps ", fps)

if cap.isOpened() == False:
    print("Error File Not Found")

while cap.isOpened():
    ret,frame= cap.read()

    if ret == True:

        time.sleep(1/fps)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()

