# Program that takes numerical input from the user that specifies how many random numbers to create and writes a series of random numbers up to the inputted value in the range of 1-500

import random

def generateRandomNumbers(num_numbers):
    return [random.randint(1, 500) for _ in range(num_numbers)]

def writeNumbersToFile(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')

def readNumbersFromFile(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def main():
    numNumbers = int(input("Enter the number of random numbers to generate: "))
    filename = input("Enter the name of the file to save the numbers to: ")

    # Generate random numbers
    randomNumbers = generateRandomNumbers(numNumbers)

    # Write numbers to file
    writeNumbersToFile(randomNumbers, filename)
    print(f"Random numbers written to {filename}")

    # Read numbers from file and display on the console
    readNumbers = readNumbersFromFile(filename)
    print("Numbers read from file:")
    for number in readNumbers:
        print(number)

if __name__ == "__main__":
    main()
