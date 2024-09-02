import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QRadioButton, QButtonGroup

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # 윈도우의 타이틀과 크기 설정
        self.setWindowTitle('PyQt 예제')
        self.setGeometry(100, 100, 300, 250)  # 창의 위치와 크기를 설정합니다.

        # UI 설정을 위한 메서드 호출
        self.initUI()

    def initUI(self):
        # 레이블 생성
        self.label = QLabel('안녕하세요, PyQt!', self)  # 기본 텍스트를 가진 레이블 위젯 생성

        # 텍스트 박스 생성
        self.textbox = QLineEdit(self)  # 사용자 입력을 받을 수 있는 텍스트 박스 생성
        self.textbox.setPlaceholderText('여기에 텍스트를 입력하세요')  # 텍스트 박스에 placeholder 텍스트 추가 

        # 버튼 생성
        self.button = QPushButton('버튼 클릭', self)  # 클릭 버튼 생성
        self.button.clicked.connect(self.on_button_click)  # 버튼 클릭 시 on_button_click 메서드를 호출하도록 연결

        # 종료 버튼 생성
        self.exit_button = QPushButton('종료', self)  # 종료 버튼 생성
        self.exit_button.clicked.connect(self.close)  # 종료 버튼 클릭 시 애플리케이션을 종료하도록 연결

        # 라디오 버튼 생성
        self.radio1 = QRadioButton('옵션 1', self)
        self.radio2 = QRadioButton('옵션 2', self)
        self.radio3 = QRadioButton('옵션 3', self)

        # 라디오 버튼 그룹화
        self.radio_group = QButtonGroup(self)
        self.radio_group.addButton(self.radio1)
        self.radio_group.addButton(self.radio2)
        self.radio_group.addButton(self.radio3)

        # 수직 레이아웃 생성
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)  # 레이블을 수직 레이아웃에 추가
        vbox.addWidget(self.textbox)  # 텍스트 박스를 수직 레이아웃에 추가
        vbox.addWidget(self.button)  # 버튼을 수직 레이아웃에 추가

        # 라디오 버튼을 수직 레이아웃에 추가
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(self.radio3)

        # 수평 레이아웃 생성
        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 수평 레이아웃의 나머지 공간을 차지하도록 설정
        hbox.addWidget(self.exit_button)  # 종료 버튼을 수평 레이아웃에 추가

        # 수직 레이아웃에 수평 레이아웃 추가
        vbox.addLayout(hbox)

        # 수직 레이아웃을 윈도우의 레이아웃으로 설정
        self.setLayout(vbox)

    # 버튼 클릭 시 호출되는 메서드
    def on_button_click(self):
        text = self.textbox.text()  # 텍스트 박스에서 텍스트를 가져옴
        selected_radio = self.radio_group.checkedButton()  # 선택된 라디오 버튼을 가져옴
        if selected_radio:
            radio_text = selected_radio.text()  # 선택된 라디오 버튼의 텍스트를 가져옴
            self.label.setText(f'입력한 텍스트: {text}\n선택된 옵션: {radio_text}')  # 레이블의 텍스트를 텍스트 박스와 선택된 라디오 버튼의 내용으로 변경
        else:
            self.label.setText(f'입력한 텍스트: {text}\n선택된 옵션: 없음')  # 선택된 라디오 버튼이 없을 때의 처리

if __name__ == '__main__':
    app = QApplication(sys.argv)  # QApplication 객체 생성, 애플리케이션을 실행할 준비
    mainWindow = MyApp()  # MyApp 클래스의 인스턴스 생성
    mainWindow.show()  # 윈도우를 화면에 표시
    sys.exit(app.exec_())  #
