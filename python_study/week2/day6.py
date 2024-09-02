'''
#실습문제1

def isLeapYear(year):
    return (year % 400 == 0) or (year% 4 ==0 and year%100 != 0)

print(isLeapYear(1234))
print(isLeapYear(1900))
print(isLeapYear(2000))
print(isLeapYear(2204))


#실습문제2

def getSecondWord(s):
    s=s.strip()
    pos1= s.find(' ')
    pos2= s.find('\t')
    pos3= s.find('\n')
    p1= max(pos1, pos2, pos3) + 1
    s2= s[p1:]
    pos1= s2.find(' ')
    pos2= s2.find('\t')
    pos3= s2.find('\n')
    p2= max(pos1, pos2, pos3)
    if p2== -1:
        p2 = len(s)
    else:
        p2+=p1
    
    return s[p1:p2]

print(getSecondWord("what a beautiful day"))
print(getSecondWord("Beautiful day"))

#예제
def printMinusNunber(num):
    if num>= 0:
        return
    else:
        print(num)

print(printMinusNunber(3))
print(printMinusNunber(-5))

#예제
def add(num1, num2, num3):
    return num1 + num2 + num3

s= add(2, 3, 5)
print(s)
s= add(num3=5, num2=3, num1=2)
print(s)

#예제
def printNum(n1=1, n2=10):
    print(f"n1 = {n1}, n2 = {n2}")

printNum()
printNum(3,13)

#실습문제3
def CompareScores(score1, score2, score3, order=True):
    if order: #내림차순
        if score1>= score2 and score1>= score3:
            if score2>= score3:
                print(score1, score2, score3)
            else:
                print(score1, score3, score2)
        elif score2>=score3 and score2>= score1:
            if score1>= score3:
                print(score2, score1, score3)
            else:
                print(score2, score3, score1)
        else:
            if score1 >= score2:
                print(score3, score1, score2)
            else:
                print(score3, score2, score1)

    else: #오름차순
        if score1 < score2 and score1 < score3:
            if score2< score3:
                print(score1, score2, score3)
            else:
                print(score1, score3, score2)
        elif score2 < score1 and score2< score3:
            if score1 < score3:
                print(score2, score1, score3)
            else:
                print(score2, score3, score1)
        else:
            if score1< score2:
                print(score3, score1, score2)
            else:
                print(score3, score2, score1)
    
print("내림차순")
CompareScores(85, 80, 90)
print("오름차순")
CompareScores(85, 80, 90, False)

#예제
sum = 0
def add(a, b, c):
    sum= a+b+c
    print(sum)

add(3, 2, 4)
print(sum) #해당 sum은 내부가 아닌 외부 변수값 출력

#예제
sum= 0
def add(a, b, c):
    global sum  #먼저 만들어진 외부 변수를 함수 내부에서 사용하겠다는 의미임.
    sum= a+b+c
    print(sum)

add(3, 2, 4)
print(sum)


#재귀호출
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(1))
print(factorial(10))

#재귀호출 최대공약수
def gcd(m, n):
    if m == n:
        return m
    elif m > n:
        return gcd(m-n, m)
    else:
        return gcd(m, n-m)
    
print(gcd(12, 4))
print(gcd(12, 18))

#재귀호출 피보나치
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(6))


#실습문제4
def Sum(n):
    if n == 1:
        return 1
    return n + Sum(n-1)

print(Sum(1))
print(Sum(10))
print(Sum(100))

#실습문제5
def add_numbers(a, b):
    return a+b
result = add_numbers(3,5)
print(result)

#실습문제5-1
def reverse(s):
    return s[::-1]
print(reverse("hello"))

#실습문제6
def upper(s):
    return s[0].upper() + s[1:]
print(upper("upper"))

'''
'''
#문제2
def add(num1, num2, num3):
    return num1 + num2 + num3
#print(add(2,3,5))
#print(add(2, num3=5, num2=3))
#print(add(2, num3= "5", num2="3"))
print(add(2, num2=3, 5))


print(2, 3, sep=",")

#문제5
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
print(sum(100))

#문제6
humid= float(input('write humid : '))
temperature= float(input('write temperature : '))

import math
d1 = math.log(humid / 100)
d2 = (17.62 * temperature) / (243.12 + temperature)
water = (243.12 * (d1+d2)) / (17.62-(d1+d2))

print(f'humidity : {humid}, temperature : {temperature}, dew point : {water}')


#문제7
def printDate(year, month, day):
    print(f'Year : {year}')

    months=["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    month_name = months[month-1]
    print(f'Month : {month_name}')

    print(f'Day : {day}')

printDate(2022, 9, 20)
printDate(2023, 3, 3)

#문제8
def countWord(s):
    word= s.split()
    return len(word)

s= "Hello World"
print(countWord(s))


#문제10
def getWord(line, num):
    word= line.split()  #문자열을 공백을 기준으로 리스트 만들기
    if 1<= num <= len(word):
        return word[num-1]
    else:
        return None
print(getWord("A beautiful day", 3))


#문제11
def year(num):
    if num % 4 ==0:
        if num % 100:
            print('False')
        else:
            print('True')
    else:
        print('False')

num= int(input('write year : '))
year(num)


#문제12
def getSecondWord(s):
    s=s.strip()
    pos1 = s.find(' ')
    pos2 = s.find('\t')
    pos3 = s.find('\n')
    p1 = max(pos1, pos2, pos3) + 1
    s2 = s[p1:]
    pos2 = s2.find(' ')
    pos2 = s2.find('\t')
    pos2 = s2.find('\n')
    p2 = max(pos1, pos2, pos3)

    if p2==-1:
        p2 = len(s)
    else:
        p2 +=p1
    
    return s[p1:p2]

print(getSecondWord("beautiful day"))

#문제13
def CompareScore(score1, score2, score3, order = True):
    if order: #True
        if score1 >= score2 and score1 >= score3:
            if score2 >= score3:
                print(score1, score2, score3)
            else:
                print(score1, score3, score2)
        elif score2 >= score1 and score2 >= score3:
            if score1 >= score3:
                print(score2, score1, score3)
            else:
                print(score2, score3, score2)
        else:
            if score1 >= score2:
                print(score3, score1, score2)
            else:
                print(score3, score2, score1)
        
    else:
        if score1 <= score2 and score1 <= score3:
            if score2 <= score3:
                print(score1, score2, score3)
            else:
                print(score1, score3, score2)
        elif score2 <= score1 and score2 <= score3:
            if score1 <= score3:
                print(score2, score1, score3)
            else:
                print(score2, score3,score1)
        else:
            if score1 <= score2:
                print(score3, score1, score2)
            else:
                print(score3, score2, score1)

print('내림차순')
CompareScore(85, 80, 90)
print('오름차순')
CompareScore(85, 80, 90, False)

#문제14
def fibonacci(n):
    if n == 1 or n == 2 :
        return 1
    else: 
        return fibonacci(n-1) * fibonacci(n-2)
    
print(fibonacci(1))
print(fibonacci(6))
'''

'''
#문제15
def gcd(m, n):
    if m == n:
        return m
    elif m > n:
        return gcd(m-n, n)
    else:
        return gcd(m, n-m)
    
print(gcd(12,4))
print(gcd(12,18))
'''

#문제 16
def reverse(n):
    return n[::-1]
print(reverse("hello"))

#문제17
def hello(*names):
      for each in names: #names 내의 모든 요소들을 순서대로 참조하는 순환문
            print('안녕, {}!'.format(each))
 
hello('민정')
hello('David','Veronica','Paul')
hello('방탄소년단','블랙핑크')

#문제18
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 