words = ['salom','hi','bonjour','privet']

max_length = len(words[0])

for word in words :
    if len(word) > max_length:
        max_length = len(word)


max_words = []

for word in words:
    if len(word) == max_length:
        max_words.append(word)

print(max_words)