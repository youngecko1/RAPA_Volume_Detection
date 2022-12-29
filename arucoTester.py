import cv2
import argparse
import imutils
import sys

# ARUCO_DICT = {
#     "DICT_6x6_50": cv2.aruco.DICT_6x6_50
# }

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="path to input image containing Aruco Tag")
# ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORIGINAL", help="type of Aruco tag either 5x5 or 6x6")
# args = vars(ap.parse_args())


image = cv2.imread("runs/detect/exp26/crops/0/pic_500.jpg")
arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_100)
arucoParams = cv2.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

print(ids[0][0])


