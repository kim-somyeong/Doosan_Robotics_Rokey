'''
#smartphoen class
class SmartPhone:
    def __init__(self, name, phonenum, battery):  #생성자 : __init__(self, 매개 변수 리스트)-> 주로 멤버 변수를 생성하고 초기화시키는 목적
        self.owner= name
        self.number= phonenum
        self.battery= battery

    def printMemberVariables(self):  #멤버 변수를 화면에 출력하는 printMemberVariables 함수를 클래스에 추가
        print(f"owner= {self.owner}, phone number= {self.number}, battery= {self.battery}")

#객체 생성
sp1= SmartPhone("Cho","010-1111-1111",80)
sp2= SmartPhone("Lim","010-2222-2222",70)
#멤버 함수 호출
sp1.printMemberVariables()
sp2.printMemberVariables()

#smartphoen class version 2
class SmartPhone:
    def __init__(self, name, phonenum, battery):  #생성자 : __init__(self, 매개 변수 리스트)-> 주로 멤버 변수를 생성하고 초기화시키는 목적
        self.owner= name
        self.number= phonenum
        self.battery= battery

    def call(self, phoneNum):
        if self.battery>=10:
            print(f'{self.number}에서 {phoneNum}으로 전화를 겁니다.')
            self._hwCall(phoneNum)
        else:
            print('배터리가 부족합니다.')

    def getBatteryStatus(self):  
        return self.battery

    def _hwCall(self, phoneNum):
        print(f'하드웨어를 제어해서 {phoneNum}으로 전화를 겁니다.')

#객체 생성
sp1= SmartPhone("Cho","010-1111-1111",80)
sp2= SmartPhone("Lim","010-2222-2222",70)

sp1.call("010-3333-3333")
sp2.call("010-4444-4444")

print(f'sp1의 배터리 충전 상태 : {sp1.getBatteryStatus()}')
print(f'sp2의 배터리 충전 상태 : {sp2.getBatteryStatus()}')

#문제7
class Rectangle:
    def __init__(self, x, y, width, height): #__init__을 사용함으로써 사각형 객체 초기화
        self.x= x
        self.y= y
        self.width= width
        self.height= height

    def display(self):
        print(f'Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}')

rect= Rectangle(10, 20, 30, 40)
rect.display()

#문제8
class Parent:
    def foo(self):
        print("Parent's foo() method")

class Child(Parent):
    def foo(self):
        print("Child foo() method. ")
        super().foo()  #부모 클래스의 foo() 매서드 호출

child= Child()
child.foo()

#추가문제1
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x= x
        self.y= y
        self.width= width
        self.height= height

    def display(self):
        print(f'Rectangle x, y : {self.x},{self.y}, width : {self.width}, height :{self.height}')

rect=Rectangle(20,20,30,30)
rect.display()

#추가문제2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle initialized: {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, horsepower):
        super().__init__(brand, model) # 부모 클래스의 생성자 호출
        self.horsepower = horsepower
        print(f"Car initialized: {self.brand} {self.model} with {self.horsepower} HP")

# 객체 생성
my_car = Car("AAA", "BBB", 350)

#추기문제3
import math

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        # Write your code here
        self.x1= x1
        self.y1= y1
        self.x2= x2
        self.y2= y2


    def calcArea(self):
         # Write your code here
        return(self.x2 - self.x1) * (self.y2 - self.y1)

class Circle:
    def __init__(self, x, y, r):
        # Write your code here
        self.x= x
        self.y= y
        self.r= r


    def calcArea(self):
        # Write your code here
        return math.pi * self.r**2

shapeList = []

shapeList = []

for i in range(3):
    s = input("도형 모양을 입력하세요 (1:사각형 0:원): ")
    if s == "1":
        x1 = int(input("왼쪽 상단의 x좌표를 입력: "))
        y1 = int(input("왼쪽 상단의 y좌표를 입력: "))
        x2 = int(input("오른쪽 하단의 x좌표를 입력: "))
        y2 = int(input("오른쪽 하단의 y좌표를 입력: "))
        shapeList.append(Rectangle(x1, y1, x2, y2))
    elif s == "0":
        x = int(input("원의 중심 x 좌표를 입력: "))
        y = int(input("원의 중심 y 좌표를 입력: "))
        r = int(input("원의 반지름을 입력: "))
        shapeList.append(Circle(x, y, r))
for s in shapeList:
    print(f"면적: {s.calcArea()}")

#추가문제4
import math
class Rectangle:
    def __init__(self):
        #사각형의 좌표 초기화
        self.x1= 0
        self.y1= 0
        self.x2= 0
        self.y2= 0

    def calcArea(self):
        # 사각형의 면적
        return (self.x2 - self.x1) * (self. y2 - self. y1)

    def getCoordsInfo(self):
        self.x1 = int(input("왼쪽 상단의 x 좌표값을 정수로 입력하세요: "))
        self.y1 = int(input("왼쪽 상단의 y 좌표값을 정수로 입력하세요: "))
        self.x2 = int(input("오른쪽 하단의 x 좌표값을 정수로 입력하세요: "))
        self.y2 = int(input("오른쪽 하단의 y 좌표값을 정수로 입력하세요: "))

class Circle:
    def __init__(self):
        # 원의 중심 좌표 및 반지름 초기화
        self.x= 0
        self.y= 0
        self.r= 0

    def calcArea(self):
        # 원의 넓이
        return math.pi * self.r**2

    def getCoordsInfo(self):
        #사용자로부터 값 입력받기
        self.x= int(input('원의 중심 x 좌표값을 정수로 입력 : '))
        self.y= int(input('원의 중심 y 좌표값을 정수로 입력 : '))
        self.r= float(input("원의 반지름 값 입력 : "))

shapeList = []
for i in range(3):
    s = input("도형 모양을 입력하세요 (1:사각형 0:원): ")
    if s == "1":
        rect = Rectangle()
        rect.getCoordsInfo()
        shapeList.append(rect)
    else:
        circle = Circle()
        circle.getCoordsInfo()
        shapeList.append(circle)
for s in shapeList:
    print(f'도형의 면적 :{s.calcArea()}')

#추가문제5
class Point:
    def __init__(self, x, y):
        self.x= x
        self.y= y

    #x, y를 변경할 수 있는 멤버 함수 구현 -> 좌표를 변경하는 메서드
    def setX(self, x):
        self.x= x

    def setY(self, y):
        self.y= y
    
    #x, y를 각각 반환하는 함수
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
point= Point(10, 20)

print(f' 초기 x 좌표 : {point.getX()}, 초기 y 좌표 : {point.getY()}')

point.setX(30)
point.setY(40)

print(f' 변경된 x 좌표 : {point.getX()}, 변경된 y 좌표 : {point.getY()}')

'''
#추가문제6
