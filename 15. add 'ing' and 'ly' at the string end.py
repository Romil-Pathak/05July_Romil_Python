x = input("Enter a string:")
if len(x)>=3:
    if x[-1]=='g' and x[-2]=='n' and x[-3]=='i':
        x = x + 'l'+ 'y'
        print(x)
    else:
        x = x + 'i'+ 'n'+ 'g'
        print(x)
else:
    print(x)