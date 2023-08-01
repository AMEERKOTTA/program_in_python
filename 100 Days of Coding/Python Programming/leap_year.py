## Write a program that works out whether if a given year is a leap year. 
## A normal year has 365 days, leap years have 366, with an extra day in February. 

## This is how you work out whether if a particular year is a leap year.
## on every year that is evenly divisible by 4 
## **except** every year that is evenly divisible by 100 
## **unless** the year is also evenly divisible by 400

year = int(input("Enter the Year of your Choice : "))
print(f"The year choosen by the user is : {year}")

## If the year is evenly divisible by 4, go to step 2. Otherwise, it's not a leap year.
## If the year is evenly divisible by 100, go to step 3. Otherwise, it's a leap year.
## If the year is evenly divisible by 400, it's a leap year. Otherwise, it's not a leap year.

if year % 4 == 0:
    print()
    if year % 100 == 0:
        print()
        if year % 400 == 0:
            print("IT'S A LEAP YEAR !!")
        else:
            print("IT'S NOT LEAP YEAR !!")
    else:
        print("IT'S A LEAP YEAR !!")
else:
    print("NOT LEAP YEAR !!")

