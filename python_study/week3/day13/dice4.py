import random

def throwDice():
    return random.randint(1, 6)

print(f"dice4 : __name__ = {__name__}")
print("testing throwDice()")
for i in range(10):
    print(throwDice(), end= ' ')
print("")    