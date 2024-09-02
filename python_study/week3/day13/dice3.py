import random

def throwDice():
    return random.randint(1,6)

print("testhing throwDice()")
for i in range(10):
    print(throwDice(), end= ' ')
print("")