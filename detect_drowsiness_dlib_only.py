
from imutils.video import VideoStream
from imutils import face_utils
from imutils.face_utils import rect_to_bb
import numpy as np
import imutils
import time
import dlib
import cv2

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Optional - sample region of iterest passed to the detector
# can also just pass the entire image, but it will be slower
bx_start = 460
by_start = 500
bx_end = 1040
by_end = 780

frame = cv2.imread('0115.jpg')
frame_crop = frame[by_start:by_end,bx_start:bx_end]

# upsize the cropped portion of the image (the ROI)
frame_up = cv2.pyrUp(frame_crop)
gray = cv2.cvtColor(frame_up, cv2.COLOR_BGR2GRAY)

# detect faces in the grayscale frame
rects = detector(gray, 0)

# loop over the face detections on the upsized cropped frame
for rect in rects:
    x, y, w, h = rect_to_bb(rect)
    print(x,y,w,h)
    
    # rectify to the original frame size
    x1 = int(x/2) + bx_start    # half as large, but also offset by the ROI start coords
    y1 = int(y/2) + by_start
    x2 = int(x/2 + w/2) + bx_start
    y2 = int(y/2 + h/2) + by_start
    
    # draw the bounding box on the original frame
    cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), 3)
    

# show the frame
cv2.imshow("Frame", frame)
key = cv2.waitKey(0) & 0xFF
