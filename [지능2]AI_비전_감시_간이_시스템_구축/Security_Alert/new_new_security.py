import cv2
import sys
import threading
from ultralytics import YOLO
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5 import QtGui, QtCore
import time

class YoloCameraApp:
    def __init__(self):
        self.model = YOLO('../Downloads/amr_best_500.pt')  # YOLO 모델 로드
        self.cap = cv2.VideoCapture(0)  # 카메라 인덱스 설정 (필요에 따라 변경)

        # PyQt5 GUI 설정
        self.app = QApplication(sys.argv)
        self.win = QWidget()
        self.vbox = QVBoxLayout()
        self.label = QLabel()
        self.vbox.addWidget(self.label)
        self.win.setLayout(self.vbox)
        self.win.show()

        # 스레드 설정
        self.running = True
        self.thread = threading.Thread(target=self.run_yolo)
        self.thread.start()

    def run_yolo(self):
        while self.running:
            ret, img = self.cap.read()
            if not ret:
                print("Cannot read frame.")
                break

            # YOLO 감지 수행
            results = self.model(img)
            annotated_frame = results[0].plot()
            annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

            # 특정 구역 설정 (우측 절반)
            height, width, _ = annotated_frame.shape
            detection_zone = (int(width / 2), 0, width, height)  # 우측 절반 영역
            cv2.rectangle(annotated_frame, (detection_zone[0], detection_zone[1]), 
                          (detection_zone[2], detection_zone[3]), (0, 0, 255), 2)  # 붉은색 테두리

            # 객체 침입 확인
            intrusion_detected = False
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # 바운딩 박스 좌표
                    score = float(box.conf[0])  # 객체 인식 정확도
                    
                    # 바운딩 박스가 우측 영역에 있고 정확도가 0.9 이상인 경우 침입으로 간주
                    if x1 >= detection_zone[0] and score >= 0.8:
                        intrusion_detected = True
                        break
                if intrusion_detected:
                    break

            # 침입 시 화면 깜빡임 효과
            if intrusion_detected:
                print("침입 감지: 화면 깜빡임 신호 발생!")
                self.label.clear()  # 화면 지우기 (깜빡임 효과)
                self.app.processEvents()
                time.sleep(0.1)  # 잠시 대기
                # 다시 화면 표시
                h, w, c = annotated_frame.shape
                qImg = QtGui.QImage(annotated_frame.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qImg)
                self.label.setPixmap(pixmap)
            else:
                # PyQt5로 이미지 표시 (침입 감지 없을 때)
                h, w, c = annotated_frame.shape
                qImg = QtGui.QImage(annotated_frame.data, w, h, w * c, QtGui.QImage.Format_RGB888)
                pixmap = QtGui.QPixmap.fromImage(qImg)
                self.label.setPixmap(pixmap)

            # PyQt 이벤트 처리
            self.app.processEvents()

    def stop(self):
        self.running = False
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    app = YoloCameraApp()
    app.app.aboutToQuit.connect(app.stop)
    sys.exit(app.app.exec_())

if __name__ == '__main__':
    main()