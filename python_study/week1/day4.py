'''
#if문
s= input("단어 한 개를 입력하세요: ")
if s=="hello":
    print("사용자가 입력한 단어가 hello입니다.")
'''

'''
#실습문제1

num= int(input("숫자 한 개를 입력하세요: "))

if num>=5:
    print("5보다 크거나 같습니다.")

if num<5:
    print("5보다 작습니다.")

'''
'''
#실습문제2

num= int(input("숫자를 입력하세요: "))

if num>=10:
    print("10보다 크거나 같습니다.")

else:
    if 5<=num<10:
        print("5보다 크거나 같지만 10보다 작습니다.")
    else:
        print("5보다 작습니다.")
        '''
'''
num= int(input("숫자를 입력하세요: "))

if num>=10:
    print("10보다 크거나 같습니다.")

elif 5<=num:
    print("5보다 크거나 같지만 10보다 작습니다.")

elif num<5:
    print("5보다 작습니다.")
'''
'''
num= int(input("숫자를 입력하세요: "))

if num>=10:
    print("10보다 크거나 같습니다.")

elif 5<=num:
    print("5보다 크거나 같지만 10보다 작습니다.")
    
else:
    print("5보다 작습니다.")

'''
'''
#if-elif-else문

score= int(input("점수를 입력하세요: "))

if score>=90:
    print("A")
if 80<=score<90:
    print("B")
if 70<=score<80:
    print("C")
if score<70:
    print("D")

score= int(input("점수를 입력하세요: "))

if score>=90:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
elif score<70:
    print("D")

score= int(input("점수를 입력하세요: "))

if score>=90:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
else:
    print("D")

'''
'''
#실습문제3

ticket= input("type of ticket: ")

if ticket=="VIP":
    print('150000')
elif ticket=="S":
    print('110000')
elif ticket=="A":
    print('90000')
elif ticket=="B":
    print('70000')
else:
    print("input wrong")
'''
'''
#윤년
year= int(input("year : "))

if year%4==0 and year % 100!=0:
    print("윤년입니다.")

elif year%400==0:
    print("윤년입니다.")

else:
    print("윤년이 아닙니다.")
    '''
