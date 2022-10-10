try:
    n=int(input('enter the odd no.:')) 
    if n%2==0:
        raise ValueError(n)
    else:
        print('the no. entered is correct')
except ValueError:
    print('enter odd no. only')

