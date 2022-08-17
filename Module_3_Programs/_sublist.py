l= [1, 5, 8, 9, 10]
for i in l:
    if type(i)== list:
        print("The list contains a sublist")
        break
else:
    print("The list doesn't contain a sublist")
