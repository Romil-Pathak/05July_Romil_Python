n = int(input("Enter any positive integer:"))
if n==0:
    print("The sum of given no. is 0")
elif n>0:
    for i in range(n-1,0,-1):
            n = n + i
    print("The sum of given integers is", n)