class RomanNumerals:

    @staticmethod
    def to_roman(val : int) -> str:
        nums = {1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
            }
        sum = ""    
        for value, letter in reversed(nums.items()):
            while val >= value:          
                sum += letter
                val -= value                
        return sum
    
    
    # def to_roman(num):
    #     R2M = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
    #     string = ''
    #     for k, v in R2M.items():
    #         count = num // v
    #         num %= v
    #         string += count * k
    

    @staticmethod
    def from_roman(roman_num : str) -> int:
        nums = {1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
            }
        sum = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num):
                if 'C' == roman_num[i] and 'M' == roman_num[i+1]:
                    sum += 900
                    i += 2
                elif 'C' == roman_num[i] and 'D' == roman_num[i+1]:
                    sum += 400
                    i += 2
                elif 'X' == roman_num[i] and 'C' == roman_num[i+1]:
                    sum += 90
                    i += 2
                elif 'X' == roman_num[i] and 'L' == roman_num[i+1]:
                    sum += 40
                    i += 2
                elif 'I' == roman_num[i] and 'X' == roman_num[i+1]:
                    sum += 9
                    i += 2
                elif 'I' == roman_num[i] and 'V' == roman_num[i+1]:
                    sum += 4
                    i += 2
                else:
                    for key, val in nums.items():
                        if roman_num[i] in val:          
                            sum += key
                            i += 1
                            break
            elif i < len(roman_num):
                for key, val in nums.items():
                    if roman_num[i] in val:          
                        sum += key
                        i += 1
                        break            
        return sum
    
# print(RomanNumerals.from_roman("IV"))
# assert RomanNumerals.from_roman("IV") == 4
# assert RomanNumerals.from_roman('XXI') == 21
# assert RomanNumerals.from_roman('I') == 1
# assert RomanNumerals.from_roman('IV') == 4
# assert RomanNumerals.from_roman('MMVIII') == 2008
# assert RomanNumerals.from_roman('MDCLXVI') == 1666
    
assert RomanNumerals.from_roman(1000) == 'M'
assert RomanNumerals.from_roman(4) == 'IV'
assert RomanNumerals.from_roman(1) == 'I'
assert RomanNumerals.from_roman(1990) == 'MCMXC'
assert RomanNumerals.from_roman(2008) == 'MMVIII'
# +--------+-------+
# | Symbol | Value |
# +--------+-------+
# |    M   |  1000 |
# |   CM   |   900 |
# |    D   |   500 |
# |   CD   |   400 |
# |    C   |   100 |
# |   XC   |    90 |
# |    L   |    50 |
# |   XL   |    40 |
# |    X   |    10 |
# |   IX   |     9 |
# |    V   |     5 |
# |   IV   |     4 |
# |    I   |     1 |
# +--------+-------+