# to check whether the entered number is palindrome or not.

a = int(input("Enter the number : "))

def palindrome_checker(a):
    copy = a
    rev = 0

    while a > 0:
        rev = rev * 10 + a%10
        a = a // 10

    if rev == copy:
        print(f"{copy} is palindrom number. ")

    else:
        print(f"{copy} is not palindrome number.")

palindrome_checker(a)