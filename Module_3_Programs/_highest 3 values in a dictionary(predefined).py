d = {'a': 10, 'b': 15, 'c': 11, 'd': 19, 'e':6}
'''for i in d.keys():
    for j in d.keys():
        if d[i]>d[j]:
            x = d[i]
print(x)'''
y = sorted(d, key=d.get)
dict={}
for j in y:
    dict[j]=d[j]
l = list(dict.values())
n = len(l)
for i in range(-1,-4,-1):
    print(l[i])

