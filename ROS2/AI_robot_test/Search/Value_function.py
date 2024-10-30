#-------------------------------
# Problem:
# 
# 반환하는 함수 계산_값을 만듭니다
# 값의 그리드. 셀의 값은 최소값입니다
# 셀에서 목표까지 이동하는 데 필요한 이동 횟수
#
# 셀이 벽이거나 셀에서 목표 달성이 불가능한 경우,
# 해당 셀에 값 99를 할당
#--------------------------------


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]

goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1        # the cost associated with moving from a cell to an adjacent one

init = [0,0]

delta = [[-1, 0],       # go up
         [0, -1],       # go left
         [1, 0],        # go down
         [0, 1]]        # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1

def compute_value(grid, goal, cost):
    change = True
    while change:
        change = False

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
                            v2 = value[x2][y2] + cost_step

                            if v2 < value[x][y]:
                                change = True
                                value[x][y] = v2


                #print value
    return value                            


print(compute_value(grid, goal, cost))

for row in compute_value(grid, goal, cost):
    print(row)