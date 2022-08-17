d = {'1':['a','b'],'2':['c','d']}
l1 = d['1']
l2 = d['2']
for i in range(0,2):
    for j in range(0,2):
        x  = l1[i]+l2[j]
        print(x, end=' ')
print()

