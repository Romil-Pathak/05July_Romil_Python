n1 = int(input("Enter the first no.:"))
n2 = int(input("Enter the second no.:"))
n3 = int(input("Enter the third no.:"))
if n1 == n2 or n1 == n3 or n2 == n3:
    sum = 0
else:
    sum = n1+n2+n3
print("The sum of the given three numbers is:", sum)   