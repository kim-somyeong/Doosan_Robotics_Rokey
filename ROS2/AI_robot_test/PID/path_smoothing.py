# 경로를 입력으로 사용하는 함수 Smooth를 정의한다
# (weight_data, Weight_smooth에 대한 선택적 매개변수 포함 및 허용 오차) 및 부드러운 경로를 반환
# 첫 번째와 마지막 포인트는 변경되지 않고 그대로 유지되어야 한다
# 
# 스무딩은 반복적인 업데이트를 통해 구현되어야 한다
# 원하는 정확도 수준까지 newpath의 각 항목에 도달
# 업데이트는 다음 지침에 따라 수행되어야 한다
# 경사 하강 방정식
#---------------------------------------------------------------------------------------------

from copy import deepcopy

def printpaths(path, newpath):
    for old, new in zip(path, newpath):
        print('[' + ','.join(' %.3f'%x for x in old) + '] -> [' + ','.join('%.3f'%x for x in new) + ']')

path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):

    # Make a deep copy of path into newpath
    newpath = deepcopy(path)

    change = tolerance

    while change >= tolerance:          # 변경 값이 거의 없을 때까지 계속
        change = 0
        # 스무딩 과정
        # path의 두번째 점부터 마지막에서 두번째 점까지만 반복
        #       : 시작점과 끝점은 그대로 유지하고, 경로의 중간 지점만 부드럽게 조정하기 위함
        for i in range(1, len(path) - 1):
            for j in range(len(path[0])): 

                # 두 가지 스무딩 변위
                d1 = weight_data * (path[i][j] - newpath[i][j])         # weight_data에 기반하여 원본 경로와의 차이를 줄이려는 변위
                d2 = weight_smooth * (newpath[i-1][j] + newpath[i+1][j] - 2 * newpath[i][j])    # weight_smooth에 기반한 변위로, 좌우 좌표 간 차이를 줄여 경로의 평활성을 높임
                
                # 변화 적용 및 업데이트
                change += abs(d1 + d2)          # change에 변화량을 더해 다음 반복의 기준으로 사용
                newpath[i][j] += d1 + d2        # d1, d2의 합이 newpath에 적용

    return newpath

# printpaths 함수
#   각 점을 원래 경로(path)와 조정된 경로(newpath)로 출력하여 스무딩이 적용된 결과를 시각적으로 확인
printpaths(path, smooth(path))