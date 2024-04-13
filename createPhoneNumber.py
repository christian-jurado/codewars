def create_phone_number(n):
    #your code here
    pn1 = ""
    pn2 = ""
    pn3 = ""
    for x in n[:3]:
        pn1 += str(x)
    for x in n[3:6]:
        pn2 += str(x)
    for x in n[6:]:
        pn3 += str(x)
    return f"({pn1}) {pn2}-{pn3}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
