words = []
palindromes = []

for i in range(5):
    word = input("So'z kiriting!: ")

    words.append(word)

    if word == word[::-1]:
        palindromes.append(word)
        
print(palindromes)
