## develop a script for making tip calcultor
print("Welcome to the TIP CALCULATOR PROGRAM !!!")

## check for the total bill for the food.
total_bill = float(input("Enter the Total Bill : "))
print(f"The Total Bill amount is {total_bill}")

## check for how much the customer is willing to pay the tip in percentage
tip_figure = int(input("Enter the Percentage Figure you want to give as a Tip (10,12,15) ???"))
## calculate the tip bill
tip_bill = total_bill * (tip_figure / 100)
## total amount to be paid will be the sum of the total_bill and tip_bill
total_amount_payable = total_bill + tip_bill

## checking how the customer need to divide the amount between them.
divide_by = int(input("How much People Dividing the Bill : ??"))

## calculating how much each person should pay for the food
each_person_bill = total_amount_payable / divide_by
## round the each person bill to two decimal places
each_person_bill = round(each_person_bill, 2)

print(f"Each Person should pay {each_person_bill}, Thank You !!!")