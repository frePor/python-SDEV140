# Program that prompts user to enter two primary colors to mix resulting in its respective secondary color

colorCombinations = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
}

primaryColor1 = input("Enter your first color here (red, blue, or yellow): ").lower()
primaryColor2 = input("Enter your second color here (red, blue, or yellow): ").lower()


# Mixing function
secondaryColor = colorCombinations.get((primaryColor1, primaryColor2))
if secondaryColor is None:
    print("ERROR: Please enter a valid primary color(red, blue, or yellow)")
else:
    print(f"The secondary color is {secondaryColor}")
    



