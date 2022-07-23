print('Input any word and press enter to add the another word:')
words = input() 
list = []
while words != "":
    list.append(words) 
    words = input()
print(list)
longest_word = 0
for word in list:
    if len(word) > longest_word:
        longest_word = len(word)
        words = word
print("The length of the longest word in the given list of words is", len(words))