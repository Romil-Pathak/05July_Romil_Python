t=open('text1.txt','r+')
x=t.read().split()
'''a=x[0]
l=[]
for i in x:
    for j in x:
        if len(i)>len(j):
            x=i
        else:
            x=j
print('the longest word is:',x)'''

l=list(sorted(x,key=len))
'''print('the longest word is:',l[-1])'''
'''for items in range(0,(len(l)-1)):
    if len(l[items])==len(l[-1]):
        print('longest words are:',l[items],l[-1])
    elif len(l[items])!=len(l[-1]):
        print('longest word:',l[-1])
        break'''

a=max(l,key=len)
print(a)



