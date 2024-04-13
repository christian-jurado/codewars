def max_sequence(arr):
    max_sum = float('-inf')  # Initialize with negative infinity to ensure any sum is greater
    if not arr:
        return 0  # Empty list has maximum sum of 0
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum if max_sum > 0 else 0  # Negative numbers return 0

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
