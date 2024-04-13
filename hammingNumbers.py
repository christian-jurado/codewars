def hamming(n):
    hamming_numbers = [1] # Initialize a list to store computed Hamming numbers
    i, j, k = 0, 0, 0  # Initialize indices for each prime factor

    while len(hamming_numbers) < n:
        next_hamming = min(2 * hamming_numbers[i], 3 * hamming_numbers[j], 5 * hamming_numbers[k])
        hamming_numbers.append(next_hamming)

        if next_hamming == 2 * hamming_numbers[i]:
            i += 1
        elif next_hamming == 3 * hamming_numbers[j]:
            j += 1
        elif next_hamming == 5 * hamming_numbers[k]:
            k += 1

    return hamming_numbers[n - 1]

# Test cases
print(hamming(10))  # Output: 12

# def hamming(n):
#     i, j, k = 0, 0, 0
    
#     if n == 1:
#         return 1
#     else:
#         while n != 0:
#             if n % 5 == 0:
#                 k += 1
#                 n -= 5
#             elif n % 3 == 0:
#                 j += 1
#                 n -= 3
#             elif n % 2 == 0:
#                 i +=1
#                 n -= 2
#             else:
#                 print("Not divisible by 5, 3 nor 2")
#     return n