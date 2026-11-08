Case1 = 121
Case2 = 125
def IsItAPalindrome(num):
    temp_polidrome = str(num)[::-1]
    print(f"reversed {num} is {temp_polidrome}")
    if int(temp_polidrome) == num:
        print(f"so {num} is a palindrome")
    else:
        print(f"so {num} isn`t a palindrome")
IsItAPalindrome(Case1)
IsItAPalindrome(Case2)