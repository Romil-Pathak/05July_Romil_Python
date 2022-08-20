import random
def randomline(file):
    lines = open(file).read().splitlines()
    return random.choice(lines)
print(randomline('text.txt'))