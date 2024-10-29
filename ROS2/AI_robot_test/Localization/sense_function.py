# p와 Z를 입력으로 사용하고, 정규화되지 않은 결과를 출력
# 확률 분포, p 항목을 곱한 후 p by pHit 또는 pMiss 색상에 따라 각 셀을 리스트로 구성

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    #Enter code here
    for i in range(len(p)):
        if world[i] == Z:
            p[i] *= pHit
        else:
            p[i] *= pMiss
    return p

print (sense(p,Z))