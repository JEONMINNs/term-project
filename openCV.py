import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 감지할 색상 범위 정의 (HSV 형식)
lower_color = np.array([0, 0, 0])
upper_color = np.array([150, 150, 150])

while True:
    # 프레임 읽기
    ret, frame = cap.read()

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
