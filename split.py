print("Welcome to the tip calculator")
bill = int(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
bill_tip = bill+bill*tip/100
split = bill_tip/people
print(f"Each person should pay:{round(split,2)}")

