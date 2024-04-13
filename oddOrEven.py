def find_outlier(integers):
    odd = []
    pair = []
    for number in integers:
        if number %2 == 0:
            pair.append(number)
        else:
            odd.append(number)
    if len(odd) == 1:
        return int(odd[0])
    else:
        return int(pair[0])

print = find_outlier([2, 4, 6, 8, 10, 3])
