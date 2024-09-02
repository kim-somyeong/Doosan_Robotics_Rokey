'''
#예외처리기법
print('예외 처리 확인 프로그램')
try:
    s= input("write the num : ")
    n= int(s)
    print(f'write num : {n}')

except:
    print(f' 정수로 변환할 수 없습니다.')


#예외처리_ 모든 오류 함께 처리
try:
    lst=[1,2,3]
    idx= int(input('변경할 요소의 위치를 입력하세요 : '))
    n= int(input("새로운 값을 입력하세요 :"))
    lst[idx]= n
    print(lst)
except:
    print("오류 : 인덱스 범위를 벗어났거나 정수가 아닌 문자열을 입력했음")

#예외처리_각 오류 명시
try:
    lst= [1, 2, 3]
    idx= int(input("변경할 요소의 위치(인덱스)를 입력하세요 : "))
    n= int(input("새로운 값을 입럭하세요. : "))
    lst[idx]= n
    print(lst)
except ValueError:
    print("오류 : 정수가 아닌 문자열을 입력했음.")
except IndexError:
    print("오류 : 인덱스 범위를 벗어남.")

#sys 모듈의 exit함수 이용
import sys
try:
    fname= "a.ini"
    f=open(fname)
    lines= f.readlines()
    f.close()
except FileNotFoundError:
    print("Could you open " + fname)
    sys.exit()
except:
    print("Other error occurred")
print("ENd of the program")

#실습문제1
def basic_exception_hadling():
    try:
        a= int(input('분자를 입력하세요 : '))
        b= int(input('분모를 입력하세요 :'))
        result= a/b
        print("result :", result)
    except ZeroDivisionError:
        print("오류 : 0으로 나눌 수 없습니다.")
basic_exception_hadling()


#raise
try:
    x= int(input("3의 배수 입력 : "))
    if x%3 != 0:
        raise Exception("3의 배수 아님!")
    print(x)
except Exception as e:
    print('에러 발생 :', e)
print("End of the program")

#re-raise
def three_div():
    try:
        x= int(input("3의 배수 입력 : "))
        if x%3 != 0:
            raise Exception("3의 배수 아님!")
        print(x)
    except Exception as e:
        print('에러 발생 :', e)
        raise

try:
    three_div()
except Exception as e:
    print('code error : ', e)

#pass
try:
    print(3/0)
except ZeroDivisionError:
    pass
print("error but print ")

#실습문제3
def print_exception_info():
    try:
        num= int(input('write the num : '))
        result= 100 / num
        print('result :', result)

    except Exception as e:
        print(f'error :{type(e).__name__}, explain : {e}')

print_exception_info()

#실습문제4
def read_file_with_finally():
    try:
        file= open("output.txt", "r")
        print(file.read())
    except FileExistsError:
        print("Error : Not found the file")
    finally:
        file.close()
        print("file close")

read_file_with_finally()

#실습문제5
def raise_exception_on_age():
    age= int(input("write the age :"))
    if age <= 0:
        raise ValueError("age bigger than 0 ")
    print("age :", age)

try:
    raise_exception_on_age()
except ValueError as e:
    print(f' error : {e}')

#실습문제7
def exception_chaining():
    try:
        filename= input('writet the file name :')
        with open (filename, "r") as file:
            print(file.read())
    except FileNotFoundError as e:
        raise FileNotFoundError("Can't open the file. Check the filename.") from e
    
try:
    exception_chaining()
except FileNotFoundError as e:
    print(e)
    print("원래의 예외 : ", e.__cause__)


#실습문제8
def safe_file_handling():
    try:
        with open("data.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error : Can't find the file.")

safe_file_handling()

#문제3
print("try/except ")
try:
    s=input("정수를 입력하세요 :")
    n= int(s)
    print(f'사용자가 입력한 정수 : {n}')
except:
    print("숫자를 입력하지 않았어요.")

#문제4
import sys

def search_file(): 
    while True:  #무한 루프 
        try:
            filename=input("write thie file name : ")
            with open(filename) as f:
                lines=f.readlines()
                print(lines)
                return
        except FileNotFoundError:
            print('Could not open. Try again.')

        try:
            filename2= input('write again :')
            with open(filename2) as f2:
                lines=f.readlines()
                print(lines)
                return #파일 성공적으로 읽으면 종료
        except FileNotFoundError:
            print('Coult not open file. Exiting the program')
            sys.exit()
print("End of the program") 
search_file()    

#문제5 (1)
try:
    A=[1,2,3]
    A[3]
except IndexError:
    print('Error: Index Error.')

#문제5 (2)
try:
    {'fb': 11, 'bb' : 9, 'vb' :6}['foot']
except KeyError:
    print('Error : Key Error')

#문제5 (3)
try:
    p1= 'python' + 3
except TypeError:
    print('Error : Type Error') 


#문제6
def divide(x, y):
    try:
        answer= x/y
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다.')
    else:
        print(f'결과 : {answer}')
        return answer
    
divide(16, 10)

#문제7 (1)
try:
    print(int("abc"))

except Exception as e:
    print(f'예외 발생 이름 : <{type(e).__name__}>')
    print(f'예외 발생 이유 : {e}')

else:
    print('예외가 발생하지 않았습니다')

finally:
    print('예외 처리가 잘되는군요!')

#문제7 (2)
try:
    print(int("10"))

except Exception as e:
    print(f'예외 발생 이름 : .{type(e).__name__}>')

else:
    print('잘 실행됐습니다.')

finally:
    print('예외 처리가 잘되는군요')


#문제8
try:
    s= input('정수를 입력하세요 : ')
    number= int(s)

except ValueError as e:
    print(f'예외 발생 이름 : {type(e).__name__}')
    print(f'예외 발생 이유 : {e}')

else:
    print(f'입력한 정수는 {number}입니다. ')

finally:  #예외 발생 여부오 상관없이 항상 실행
    print('입력 처리 완료')

#문제9
try:
    file = input('write the file name :')
    with open(file, "r") as f:
        lines=f.readlines

except FileNotFoundError as e:
    print(f'예외 발생 이름 : {type(e).__name__}')
    print(f'예외 발생 이유 : {e}')

else:
    print(f'file name : {file}')

finally:
    print('finish')

#문제10
def calculator():
    try:
        num1 = float(input('첫 번째 숫자를 입력하세요. : '))
        num2= float(input('두 번째 숫자를 입력하세요 : '))
        operator = input("연산자를 입력하세요.(+, -, *, /) : ")

        result= 0

        if operator == '+':
            result= num1 + num2
        elif operator == '-':
            result= num1 - num2
        elif operator == '*':
            result= num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("0으로 나눌 수 없습니다.")
            result = num1/ num2
        else:
            raise ValueError("잘못된 연산자입니다.")
        
    except ValueError as ve:
        print(f'예외 발생 이름 : <{type(ve).__name__}>')
        print(f'예외 발생 이유 : {ve}')
    
    except ZeroDivisionError as zde:
        print(f'예외 발생 이름 : <{type(zde).__name__}>')
        print(f'예외 발생 이유 : {zde}')
    
    else:
        print(f'계산 결과: {result}')
    
    finally:
        print('계산이 완료되었습니다.')

calculator()

'''
#문제11
def calculate_sum():
    input_str= input('숫자를 쉼표로 구분하여 입력하세요(e.x. 1, 2, 3, 4) :')

    try:
        numbers= input_str.split(',')
        int_number= [int(num.strip()) for num in numbers]

        total= sum(int_number)

        print('total :{total}')

    except ValueError:
        print('입력값에 숫자가 아닌 값이 있습니다.')

calculate_sum()