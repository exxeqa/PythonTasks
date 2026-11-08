base = 2
exp = 5
def exponent(base, exp):
    result = base
    for i in range(1, exp):
        result *= base
    print(base, "raises to the power of", exp, "is:", result)
exponent(2, 5)