import cv2
import dlib
import numpy as np

#Dlib의 얼굴 및 눈 감지기 초기화
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#기본 카메라 열기
cap = cv2.VideoCapture(0) 
