'''
#실습문제4
def count_word_in_file():
    word=input("write the count word :")
    count=0
    with open("output.txt", "r") as file:
        content= file.read()
        count= content.count(word)
    print(f'{word} : {count}')

count_word_in_file()


#실습문제5
def print_lines_with_numbers():
    with open("output.txt", "r") as file:
        lines = file.readlines()
        for index, line in enumerate(lines):
            print('{index+1} : {line.strip()}')

print_lines_with_numbers()


#문제5
f= open("data.txt", encoding="utf=8")
s= f.read()
print(s)

#문제7
with open("data.txt")as f:
    for line in f:
        print(line.strip())
f.close()

#문제8
with open("data.txt", "a") as file:
    file.write("Here coems to the end.\n")

with open("data.txt") as file:
    s= file.read()
    print(s)


#문제9
with open("python.txt", encoding="utf-8") as f:
    s=f.read()
    print(s)


#문제10
with open("data.txt", "r") as f:

    new_file_name = input('write the file name :')

    with open(new_file_name,"w") as file:
        line = f.readline()
        while line:
            file.write(line)
            line=f.readline()

with open(new_file_name, "r") as new_file:
    print(new_file_name)
    for line in new_file:
        print(line, end='')


#문제11
with open("data2.txt", "w") as f:
    f.write("Hello. This is data2.txt.\n")
    f.write("This is simple txt file.")

with open("data.txt", "r") as f1:
    content1= f1.readlines()
    print(f' data1.txt : {content1}')

with open("data2.txt", "r") as f2:
    content2= f2.readlines()
    print(f' data2.txt : {content2}')

new_content= content1 + content2

with open("data3.txt", "w") as f3:
    f3.writelines(new_content)

with open("data3.txt", "r") as f3:
    for line in f3:
        print(line.strip())

       

#문제14
def search_list(filename, find_str): #파일에서 검색할 문자열을 찾아서 해당 줄에 출력하는 함수
    lineNum= 1 #줄 번호 초기화
    found = False #검색 결과 여부 초기화

    with open(filename) as f:
        for line in f:
            if find_Str in line:
                found = True #검색한 문자열 발견
                print(f"{lineNum} : {line.strip()}")
            lineNum +=1 #다음 줄

    if found == False:
        print("No word in file") #검색 결과 없는 경우 

filename= input('write the file name :')
find_Str = input('What do you want to search? :')

search_list(filename, find_Str)


#문제15 & 문제12
with open("data1.txt", "r") as f1:
    lines1 = f1.readlines()
    float1 = [float(line.strip()) for line in lines1]

with open("data2.txt", "r") as f2:
    lines2 = f2.readlines()
    float2 = [float(line.strip()) for line in lines2]

new_list = float1 + float2

sorted_list = sorted(new_list)

with open("data3.txt", "w") as f:
    for num in sorted_list:
        f.write(f"{num}\n")

print("data3.txt 파일에 정렬된 결과가 저장되었습니다.")

search_num= float(input("write the search num : "))

found=False
line_num=0

with open("data3.txt", "r") as f:
    for line in f:
        line_num+= 1
        num= float(line.strip())
        if float(search_num) == num:
            found= True
            print('search num : ', line_num)
            break

if not found:
    print('There is no num.')

#문제13 & 문제16


#문제17
def copy_file():
    target_fil= input('write the copy file : ')
    new_file= input("write the new file name : ")

    with open(target_fil, 'r') as f:
        content = f.read()

    with open(new_file, 'w') as f2:
        f2.write(content)

    with open(new_file, 'r') as f2:
        for line in f2:
            print(line.strip())

copy_file()


#문제18
def without_comment():
    source_file = input("write the file name : ")
    new_file = "new_" + source_file

    with open(source_file, 'r') as f:
        lines= f.readlines()

    with open(new_file, 'w') as f2:
        for line in lines:
            if "#" in line:
                line= line.split("#")[0].rstrip() + "\n"
            if line.strip():
                f2.write(line)
    print(new_file)
    with open(new_file, 'r') as f2:
        for line in f2:
            print(line, end=" ")
        

without_comment()


#문제19
def count_word():
    file_name = input("write the file name : ")

    with open(file_name, 'r') as f:
        content = f.read()

    #단어분리
    words= content.split()

    word_count = len(words)
    print(f'{file_name} words : total {word_count}')

count_word()


#문제16

# data1.txt 파일 읽기
with open("data1.txt", "r") as f1:
    lines1 = f1.readlines()
    float1 = [float(line.strip()) for line in lines1]

# data2.txt 파일 읽기
with open("data2.txt", "r") as f2:
    lines2 = f2.readlines()
    float2 = [float(line.strip()) for line in lines2]

# 두 리스트 합치기
new_list = float1 + float2

# 합친 리스트 정렬
sorted_list = sorted(new_list)

# 정렬된 결과를 data3.txt 파일에 쓰기
with open("data3.txt", "w") as f:
    for num in sorted_list:
        f.write(f"{num}\n")

print("data3.txt 파일에 정렬된 결과가 저장되었습니다.")

# 사용자가 입력한 숫자 검색
search_num = float(input("검색할 숫자를 입력하세요: "))

found = False
line_num = 0

# data3.txt 파일에서 숫자 검색
with open("data3.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line_num += 1
        num = float(line.strip())
        if search_num == num:
            found = True
            print('검색한 숫자 위치: ', line_num)
            break
            
#문제20
import csv

def merge_and_filter_csv():
    input_files = ["data1.csv", "data2.csv"]
    output_file = "data3.csv"
    combined_rows = []

    # 각 파일을 읽고 나이가 20세 이상인 데이터만 combined_rows에 추가
    for file in input_files:
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            if not combined_rows:
                combined_rows.append(headers)  # 첫 번째 파일의 헤더만 추가
            combined_rows.extend(row for row in reader if int(row[1]) >= 20)

    # 합친 데이터를 새로운 CSV 파일에 저장
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(combined_rows)

    print(f"{output_file} 파일에 20세 이상인 데이터가 저장되었습니다.")

merge_and_filter_csv()

#문제21
import os
import shutil

def copy_file(source, destination, extension):
    #대상 디렉토리 생성
    os.makedirs(destination, exist_ok=True)

    #파일 검색 및 복사
    for filename in os.listdir(source):
        if filename.endswith(extension):
            source_file= os.path.join(source, filename)
            dest_file= os.path.join(destination,filename)
            shutil.copy(source_file,dest_file)
            print("copy finish")

def main():
    source_dir= input("write the source path : ")
    dst_dir= input("write the target path : ")
    file_extention= input("write the copy file (e.x. .txt) : ")

    copy_file(source_dir, dst_dir, file_extention)

main()   


#문제22
def count_word():
    word= input("write the count word : ")
    count=0
    with open("news.txt", 'r') as f:
        content= f.read()
        count= content.count(word)
    print(f'{word} : total {count}')

count_word()

'''
#문제23
import os
import hashlib

def find_and_delete_duplicates():
    directory = input("중복 파일을 찾을 디렉토리 경로를 입력하세요: ")
    file_hashes = {}
    duplicates = []

    # 디렉토리 내 파일의 해시값 계산 및 중복 파일 찾기
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in file_hashes:
                duplicates.append(file_path)
            else:
                file_hashes[file_hash] = file_path

    # 중복 파일 삭제
    for file in duplicates:
        os.remove(file)
        print(f"삭제됨: {file}")

    print(f"총 {len(duplicates)}개의 중복 파일이 삭제되었습니다.")

find_and_delete_duplicates()