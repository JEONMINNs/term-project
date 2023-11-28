import cv2
import dlib
import numpy as np

# Dlib의 얼굴 및 눈 감지기 초기화
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# 카메라 열기
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 의미합니다.

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 그레이 스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴 감지
    faces = detector(gray)
