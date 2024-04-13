def get_pins(observed):

#Create a dictionary with all the possibles adjacent digits (list), including the observed number
#Create a list where would go the result
#If is 1 digit return the list of the number
#If is more than 1 digit, have to copy the first list, the iterate the second list (combine) with the first in all possibe variation
#Repeat previous step
#Return the result
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }
    
    variations = ['']
    
    for digit in observed:
        new_variations = []  # Create a new list to store variations for the current digit
        for prefix in variations:  # Iterate over existing variations
            for suffix in adjacent_digits[digit]:  # Iterate over adjacent digits for the current digit
                new_variation = prefix + suffix  # Concatenate prefix and suffix to form a new variation
                new_variations.append(new_variation)  # Add the new variation to the list
        variations = new_variations  # Update the list of variations with variations for the current digit
    
    return variations
    # for digit in observed:
    #     variations = [prefix + suffix for prefix in variations for suffix in adjacent_digits[digit]]
# Test cases
print(get_pins('813'))  # Output: ['5', '7', '8', '9', '0']
print(get_pins('11')) # Output: ['11', '12', '14', '21', '22', '24', '41', '42', '44']
