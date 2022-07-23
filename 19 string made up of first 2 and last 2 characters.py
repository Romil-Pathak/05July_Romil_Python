str = input("Enter a string:")
if len(str)>3:
    str1 = str[0:2]+str[-2:]
    print(str1)
elif len(str)==2:
    print(str+str)
else:
    print('Empty String')