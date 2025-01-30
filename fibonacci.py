def fibonacci(n):
    if n <= 0:
        return "Invalid Input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter a number : "))  
print(fibonacci(n)) 