'''
#실습문제4

temp= int(input("온도를 입력하세요: "))
wet= int(input("습도를 입력하세요: "))

if temp>=25 and wet>=70:
    print("냉방 모드로 에어컨 작동")

elif temp>=25 and wet<70:
    print("제습 모드로 에어컨 작동")

else:
    print("에어컨을 끕니다.")
    

#실습문제5

age= int(input("input your age: "))

if age>=20:
    print("adult")
else:
    print("child")


#실습문제6

num= int(input("input number: "))

if num%2==0:
    print('even')
else:


#실습문제8

temp= float(input("temperature: "))

if temp<=0:
    state='solid'
elif 0<temp<100:
    state='liquid'
else:
    state='gas'

print(f'{temp:.2f} is {state}')


#실습문제10

line1= float(input('첫번째 변의 길이 : '))
line2= float(input('두번째 변의 길이 : '))
line3= float(input('세번째 변의 길이 : '))

if line1+line2>line3 and line2+line3>line1 and line3+line1>line2:
    if line1==line2==line3:
        print('정삼각형입니다.')

    elif line1==line2 or line2==line3 or line1==line3:
        print('이등변삼각형입니다.')

    else:
        print('일반삼각형입니다.')



#실습문제11

num1= int(input('숫자를 입력하세요: '))
num2= int(input('숫자를 입력하세요: '))

if num1%num2 == 0:
    print('배수 관계')
else:
    print('배수 관계가 아닙니다')

if num1 + num2 >= 100:
    print('합이 100 이상입니다.')
else:
    print('합이 100 미만입니다.')


#실습문제12

a= input('문자열을 입력하세요:')
b= input('다음 문자열을 입력하세요:')

if a==b:
    print('두 문자열은 같은 문장입니다.')
elif len(a)==len(b):
    print('두 문자열의 길이가 같습니다.')
else:
    print('두 문자열을 서로 다릅니다.')

is_equal = a==b
is_same_len = len(a)==len(b)

print(f'두 문자열이 같은가요? {'예' if is_equal else '아니오'}')
print(f'두 문자열 길이가 같은가요? {'예' if is_same_len else '아니오'}')


#문제3
temperature = input('온도를 작성하세요: ')
humidity = input('습도를 작성하세요: ')

if temperature >= 25:
    if humidity >= 70:
        print('에어컨을 켠다.')
print('end')


#문제4

num= int(input('input number :'))

if num>=10:
    print('number >= 10')
elif 5<=num<10:
    print('5 <= number < 10')
else:
    print('number < 5')



#문제8번


year = int(input("년도를 입력하세요: "))
month = int(input("월을 입력하세요: "))
day = int(input("일을 입력하세요: "))


days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if month < 1 or month > 12:
    print(f"{year}년 {month}월 {day}일은 유효하지 않은 날짜입니다.")
elif day < 1 or day > days_in_month[month - 1]:
    print(f"{year}년 {month}월 {day}일은 유효하지 않은 날짜입니다.")
else:
    print(f"{year}년 {month}월 {day}일은 유효한 날짜입니다.")



#문제9번

time= int(input('근로 시간 :'))
price= 12000

if time>=40:
    print((time-40)*price*1.5+(40*price))

else:
    print(time*price)



#문제10

weight= int(input('우편물의 무게를 입력하세요 :'))

if weight<=5:
    print(weight*400)
elif 5 < weight <=25:
    print(weight*430)
elif 25 < weight <= 50:
    print(weight*450)
else:
    print('우체국에 문의하십시오.')


#문제11

ta= int(input('건구온도 입력 : '))
tw= int(input('습구온도 입력 : '))

discomfortIndex= 0.72* (ta + tw) + 40.6

if  discomfortIndex < 68:
    print('모든 사람이 쾌적함을 느낌!')
elif discomfortIndex <75:
    print('불쾌감을 나타내기 시작함')
elif discomfortIndex <80:
    print('반 정도의 사람이 불쾌감을 느낌')
else:
    print('모든 사람이 불쾌감을 느낌')


#문제12

a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

total = b**2 - 4*a*c

if total > 0:
    print('해는 실수이고 2개의 다른 값이 존재함')
elif total == 0:
    print('해는 실수이고 1개 값만 존재함')
else:
    print('해는 복소수이고 2개의 다른 값이 존재함.')


#문제13

a= int(input('line x : '))
b= int(input('line y :'))
c= int(input('line c :'))

p1= int(input('dot p1: '))
p2= int(input('dot p2: '))

distance= (a*p1 + b*p2 + c)/((a**2+b**2)**(1/2))

if distance < 0:
    print(distance*(-1))
else:
    print(distance)


#문제14

slope1 = int(input('input slope1 : '))
slope2 = int(input('input slope2 : '))

if slope1 * slope2 == -1:
    print('right angle')
elif slope1 == slope2:
    print('parallel')
else:
    print('nothing')


#문제15

seat= input('Type of the seat : ')

if seat == 'VIP':
    print('150000')
elif seat == 'S':
    print('110000')
elif seat == 'A':
    print('90000')
elif seat == 'B':
    print('70000')
else:
    print('NO seat in ticket')



#문제16

import random

random_numbers = random.sample(range(1, 100), 3)

print("생성된 난수들:", random_numbers)

max_number = max(random_numbers)
print("가장 큰 정수:", max_number)

#문제17

num= int(input('input number : '))

if num <= 1:
    print('소수가 아닙니다.')
elif num <=3:
    print('소수입니다.')
elif num%2 == 0 or num%3 == 0:
    print('소수가 아닙니다.')
elif num ==5 or num == 7:
    print('소수입니다.')
elif num % 5 ==0 or num% 7==0:
    print('소수가 아닙니다.')
else:
    print('소수입니다.')



#문제18

h, w = map(float, input('당신의 키(cm)와 몸무게(kg)는?').split())

bmi= w/((h/100)**2)

if 40 <= bmi:
    print('고도비만') 
elif 35 <= bmi < 40:
    print('중등도 비만')
elif 30 <= bmi < 35:
    print('비만') 
elif 25 <= bmi < 30:
    print('과체중')
elif 18.5 <= bmi < 25:
    print('정상')
else:
    print('저체중') 

#문제19

interest= input('없음, 조금, 보통, 많음, 매우 많음 중 적으시오 : ')
efforts= input('상, 중, 하 중 적으시오 : ')

if interest == '없음' or interest == '조금':
    print('파이썬에 대해 관심을 가져 보세요.')
elif efforts == '상':
    print('예비 파이썬 고수 ')
elif efforts == '중':
    print('예비 파이썬 중수')
else:
    print('노력 필요')


'''