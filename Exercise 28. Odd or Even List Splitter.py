numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
odd = []
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("odd numbers: ", odd)
print( "even numbers: ", even)
