'''
#실습문제1

file_name= input('file name : ')

final= file_name.rindex('.') #rindex는 '.'이 없으면 오류 발생

print(file_name[:final])


#실습문제2

name= input('file name : ')

file= name.rfind('.')
if file==-1:  #rfind는 '.'이 없으면 -1을 반환한다.
    print(name)
else:
    print(name[:file])


word= input('word input : ')

word= word.strip()
word1=word.find(" ")

print(word[:word1])



#실습문제4

file= input('file : ')

n=file.rfind(".png")

if n==-1:
    print(file)
else:
    print(file[:n]+".jpg")


#실습문제5

inputstr= input('write the str :')

reversestr= inputstr[::-1]

print(reversestr)

#실습문제6

inputstr = input('write the str :')
upperstr = inputstr.upper()

print(upperstr)


#실습문제7

inputstr= input('write str :')
removeal= input('write remove alpha : ')

outputstr= inputstr.replace(removeal,'')

print(outputstr)

#실습문제9

inputstr= input('write str :')

wordCnt= len(inputstr.split())

print(wordCnt)


#실습문제14

inputstr= input('write str :')

code= inputstr.encode('utf-8')

print(code)


#문제8

input_string = input("세 개 이상의 단어로 구성된 문자열을 입력하세요: ")

words = input_string.split()

print(words[1])


#문제9

s= "Hello World"

new_s=s.split()

print(new_s[1].index('o'))


#문제10

numbers = "123456789"

print(numbers[0::2])
print(numbers[1::2])

#문제11

num= input('put in the hex string : ')

new_num= int(num, 16)

print(new_num)

#문제12

name= input('please write .jpg file : ')

name1= name.replace(".jpg",".png")
print(name1)

name2=name.rfind(".jpg")
print(name[:name2]+".png")

#문제13
first_str= input("write first str : ")
second_str= input("write second str : ")

result= first_str.find(second_str)

if result ==-1:
    print('nothing')
else:
    print('check in first_str')

new_result= first_str.index(second_str)
print(new_result)


#문제14

words= input('please write words : ')

reverse= words[::-1]

if words==reverse:
    print('palindrome')
else:
    print('not palindrome')


#문제16

first_str= input('write first str :')
second_str= input('write second str : ')

sorted_first_str= sorted(first_str)
sorted_second_str= sorted(second_str)

if sorted_first_str== sorted_second_str:
    print("That is are anagrams")
else:
    print("THat is not anagrams")


#문제17
num= int(input('choice your temperature type 1. cel or 2.fah : '))
temperature= float(input('write your temperature : '))

if num==1:
    print((temperature*9/5)+32)
else:
    print((temperature - 32)*5/9)


#문제18

first= input('write first string :')
second= input('write second string :')

first_sort=sorted(first)
second_sort= sorted(second)

if first_sort == second_sort:
    print('This is anagrams')
else:
    print('This is not anagram.')


#문제19

rgb= input('please write color code :')

red= int(rgb[0:2], 16)
green= int(rgb[2:4], 16)
blue= int(rgb[4:6],16)

print(f'({red}, {green}, {blue})')

'''

#문제20

p1= input('rock, scissors, paper : ')
p2= input('rock, scissors, paper : ')

if p1=='rock'and p2=='paper':
    print('p2 win')

if p1=='rock' and p2== 'rock' :
    print('end')
elif p1=='rock' and p2=='paper':
    print('p2 win!')
else:
    print('p1 win')
