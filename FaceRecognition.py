import threading 
import cv2
from deepface import DeepFace

# 0 = default camera input from computer
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# set dimensions of video
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

reference_image = cv2.imread("insert image here")

while True:   
    return_val, frame = cap.read() # reads camera
    
    if return_val:
        pass
        
    # allows user to close window with a key
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    
    cv2.destroyAllWindows

