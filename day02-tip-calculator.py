print("Welcome to the Tip Calculator!")

total = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill?"))

person_pay = round(total / people * (1 + tip / 100), 2)

print(f"Each person should pay ${person_pay:.2f}")
