# All starts with "("
# All end with ")"

def balanced_parens(n):
    if n == 0:
        return ['']
    else:
        results = set()
        for combination in balanced_parens(n - 1):
            for i in range(len(combination)):
                if combination[i] == '(':
                    results.add(combination[:i+1] + '()' + combination[i+1:])
            results.add('()' + combination)
        return list(results)


# Test cases
print(balanced_parens(0))  # Output: [""]
print(balanced_parens(1))  # Output: ["()"]
print(balanced_parens(2))  # Output: ["()()", "(())"]
print(balanced_parens(3))  # Output: ["()()()", "(())()", "()(())", "(()())", "((()))"]


# Didn't work, the result had repeated answers
# def balanced_parens(n):
#     if n == 0:
#         return [""]
#     else:
#         result = []
#         for p in balanced_parens(n - 1):
#             result.append("()" + p)  # Add parentheses around the existing string
#             result.append("(" + p + ")")  # Add parentheses before and after the existing string
#             result.append(p + "()")  # Add parentheses after the existing string
#         return result


# Sure, let's consider the combination '(())' as an example:

# When i = 0:
# combination[:i+1] is '('.
# When i = 1:
# combination[:i+1] is '(('.
# When i = 2:
# combination[:i+1] is '(()'.
# When i = 3:
# combination[:i+1] is '(())'.

# Sure, let's consider the combination (()) as an example:

# When i = 0:
# combination[i+1:] is ')())'.
# When i = 1:
# combination[i+1:] is '))'.
# When i = 2:
# combination[i+1:] is ')'.
# When i = 3:
# combination[i+1:] is an empty string, since there is no character after index 3.




