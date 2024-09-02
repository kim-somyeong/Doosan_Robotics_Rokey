'''
#list
a=[]
a.append(4)
a.append('5')
a.append([2,3])

print(a)

#for & list
a=[4, 8, 7, 2, 1]
for n in a:
    print(n)

l=[1, 'g', 'h', 3, "abc"]
for n in l:
    print(n)

for n in a:
    if n>4:
        print(n)

#실습문제1
def sum_list():
    numbers=[]
    numbers.append(int(input("write the first number : ")))
    numbers.append(int(input("write the second number : ")))
    numbers.append(int(input("write the third number : ")))

    total= sum(numbers)
    print(f'total : {total}')

sum_list()

#실습문제2
def min_max_value():
    numbers=[]

    numbers.append(int(input("write the numbers : ")))
    numbers.append(int(input("write the numbers : ")))
    numbers.append(int(input("write the numbers : ")))

    min_value= min(numbers)
    max_value= max(numbers)

    print(f'min : {min_value}, max : {max_value}')

min_max_value()


#실습문제3
def get_user_data(str1, str2):
    name= str1
    age= str2
    return (name, age)

str1= input('write the name :')
str2= str(input('write the age :'))

user_data= get_user_data(str1, str2)

print(user_data)

#실습문제4
def print_tuple():
    a= int(input('write the first number : '))
    b= int(input('write the second number : '))
    c= int(input('write the third number : '))

    my_tuple= (a,b,c)

    print('your tuple : ', my_tuple)
    print('first of tuple : ', my_tuple[0])
    print('last of tuple : ', my_tuple[-1])

print_tuple()


#문제21
list = [[1, 2], [3, 4], [5, 6], [7, 8]]
print("행과 열을 맞춰서 출력:")
for i in range(2):
    for j in range(4):
        print(list[j][i], end=' ')
    print()
print("\n행과 열을 바꾼 형태로 출력:")
for i in range(4):
    for j in range(2):
        print(list[i][j], end=' ')
    print()



#문제10

my_list= [1, 2, 3, 4]

tuple1= tuple(my_list)
print(tuple1)

list2= list(tuple1)
print(list2)

#문제11
def device(n):
    devices= []
    for i in range(1,n+1):
        if n%i == 0:
            devices.append(i)
    return devices

for num in range(2,21):
    devices= device(num)

    print(f'{num}의 약수 개수 : {len(devices)}')

#문제12
myList= [1, 2, 2, 3, 4, 4, 5]
new_mylist= []
for i in myList:
    if i not in new_mylist:
        new_mylist.append(i)

print(new_mylist)


#문제13
def num_device(n1, n2):
    for num in range(n1, n2+1):
        device=[]
        for i in range(1, num+1): 
            if num%i==0:
                device.append(i)
        print(device)

n1= int(input('write the number: '))
n2= int(input("write the second number : "))

num_device(n1, n2)

#문제14
def make_list(list1, list2):
    new_list=[]
    i, j = 0, 0

    while i < len(list1) and j< len(list2):
        if list1[i]<list2[j]:
            new_list.append(list1[i])
            i+=1
        else:
            new_list.append(list2[j])
            j+=1

    new_list.extend(list1[i:])
    new_list.extend(list2[j:])

    return new_list

list1=[1,5,8,10,14]
list2=[2,4,5,9]

result= make_list(list1, list2)

print(result)


#문제15
def get_num(n):
    list=[] #리스트 초기화
    for _ in range(n): #n번 반복
        num= int(input(f' write the num : ({len(list)+1} / {n}): ')) #정수 입력받기
        list.append(num) #입력 받은 정수를 리스트에 추가
    return list #완성된 리스트 반환

n= int(input('how many num :'))
result= get_num(n)
print(result)


#문제16
def createDivisorsList(n):
    list= []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(n)
    return list #n의 약수 리스트 반환

n= int(input('write the num : '))
result= createDivisorsList(n) #약수 리스트 생성

divisorSum= sum(result)
print('sum :', divisorSum)


#문제17
def get_num(n):
    list=[] #리스트 초기화
    for _ in range(n): #n번 반복
        num= int(input(f' write the num : ({len(list)+1} / {n}): ')) #정수 입력받기
        list.append(num) #입력 받은 정수를 리스트에 추가
    return tuple(list) #완성된 리스트 반환

n= int(input('how many num :'))
result= get_num(n)
print(result)

'''

#문제19
data=[
    [1,2,3]
    [4,5,6]
    [7,8,9]
]

rsum= [sum(row) for row in data] #각 행의 합을 계산하여 rsum리스트에 저장

num_rows=len(data) #행의 개수
num_cols=len(data[0]) #열의 개수

csum= [0] * num_cols #열의 합을 저장할 리스트 csum에 초기화

for row in data:  #각 행에 대해서 반복
    for col_index in range(num_cols): #각 열에 대해서 반복
        csum[col_index]+= row[col_index] # 해당 열의 값을 더해 csum에 저장

print('row : ', rsum)
print('col :', csum)