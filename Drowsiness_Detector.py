# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 02:18:45 2019

@author: Saransh
"""
import pygame
import math
import dlib
import cv2

pygame.init()

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
play = False
eye_ar_consec_frames = 20 # If a person has closed their eyes for 20 consecutive frames, we’ll play the alarm sound
count_check = 0
pygame.mixer.music.load('Industrial Alarm.wav')
while True:
    _,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #To convert video in gray scale
    faces = detector(gray)
    
    for face in faces:
        landmarks = predictor(gray,face)
        dist=[]
        x=(37,38,43,44)
        y=(41,40,47,46)
        for xy in range(4):
            x1 = landmarks.part(x[xy]).x
            y1 = landmarks.part(x[xy]).y
            x2 = landmarks.part(y[xy]).x
            y2 = landmarks.part(y[xy]).y
            dist.append(int(math.sqrt((x2 - x1)**2 + (y2 - y1)**2)))
        avg_dist = (dist[0]+dist[1]+dist[2]+dist[3])/4.0
        cv2.putText(frame,str(avg_dist),(550,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        if avg_dist < 6.5:
            count_check += 1
            cv2.putText(frame,"Count: "+str(count_check),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            if count_check >= eye_ar_consec_frames:
                play = True
            if play and not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play(-1)
                    
        else:
            count_check = 0
            cv2.putText(frame,"Count: "+str(count_check),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
            play = False
            pygame.mixer.music.stop()
            
        ## Display Landmarks ##
        for n in range(68):
            x1 = landmarks.part(n).x
            y2 = landmarks.part(n).y
            cv2.circle(frame,(landmarks.part(n).x,landmarks.part(n).y),2,(0,255,0),-1)
        #######################
        
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()