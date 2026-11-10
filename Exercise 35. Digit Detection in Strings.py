input_string = "Python3"
for i in input_string:
    if i.isdigit() == True:
        x = True
        break
    else:
        x = False
print(f"The string 'Python3' contains digits: {x}")