case1 = int(input())
case2 = int(input())
if case1 * case2 <= 1000:
    print(case1*case2)
elif case1 * case2 > 1000:
    print(case1+case2)
else:
    print("incorrectinput")