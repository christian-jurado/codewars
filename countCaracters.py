def count(s):
    # The function code should be here
    letters = {}
    for letter in s:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    return letters

print(count('aba'))
