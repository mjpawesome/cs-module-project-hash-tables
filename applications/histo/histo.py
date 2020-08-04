# Your code here

with open("robin.txt", mode='r', encoding='utf-8') as data:
    f = data.read()

counts = dict()
wordlist = []
word = ""

for char in f:  
    if char.isalpha():
        word += char
    else:
        if len(word) != 0:
            wordlist.append(word)
        word = ""

for word in wordlist:
    word = word.lower()
    if word in counts and word != "":
        counts[word] += 1
    elif word != "":
        counts[word] = 1

s = sorted(counts.items(), key=lambda x: x[0], reverse=False)

sort_counts = sorted(s, key=lambda x: x[1], reverse=True)

for i in sort_counts:

	print(i[0] + " " * (17 - len(i[0])) + '#' * i[1])

