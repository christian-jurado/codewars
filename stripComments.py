# def strip_comments(strng, markers):
    # First marker ignore the next word, second cut off the string
    # Need to make the string separeted (for loop)
    # Need to check if the first marker exist
    # if the second marker does exist, end the iteration
    # While iterating create a new string with the words
    # Return the new string


    # skip = markers[0]
    # end = markers[1]
    # new_strng = ""
    # skip_next_word = False
    # skip_space = True
    # if " " == strng[0]:
    #         new_strng += " "
    # for word in strng:
    #     if skip_next_word:
    #         skip_next_word = False
    #         continue
    #     if skip == word:
    #         skip_next_word = True
    #     elif end == word:
    #         return new_strng
    #     elif word == ",":
    #         new_strng += word
    #         skip_space = False
    #     elif word == "\n":
    #         new_strng += word
    #     elif word.isspace() and skip_space:
    #         skip_space = True
    #         continue
    #     else:
    #         new_strng += word

    # return new_strng

def strip_comments(strng, markers):
    new_strng = ""
    marker_found = False

    for char in strng:
        if char in markers:
            marker_found = True
        elif char == '\n':
            marker_found = False
            new_strng = new_strng.rstrip(" ")
            new_strng += char
        elif char == '\t':
            continue
        elif not marker_found:
            new_strng += char
    new_strng = new_strng.rstrip(" ")
    return new_strng

# print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))
# a
# c
# d

# print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
# apples, pears
# grapes
# bananas

print(strip_comments("\t#\n", [',', '!', '#', '-', '?', "'"]))
# '\t\n' should equal '\n'
