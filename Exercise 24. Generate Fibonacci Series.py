Terms = 15
last = 1
sum = 0
for i in range(Terms):
    print(sum, end=" ")
    sum = last + sum
    last = sum - last

