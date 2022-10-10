t=open('text1.txt','r+')
list=[]
for number in range(ord("a"), ord("h")):
    list.append(chr(number))
x=zip(list,t.readlines())
y=dict(x)
for i in y:
    print(i,':',y[i],end='')
print()

    