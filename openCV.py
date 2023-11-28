# -*- coding: utf-8 -*-
import cv2
import dlib
import numpy as np

# DlibÀÇ ¾ó±¼ ¹× ´« °¨Áö±â ÃÊ±âÈ­
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Ä«¸Ş¶ó ¿­±â
cap = cv2.VideoCapture(0)  # 0Àº ±âº» Ä«¸Ş¶ó¸¦ ÀÇ¹ÌÇÕ´Ï´Ù.

while True:
    # ÇÁ·¹ÀÓ ÀĞ±â
    ret, frame = cap.read()
    if not ret:
        break

    # ±×·¹ÀÌ ½ºÄÉÀÏ º¯È¯
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ¾ó±¼ °¨Áö
    faces = detector(gray)

# ì–¼êµ´ ê°ì§€
    faces = detector(gray)

    for face in faces:
        # ì–¼êµ´ ì „ì²´ ì¢Œí‘œ
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # ìœ—ìª½ ì ˆë°˜ ì¢Œí‘œ ê³„ì‚°
        y_top = max(y, y + h // 3)

        # ëˆˆ ê°ì§€
        landmarks = predictor(gray, face)
        for n in range(36, 48):  # 36ë¶€í„° 47ê¹Œì§€ëŠ” ëˆˆ ë¶€ë¶„
            x_eye = landmarks.part(n).x
            y_eye = landmarks.part(n).y

            # ëˆˆ ì£¼ë³€ ì¢Œí‘œ ê³„ì‚°
            x1 = max(0, x_eye - 5)
            y1 = max(0, y_eye - 5)
            x2 = min(frame.shape[1], x_eye + 5)
            y2 = min(frame.shape[0], y_eye + 5)

            # ì–¼êµ´ì—ì„œ ëˆˆì„ ì œì™¸í•œ ì£¼ë³€ ë¶€ë¶„ ëª¨ìì´í¬ ì²˜ë¦¬
            if y1 < y2 and x1 < x2:
                # ëª¨ìì´í¬ ì²˜ë¦¬í•  ë¶€ë¶„
                mosaic_region = frame[y_top:y + h, x:x + w]
