intro = input("Give an Introduction")
characterCount=0
wordCount=1

for i in intro:
    characterCount=characterCount+1

    if(i==' '):
        wordCount=wordCount+1

print("number of word in intro")
print(wordCount)
print("number of characters in the intro")
print(characterCount)