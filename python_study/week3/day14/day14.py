'''
#요소에 값 할당
a= [0, 0, 0, 0, 0]
a[0]= 38
a[1]= 21
a[2]= 53
a[3]= 62
a[4]= 192

print(a)

#실습문제1
def most_frequent_word(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            text= file.read()
        words= text.split()
        word_count= {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        most_frequent= max(word_count, key=word_count.get)
        return most_frequent, word_count[most_frequent]
    except FileNotFoundError:
        return "File not found"
    
filename= "info.txt"
result= most_frequent_word(filename)
print(f"The most frequent word is '{result[0]}'with {result[1]}occurrences.")

#문제2
sequence= list(range(1, 101))

num= int(input('write the num :'))

if num in sequence:
    print('True')
else:
    print('False')

#문제4
list_1=[1, 2, 3]
tup_1= (4, 5, 6)

list_2= list(tup_1)

total_list= list_1 + list_2

print(total_list)

#문제6

#리스트 컴프리헨션(List Comprehension) : for 루프와 조건문을 한 줄로 작성
#표현식 for 항목 in 반복 가능한 객체 if 조건

my_tuple=(1, 2, 3, 4, 5)
num= int(input('write the delete num : '))

#my_tuple의 요소를 x라는 변수로 참조, x는 1, 2, 3, 4, 5 등 튜플의 각 요소를 의미
#x 와 num이 다르다면 x를 출력
#맞는 조건이면 새로운 리스트 생성
new_list = [x for x in my_tuple if x != num]

new_tuple= tuple(new_list)

print('original tuple :', my_tuple)
print('new tuple : ', new_tuple)

#문제7
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
del(alp[3])
print(alp)

#문제8
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
alp.clear()
print(alp)

#문제10
line= input('write the word : ')

reversed_line= line[::-1]

if line == reversed_line:
    print('That is "Palindrome!!')
else:
    print('That is not Palindrome..')

#문제11
def sort(n):
    char_list= list(n)

    char_list.sort()  #오름차순 정렬
    print(char_list)

    char_list.sort(reverse= True)  #역순 정렬
    print(char_list)

n='잣밤배귤감'
sort(n)

#문제12
strings = ["mango", "apple", "banana", "cherry", "date", "fig", "apple", "banana"]

new_strings= list(set(strings)) #set : 동일한 값이 여러 개 있어도, set에는 한 번만 저장

new_strings.sort()

print(new_strings)

#추가문제1

#리스트 컴프리헨션(List Comprehension) : for 루프와 조건문을 한 줄로 작성
#표현식 for 항목 in 반복 가능한 객체 if 조건
even= [i for i in range(2, 11, 2)]
print(even)

#추가문제2
s= [i**2 for i in range(10) if i%2 == 1]
print(s)

#추가문제3
mylist= [1, 5, 1, 7, 1]
mylist[mylist.count(1)]=70 #리스트 내 1의 총 개수 : 3, mylist[3]
mylist[len(mylist)-1]= 80  #mylist[4]
mylist.insert(1,50)        #인덱스 1에 50을 삽입
print(mylist)

#추가문제4
import random
list1=[]

def make_list():
    for num in range(10):
        num= random.randint(1,100)
        list1.append(num)
    print(list1)

    new_list= sorted(list1)
    print("Sorted List : ", new_list)

    reversedList= sorted(list1, reverse=True)
    print('Reversed List : ', reversedList)

make_list()

#추가문제5
korean= ('정렬','문자','내포','사전','사과')
english=('sorting','text','comprehension','dictionary','apple')

def exchange():
    n= input('write the english word : ')
    if n in english:
        index= english.index(n)
        print(f'Korean Word : ', {korean[index]})
    else:
        print('Not Found')
exchange()

#추가문제6
data= [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

rsum= [sum(row) for row in data]

csum= [sum(col)for col in zip(*data)]
#zip(*data)는 리스트를 열 단위로 묶는다.

print(f'rsum : {rsum}')
print(f'csum : {csum}')

'''
#추가문제7
m= [[1,2], [3,4], [5,6], [7,8]]

transpose= [[row [i] for row in m] for i in range(len(m[0]))]

print(transpose)

#추가문제8
from random import sample

A= set(sample(list(range(1, 21)), 5))
B= set(sample(list(range(1, 21)), 5))

#합집합
union= A|B

#차집합
difference= A - B

#교집합
intersection = A & B

#여집합
universal_set= set(range(1,21))
complement= universal_set - (A|B)

print('A : {A}')
print('B : {B}')
print(f'합집합 : {union}')
print(f'차집합 : {difference}')
print(f'교집합 : {intersection}')
print(f'여집합 : {complement}')