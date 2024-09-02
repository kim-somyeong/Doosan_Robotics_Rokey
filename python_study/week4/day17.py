'''

이터레이터 (Iterator)
파이썬에서 반복 가능한 객체를 순회하는 데 사용되는 객체

이터레이터는 반복을 지원하는 모든 객체에서 사용

__iter__()와 __next__() 메서드를 구현하여 반복 가능한 객체를 생성
직접 이터레이터 클래스를 작성해야 한다.

__iter__() 
이 메서드는 이터레이터 객체 자체를 반환해야 한다.
일반적으로 self를 반환한다.

__next__()
이 메서드는 반복 가능한 시퀀스의 다음 항목을 반환한다.
더 이상 반환할 항목이 없으면 StopIteration 예외를 발생시킨다.

메모리 효율성 무한 시퀀스 지원

이터레이션 데이터 구조를 순회하는 과정
->이터레이터 : 반복 가능한 객체를 순회하기 위한 객체로, __iter__()와 __next__() 메서드를 구현
->이터러블 : __iter__() 메서드를 구현한 객체로 이터레이터를 반환 (list, dict, set, str, bytes, tuple, range)



------------------------------------------------------------------------------------

제너레이터(Generator)
이터레이터를 더 간편하게 구현할 수 있는 특별한 유형의 이터러블 객체
반복적인 작업을 간단하고 효율적으로 수행할 수 있으며, 메모리 사용을 최소화하면서 대용량 데이터를 처리

yield를 사용하여 이터레이터를 간편하게 구현
자동으로 __iter__() 와 __next__() 메서드를 구현

yield
-> 제너레이터 함수는 yield 키워드를 사용하여 값을 반환
yield는 함수의 상태를 유지하면서 결과를 하나씩 생성
return 대신 yield를 사용하여 값을 반환

상태유지
-> yield가 호출될 때마다 함수는 이전 상태를 기억하고 계속 실행

지연평가 (Lazy Evaluation)
->제너레이터는 필요한 값만을 계산하며, 전체 데이터를 메모리에 저장하지 않으므로 메모리 사용이 효율적





'''

'''


#iterator with range
it= range(3).__iter__()

print(it.__next__())
print(it.__next__())
print(it.__next__())

#make iterator
class Counter:
    def __init__(self, stop):
        self.current=0
        self.stop=stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            r=self.current
            self.current += 1
            return r
        else:
            raise StopIteration
        
for i in Counter(3):
    print(i, end=' ')

#iterator unpacking
a, b, c= Counter(3)
print(a,b,c)

a, b, c, d, e= Counter(5)
print(a, b, c, d, e)

#approch iterator used index
class Counter:
    def __init__(self, stop):
        self.stop= stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError

print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

for i in Counter(3):
    print(i, end= ' ')

#iter, next func
it= iter(range(3))

print(next(it))
print(next(it))
print(next(it))

#callable iter
import random

it= iter(lambda : random.randint(0, 5), 2)
print(next(it))
print(next(it))
print(next(it))

#for iter
import random

for i in iter(lambda : random.randint(0, 5), 2):
    print(i, end=' ')

#next
it= iter(range(3))

print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))  #기본값 출력
print(next(it, 10))  #기본값 출력

#generator, yield
def number_generator():
    yield 0
    yield 1
    yield 2

for i in number_generator():
    print(i)

g= number_generator()
#print(dir(g))
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

#make generator working like range
def number_generator(stop):
    n= 0
    while n<stop:
        yield n
        n += 1

for i in number_generator(3):  #외부에서 호출 -> range처럼 사용
    print(i)

#next 사용 가능
g= number_generator(3)

print(next(g))
print(next(g))
print(next(g))
print(next(g)) #자동으로 StopIteration

#call yield function
def upper_generator(x):
    for i in x:
        yield i.upper()

fruits= ['apple','pear','pineapple','orange']

for i in upper_generator(fruits):
    print(i)

#before yield from
def number_generator():
    x= [1, 2, 3]
    for i in x:
        yield i

for i in number_generator():
    print(i)

#after yield from
def number_generator():
    x=[ 1, 2, 3 ]
    yield from x

for i in number_generator():
    print(i)

#dir(g)
g= number_generator()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

#yield from
def number_generator(stop):
    n= 0
    while n< stop:
        yield n
        n += 1

def three_generator():
    yield from number_generator(3)

for i in three_generator():
    print(i)

#연습문제1
class RangeIterator:
    def __init__(self, start, end):
        self.current= start
        self.end= end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            number= self.current
            self.current += 1
            return number
        else:
            raise StopIteration
        
for num in RangeIterator(1, 10):
    print(num)

#연습문제2
def even_numbers(max_num):
    n= 0
    while n <= max_num:
        if n % 2 == 0:
            yield n
        n += 1

for num in even_numbers(10):
    print(num)

#연습문제7
def read_lines(filename):
    with open(filename, 'r') as file:
        while line := file.readline():
            yield line.strip()

filename= 'show.txt'
with open(filename, 'w') as f:
    f.write("First line\nSecond line\nThird line")

for line in read_lines(filename):
    print(line)

#문제2
numbers= [1, 2, 3, 4, 5].__iter__()

print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())
print(numbers.__next__())

#문제3
numbers= [1, 2, 3, 4, 5].__iter__()

while True:
    try:
        print(numbers.__next__())
    except StopIteration:
        print("모든 요소를 순회")
        break

#문제5
class MyIterator:
    def __init__(self, data):
        self.data= data
        self.current= 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.data):
            result= self.data[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

numbers= [1, 2, 3, 4, 5]
iterator= MyIterator(numbers)

for num in iterator:
    print(num)

#문제6
class MyIterator:
    def __init__(self, data):
        self.data= data
        self.current= 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < len(self.data):
            result = self.data[self.current]
            self.current += 1
            return result
        
        else:
            raise StopIteration
        
    def __getitem__(self, index):
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")
        
numbers= [1, 2, 3, 4, 5]

iterator= MyIterator(numbers)

for num in iterator:
    print(num)

try:
    print(iterator[10])
except IndexError as e:
    print(e)

#문제7
def file_line_iterator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.rstrip('\n')

with open('example.txt', 'w') as f:
    f.write("First line\nSecond line\nThird line\n")

iterator= file_line_iterator('example.txt')

for line in iterator:
    print(line)

#문제8
class FibonacciIterator:
    def __init__(self):
        self.a=0
        self.b=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a>100:
            raise StopIteration
        
        current= self.a
        self.a, self.b = self.b, self.a+self.b
        return current

fib_iter= FibonacciIterator()

for number in fib_iter:
    print(number)

#문제10
def fibonacci_generator():
    a, b = 0, 1
    while a <= 100:
        yield a
        a, b = b, a + b

# 사용 예시
for number in fibonacci_generator():
    print(number)

'''
#문제11
def filter_even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

# 사용 예시
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for even in filter_even(nums):
    print(even)