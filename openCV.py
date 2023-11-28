import cv2
import dlib
import numpy as np

# Initialize Dlib's face and eye detectors
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Open the camera
cap = cv2.VideoCapture(0)  # 0 indicates the default camera.

while True:
    # Read the frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    for face in faces:
        # Coordinates of the entire face
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Calculate coordinates for the top half of the face
        y_top = max(y, y + h // 3)

        # Detect eyes
        landmarks = predictor(gray, face)
        for n in range(36, 48):  # Eyes are represented by landmarks from 36 to 47
            x_eye = landmarks.part(n).x
            y_eye = landmarks.part(n).y

            # Calculate coordinates around the eyes
            x1 = max(0, x_eye - 5)
            y1 = max(0, y_eye - 5)
            x2 = min(frame.shape[1], x_eye + 5)
            y2 = min(frame.shape[0], y_eye + 5)

            # Mosaic the surrounding area excluding the eyes from the face
            if y1 < y2 and x1 < x2:
                # Region to be mosaic
                mosaic_region = frame[y_top:y + h, x:x + w]

                # Mosaic size specification
                mosaic_size = (10, 10)

                # Apply mosaic
                mosaic = cv2.resize(mosaic_region, mosaic_size, interpolation=cv2.INTER_NEAREST)
                frame[y_top:y + h, x:x + w] = cv2.resize(mosaic, mosaic_region.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    # Display the result
    cv2.imshow('Mosaic Face without Eyes', frame)

    # Exit condition (ESC key)
    if cv2.waitKey(1) == 27:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
