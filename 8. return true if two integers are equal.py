n1 = int(input("Enter the 1st no.:"))
n2 = int(input("Enter the 2nd no.:"))
if n1 == n2:
    print("True")
elif n1+n2 == 5 or n1-n2 == 5 or n2-n1 == 5:
    print("True")