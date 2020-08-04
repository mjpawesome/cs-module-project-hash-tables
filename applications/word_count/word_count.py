def word_count(s):
    ignore = '"":;,.-+=/\|[]{}()*^&'
    counts = dict()
    lowercase = s.lower()
    words = lowercase.split()
    
    for word in words:
        word = word.strip(ignore)
        if word in counts and word != "":
            counts[word] += 1
        elif word != "":
            counts[word] = 1

    return counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))