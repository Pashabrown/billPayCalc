print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
tip = int(input("What percentage of tip would you like to give? "))
split_bill = int(input("How many people to split the bill? $"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill // split_bill
print(bill_per_person)