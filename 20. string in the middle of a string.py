str = input("Enter a string with even no. of characters only:")
str2 = input("Enter character or string to be inserted in the middle of the first string:")
n = int(len(str)/2)
str3 = str[0:n] + str2 + str[n:]
print(str3)