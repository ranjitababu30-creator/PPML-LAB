def check_palindrome(s):
    s = s.lower()
    if s ==s[::-1]:
        print("palindrome")
    else:
        print("Not palindrome")
text = input("Enter a string: ")
check_palindrome(text)