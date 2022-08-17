def l():
    n = input("Enter the numbers to be added into a list separated by a space:")
    list = n.split()
    for i in range(0,len(list)):
        list[i] = int(list[i])
    print(list)
    j = list[0]
    for number in list:
        if number > j:
            j = number
    print("Largest number in the list is:", j)
    for number in list:
        if number < j:
            j = number
    print("Smallest number in the list is:", j)
    sum = 0
    for number in range(0,len(list)):
        sum = sum + list[number]
    print("The sum of all numbers in the list is:", sum)
l()

'''l=list(map(int, input("Enter numbers separated by a space:").split()))
print(l)'''