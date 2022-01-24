from sys import get_asyncgen_hooks
import numpy as np
from pickle import FALSE, TRUE
from unittest import result
import cv2
import mediapipe as mp
from IPython.display import clear_output
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


run = FALSE
fr_cnt = 0
good_rep = 0
wrn_rep = 0
isx = 0
isy = 0
cap = cv2.VideoCapture("KneeBend.mp4")


def get_angel(dc):
    a = np.array(dc[0])
    b = np.array(dc[1])
    c = np.array(dc[2])

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)


with mp_pose.Pose(

        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        # print(results.pose_landmarks)
        la1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        la2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        if(results.pose_landmarks):
            for id, ma in enumerate(results.pose_landmarks.landmark):
                if(id == 25 and ma.visibility > 0.1):
                    la1[1][0] = ma.x
                    la1[1][1] = ma.y
                    #la1[1][2] = ma.z
                if(id == 27 and ma.visibility > 0.1):
                    la1[2][0] = ma.x
                    la1[2][1] = ma.y
                    #la1[2][2] = ma.z

                if(id == 26 and ma.visibility > 0.1):
                    la2[1][0] = ma.x
                    la2[1][1] = ma.y
                    #la2[1][2] = ma.z

                if(id == 28 and ma.visibility > 0.1):
                    la2[2][0] = ma.x
                    la2[2][1] = ma.y
                    #la2[2][2] = ma.z
                if(id == 24 and ma.visibility > 0.1):
                    la2[0][0] = ma.x
                    la2[0][1] = ma.y
                    #la2[0][2] = ma.z
                if(id == 23 and ma.visibility > 0.1):
                    la1[0][0] = ma.x
                    la1[0][1] = ma.y
                    #la1[0][2] = ma.z

        a=get_angel(la1)
        b=get_angel(la2)
       
        if(a<120 or b<120):
            fr_cnt += 1
            run = True
        else:
            
            if(run == True and (a!=180 or b!=180)):
                if((fr_cnt/24) < 8 and fr_cnt/24 > 1):
                    print("Keep your knee bent")
                    wrn_rep += 1
                elif((fr_cnt/24) >= 8):
                    good_rep += 1
                 
                print("GOOD CNT :" + str(good_rep), "BAD_CNT :"+str(wrn_rep))
            else:
               
                print("START EXE")
                wrn_rep = 0
                good_rep = 0
                run = False
         
            fr_cnt = 0
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        # Flip the image horizontally for a selfie-view display.
        cv2.putText(image, str("Timer :"+str(fr_cnt/8)), (70, 40),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(image, str("Good_CNT :"+str(good_rep)), (70, 80),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(image, str("Bad_CNT :"+str(wrn_rep)), (70, 120),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cap.release()
