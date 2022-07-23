n = int(input("Enter any positive integer:"))
if n==0:
    print("The sum of given no. is 0")
elif n>0:
    for i in range(1,n):
            n = n + i
    print("The sum of given integers is", n)