def factorial_finder(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = i * factorial
        i -= 1
    print(factorial)

number = int(input("Enter a number: "))
if number <= 1:
    print("factorial is 1")
else:
    factorial_finder(number)