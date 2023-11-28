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
