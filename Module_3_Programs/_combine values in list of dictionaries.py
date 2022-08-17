from collections import Counter
l = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},{'item': 'item1', 'amount': 750}]
result = Counter()
for items in l:
    result[items['item']]= result[items['item']] + items['amount']
print(result)


'''from collections import Counter
l = [{'item': 100, 'amount': 100}, {'item': 200, 'amount': 100},{'item': 300, 'amount': 100}]
dict1 = l[0]
dict2 = l[1]
dict3 = l[2]
Cdict = Counter(dict1) + Counter(dict2) + Counter(dict3)
print(Cdict)'''


