def sort_array(numbers):
    odd_numbers = []
    for x in numbers:
        if x % 2 == 0:
            continue
        else:
            odd_numbers.append(x)

    odd_numbers.sort()

    odd = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            continue
        else:
            numbers[i] = odd_numbers[odd]
            odd += 1

    return numbers

# def sort_odd_numbers(numbers):
#     # Extract odd numbers from the original list
#     odd_numbers = [x for x in numbers if x % 2 != 0]

#     # Sort the odd numbers
#     odd_numbers.sort()

#     # Update the original array with sorted odd numbers
#     odd_index = 0
#     for i in range(len(numbers)):
#         if numbers[i] % 2 != 0:
#             numbers[i] = odd_numbers[odd_index]
#             odd_index += 1

#     return numbers

# Example usage:
# input_array = [5, 2, 9, 1, 8, 4, 7]
# result = sort_odd_numbers(input_array)
# print(result)

print(sort_array([5, 3, 2, 8, 1, 4]))
# [1, 3, 2, 8, 5, 4])
