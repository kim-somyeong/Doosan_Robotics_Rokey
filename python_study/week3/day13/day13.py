'''
#모듈 활용
import Circle
import Rectangle

r= Rectangle.Rectangle(10, 20, 20, 10) #class name.class 생성자()
print(r.calcArea())

c= Circle.Circle(10, 10, 20)
print(c.calcArea())

#dice1 
import dice1
print(dice1.throwDice())
print(dice1.throwDice())

#dice2
import dice2

print(dice2.throwDice())

#from ... import
from Rectangle import Rectangle

r= Rectangle(1, 30, 20, 10)
print(r.calcArea())

from dice1 import throwDice

print(throwDice())

#TestingDice3
import dice3 #dice3.py 모듈 먼저 실행 후 TestingDice3.py 코드가 실행

print("Testing dice3 module")

for i in range(3):
    print(dice3.throwDice())

#TestDice4.py
import dice4

print("Testing dice4 module")
print(f'TestingDice4 : _name__ = {__name__}')
for i in range(3):
    print(dice4.throwDice())

#TestDice5.py
import dice5

print("Testing dice5 module")
print(f'TestDice5 : __name__={__name__}')
for i in range(3):
    print(dice5.throwDice())

#date class
from datetime import date #datetime module, date class

d= date.today()
print(d)

print(d.weekday())

d2= date(1974, 1, 3)
print(d2.weekday())

s= d.strftime("%Y / %m / %d")
print(s)

print(d.strftime("%Y %m %d, date :%a"))

print(d.strftime("year : %Y, month : %m, day : %d, date : %A"))

#실습문제1
import glob, sys

lst= []

if len(sys.argv) == 1:
    lst= glob.glob("*")
else:
    lst= glob.glob(sys.argv[1])

if len(lst) == 0:
    print("Anything match the file")
else:
    for name in lst:
        print(name)

#문제5
import datetime

def date():
    #(1)
    d=datetime.date.today()
    print(d)

    #(2)
    s= d.strftime("%Y 년 %m 월 %d 일 요일 : %A")
    print(s)

def time():
    #(3)
    t= datetime.time(12, 35, 25)
    t_time= t.strftime("%H 시 %M 분 %S초")
    print(t_time)

date()
time()

#문제6
import time

t1= time.time() #Epoch times 초 단위로 얻기

print(f'현재까지 {t1}초가 흘렀습니다.')

#문제7
import time_utils
import time

print("Current time:", time_utils.current_time()) # a
print("Sleeping for 2 seconds...")
start_time = time.time()
time_utils.sleep_for(2) # b
print("Current time:", time_utils.current_time()) # c
print("Elapsed time after sleeping:", time_utils.time_elapsed(start_time), "seconds")

'''
#문제8
import Triangle

def main():
    t= Triangle.Triangle(0,0,0,0,0,0) #초기값 0으로 설정
    t.getCoordsInfo()
    area= t.calcArea()
    print(f'삼각형의 면적 :{area}')

main()