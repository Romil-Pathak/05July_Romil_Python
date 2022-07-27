x = input("Enter words separated by a space:")
l = x.split()
longest_word = 0
for word in l:
    if len(word) > longest_word:
        y = word
print("The length of the longest word/words in the given list of words is", len(y))