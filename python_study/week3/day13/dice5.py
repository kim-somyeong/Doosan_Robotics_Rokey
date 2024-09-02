import random

def throwDice():
    return random.randint(1, 6)

if __name__ == "__main__":
    print("testing throwDice()")
    for i in range(10):
        print(throwDice(), end= ' ')
    print("")