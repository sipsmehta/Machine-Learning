# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 22:50:32 2021

@author: sipsm
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8)

while True:
  success, img=cap.read()
  img=detector.findHands(img)
  lmList, _=detector.findPosition(img)
  cv2.imshow("Image",img)
  cv2.waitKey(1)
  