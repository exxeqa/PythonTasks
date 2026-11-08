numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
def list_comp(list):
    print(f"given list {list} | ")
    if list[0] == list[-1]:
        return False
    else:
        return True


print("result is", list_comp(numbers_x))
print("result is", list_comp(numbers_y))