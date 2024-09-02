'''
#키
d= {1:2, False :20, (1,2): "튜플"}
print(d[1])
print(d[False])
print(d[(1,2)])

#딕셔너리 요소 개수 확인
d= {}
d1= {'a':1, 'b':2, 'c':3}
print(len({}))
print(len(d))
print(len(d1))
print(len({'a':1, 'b':2, 'c':3}))

#요소 접근
d= {"name":"hong gil-dong", "age":20, "hobby":["movie", "game", "reading a book"]}

print(d["name"])
print(d["hobby"])

print(d.get("name"))
print(d.get("hobby"))
print(d.get("이름"))

#키 중복
d={"name" :"홍길동", "age":"20", "name":"김길동"}

print(d["name"])

#값 추가 또는 수정
#단일 요소
d= {1:2, False :20, (1,2): "튜플"}
d["key"]="value"

print(d["key"]) #새로운 키와 값 추가
print(d[1])

#여러 요소 한꺼번에 수정
d= {1:2, False :20, (1,2): "튜플"}
d.update({1:3, False:"boolen",(1,2):2, "key":"value"})
print(d[1])     

#for문
d= {1:2, False :20, (1,2): "튜플"}
for key in d:
    print(f"{key}:d{[key]}")

for key in d.keys():
    print(f"{key}:{d[key]}")

for n in d.values():
    print(n)

for k, v in d.items():
    print(k, v)

#in
d= {1:2, False :20, (1,2): "튜플"}

if 1 in d:
    print(d[1])
else:
    print("1 is not key of 'd'. ")

#del()
d= {1:2, False :20, (1,2): "튜플"}

del(d[1])
print(d)

#실습문제2
def store_in_dictionary():
    name= input('write the name :')
    age= input('write the age :')
    person= {"name": name, "age": age}
    print(person)
    print(type(person))

store_in_dictionary()

#실습문제3
def access_dictionary():
    data= {'name': 'Elena', 'age': 23}
    key= input('write the key :')
    try:
        print(f'{key}의 값 : {data[key]}')
    except KeyError:
        print(f'Error : {key}는 존재하지 않는 키입니다.')

access_dictionary()

#set요소 추가
a= set([1,2,3])
a.add("string")
print(a)

a= set([1,2,3])
a.update("string")
print(a)

#교집합 -> 중복된 값
s1= {1,2,20,(1,2),"문자열"}
s2= {1,2,3}

ints= s1&s2
print(ints)

ints2= s1.intersection(s2)
print(ints2)

#합집합 -> 두 값을 합침
unions= s1 | s2
print(unions)

unions2= s1.union(s2)
print(unions2)

#차집합 -> 중복되지 않는 값
diffs= s1 - s2
print(diffs)

diffs2= s1.difference(s2)
print(diffs2)

#in
s= {1,2,20,(1,2),"문자열"}

if 1 in s:
    print("1 include set s.")
else:
    print('1 is not include set s.')

#실습문제4
def create_and_print_set():
    numbers= input('숫자들을 공백으로 구분하여 입력하세요.: ').split()
    number_set= set(numbers)
    print('생성된 집합 :', number_set)

create_and_print_set()

#실습문제5
def update_dictionary():
    data= {'name':'Elena', 'age':23}
    key= input('Add key : ')
    value= input('Add value : ')
    data[key]=value
    print('Update dictionary : ', data)

update_dictionary()

#실습문제6
def delete_from_dictionary():
    data= {'name':'elena','age':23, 'city':'new york'}
    key= input('write of the delete key : ')
    if key in data:
        del data[key]
        print("dictionary after delete : ", data)
    else:
        print(f'Error: there is no {key}')

delete_from_dictionary()

#실습문제7
def list_dictionary_keys():
    data= {'name':'elena','age':23, 'city':'new york'}
    keys= list(data.keys())
    print('keys of dictionary : ',keys)

list_dictionary_keys()

#실습문제8
def iterate_dictionary_items():
    data= {'name':'elena','age':23, 'city':'new york'}
    for key, value in data.items():
        print(f'{key} : {value}')

iterate_dictionary_items()

#실습문제9
def merge_dictionarys():
    dict1= {'name':'Elena', 'age':23}
    dict2={'city':'new york', 'country':'usa'}
    dict1.update(dict2)
    print('merge dictionarys : ', dict1)

merge_dictionarys()

#실습문제10
def get_with_default():
    data= {'name':'Elena', 'age':23}
    key= input('write the key for the search : ')
    value = data.get(key, 'Not found')
    print(f'{key}: {value}')

get_with_default()

#실습문제11
def filter_dictionary():
    data= {'Alice':25, 'Bob':19, 'Cathy':34, 'Dan':20}

    filtered_data= {k: v for k,v in data.items() if v > 20}

    print('itmes of value over 20 : ', filtered_data)

filter_dictionary()

#실습문제12
def add_to_set():
    my_set= {1, 2, 3}
    new_element= int(input('write the add num : '))
    my_set.add(new_element)
    print('update set : ',my_set)

add_to_set()

#실습문제13
def remove_from_set():
    my_set= set([1, 2, 3, 4, 5])
    element= int(input('write the remove set :'))
    try:
        my_set.remove(element)
    except KeyError:
        print('there is no set.')
    print('update set : ',my_set)

remove_from_set()

#문제4
def merge_dictionary(dict1, dict2):
    common_dict= {}

    for key in dict1:
        if key in dict2 and dict1[key] == dict2[key]:
            common_dict[key]=dict1[key]

    return common_dict

dict1= {'a':1, 'b':2, 'c':3, 'd':4}
dict2= {'a':1, 'b':2, 'c':4, 'e':5}
result = merge_dictionary(dict1, dict2)

print("공통된 키-값 쌍 : ", result)

#문제5
s1= {1,2}

s1.add(1)
print(s1)

#문제6
s1= {1, 2, 3}
s2= {1, 2, 4, 5}

ints= s1&s2
print(ints)

s1= {1, 2, 3}
s2= {1, 2, 4, 5}

ints2= s1 | s2
print(ints2)

#문제7
def store_in_dictionary():
    person= {'이름':'김영희', '전화번호':'010-1111-2222', '성별':'여자', '나이': 22, '대학교':'한국대학교'}
    for key, value in person.items():
        print(f'{key} : {value}')

store_in_dictionary()

#문제8
def compare_dictionary(str1, str2):
    set1= set(str1.lower())
    set2= set(str2.lower())

    set1.remove(' ')
    set2.remove(' ')

    common_characters= set1.intersection(str2)

    return common_characters

str1= "Hello World"
str2= "Python Programming"

result=compare_dictionary(str1, str2)
print(result)

#문제9
def get_company():
    data= {'삼성에스디에스': 242000, '삼성전자': 67000, '엔씨소프트': 52000, '핸디소프트': 5120, '골프존': 215000, '기아': 65000}
    key= input('주식 이름? ')
    value= data.get(key,'주식 이름이 없습니다')
    print(f'{key} : {value}')

get_company()

'''
#문제10
def find_book_writer():
    books= {'파이썬 개론' : ['홍길동'], 'Perfect C' : ['김영수','이동준'], '컴퓨터 개론':['최환수','주용호','박해성']}

    key= input('책 이름 : ')
    value= books.get(key, '해당 책이 없습니다.')

    value_str= ', '.join(value) #리스트의 각 원소를 문자열로 변환한 후 join으로 연결
    print(f'저자 : {value_str}')

find_book_writer()
