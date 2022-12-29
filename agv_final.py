import cv2
from cv2 import aruco
import threading
import detect

# ARUCO Marker dictionary import
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

# 카메라 불러오기


class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        
    def run(self):
        print ("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)
        detect.run()


def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    detected_markers = []
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        
        rval, frame = cam.read()
        h,w,c = frame.shape
        frame = cv2.rectangle(frame,(50, 250), (400, 450), (0,0,255))
        cv2.imshow(previewName, frame)
        cropped_frame = frame[250:450, 50:400]   # target area
        gray = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedframePoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        key = cv2.waitKey(20)
        if ids is not None:
            if (len(ids) == 1) and (ids[0][0] not in detected_markers):
                cv2.imwrite("images/cabinet" + str(ids[0][0]) + ".jpg", frame)
                detected_markers.append(ids[0][0])
                print("Cabinet is detected!")
                print("Id is: " , ids)
                print("detected markers are: ", detected_markers)
                
                cv2.waitKey(1)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)

# Create two threads as follows
thread1 = camThread("Camera 1", 0)
thread2 = camThread("Camera 2", 1)
thread1.start()
thread2.start()

