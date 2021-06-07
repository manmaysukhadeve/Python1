f = open("text.txt","r")
filelines = f.readlines()
numberOfWords = 0
for line in filelines:
    words = line.split()
    numberOfWords = numberOfWords + len (words)
    print(line)
    print("Number Of Words")
    print(numberOfWords)
f.read()
f.close()