# -*- coding: utf-8 -*-
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

# �뼹援� 媛먯��
    faces = detector(gray)

    for face in faces:
        # �뼹援� �쟾泥� 醫뚰몴
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # �쐵履� �젅諛� 醫뚰몴 怨꾩궛
        y_top = max(y, y + h // 3)

        # �늿 媛먯��
        landmarks = predictor(gray, face)
        for n in range(36, 48):  # 36遺��꽣 47源뚯���뒗 �늿 遺�遺�
            x_eye = landmarks.part(n).x
            y_eye = landmarks.part(n).y

            # �늿 二쇰�� 醫뚰몴 怨꾩궛
            x1 = max(0, x_eye - 5)
            y1 = max(0, y_eye - 5)
            x2 = min(frame.shape[1], x_eye + 5)
            y2 = min(frame.shape[0], y_eye + 5)

            # �뼹援댁뿉�꽌 �늿�쓣 �젣�쇅�븳 二쇰�� 遺�遺� 紐⑥옄�씠�겕 泥섎━
            if y1 < y2 and x1 < x2:
                # 紐⑥옄�씠�겕 泥섎━�븷 遺�遺�
                mosaic_region = frame[y_top:y + h, x:x + w]
