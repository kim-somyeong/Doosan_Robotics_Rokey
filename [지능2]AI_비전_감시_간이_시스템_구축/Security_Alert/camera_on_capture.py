import cv2
import datetime

# 카메라 장치 번호 (필요 시 변경하세요)
cap = cv2.VideoCapture(0)  

# 카메라 열기 확인
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# 프레임 읽고 캡처 기능 추가
while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break

    # 화면에 프레임을 보여줌
    cv2.imshow("Camera Feed", frame)

    # 키 입력을 기다림
    key = cv2.waitKey(1) & 0xFF

    # 'c' 키를 누르면 현재 프레임을 캡처
    if key == ord('c'):
        # 캡처 파일 이름을 현재 날짜와 시간으로 생성
        filename = datetime.datetime.now().strftime("capture_%Y%m%d_%H%M%S.png")
        cv2.imwrite(filename, frame)
        print(f"이미지가 저장되었습니다: {filename}")

    # 'q' 키를 누르면 종료
    elif key == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
