'''
print("백슬래시를 표현하려면 \\를 써야합니다")
print("첫 \t번째 문장 \n 새로운 문장")
print("문자열 상수에서 큰 따옴표 \" 표현 방법")
print('문자열 상수에서 큰 따옴표 " 표현 방법')
print('문자열 상수에서 작은 따옴표 \'표현 방법')
print("문자열 상수에서 작음 따옴표 ' 표현 방법")
'''

'''
print(2+5)
print(2-5)
print(2*5)
print(5/2)
print(5//2)
print(5%2)
print(2/5)
print(2//5)
print(2**5)
print("----------------")
print(2.3+5.2)
print(2.3-5.2)
print(2.3*5.2)
print(5.2/2.3)
print(5.2//2.3)
print(5.2%2.3)
print(2.3/5.2)
print(2.3//5.2)
print(2.3**5.2)
'''

'''
print((22.44*30)/(13.10+40))
'''
'''
#실습문제2
a=50
b=25
c=10
d=5

print((a+b)*c/d-b)

#실습문제3
a=15
b=6
c=3
d=2

print(a*(b+c)/d+b-c)

#실습문제4
a=8
b=4
c=2
d=1

print((a+b)*c/(d+b)-a)

#실습문제5
a=2
b=3
c=4

print(a**b+b**c-(a+c))

#실습문제6
a=100
b=7
c=3

print((a%b)*c+b//c)

#실습문제7
a=12
b=5
c=3
d=2

print((a//b+c)**d-a%c)

#실습문제8
a=15.5
b=2.3
c=4.1

result = (a/b)+(c*b)-(a//c)

print(result)

#실습문제9
a=9
b=3
c=2
d=4
e=5

result = (((a+b*c)//d)**e-a%b)

print(result)

'''

'''

#실습문제1

print("*"*3, "*"*3, "*"*3, sep="\n")

#실습문제2

str1= "Python"
str2= "Programming"

print(str1+str2)

#실습문제3

str1= "Data"
str2= "Science"

print(str1+" "+str2)
print(str1,str2,sep=' ')

#실습문제4

num1=123
num2=456

print(str(num1)+str(num2))

#실습문제5

str1 = "Repeat"

print(str1*5)

#실습문제6

str1= "Echo"

print(str1, str1, str1, sep=' ')

#실습문제7

str1= "Line"

print((str1+"\n")*4)

#실습문제8

str1= "Hello"
str2= "World"

print(str1*2+str2*2)

#실습문제9

str1= "Fun"
str2= "Python"

result= str1*3+str2*3

print(result*2)

#실습문제10

str1= "Python"
n=3
str2= "Rocks"

print(str1*n+str2)

#실습문제11

str1= "AB"
n1= 2
str2= "CD"
n2= 3

print(str1*n1+str2*n2)

#실습문제12
str1= "123"
n= 4
str2= "-"

print((str1+str2)*(n-1)+str1)

#실습문제13

str1= "Cat"
n=5
char= "*"

print((str1+char)*(n-1)+str1)

'''

'''
#과제 코딩 시작

#문제4
print('그가 "안녕하세요"라고 말했다')

#문제6
print(int(111-222-3333))

#문제7
print("She said, \"It's a beautiful day.\"")
print("He replied, \"Yes, it is!\"")


#문제8
omega= '\u03A9'

smile= '\U0001F60A'

print(omega, smile)

#문제10
num = 124.578
re_num = int(num * 100) / 100  
print(re_num) 

#문제11
str1= "디비딥 "
str2= "딥디비딥"
str3= "디비디비딥 "

print(str1*2+str2)
print(str3+str2)
print(str1*2+str2)


#문제13

a= input("네자릿수 정수를 입력하세요 : ")

num= a[::-1]

print("입력한 정수의 역순 : ", num)

#문제14

a1=1
b1=4
a2=3.5
b2=2.4

distance= ((a2-a1)**2+(b2-b1)**2)**(1/2) 

print(distance)

#문제15

day= 265
month_day= 30

month= (day-1)//month_day+1
date= (day-1) % month_day+1

print(f"오늘은 {month}월 {date}일 입니다.")

#문제16

a= float(input("첫번째 실수를 입력해주세요: "))
b= float(input("두번째 실수를 입력하세요: "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)


num= int(input("숫자를 입력해주세요 : "))

a= bin(num)
b= oct(num)
c= hex(num)

print(a,b,c)


#문제19

a= float(0.1)
b= float(0.2)

print(a+b)
'''


#문제20

from tkinter import *

win = Tk()


win.title("hello")

btn = Button(win, fg='red', bg='yello', text='btn')

win.geometry("640x480")

btn.pack()

win.mainloop()