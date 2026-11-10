Rows = 9
x = Rows
for i in range(Rows, 0, -1):
    for j in range(i):
        print(f"{x}",end=" ")
        x -= 1
    print()
    x = i
    x -= 1