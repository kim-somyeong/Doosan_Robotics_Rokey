# 출력을 정규화하도록 sense_function의 코드를 수정함
# 합계가 1이 되도록 (정규화 로직을 적용하자!)
# sense 함수의 q의 항목이 합계가 1이 되어야 (정규화) 합니다.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'green'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q = []
    sum = 0
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
        sum += q[i]
    q = [x/sum for x in q]
    return q

print (sense(p, Z))