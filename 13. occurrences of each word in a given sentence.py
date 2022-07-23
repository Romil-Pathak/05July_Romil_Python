str = input("Enter a string:")
str = str.split() #converting string into a list
i = 0
count = 0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count=count+1
    print(str[i], "is present", count, "times")
    i=i+1

