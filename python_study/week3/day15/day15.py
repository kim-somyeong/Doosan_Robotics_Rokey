'''
#turtle
import turtle as t
t.shape('turtle')
print(t.shape)
t.exitonclick() #state the page

#turtle move
import turtle as t
t.shape('turtle')
print(t.shape)
t.forward(100)
t.exitonclick() #state the page

#turtle make rectangle
import turtle as t
t.shape('turtle')
print(t.shape)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.exitonclick() #state the page

#make rectangle used 'for'
import turtle as t

t.shape('turtle')
print(t)
for i in range(4):
    t.forward(100)
    t.right(90)

t.exitonclick()

#make pentagon
import turtle as t

t.shape('turtle')
print(t)
for i in range(5):
    t.forward(100)
    t.right(360/5)
t.exitonclick()

#make polygon
import turtle as t

n= int(input('write that you want to make polygon : '))
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.exitonclick()

#fill the color
import turtle as t

n=6
t.shape('turtle')
t.color('red')
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.end_fill()
t.exitonclick()

#circle
import turtle as t

t.shape('turtle')
t.circle(120)
t.exitonclick()

#make circle used 'for'
import turtle as t

n=60
t.shape('turtle')
t.speed('fastest')  #turtle speed -> fastest
for i in range(n):
    t.circle(120)
    t.right(360/n)
t.exitonclick()

#intricate pattern
import turtle as t

t.shape('turtle')
t.speed('fastest')

for i in range(300):
    t.forward(i)
    t.right(91)
t.exitonclick()

#make a start used turtle
import turtle

def draw_star():
    screen= turtle.Screen()
    screen.bgcolor("black")
    star=turtle.Turtle()
    star.speed(1)
    color= ['red', 'yellow','blue','green','purple']

    for i in range(5):
        star.color(color[i])
        star.forward(100)
        star.right(144)

    star.hideturtle()
    screen.mainloop()

draw_star()

#make a rainbow
import turtle

def draw_rainbow_circles():
    screen= turtle.Screen()
    screen.bgcolor("black")
    rainbow= turtle.Turtle()
    rainbow.speed(0)
    colors= ['red','orange','yellow','green','blue','indigo','violet']
    radius= 50

    for color in colors:
        rainbow.color(color)
        rainbow.circle(radius)
        radius +=10

    rainbow.hideturtle()
    screen.mainloop()

draw_rainbow_circles()

#PyQt5
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app= QApplication(sys.argv)
    w= QWidget()
    b= QLabel(w)
    b.setText("Hello World")
    w.setGeometry(100,100,200,50)
    b.move(50, 20)
    w.setWindowTitle("PyQt5")
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()

#class
import sys
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*

class window(QWidget):  #QWidget 을 상속받는 window 클래스 정의
    def __init__ (self, parent=None):        #클래스 초기화 메서드
        super(window, self).__init__(parent) #부모 클래스인 QWidget의 초기화 메서드 호출
        self.resize(200,50)                  #창의 크기
        self.setWindowTitle("PyQt5")
        self.label= QLabel(self)            #QLabel 객체를 생성하여 self 위에 배치
        self.label.setText("Hello World")
        font= QFont()                       #글꼴
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.move(50,20)

def main():
    app= QApplication(sys.argv)          #QApplication 객체를 생성
    ex= window()                         #window 클래스 인스턴스 생성
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

#QLineEdit
import sys
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*

def window():
    app= QApplication(sys.argv)
    win= QWidget()

    e1= QLineEdit()
    e1.setValidator(QIntValidator())
    e1.setMaxLength(4)
    e1.setAlignment(Qt.AlignRight)
    e1.setFont(QFont("Arial", 20))

    e2= QLineEdit()
    e2.setValidator(QDoubleValidator(0.99,99.99,2))

    flo= QFormLayout()
    flo.addRow("integer validator", e1)
    flo.addRow("Double validator", e2)

    e3= QLineEdit()
    e3.setInputMask('+99_9999_999999')
    flo.addRow("Input Mask", e3)

    e4= QLineEdit()
    e4.textChanged.connect(textchanged)
    flo.addRow("Text changed", e4)

    '
    '
    '
    '


#문제3
import turtle as t

t.shape('turtle')
print('turtle')
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.exitonclick()

#문제4
import turtle as t

t.shape('turtle')
for i in range(4):
    t.forward(100)
    t.right(90)
t.hideturtle()
t.exitonclick()

#문제5
import turtle as t

t.shape('turtle')
n= 6
for i in range(n):
    t.forward(100)
    t.right(360/n)
t.exitonclick()

#문제6
import turtle

t = turtle.Turtle()

t.pencolor("blue")

t.fillcolor("red")
t.begin_fill()
t.circle(100)
t.end_fill()

turtle.done()

#문제7
import turtle

t=turtle.Turtle()

t.circle(120,90)

t.left(90)
t.forward(120)
t.left(90)
t.forward(120)

turtle.done()

#문제8
import turtle

turtle.speed(0)
turtle.bgcolor("black")

colors= ['red','yellow','blue','green']

for i in range(100):
    turtle.color(colors[i%4])
    turtle.forward(i*4)
    turtle.left(91)
turtle.done()

#문제9
import turtle

t= turtle.Turtle()
screen= turtle.Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_right():
    t.right(5)

def move_left():
    t.left(5)

screen.onkeypress(move_forward, "Up")
screen.onkeypress(move_backward, "Down")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "Left")

screen.listen()
screen.mainloop()

#문제10
import matplotlib.pyplot as plt  #yplot 모듈은 다양한 유형의 그래프를 그릴 때 사용

x= [1, 2, 3, 4, 5]
y=[2, 3, 5, 7, 11]

#x, y 데이터 포인트를 인자로 받아서 산포 그래프를 그린다.
#점은 파란색, 원형으로 설정
plt.scatter(x, y, color= 'blue', marker= 'o')

plt.title('Scatter Plot of x vs y') #그래프의 제목
plt.xlabel('x')                     #x축 레이블 설정
plt.ylabel('y')                     #y축 레이블 설정

plt.show()

#추가문제1
import numpy as np
import matplotlib.pyplot as plt
import random

x=np.random.normal(size=100)
y= 2.5 * x + np.random.normal(size=100)

plt.scatter(x, y, color= 'blue', marker= 'o')

plt.title('Scatter Plot of x vs y ')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

'''
