def l(list):
        i = list[0]
        for n in list:
                if n>i:
                        i = n
        print("Largest number in the list is:", i)
        for n in list:
                if n < i:
                        i = n
        print("Smallest number in the list is:", i)
        sum = 0
        for n in range(0,len(list)):
                sum = sum + list[n]
        print("The sum of all numbers in the list is:", sum)
l(list(map(int, input("Enter numbers separated by a space:").split())))