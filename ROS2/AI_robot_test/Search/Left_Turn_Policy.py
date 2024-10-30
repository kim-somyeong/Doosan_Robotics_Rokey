#----------주요 변수 및 설정----------
# grid : 이동 가능한 공간(값이 0)과 장애물(값이 1)을 나타내는 2차원 리스트
# init : 시작 지점의 좌표 [x, y]
# goal : 목표 지점의 좌표 [x, y]
# cost : 각 이동의 비용으로, 여기서는 1로 설정되어 있다
# delta : 가능한 이동 방향을 나타내는 리스트
#       [-1, 0] : 위로 이동
#       [0, -1] : 왼쪽으로 이동
#       [1, 0] : 아래로 이동
#       [0, 1] : 오른쪽으로 이동
# delta_name : 각 이동 방향에 대한 기호
#       ^ : 위로 이동
#       < : 왼쪽으로 이동
#       v : 아래로 이동
#       > : 오른쪽으로 이동
#-----------------------------------

#-------------코드의 주요 기능--------------
# 경로 탐색 (search 함수):
#       시작 지점에서 목표 지점까지의 최단 경로를 찾는다
#       open 리스트를 사용하여 다음에 탐색할 노드를 관리한다
#       closed 리스트를 사용하여 이미 방문한 셀을 추적한다
#       action 리스트를 사용하여 각 셀에 도달하기 위해 어떤 행동 (이동 방향)을 취했는지 기록
# 정책 그리드 생성:
#       목표 지점에서 시작 지점까지 역추적하여 최단 경로를 구성
#       policy 그리드를 생성하여 각 셀에서 다음에 취할 방향을 기호로 표시한다
#       방향 기호는 delta_name에 정의된 기호를 사용
#       목표 지점은 '*'로 표시
#---------------------------------------

#-------------코드의 동작 과정--------------
# 초기화 :
#       closed 리스트를 생성하여 모든 셀을 0으로 초기화하고, 시작 지점을 1로 설정하여 방문 처리한다
#       action 리스트를 생성하여 모든 셀을 -1로 초기화
#       policy 리스트를 생성하여 모든 셀을 ''(공벡)으로 초기화
#       open 리스트를 시작 노드 [g, x, y]를 추가한다. 여기서 g는 이동 비용이다.
# 탐색 루프:
#       open 리스트가 빌 때까지 또는 목표 지점을 찾을 때까지 반복
#       open 리스트를 정렬하고 (비용 g에 따라 오름차순), 가장 비용이 적은 노드를 선택
#       선택된 노드가 목표 지점인지 확인하고, 맞다면 탐색을 종료
#       그렇지 않다면, 현재 위치에서 가능한 모든 이동 방향(상, 좌, 하, 우)을 확인한다
#               그리드 범위를 벗어나지 않고, 장애물이 아니며(grid[x2][y2]==0), 방문하지 않은 셀(closed[x2][y2] == 0)에 대해:
#                   새로운 위치 [x2, y2]를 open리스트에 추가하고, 비용 g2를 갱신한다
#                   해당 위치를 closed 리스트에 방문 처리한다
#                   action 리스트에서 해당 위치에 도달하기 위해 어떤 이동을 했는지 인덱스 i를 저장
# 경로 재구성:
#       목표 지점에서 시작하여 시작 지점까지 역으로 추적한다
#       현재 위치에서 action 리스트를 참조하여 이전 위치를 계산한다.
#       policy 그리드에 해당 이동 방향의 기호를 기록한다.
#       이 과정을 시작 지점에 도달할 때까지 반복한다.
#       목표 지점은 '*'로 표시한다
# 결과 반환:
#       완성된 policy 그리드를 반환한다.
#       이 그리드는 시작 지점에서 목표 지점까지의 최단 경로를 방향 기호로 보여준다.
#--------------------------------------

#grid = [[0, 0, 1, 0, 0, 0],             # 0 : 이동 가능
#        [0, 0, 0, 0, 0, 0],             # 1 : 장애물
#        [0, 0, 1, 0, 1, 0],
#        [0, 0, 1, 0, 1, 0],
#        [0, 0, 1, 0, 1, 0]]

grid = [[0, 0, 0, 0, 0, 0],             # 0 : 이동 가능
        [0, 0, 0, 0, 0, 0],             # 1 : 장애물
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],       # go up
         [0, -1],       # go left
         [1, 0],        # go down
         [0, 1]]        # go right

delta_name = ['^', '<', 'v', '>']

def search(grid, init, goal, cost):

    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [['' for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False           # flag that is set when search is complete
    resign = False          # flag set if we can't find expand
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()

            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i

    # policy search
    x = len(grid) - 1
    y = len(grid[0]) - 1
    policy[x][y] = '*'
    while([x, y] != init) :
        x1 = x - delta[action[x][y]][0]
        y1 = y - delta[action[x][y]][1]
        policy[x1][y1] = delta_name[action[x][y]]
        x = x1
        y = y1

    return policy   # make sure you return the shortest path

#print(search(grid, init, goal, cost))
for row in search(grid, init, goal, cost):
    print(row)