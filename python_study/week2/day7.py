'''
#while문
n=1
while n<4:
    print(n)
    n+=1

#while 0~10까지 덧셈
sum= 0
n= 1
while n<=10:
    sum+= n
    n+=1
print(sum)

#실습문제1
def sum_until_100():
    total = 0
    while total <=100:
        num= int(input("please write number :"))
        total+= num
    print(f'total : {total}')

sum_until_100()

#실습문제2
def user_authentication():
    password = "rockey"
    while True:
        user_input = input("please write the password : ")
        if user_input == password:
            print('complete')
            break
        else:
            print('wrong password')

user_authentication()


#for문
s= "hello"
for ch in s:
    print(ch)

#for문과 range()
for i in range(3):
    print('hello')

#1~10까지의 합
sum= 0
for n in range(1, 11):
    sum+= n
    
print(sum)

for n in range(-5, -2):
    sum+= n
    
print(sum)

for n in range(-5, 3, 2):
    sum+= n
    
print(sum)

for n in range(7, 1, -3):
    sum+= n
    
print(sum)

for n in range(7, -3, -2):
    sum+= n
    
print(sum)

#실습문제3
def reverse_string(s):
    reversed_s= ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

s= input(" write the str :")

reversed_s = reverse_string(s)
print(f'reverse : {reversed_s}')

#실습문제4
import random

def sum_of_random_numbers(n):
    total = 0
    for _ in range(n):
        rand_num = random.randint(1, 100)
        print(f"random number : {rand_num}")
        total += rand_num
    return total

n= int(input("how many random number : "))

total_sum= sum_of_random_numbers(n)
print(f"sum of random number : {total_sum}")


#실습문제5
def print_chess_board():
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                print("#", end = ' ')
            else:
                print(' ', end= ' ')
        print()

print_chess_board()

#break 문
s= "what are the 10 best-selling products in this"
idx=0
while idx < len(s):
    if s[idx].isdigit():
        print(idx)
        break
    idx +=1

#continue
count = 0
sum = 0
while count <10:
    n= int(input('please write positive num : '))
    if n<=0:
        continue
    sum += n
    count += 1
    print("count = ", count)

print("sum = ", sum)


#실습문제6
def sum_num(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
num = int(input('write the number : '))

result = sum_num(num)

print(result)


#실습문제7
def printStar(n):
    i=0
    while i<n:
        print("*", end= "")
        i += 1
    print()

num= int(input("write the num :"))

printStar(num)


#실습문제8
import random

def guess():
    rand_num= random.randint(1,100)
    while True:   #True값이 나올 때까지 진행
        num= int(input("guess the num : "))
        if num== rand_num:
            break
        elif num > rand_num:
            print("Down")
        else:
            print("Up")
        
    print("Complete")

guess()

#실습문제11
def number_odd(n):
    product = 1
    i= 1
    
    while i<=n:
        if i%2 == 1:
            product *= i
        i += 1
    return product
num= int(input("write the number : "))

print(number_odd(num))
    


#문제5
def find_max_number():
    numbers = []  # 입력받은 숫자를 저장할 리스트
    
    # 숫자 5개 입력받기
    for i in range(5):
        number = int(input(f"숫자 {i+1} 입력: "))
        numbers.append(number)  # 리스트에 숫자 추가
    
    # 초기 최대값 설정
    max_number = numbers[0]
    
    # 입력된 숫자들 중에서 최대값 찾기
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    
    return max_number

max_value = find_max_number()

print(f"가장 큰 값은 {max_value}입니다.")


#문제6 (1)     
n=100
sum= 0
while n<200:
    sum+=n
    n+=1
print(sum)

 #for문 사용 시
n= 100
for n in range(100,200):
    sum+=n
print(sum)

#(2)
n=100
sum= 0
while n<200:
    if n%2==0:
        sum+=n
    n+=1
print(sum)

#(3)
n=100
sum=0
while n<200:
    if n%3==0:
        sum+=n
    n+=1
print(sum)


#문제7
def getSum():
    n=100
    sum1=0
    sum2=0
    sum3=0
    while n<200:
        if n%2==0:
            sum1+=n

        sum2+=n

        if n%3 ==0:
            sum3+=n
        
        n+=1

    print(sum1)
    print(sum2)
    print(sum3)

getSum()

#문제8
def devicer(n):

    device=[]
    for i in range (1, n+1):
        if n%i == 0:
            device.append(i)
        
    print(device)

devicer(12)
devicer(16)


#문제9
def devicion(n1, n2):
    for num in range(n1, n2+1):
        device = []
        for i in range(1, num+1):
            if num % i == 0:
                device.append(i)

        print(device)

devicion(10,16)


#문제10
import random

def guess():
    result= []
    for _ in range(5):
        rand_num= random.randint(1,6)
        result.append(rand_num)  #list에 각 숫자 저장

    print(result)

    duplicate = set([num for num in result if result.count(num)>1])

    if duplicate:
        print(duplicate)
    else:
        print("nothing")

guess()

#문제11
import random

def generate():
    n=0
    for _ in range(10):
        rand_num= random.randint(1,6)
        
        while rand_num>4:
            rand_num = random.randint(1,6)

        print(rand_num)

generate()       

#문제12
def delete(input_str):
    
    punc = ".!\n"

    clean_str = input_str
    for char in punc:
        clean_str = clean_str.replace(char,"")

    return clean_str

input_string = "...What a beautiful day!\n"

result = delete(input_string)
print(result)

#문제13
def triple():
    n=1
    while True:
        if n**3>100:
            return n
        n+=1

first_n=triple()
print(first_n)

#문제14
def special():
    number=[]

    for n in range(1000, 10000):
        n_str = str(n)
        n1= int(n_str[0])
        n2= int(n_str[1])
        n3= int(n_str[2])
        n4= int(n_str[3])

        number= n1**4 + n2**4 + n3**4 + n4**4

    return number

result = special()
print(result)


#문제15
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2와 3은 소수
    if n % 2 == 0 or n % 3 == 0:
        return False  # 2나 3으로 나누어지면 소수가 아님
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # i 또는 i+2로 나누어지면 소수가 아님
        i += 6
    
    return True  # 위의 조건을 모두 만족하지 않으면 소수임

# 사용자 입력 받기
try:
    n = int(input("정수를 입력하세요: "))
    
    if is_prime(n):
        print(f"{n}은(는) 소수입니다.")
    else:
        print(f"{n}은(는) 소수가 아닙니다.")
except ValueError:
    print("정수를 입력해야 합니다.")


#문제16
def find_n1_n2():
    for n1 in range(1, 10):  
        for n2 in range(0, 10):  
            if n1 != n2 and n1 * 10 + n2 + n2 * 10 + n1 == 110:
                print(f"n1 = {n1}, n2 = {n2}")

# 함수 호출
find_n1_n2()

#문제17
import random

def coin_toss_simulation(num_tosses):
    heads_count = 0
    tails_count = 0

    for _ in range(num_tosses):
        # 1 또는 2를 무작위로 선택하여 동전 던지기 시뮬레이션
        result = random.randint(1, 2)
        if result == 1:
            heads_count += 1
        else:
            tails_count += 1
    
    # 앞면과 뒷면이 나오는 횟수 출력
    print(f"동전을 {num_tosses}회 던졌을 때:")
    print(f"앞면이 나온 횟수: {heads_count}")
    print(f"뒷면이 나온 횟수: {tails_count}")

    # 앞면과 뒷면이 나올 확률 계산 및 출력
    heads_probability = heads_count / num_tosses
    tails_probability = tails_count / num_tosses
    print(f"앞면이 나올 확률: {heads_probability:.2f}")
    print(f"뒷면이 나올 확률: {tails_probability:.2f}")

# 각각 100, 1000, 10000회 동전 던지기 시뮬레이션 결과 출력
coin_toss_simulation(100)
print()
coin_toss_simulation(1000)
print()
coin_toss_simulation(10000)

#문제18
def print_table(n, rows, cols):
    # 첫 번째 행 출력 (헤더)
    headers = [f"{i}*n" for i in range(1, cols + 1)]
    print("\t".join(headers))
    
    # 데이터 행 출력
    for i in range(1, rows + 1):
        row = [i * j for j in range(1, cols + 1)]
        print("\t".join(map(str, row)))

print_table(1, 10, 8)

#문제19
def compound_interest(principal, annual_rate, years):
    rate = annual_rate / 100 

    for year in range(1, years + 1):
        # 복리 계산: A = P * (1 + r)^n
        amount = principal * (1 + rate) ** year
        total_interest = amount - principal
        print(f"{year}년: 복리총액 {amount:,.0f}원, 총이자액 {total_interest:,.0f}원")

principal = int(input("원금을 입력하세요: "))
annual_rate = float(input("연이자율을 입력하세요 (예: 5 for 5%): "))
years = int(input("투자기간을 입력하세요 (년): "))

compound_interest(principal, annual_rate, years)

'''

#기본 문제6
s= "hello \t world"
for ch in s:
    print(ch)

#기본 문제11
count = 0
while count <10:
    print(count)
    count +=1
    if count == 5:
        break

#기본 문제12
num=0
