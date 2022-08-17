d = {1:'pradip',3:'dipal'}
n=int(input('enter key no. to be checked:'))
for i in d:
    if n==i:
        print('Key is present in the dictionary')
        break
else:
    print('Key is not present in the dictionary')

