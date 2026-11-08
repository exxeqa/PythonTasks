income = 45000
tax = 0
if income <= 10000:
    tax = 0
elif income <= 20000:
    tax += ((income - 10000) / 100)*10
elif income > 20000:
    tax = (10000 / 100) * 10
    tax += ((income - 20000) / 100)*20
print(tax)
