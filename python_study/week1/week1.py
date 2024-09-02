'''
#1-1

num=int(input('please write number (0~9): '))

print((str(num)*10+'\n')*10)

#1-2
num=int(input('please write number(0~9): '))

for i in range(10):
    # 공백 출력
    print(' ' * (9 - i), end='')
    
    # 숫자 출력
    print(str(num) * (i * 2 + 1))


#3-21
line= input('write string : ')
num= int(input('location of char : '))

print(f'문자열 : {line}, 길이 : {len(line)}')
print(f'{num+1}번째 문자열 : {line[num]}')

#4-20
hour=int(input('hour(0~24) : '))
min= int(input('minute(0~59) : '))

new_hour = hour
new_minute = min - 45
    
if new_minute < 0:
    new_hour -= 1
    new_minute += 60
    
if new_hour < 0:
    new_hour = 23 

print(f'{new_hour}:{new_minute}')
print('alarm set!')

'''
#5-30
line1= input('write string 1: ')
line2= input('write string 2:')

sorted_line1= sorted(line1)
sorted_line2= sorted(line2)

if sorted_line1==sorted_line2:
    print('This is anagram!')
else:
    print('This is not anagram..')
