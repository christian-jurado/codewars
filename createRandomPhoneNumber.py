import random

def create_phone_number(n):
    #your code here
    pn1 = ""
    pn2 = ""
    pn3 = ""
    for _ in range(3):
        pn1 += str(random.choice(n))
    for _ in range(3):
        pn2 += str(random.choice(n))
    for _ in range(4):
        pn3 += str(random.choice(n))

    return f"({pn1}) {pn2}-{pn3}"

print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
