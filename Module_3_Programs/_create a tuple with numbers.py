t=list((input('enter numbers without a space or a comma:')))
for i in range(len(t)):
    t[i]=int(t[i])
t=tuple(t)
print(t)

'''l=list(map(int, input("Enter numbers separated by a space:").split()))
print(l)
t=tuple(l)
print(t)'''