
# REP_CNT-FOR-KNEE-BENT-EXERCISE

I am writing code to detect the REP_CNT-FOR-KNEE-BENT-EXERCISE.
In this project, I used the google media pipe library which provide us the 33 3D landmarks of the human body.![name-of-you-image](https://github.com/9834703848/REP_CNT-FOR-KNEE-BENT-EXERCISE/blob/4f0cc0330058856e02e70457d3bbc5378e0e5ba9/pose_tracking_full_body_landmarks.png)
As you can see in the above image we are sufficient only 6 ids of the human body to detect the count of reps in knee bend exercise.

id-24,26,28 for one leg and

id-23,25,27 for another leg.


## Deployment

TO USE THIS PROJECT I HAVE IMPORTED THE FOLLOWING LIBRARIES' 

```bash
  !from sys import get_asyncgen_hooks
  !import numpy as np
  !from pickle import FALSE, TRUE
  !from unittest import result
  !import cv2
  !import mediapipe as mp
  !from IPython.display import clear_output 

```

Next, I opened the video using OpenCV and then passed each frame through the media pipe library to get the landmarks.
I extracted the x,y,z coordinates of a landmark in each frame.

```bash
  cap = cv2.VideoCapture("KneeBend.mp4")

```
```bash
  image.flags.writeable = False
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  results = pose.process(image)

```
Here our "results" contain id for each landmark with x,y,z co-ordinates and visibility for that landmark. we can extract this information from here and use it to find the angle bw the id's.
```bash
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

```

Here get_angel function give us the angle bw the three co-ordinates of id's 24,26,28 and id's 23,25,27..
```bash
  def get_angel(dc):
    a = np.array(dc[0])
    b = np.array(dc[1])
    c = np.array(dc[2])

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)

```

At the start, the angle bw these coordinates are 180  degrees as soon as we start to exercise our timer on the screen start. This means as soon as our angle is on of the id(it depend on which leg we are using for exercise) drops below 120 degrees our timer start. If we maintain the same angel for at least 8 sec it will be counted as a good rep otherwise it will be counted as a bad rep.
```bash
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
        

```
We can also add this landmark on the images just for the reference using draw_landmark function.
```bash
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        

```
Using OpenCV library we can add timer,good_rep,bad_rep count on the image. It will be more efficient to keep count of our successful reps.


# REP_CNT-FOR-KNEE-BENT-EXERCISE

I am writing code to detect the REP_CNT-FOR-KNEE-BENT-EXERCISE.
In this project, I used the google media pipe library which provide us the 33 3D landmarks of the human body.![name-of-you-image](https://github.com/9834703848/REP_CNT-FOR-KNEE-BENT-EXERCISE/blob/4f0cc0330058856e02e70457d3bbc5378e0e5ba9/pose_tracking_full_body_landmarks.png)
As you can see in the above image we are sufficient only 6 ids of the human body to detect the count of reps in knee bend exercise.

id-24,26,28 for one leg and

id-23,25,27 for another leg.


## Deployment

TO USE THIS PROJECT I HAVE IMPORTED THE FOLLOWING LIBRARIES' 

```bash
  !from sys import get_asyncgen_hooks
  !import numpy as np
  !from pickle import FALSE, TRUE
  !from unittest import result
  !import cv2
  !import mediapipe as mp
  !from IPython.display import clear_output 

```

Next, I opened the video using OpenCV and then passed each frame through the media pipe library to get the landmarks.
I extracted the x,y,z coordinates of a landmark in each frame.

```bash
  cap = cv2.VideoCapture("KneeBend.mp4")

```
```bash
  image.flags.writeable = False
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  results = pose.process(image)

```
Here our "results" contain id for each landmark with x,y,z co-ordinates and visibility for that landmark. we can extract this information from here and use it to find the angle bw the id's.
```bash
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

```

Here get_angel function give us the angle bw the three co-ordinates of id's 24,26,28 and id's 23,25,27..
```bash
  def get_angel(dc):
    a = np.array(dc[0])
    b = np.array(dc[1])
    c = np.array(dc[2])

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)

```

At the start, the angle by these coordinates is 180  degrees as soon as we start exercising our timer on the screen start. This means as soon as our angle is on of the id(it depend on which leg we are using for exercise) drops below 120 degrees our timer start. If we maintain the same angel for at least 8 sec it will be counted as a good rep otherwise it will be counted as a bad rep.
```bash
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
        

```
We can also add this landmark on the images just for the reference using draw_landmark function.
```bash
        cv2.putText(image, str("Timer :"+str(fr_cnt/8)), (70, 40),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(image, str("Good_CNT :"+str(good_rep)), (70, 80),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(image, str("Bad_CNT :"+str(wrn_rep)), (70, 120),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))

```

This is how we can create our KNEE BENT REP counter using the media pipe library and python.
This is how we can create our KNEE BENT REP counter using media pipe library and python.




