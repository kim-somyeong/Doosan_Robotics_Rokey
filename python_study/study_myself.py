'''
#no.7
person_info={
    "이름":"김영희",
    "전화번호":"010-1111-2222",
    "성별":"여자",
    "나이":23,
    "대학교":"한국대학교"
}

for key, value in person_info.items():
    print(f"{key} : {value}")

#no.9
stock_prices={
    'samsung sds': 242000,
    'samsung dx': 67000,
    'nc soft': 52000,
    'handy soft': 5120,
    'golfzon': 215000,
    'kia': 65000
}

stock_name= input('write the company : ')

if stock_name in stock_prices:
    print(f"{stock_name}: {stock_prices[stock_name]}")

else:
    print("can't find the company.")

#rectangle

import math

class Renctangle:
    def __init__(self, x, y, width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height

    def calcArea(self):
        return (self.x2-self.x1)*(self.y2-self.y1)

class Circle:
    def __init__(self, x, y, r):
        self.x= x
        self.y= y
        self.r= r
    
    def calcArea(self):
        return math.pi * self.r * self.r
    
shapeList=[]
for i in range(3):
    s= input('choose the shape(1. rectangle, 2.circle) : ')
    if s==1:
        x1= int(input('write the upper x:'))
        y1= int(input('write the lower x :'))
        x2= int(input('write the upper x2: '))
        y2= int(input('write the lower y : '))
        shapeList.append(Renctangle(x1, y1, x2, y2))
    else:
        x= int(input('write the x location :'))
        y= int(input('write the y location : '))
        r= int(input('write the circle r :'))
        shapeList.append(Circle(x, y, r))

for s in shapeList:
    print(f'area : {s.calcArea}')

'''
