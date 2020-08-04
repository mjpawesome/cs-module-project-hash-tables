import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

wordList = words.split()
wordDict = dict()

for (index, word) in enumerate(wordList):
    if index < len(wordList)-1:
        if word not in wordDict:
            wordDict[word] = [wordList[index+1]]
        elif word in wordDict:
            wordDict[word].append(wordList[index+1])

while True:
    rnd_word = random.choice(wordList)
    if rnd_word[0].isupper() == True:
        break
    
while True:
    print(rnd_word,end=" ")
    old_word = rnd_word
    length = len(wordDict[old_word])
    rnd_index = random.randint(0, length-1)
    rnd_word = wordDict[old_word][rnd_index]
    if "?" in rnd_word or "!" in rnd_word or "." in rnd_word:
        print(rnd_word,end=" ")
        break