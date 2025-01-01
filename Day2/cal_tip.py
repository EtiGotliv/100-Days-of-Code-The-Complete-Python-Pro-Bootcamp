print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How mach tip would you like to give? 10,12 or 15?"))
people = int(input("How many people to split thr bill?"))
pay = (tip/100 * total_bill + total_bill)/people
print(f"Each person should pay: ${round(pay,2)}")