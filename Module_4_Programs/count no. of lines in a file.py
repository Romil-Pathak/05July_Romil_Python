with open('text1.txt', 'r') as p:
    nlines = len(p.readlines())
    print('Total Number of lines:', nlines)