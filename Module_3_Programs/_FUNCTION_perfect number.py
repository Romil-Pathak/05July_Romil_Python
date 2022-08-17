def per_num():
    sum=0
    n=int(input("enter any no."))
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print('the no. is a perfect no.')
    else:
        print('the no. is not a perfect no.')
per_num()
        