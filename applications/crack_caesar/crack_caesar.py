# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

with open("ciphertext.txt", mode='r', encoding='utf-8') as data:
    f = data.read()

tally = {}

lettersbyfreq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# count frequency of each character in ciphertext file.
for char in f:
    if char.isalpha():
        if char not in tally:
            tally[char] = 1
        else:
            tally[char] += 1

# sort by freqency.
tally_sorted = sorted(tally.items(), key=lambda x: x[1], reverse=True)

# create new dictionary to hold translation table.
translate_dict = {}
index = 0

# merge key from tally_sorted with values from ordered lettersbyfreq list into translate_dict.
for key, value in tally_sorted:
    if key in lettersbyfreq:
        translate_dict[key] = lettersbyfreq[index]
        print(key, lettersbyfreq[index])
        index += 1

translated = ""

# iterate through ciphertext file and replace existing letters with those from translation dictionary.
for char in f:
    if char in translate_dict:
            # key = str(new_dict[char])
        translated += translate_dict[char]
    else:
        translated += char

print(translated)