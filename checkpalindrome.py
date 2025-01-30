def is_palindrome(s):
    s = s.lower() 
    return all(s[i] == s[-i-1] for i in range(len(s) // 2))

char = input("Enter your stirng/number: ")
if is_palindrome(char):
    print(f"The string {char} is a palindrom")
else:
    print(f"The string {char} is not a palindrome")

  
