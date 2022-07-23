str = input('Enter a string:')

if str.find('not') != -1 and str.find('not')< str.find('poor'):
    str2 = str[0:str.find('not')] + 'good'
    print(str2)
else:
    print(str)