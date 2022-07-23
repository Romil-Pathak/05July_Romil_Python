n = int(input("Enter any positive number:"))
x = 1
if n==0:
    print("The factorial of zero is 1")
else:
    for i in range(n,0,-1):
            x = x*i
    print("The factorial of a given number is", x)