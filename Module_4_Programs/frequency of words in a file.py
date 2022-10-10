from collections import Counter
with open('text1.txt', 'r') as p:
    nwords = Counter(p.read().split())
    print('Total Number of words:', nwords)

