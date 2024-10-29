# 로봇이 일정 거리를 이동한 후 감지
# 그리고 각각 이후 사후 분포 신념으로 종료

# 주어진 목록의 Motions = [1, 1]은 로봇을 의미
# 오른쪽으로 이동한 다음 다시 오른쪽으로 이동하여 후방을 계산
# 분포 로봇이 먼저 빨간색을 감지한 다음 이동하면 오른쪽 하나, 녹색을 감지한 다음 다시 오른쪽으로 이동
# 균일한 사전 분포로 시작

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1, 1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)

    for i in range(len(q)):
        q[i] = q[i]/s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for i in range(len(measurements)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])

'''   
# 로봇이 빨간색을 두 번 감지하도록 이전 코드를 수정
for k in range(len(measurements)):
    p = sense(p, 'red')
    p = move(p, motions[k])
'''
    
print(p)