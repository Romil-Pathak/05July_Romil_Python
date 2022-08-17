def fact(x):
    if x==1:
        return x
    else:
        return x*fact(x-1)
n=int(input("Enter any positive no.:"))
if n==0:
    print("The factorial of 0 is 1")
elif n<0:
    print("The no. is not positive")
else:    
    print(fact(n))


