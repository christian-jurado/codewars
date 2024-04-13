def prime_factors(n):
    result = ""
    divisor = 2

    while n > 1:
        count = 0
        while n % divisor == 0:
            count += 1
            n //= divisor

        if count > 0:
            if result:
                result += ")"
            result += "({}{}".format(divisor, "**" + str(count) if count > 1 else "")

        divisor += 1

    return result + ")" if result else ""

prime_factors(7775460)
# "(2**2)(3**3)(5)(7)(11**2)(17)"
