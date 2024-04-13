def duplicate_encode(word):
    #your code here
    encoded_word = []
    result = []
    for letter in word:
        l_letter = letter.lower()
        encoded_word.append(l_letter)
    for letter in encoded_word:
        if encoded_word.count(letter) > 1:
            letter = ")"
            result.append(letter)
        else:
            letter = "("
            result.append(letter)

    return "".join(result)

x = duplicate_encode("ddin")

print(x)


