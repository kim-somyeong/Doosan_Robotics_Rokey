# Modify the move function to accommodate the added
# probabilities of overshooting or undershooting
# the intended destination

p = [0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.appened(p[i] *(hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i]/s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        exact = p[(i-U) % len(p)] * pExact
        under = p[(i-U-1) % len(p)] * pUndershoot
        over = p[(i-U+1) % len(p)] * pOvershoot
        q.append(exact + under + over)
    return q

print (move(p, 1))      # Move Once
print (move((move(p, 1)), 1))       # Move Twice

for _ in range(1000):
    p = move(p, 1)

print(p)        # moved a thousand times