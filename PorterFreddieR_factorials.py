# Program that lets user input a nonnegative integer and calculates the factorial of that integer

# Takes input from user



n = (int(input("Enter an integer here:")))

# Calculates the factorial of n using a for loop

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Prints result
print(f"{n}! = {factorial(n)}")