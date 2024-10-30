#------------------------
# 다음을 반환하는 optim_policy 함수를 작성합니다
# 로봇에 대한 최적의 정책을 보여주는 그리드
# 모션. 이는 최적의 조건이 있어야 함을 의미
# 탐색 가능한 각 셀과 연관된 방향
# 목표는 달성할 수 있다
#
# 탐색할 수 없는 셀뿐만 아니라
# 목표에 도달할 수 없는 경우 문자열이 있어야 합니다
# 다음과 같이 단일 공백(' ')을 포함한다
# 목표 셀에는 '*'가 있어야 한다
#-------------------------

# 기본 입력 및 설정

grid = [[0, 1, 0, 0, 0, 0],             # 0 : 이동 가능
        [0, 1, 0, 0, 0, 0],             # 1 : 장애물
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]                           # 시작 위치를 지정
goal = [len(grid) - 1, len(grid[0]) -1] # 목표 위치 (마지막 행과 마지막 열의 좌표로 설정)
cost = 1            # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],       # go up
         [0, -1],       # go left
         [1, 0],        # go down
         [0, 1]]        # go right

delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid, goal, cost):
    # 최적 경로를 찾기 위한 초기화
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]   # 목표 위치까지의 최소 이동 비용을 저장하는 그리드 (초기값으로 높은 값 99를 설정)
    policy = [['' for row in range(len(grid[0]))] for col in range(len(grid))]  # 각 셀에서 목표까지 가기 위한 최적의 방향을 표시할 2D 리스트
    policy[len(grid) - 1][len(grid[0]) - 1] = '*'                               # 목표 위치는 '*'로 설정해 목표지임을 표시
    
    # 최적 경로 계산을 위한 반복 (탐색 단계)
    change = True               # value 그리드가 업데이트 -> True로 설정해 반복
    while change:
        change = False          # 모든 경로가 안정화 -> False로 반복 종료

        # 셀마다 경로 탐색 및 비용 갱신
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0

                        change = True

                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]

                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2] + cost

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2
                                policy[x][y] = delta_name[a]
    return policy


#print(optimum_policy(grid, goal, cost))

for row in optimum_policy(grid, goal, cost):
    print(row)        