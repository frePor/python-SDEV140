# Program to calculate the total amount of a restaurant meal

while True:

    # Takes the food charge from the user
    food_charge = float(input("Enter the charge for the food: $"))

    # Calculates the tip @ 18%
    tip = 0.18 * food_charge

    # Calculates the sales tax @ 7%
    sales_tax = 0.07 * food_charge

    # Calculates the total bill amount
    total_amount = food_charge + tip + sales_tax

    # Displasy each of the amounts
    print(f"Food Charge: ${food_charge:.2f}")
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Sales Tax (7%): ${sales_tax:.2f}")
    print(f"Total Bill Amount: ${total_amount:.2f}")
