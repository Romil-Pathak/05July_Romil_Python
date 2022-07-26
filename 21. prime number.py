n = int(input("Enter any positive number other than 1:"))
if n==2:
    print("The number is a prime number")
elif n%2 == 0:
        print("The number is not a prime number")
else:
    for i in range(2,n):
        if n%i == 0:
            print("The number is not a prime number")