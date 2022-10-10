t=open('text1.txt','r+')
list=[a.strip() for a in t.readlines()]
print(list)