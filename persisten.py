def persistence(n):
    # your code
    if n < 10:
        return 0
    else:
        count = 0
        while n >= 10:
            product = 1
            for digit in str(n):
                product *= int(digit)
            n = product
            count += 1
    return count

print(persistence(195))
