import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
num = 1
while(True):
    ret, frame = cap.read()
    time.sleep(10)
    cv2.imwrite(f'images/image{num}.jpg', frame)
    num +=1