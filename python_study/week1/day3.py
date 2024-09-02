'''
#실습문제1

coffee_100= 10000  #변수

coffee_200 = coffee_100*2
coffee_300 = coffee_100*3
coffee_400 = coffee_100*4

print(f"커피 원두 200g 가격: {coffee_200}원")
print(f"커피 원두 300g 가격: {coffee_300}원")
print(f"커피 원두 400g 가격: {coffee_400}원")

#복합연산자

a= 5
print(a)

a+= 2
print(a)

a-= 2.1
print(a)

a*=2.1
print(a)

a/= 2.1
print(a)

a= 5
print(a)

a//=2
print(a)

a%=2
print(a)

a**=2
print(a)

print("원주율 : %.6f" %3.1415)
print("%10s" %"한글")

print("오늘의 습도는 %d%%입니다" %70)

#실습문제3

print('%d년 아카데미 영화제 작품상은 "%s"가 받았다.' %(2020, "기생충"))

movie1 = (2021, "노매트랜드")
print('%d년 아카데미 영화제 작품상은 "%s"가 받았다.' %movie1 )

print("%d년 아카데미 영화제 작품상은 \"%s\"가 받았다." %(2022, "코다"))



#실습문제4

weight= 200
price= 10000

print('커피 원두 %d 가격: %d'%(weight, weight//100*price))

weight= 300

print('커피 원두 %d 가격: %d'%(weight, weight//100*price))

#실습문제5

name= "기생충"
year= 2020

print(f'{year}년 아카데미 영화제 작품상은 "{name}"가 받았다')

#연습
input("글자 한 개를 \n 입력하세요 : ")
mesg = "단어 한개를 입력하새요: "
input(mesg)


#실습문제6

price= int(input("사과 1kg 단가 : "))
weight= float(input("무게 : "))

total_price= price*weight

print(f'총 사과의 가격은 {total_price}원 입니다.')

#실습문제7

width = float(input('가로 길이를 입력하세요 : '))
height= float(input('세로 길이를 입력하세요 : '))

area = width * height

print(f'직사각형의 넓이는 {area:.2f}입니다.')


#실습문제8

celsius= float(input('섭씨 온도를 입력 : '))
fahrenheit= celsius * (9/5) + 32

print(f'{celsius}를 변환하면 {fahrenheit:.2f}입니다.')
'''
'''
#문제6
print("%8f"%3.14)

#문제7
print("%10s"%"한글")

#문제8

address= "서울시 종로구 홍지문 2길"
temperature= 24

print(f'지역: {address}, 온도: {temperature}도')

#문제9
p= 3.1415

print(f'원주율 * 2 = {p*2:.2f}입니다.')

#문제10
x1= 1.23
x2= 12.3
x3= 123.456

print(f'{x1:6.2f}')
print(f'{x2:6.1f}')
print(f'{x3:6.3f}')



#문제11
a= float(input("반지름을 입력하세요: "))

r= 3.14

area= (a**2*r)

print(f'면적은 {area:.2f}입니다.')



#문제12
import math
rt= float(input('습도를 입력하세요:'))
temp= float(input('온도를 입력하세요: '))

dew_point= (243.12*(math.log(rt/100)+(17.62*temp)/(243.12+temp)))/(17.62-(math.log(rt/100)+(17.62*temp/(243.12+temp))))


print(float(dew_point))


#문제13
eart_m= 5.972 * 10**24
moon_m= 7.36 * 10**22
distance= 384400000
G= 6.674 * 10*(-11)

F= G*(eart_m * moon_m)/distance**2

print('지구와 달 사이의 만유인력 : %f'%F)

#문제14
weight= 100
price= 10000

print(f'커피 원두 {weight*2}g 가격: {price*2}원')
print(f'커피 원두 {weight*3}g 가격: {price*3}원')
print(f'커피 원두 {weight*4}g 가격: {price*4}원')


#문제15
weight= 100
price= 10000

weight += 100
price += 10000
print(f'커피 원두 {weight}g 가격: {price}원')

weight += 100
price += 10000
print(f'커피 원두 {weight}g 가격: {price}원')

weight += 100
price += 10000
print(f'커피 원두 {weight}g 가격: {price}원')

#문제16

movie1= (2020, "기생충")
movie2= (2021, "노매드랜드")
movie3= (2022, "코다")

print('%d년 아카데미 영화제 작품상은 "%s"가 받았다'%movie1)
print('%d년 아카데미 영화제 작품상은 "%s"가 받았다'%movie2)
print('%d년 아카데미 영화제 작품상은 "%s"가 받았다'%movie3)



#문제17

weight= 100
price= 10000

weight+=100
price+= 10000
print('커피 원두 %d g 가격: %d원'%(weight, price))

weight+=100
price+= 10000
print('커피 원두 %d g 가격: %d원'%(weight, price))



#문제18

weight= 100
price= 10000

weight+=100
price+= 10000
print(f'커피 원두 {weight} g 가격: {price}원')

weight+=100
price+= 10000
print(f'커피 원두 {weight} g 가격: {price}원')


#문제19

price= int(input('원두 100g의 단가 (원 단위): '))
weight= float(input('원두 무게 : '))

total_price= price * weight

print(f'커피 원두 {weight}g 가격은 {total_price}원 입니다.')
'''

#문제20

hello = 'world'
print(f"{hello:^11}")
print(f"{hello:*^11}")
big_num = 1234567890
print(f"{big_num:,}")
num = 2343552.6516251625
print(f"{num:,.3f}")