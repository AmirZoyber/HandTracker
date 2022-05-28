#!/usr/bash/python3
# Author : AmirZyber
# You Can Find Me Here : 
#                        https://zil.ink/AmirZoyber

import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

while(True):
    src, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if (results.multi_hand_landmarks):
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark :
                height, width,channel = img.shape
                x,y = int(lm.x * width) , int(lm.y * height)
                cv2.circle(img,(x,y),10,(255,0,255),cv2.FILLED)
            mp_draw.draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS)
    cv2.imshow("HANDTRACKER",img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):break