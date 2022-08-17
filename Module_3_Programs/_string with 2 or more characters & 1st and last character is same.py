l = ['R', 'Ahmedabad', 'Baroda', 'Surat', 'rampur']
x = 0
for i in range(0, len(l)):
    if l[i][0] == l[i][-1] and len(l[i])>2:
        x = x + 1
print('The count of the string is:', x)