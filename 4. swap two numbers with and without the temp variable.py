'''n1 = int(input("Enter the 1st number:"))# with temp variable
n2 = int(input("Enter the 2nd number:"))

temp = n1
n1 = n2
n2 = temp

print("The 1st number after swapping:", n1)
print("The 2nd number after swapping:", n2)'''

P = int(input("Enter the 1st number:"))#without temp variable
Q = int(input("Enter the 2nd number:"))

'''P = P*Q
Q = P/Q
P = P/Q
print(int(P))
print(int(Q))'''

P = P+Q
Q = P-Q
P = P-Q
print("After swapping, the 1st no. will be:", P)
print("After swapping, the 2nd no. will be:", Q)