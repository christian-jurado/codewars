def rot13(message):
    result = ""
    for char in message:
        if char.isalpha():
            shift = 13 if char.islower() else -13
            result += chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

print(rot13('aA bB zZ 1234 *!?%'))
