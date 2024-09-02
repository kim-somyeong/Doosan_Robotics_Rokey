'''
#lamda

def f(x,y):
    return x+y

print('The sum of {} and {} is'. format(3.14, 2.718), f(3.14, 2.718))

f= lambda x, y: x+y
print(f'The sum of pi number and euler number is {f(3.14, 2.718)}')

def cube_volume_def(a):
    return a*a*a
print(f'The volume of def function is {cube_volume_def(3.14)}')

cube_volume_lambda= lambda a: a* a* a
print(f'The volume of lambda function is {cube_volume_lambda(3.14)}')

#lamba in func
def mult_table(n):
    return lambda x: x*n

n= int(input('Enter a number : '))

y= mult_table(n)

print(f'The entered number is {n}, which is a perfect number.')

for i in range(11):
    print(('%d x %d = %d' %(n, i, y(i))))

#람다 표현식 자체를 호출
print((lambda x: x + 10)(1))
print((lambda x: x//3.14)(12))

#람다 표현식 바깥에 있는 변수 활용
y=10
print((lambda x :x+y)(1))

#lamba, map
print(list(map(lambda x : x+10, [1, 2, 3])))

#lamda:map
#standard
my_pets= ['alfred','tabitha','william','arla']
uppered_pets=[]

for pet in my_pets:
    pet_= pet.upper()
    uppered_pets.append(pet_)

print(uppered_pets)

#map
my_pets= ['alfred','tabitha','william','arla']

uppered_pets= list(map(str.upper, my_pets))

print(uppered_pets)

#2개 요소 람다 없이 함수로 인자 처리
def add(x,y):
    return x+y

number1= [1, 2, 3, 4, 5]
number2= [10, 20 ,30 ,40 ,50]
added_numbers= map(add, number1, number2)

print(list(added_numbers))

#조건부 표현식
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda x: str(x) if x%3 == 0 else x, a)))

#map에 여러 객체 넣기
a=[1, 2, 3, 4, 5]
b= [2, 4, 6, 8, 10]

print(list(map(lambda x, y: x*y, a, b)))

#filter
def f(x):
    return x>5 and x<10

a=[8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f, a)))

#lamba filter
def is_even(num):
    return num % 2 == 0

numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers= list(filter(is_even, numbers))

print(even_numbers)

#lamba filter
dromes= ('구로구','rewire','madam','freer','마그마','kiosk')

palindromes= list(filter(lambda word:word==word[::-1], dromes))
print(palindromes)

#reduce
def f(x,y):
    return x+y

a=[1, 2, 3, 4, 5]
from functools import reduce
print(reduce(f,a))

#reduce
from functools import reduce

numbers= [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first+second

result= reduce(custom_sum, numbers, 10)  #초기값 : 10 설정
print(result)

#func f -> lamda
a=[ 1, 2, 3, 4, 5]

from functools import reduce

print(reduce(lambda x, y: x+y, a))

#연습문제1
people= [
    {'name' : 'John', 'age':45},
    {'name':'Diana','age':32},
    {'name':'Tom','age':20}
]

sorted_people= sorted(people, key=lambda x: x['age'])

print(sorted_people)

#연습문제2
from functools import reduce

numbers= [5, 8, 6, 10, 9, 2]
max_number= reduce(lambda x, y: x if x>y else y, numbers)

print(max_number)

#연습문제3
numbers= [3, 5, 7, 10, 2, 6]
filtered_numbers= list(filter(lambda x: x>5, numbers))

print(filtered_numbers)

#연습문제4
word= ['hello','world','python','programming']
capitalized_words= list(map(lambda word: word.capitalize(), word))

print(capitalized_words)

#연습문제5
products=[
    {'name':'Product A','price':150, 'stock':5},
    {'name':'Product B','price':120, 'stock':12},
    {'name':'Product C','price':50, 'stock':20},
    {'name':'Product D','price':200, 'stock':9}
]

filtered_products= list(filter(lambda p : p['price']>100 and p['stock']>=10, products))

print(filtered_products)

#문제2
increment= lambda x: x+1
print(increment)

#문제3
number= lambda x: x**2 if x % 2 == 0 else x

num= int(input('write the number : '))

result= number(num)

print(result)

#문제4
numbers= [1, 2, 3, 4, 5]

result= list(map(lambda x: x**2 if x % 2 == 0 else x, numbers))

print(result)

#문제5
numbers = [2, 3, 4, 5, 6, 7]

result= list(map(lambda x: x if x< 3 else x * 2 if x < 6 else x *3, numbers))

print(result)

#문제6
def calculate_elements(list1, list2):
    result= []
    for i in range(len(list1)):
        if list1[i] %2 == 0:
            result.append(list1[i]+list2[i])
        else:
            result.append(list1[i] * list2[i])
    return result


list1= [1, 2, 3, 4, 5]
list2= [10,20,30,40,50]

result= calculate_elements(list1, list2)
print(result)

#문제7
list1= [1, 2, 3, 4, 5]
list2= [10, 20, 30, 40, 50]

result= list(map(lambda x, y: x + y if x % 2==0 else x*y, list1, list2))

print(result)

#문제8
words= ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def word_a(word):
    return 'a' in word

filtered_words= filter(word_a, words)

print(list(filtered_words))

#문제9
words= ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

filtered_word= list(filter(lambda word: 'a' in word, words))

print(list(filtered_word))

#문제10
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):   #숫자의 제곱근을 확인해 소수여부 검사
        if n%i == 0:
            return False
    return True

number= int(input('write the number :'))

if is_prime(number):
    print('소수입니다.')
else:
    print('소수가 아닙니다.')

'''
#문제10
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

number = int(input('write the number : '))

if is_prime(number):
    print('소수입니다.')
else:
    print('소수가 아닙니다.')