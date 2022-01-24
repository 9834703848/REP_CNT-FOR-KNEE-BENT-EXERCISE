# REP_CNT-FOR-KNEE-BENT-EXERCISE

IN this project I used google mediapipe library which provide us the 33 3D landmarks of the human body.![name-of-you-image](https://github.com/9834703848/REP_CNT-FOR-KNEE-BENT-EXERCISE/blob/4f0cc0330058856e02e70457d3bbc5378e0e5ba9/pose_tracking_full_body_landmarks.png)

As you can see in above image we are sufficient only 6 id of human body to detect the count of reps in knee bend exercise.
id-24,26,28 for one leg and
id-23,25,27 for another leg.

First we will import all the libraries we need.

from sys import get_asyncgen_hooks
import numpy as np
from pickle import FALSE, TRUE
from unittest import result
import cv2
import mediapipe as mp
from IPython.display import clear_output


Next I opend video using opencv and then passed each frame through the mediapipe library to get the landmars.
I extracted the x,y,z co-ordinates of landmark in each frame.
And then I find the angle bw three co-ordinates of id's 24,26 and 28 and id's 23,25,27.

At the start the angle bw these cordinated is 180  degrees as soon as we start exercise our timer on the scree start means as soon as our angle bw on of the id(it depend on which leg we are usign for exercise) drope below 120 degree our timer start. IF we maintain the same angel for atleat 8 sec the it will count as successful rep otherwise it will be count as bad rep.

This is how we can creat our KNEE BENT REP counter using mediapipe library and python.

