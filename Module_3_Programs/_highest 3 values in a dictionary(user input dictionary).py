d = {}
n= int(input('Enter the range of the dictionary:'))
for i in range(n):
    key = input("Enter the key:")
    value = int(input("Enter the value:"))
    d[key]=value
print(d)

y = sorted(d, key=d.get)
dict={}
for j in y:
    dict[j]=d[j]
l = list(dict.values())
n = len(l)
for i in range(-1,-4,-1):
    print(l[i])