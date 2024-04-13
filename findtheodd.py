# def find_it(seq):
#     #Dictionary to know how many times a number appear
#     counts = {}
#     #list to put the number that appear odd times
#     odd = []
#     #Iterate the list given by the user and put it in the dictionary
#     for number in seq:
#         if number in counts:
#             counts[number] += 1
#         else:
#             counts[number] = 1
#     #Check if the times the number appears are odd
#     for element in counts:
#         pair = counts[element]
#         if pair % 2 == 0:
#             continue
#         else:
#             odd = element
#     #Return the list with the odd numbers
#     return odd

# lista = find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
# print(lista)

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

lista = find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
print(lista)
