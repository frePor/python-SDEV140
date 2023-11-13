# Program that takes the sum of a series of single digit numbers 


n = int(input("Enter any number here:"))


digitList = [int(x) for x in str(n)]
total = sum(digitList)

print("The sum of all digits is: ", total)
