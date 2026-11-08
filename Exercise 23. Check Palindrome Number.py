number = str(input("Enter a number: "))
def IsItAPalindrome(num):
    temp_polidrome = num[::-1]
    if temp_polidrome == num:
        print(f"number {num} is a palindrome")
    else:
        print(f"number {num} isn`t a palindrome")
IsItAPalindrome(number)