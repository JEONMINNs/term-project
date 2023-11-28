# -*- coding: utf-8 -*-
import cv2
import dlib
import numpy as np

# Dlib�� �� �� �� ������ �ʱ�ȭ
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# ī�޶� ����
cap = cv2.VideoCapture(0)  # 0�� �⺻ ī�޶� �ǹ��մϴ�.

while True:
    # ������ �б�
    ret, frame = cap.read()
    if not ret:
        break

    # �׷��� ������ ��ȯ
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # �� ����
    faces = detector(gray)

# 얼굴 감지
    faces = detector(gray)

    for face in faces:
        # 얼굴 전체 좌표
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # 윗쪽 절반 좌표 계산
        y_top = max(y, y + h // 3)

        # 눈 감지
        landmarks = predictor(gray, face)
        for n in range(36, 48):  # 36부터 47까지는 눈 부분
            x_eye = landmarks.part(n).x
            y_eye = landmarks.part(n).y

            # 눈 주변 좌표 계산
            x1 = max(0, x_eye - 5)
            y1 = max(0, y_eye - 5)
            x2 = min(frame.shape[1], x_eye + 5)
            y2 = min(frame.shape[0], y_eye + 5)

            # 얼굴에서 눈을 제외한 주변 부분 모자이크 처리
            if y1 < y2 and x1 < x2:
                # 모자이크 처리할 부분
                mosaic_region = frame[y_top:y + h, x:x + w]
