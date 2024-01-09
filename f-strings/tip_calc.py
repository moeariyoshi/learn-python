print("Welcome to the tip calculator!")
bill = float(input("How much was the bill? $"))
tip = int(input("How much would you like to tip? ex. 15! ")) / 100
people = int(input("How many people are you splitting the bill with? "))

total_bill = bill * tip + bill
bill_per_person = round(total_bill / people, 2)

print(f"Each person pays {bill_per_person}")