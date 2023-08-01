## build an automatic pizza order program.
## Based on a user's order, work out their final bill.
## Small Pizza: $15
## Medium Pizza: $20
## Large Pizza: $25
## Pepperoni for Small Pizza: +$2
## Pepperoni for Medium or Large Pizza: +$3
## Extra cheese for any size pizza: + $1

print("WELCOME TO PIZZA ORDERING APPLICATION....")
pizza_choice = input("Which Pizza you need (S/M/L) : ??")

total_bill = 0 

if pizza_choice == "S":
    total_bill += 15
    pepperoni = input("Do you need Pepperoni (S/M/L) : ??")
    if pepperoni == "S":
        total_bill += 2
    else:
        total_bill += 3
elif pizza_choice == "M":
    total_bill += 20
    pepperoni = input("Do you need Pepperoni (S/M/L) : ??")
    if pepperoni == "S":
        total_bill += 2
    else:
        total_bill += 3
elif pizza_choice == "L":
    total_bill += 25
    pepperoni = input("Do you need Pepperoni (S/M/L) : ??")
    if pepperoni == "S":
        total_bill += 2
    else:
        total_bill += 3

extra_cheese = input("Do you need Extra Cheese : (Y/N)  ??")
if extra_cheese == "Y":
    total_bill += 1
else:
    print("We dont need extra cheeze !!")

print(f"The total bill is : {total_bill}")
