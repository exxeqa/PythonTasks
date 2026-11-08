numbers = range(10)
previous_number = 0
def interation():
    global previous_number
    for i in numbers:
        x_sum = previous_number + i
        print(f"Current Number {i} Previous Number {previous_number} Sum: {x_sum}")
        previous_number = i
interation()