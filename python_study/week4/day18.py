'''
#coroutine_consumer
def number_coroutine():
    while True:
        x= (yield)
        print(x)

co = number_coroutine()
next(co)

co.send(1)
co.send(2)
co.send(3)

#coroutine_producer_consumer
def sum_coroutine():
    total = 0
    while True:
        x = (yield total)
        total += x

co = sum_coroutine()
print(next(co))

print(co.send(1))
print(co.send(2))
print(co.send(3))

#couroutin_close
def number_coroutine():
    while True:
        x= (yield)
        print(x, end=' ')

co = number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()

#couroutine_generator_exit
def number_coroutine():
    try:
        while True:
            x= (yield)
            print(x, end = ' ')
    except GeneratorExit:
        print()
        print('close coroutine')

co= number_coroutine()
next(co)

for i in range(20):
    co.send(i)

co.close()

#coroutine_throw
def sum_coroutine():
    try:
        total = 0
        while True:
            x= (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total  #누적된 토탈 값 전달

co= sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, 'close coroutine except'))

#yield_from
def accumulate():
    total = 0
    while True:
        x= (yield)
        if x is None:               #만약 받아온 값이 none이면 
            return total            #total을 return
        total += x

def sum_coroutine():
    while True:
        total = yield from accumulate()
        print(total)

co = sum_coroutine()
next(co)

for i in range(1, 11):
    co.send(i)
co.send(None) #accumulate에 none을 보내 숫자 누적을 끝냄

for i in range(1, 101):
    co.send(i)
co.send(None)

#regular explrssion
import re

print(re.match('Hello', 'Hello, world!'))
print(re.match('Python', 'Hello, world!a'))

#search
import re

print(re.search('^Hello', 'Hello, world!'))
print(re.search('world!$', 'Hello, world!'))

#지정된 문자열
import re

print(re.match('hello|world', 'hello'))

#범위 판단
import re

print(re.match('[0-9]*', '1234'))
print(re.match('a*b', 'aab'))


#group
import re

m=re.match('([0-9]+) ([0-9]+)', '10 295')

print(m.group(1))
print(m.group(2))
print(m.group())
print(m.group(0))


#group name
import re

m=re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')

print(m.group('func'))
print(m.group('arg'))

#findall
import re

print(re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8'))

#change string
import re

result= re.sub('apple|orange', 'fruit','apple box orange box')
print(result)

result2= re.sub('[0-9]+','n','1 2 Fizz 4 Buzz Fizz 7 8')
print(result2)
 

#change func
import re

def multiple(m):
    n= int(m.group())
    return str(n*10)

result= re.sub('[0-9]+', multiple, '1 2 Fizz 4 Buzz Fizz 7 8')
print(result)

#lamba sub
import re

result= re.sub('[0-9]+', lambda m: str(int(m.group())* 10), '1 2 Fizz 4 Buzz Fizz 7 8')
print(result)

'''

#\\number
import re

result= re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1','hello 1234')
print(result)

result2= re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name":"james" }')
print(result2)


#reuse
import re

result= re.sub('({\s*)"(?P<key>\w+)":\s*"(?P<value>\w+)"(\s*})', '<\\g<key>>\\g<value></\\g<key>>', '{ "name":"james" }')
print(result)

'''
#문제2
import re #정규표현식을 사용하여 문자열 검색, 매칭, 치환 등의 작업을 수행할 수
            # 있게 해주는 모듈
# 테스트할 문장 목록
sentences = [ "I love programming in Python.",
"JavaScript is a versatile language.",
"The Python snake is a non-venomous species."]

# 정규표현식 패턴
pattern = r'Python'

# 문장 판별
for sentence in sentences:
    if re.search(pattern, sentence):
        print(f"'Python' found in: \"{sentence}\"")
    else:
        print(f"'Python' not found in: \"{sentence}\"")

#문제4
import re

text = "alice@example.com 이 첫 번째 이메일이고, 다음은 bob.smith@mail.co.uk 입니다."

pattern= '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

match= re.match(pattern, text)

if match:
    print(match.group())
else:
    print("문자열의 시작 부분에 이메일이 없습니다.")

#문제5
import re

text = "Hello, how are you today? Hello, I'm fine."

pattern= r'^Hello'

match= re.match(pattern, text)

if match:
    print("문자열은 'Hello'로 시작합니다.")
else:
    print("문자열은 'Hello'로 시작하지 않습니다.")

#문제6
import re

text= "This is a sample text with the word 'sample' in it."

pattern = r'sample'

match= re.search(pattern, text)

if match:
    print("we found word.")
else:
    print('we cannot found that word')

#문제7
import re

text = "오늘의 날짜는 2023-06-28이고, 내일은 2023-06-29입니다."

pattern= '[0-9]{4}-[0-9]{2}-[0-9]{2}'

matches= re.findall(pattern, text)

if matches:
    print("찾은 날짜들 : ", matches)
else:
    print("날짜 형식을 찾을 수 없습니다.")

#문제8
import re

text = "다음 사람들에게 이메일을 보내세요: alice@example.com, bob.smith@mail.co.uk, charlie123@domain.org."

pattern= r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails= re.findall(pattern, text)

print(emails)

#문제9
import re

text = "상품의 가격은 19.99달러와 100.0달러, 0.99달러 입니다."

pattern= r'\d+\.\d+'   #\d+는 하나 이상의 숫자

numbers= re.findall(pattern, text)

print(numbers)

#문제10
import re

text = "<html><head><title>Test</title></head><body><h1>Header</h1><p>Paragraph</p></body></html>"

pattern= r'\<[0-9a-zA-Z/]+\>'

html= re.findall(pattern, text)

print(html)

#문제11
import re

def check_password_strength(password):
    pattern = r'^(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-zA-Z]).{8,}$'

    match = re.fullmatch(pattern, password)
    
    return match is not None

password1 = "StrongPassword123!"
print(f"Password '{password1}' is strong: {check_password_strength(password1)}")

newPswd = input('\n패스워드를 입력하세요: ')
if check_password_strength(newPswd):
    print('안전한 패스워드입니다.')
else:
    print('패스워드의 기준에 맞지 않습니다')

#문제12
import re

text = "Hello! @world! This is 2024. @#$%^&*"

pattern= r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]'

line= re.sub(pattern, '', text)

print(line)

'''