import cv2
import dlib
import numpy as np

#Dlib�� �� �� �� ������ �ʱ�ȭ
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

<<<<<<< HEAD
# 감지할 색상 범위 정의 (HSV 형식)
<<<<<<< HEAD
lower_color = np.array([1, 1, 0])
=======
lower_color = np.array([1, 0, 0])
>>>>>>> a3d6b0eb2b8f4927b0de66e9b54ca589cb139fb9
upper_color = np.array([255, 255, 255])

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    ret, frame = cap.read()
    if not ret:
        break
    # 그레이 스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #얼굴 감지
    faces = detector(gray)
    # BGR을 HSV로 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 지정한 색상 범위에 해당하는 부분을 찾기
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # 원본 이미지에서 색상에 해당하는 부분만 추출
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # 결과 이미지 출력
    cv2.imshow('Color Detection', result)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 사용한 자원 해제
cap.release()
cv2.destroyAllWindows()

#주석 처리를 추가해보는 ozno
=======
#�⺻ ī�޶� ����
cap = cv2.VideoCapture(0) 
>>>>>>> ba693a7dfb18d1754596999beefb607c444fc8a3
