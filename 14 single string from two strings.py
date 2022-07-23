str1 = input("Enter the first string:")
str2 = input("Enter the second string:")

x = str1[0:2]
str1 = str1.replace(str1[0:2],str2[0:2])
str2 = str2.replace(str2[0:2],x)
str = str1 + ' ' + str2
print(str)