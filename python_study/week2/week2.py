#문제2
import random

def generate_lotto_numbers():
    result = []

    while len(result)< 6:
        rand_num= random.randint(1,45)

        if rand_num not in result:
            result.append(rand_num)

    result.sort()
    return result

numbers = generate_lotto_numbers()
print(numbers)

#문제3
def rotate_90_degrees(matrix):
    # 행렬의 크기를 얻음
    rows = len(matrix)
    cols = len(matrix[0])
    
    # 결과를 저장할 빈 행렬 생성 (크기: cols x rows)
    rotated_matrix = [[0] * rows for _ in range(cols)]
    
    # 회전 작업 수행
    for r in range(rows):
        for c in range(cols):
            rotated_matrix[c][rows - 1 - r] = matrix[r][c]
    
    return rotated_matrix

def solution(matrix):
    return rotate_90_degrees(matrix)

# 예시 입력
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 회전된 결과
result = solution(matrix)
print(result)